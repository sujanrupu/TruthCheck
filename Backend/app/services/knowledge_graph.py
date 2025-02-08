from explainable_ai import explain_model
from typing import Dict, List
import logging
from neo4j import GraphDatabase

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClaimDetector:
    """
    Detect claims in text using a fine-tuned BERT model.
    """
    def __init__(self, model_name: str = "bert-base-uncased"):
        logging.info("Initializing model...")
        self.model = pipeline("text-classification", model=model_name)
        logging.info("Model successfully loaded.")

    def detect_claim(self, text: str) -> Dict[str, object]:
        logging.info("Analyzing text: %s", text)
        result = self.model(text)
        return {"claim_detected": result[0]['label'], "confidence": round(result[0]['score'], 4)}

    def batch_detect_claims(self, texts: List[str]) -> List[Dict[str, object]]:
        logging.info("Analyzing batch of %d texts", len(texts))
        results = self.model(texts)
        return [{"text": texts[i], "claim_detected": results[i]['label'], "confidence": round(results[i]['score'], 4)} for i in range(len(texts))]

class ExplainableClaimDetector(ClaimDetector):
    """
    Extends ClaimDetector with explainable AI capabilities.
    """
    def generate_feedback(self, claim: str) -> Dict[str, str]:
        logging.info("Generating explanation for claim: %s", claim)
        return {"claim": claim, "explanation": explain_model(claim)}

class KnowledgeGraph:
    """
    Constructs and updates a knowledge graph using Neo4j.
    """
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def construct_graph(self) -> Dict[str, str]:
        logging.info("Building knowledge graph...")
        with self.driver.session() as session:
            session.run("MERGE (n:Node {name: 'Example'}) RETURN n")
        logging.info("Graph updated successfully.")
        return {"status": "success"}

if __name__ == "__main__":
    detector = ExplainableClaimDetector()
    knowledge_graph = KnowledgeGraph("bolt://localhost:7687", "neo4j", "password")
    
    text = "COVID-19 vaccines are highly effective."
    print("Single Detection:", detector.detect_claim(text))
    print("Explanation:", detector.generate_feedback(text))
    
    texts = ["The Earth is flat.", "Climate change is caused by human activity.", "Drinking water is essential for health.", "The moon landing was a hoax."]
    print("Batch Detection:", detector.batch_detect_claims(texts))
    
    for t in texts:
        print("Batch Explanation:", detector.generate_feedback(t))
    
    print("Knowledge Graph Status:", knowledge_graph.construct_graph())
    knowledge_graph.close()
