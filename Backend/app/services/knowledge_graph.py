from explainable_ai import explain_model
from typing import Dict, List
import logging
from neo4j import GraphDatabase

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClaimDetector:
    """
    A class for detecting claims in text using a fine-tuned BERT model.
    """
    def __init__(self, model_name: str = "bert-base-uncased"):
        """
        Initialize the claim detection pipeline.
        """
        logging.info("Loading model...")
        self.model = pipeline("text-classification", model=model_name)
        logging.info("Model loaded successfully.")

    def detect_claim(self, text: str) -> Dict[str, object]:
        """
        Detect whether a given text contains a claim.
        
        :param text: Input text to analyze
        :return: Dictionary containing claim status and confidence score
        """
        logging.info("Processing text: %s", text)
        result = self.model(text)
        
        response = {
            "claim_detected": result[0]['label'],
            "confidence": round(result[0]['score'], 4)
        }
        logging.info("Detection Result: %s", response)
        return response

    def batch_detect_claims(self, texts: List[str]) -> List[Dict[str, object]]:
        """
        Detect claims in a batch of texts.
        
        :param texts: List of texts to analyze
        :return: List of dictionaries with detection results
        """
        logging.info("Processing batch of %d texts", len(texts))
        results = self.model(texts)
        
        response = [
            {
                "text": texts[i],
                "claim_detected": results[i]['label'],
                "confidence": round(results[i]['score'], 4)
            } 
            for i in range(len(texts))
        ]
        logging.info("Batch processing completed.")
        return response

class ExplainableClaimDetector(ClaimDetector):
    """
    Extends ClaimDetector with explainable AI capabilities.
    """
    def generate_feedback(self, claim: str) -> Dict[str, str]:
        """
        Generate an explanation for the detected claim.
        
        :param claim: The claim to explain
        :return: Dictionary containing the claim and its explanation
        """
        logging.info("Generating explanation for claim: %s", claim)
        explanation = explain_model(claim)
        response = {"claim": claim, "explanation": explanation}
        logging.info("Explanation Generated: %s", response)
        return response

class KnowledgeGraph:
    """
    Class to construct and update a knowledge graph using Neo4j.
    """
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
    def construct_graph(self):
        """
        Constructs or updates the knowledge graph.
        """
        logging.info("Constructing knowledge graph...")
        with self.driver.session() as session:
            session.run("MERGE (n:Node {name: 'Example'}) RETURN n")
        logging.info("Knowledge graph updated successfully.")
        return {"status": "success"}

if __name__ == "__main__":
    detector = ExplainableClaimDetector()
    knowledge_graph = KnowledgeGraph("bolt://localhost:7687", "neo4j", "password")
    
    # Single text detection example
    text = "COVID-19 vaccines are highly effective."
    result = detector.detect_claim(text)
    print("Single Detection Result:", result)
    
    # Explanation example
    explanation = detector.generate_feedback(text)
    print("Explanation:", explanation)
    
    # Batch processing example
    texts = [
        "The Earth is flat.",
        "Climate change is caused by human activity.",
        "Drinking water is essential for health.",
        "The moon landing was a hoax."
    ]
    batch_results = detector.batch_detect_claims(texts)
    
    print("Batch Detection Results:")
    for res in batch_results:
        print(res)
    
    # Batch explanation example
    print("Batch Explanations:")
    for text in texts:
        explanation = detector.generate_feedback(text)
        print(explanation)
    
    # Construct knowledge graph
    graph_status = knowledge_graph.construct_graph()
    print("Knowledge Graph Status:", graph_status)
    knowledge_graph.close()
