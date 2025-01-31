import logging
from app.utils.database import query_knowledge_graph
from app.utils.nlp import extract_entities, semantic_matching

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler("verification.log"), logging.StreamHandler()]
    )
    return logging.getLogger("ClaimVerifier")

logger = setup_logger()

def verify_claim(claim):
    """
    Verifies a given claim by extracting entities, querying a knowledge graph,
    and performing semantic matching with retrieved results.
    """
    try:
        if not claim or not isinstance(claim, str):
            raise ValueError("Invalid claim: Must be a non-empty string.")
        
        logger.info(f"Verifying claim: {claim}")
        
        # Step 1: Named Entity Recognition (NER) to extract entities
        entities = extract_entities(claim)
        logger.info(f"Extracted entities: {entities}")
        
        if not entities:
            logger.warning("No significant entities found in the claim.")
            return {"claim": claim, "verified_result": "No relevant entities detected."}
        
        # Step 2: Query Knowledge Graph
        graph_results = query_knowledge_graph(entities)
        logger.info(f"Knowledge Graph results: {graph_results}")
        
        if not graph_results:
            logger.warning("No relevant data found in knowledge graph.")
            return {"claim": claim, "verified_result": "No supporting data available."}
        
        # Step 3: Semantic Matching
        verified_result = semantic_matching(claim, graph_results)
        logger.info(f"Semantic matching result: {verified_result}")
        
        return {"claim": claim, "verified_result": verified_result}
    
    except Exception as e:
        logger.error(f"Error during claim verification: {str(e)}")
        return {"claim": claim, "verified_result": "Error in verification process."}

# Example Usage
def main():
    sample_claims = [
        "COVID-19 vaccines contain microchips.",
        "The Eiffel Tower is in Paris, France.",
        "Elon Musk founded Tesla.",
        "Water boils at 100 degrees Celsius.",
        "Unicorns exist in the wild."
    ]
    
    for claim in sample_claims:
        result = verify_claim(claim)
        print(result)

if __name__ == "__main__":
    main()
