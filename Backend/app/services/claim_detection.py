from transformers import pipeline

# Example of a fine-tuned BERT-based claim detection
def detect_claim(text):
    claim_model = pipeline("text-classification", model="bert-base-uncased")
    result = claim_model(text)
    return {"claim_detected": result[0]['label'], "confidence": result[0]['score']}
