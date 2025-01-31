from transformers import pipeline
from typing import Dict, List
import logging

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

if __name__ == "__main__":
    detector = ClaimDetector()
    
    # Single text detection example
    text = "COVID-19 vaccines are highly effective."
    result = detector.detect_claim(text)
    print("Single Detection Result:", result)
    
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
