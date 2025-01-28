from flask import Flask, jsonify, request
import requests
import json
import random

app = Flask(__name__)

# Function to detect claims using Gemini API
def detect_claim_using_gemini(text):
    """
    Detect claims using Google Gemini API. 
    Replace this with the correct API URL and method from Gemini API documentation.
    """
    api_url = "https://gemini.googleapis.com/v1/claims:detect"
    api_key = os.getenv('GOOGLE_GEMINI_API_KEY')
    headers = {
        "Authorization": f"Bearer {api_key}",  # Replace with your actual API key
        "Content-Type": "application/json"
    }
    
    data = {
        "input": text
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        return {"error": "Failed to process the claim"}

# Function to fetch related entities using Gemini Knowledge Graph API
def fetch_knowledge_graph(query):
    """
    Fetch related entities using the Gemini Knowledge Graph API.
    """
    api_url = "https://gemini.googleapis.com/v1/knowledge:search"
    headers = {
        "Authorization": "Bearer YOUR_GOOGLE_CLOUD_API_KEY",  # Replace with your actual API key
        "Content-Type": "application/json"
    }
    
    params = {
        "query": query
    }

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('entities', [])
    else:
        return []

# Function to calculate credibility score based on matched entities
def calculate_credibility_score(matched_entities, source_reliability):
    """
    Calculate credibility score based on matched entities and source reliability.
    """
    entity_score = len(matched_entities) * 10  # Each matched entity adds 10 points
    reliability_score = source_reliability * 5  # Source reliability adds 5 points per level
    return min(entity_score + reliability_score, 100)  # Max score is 100

# Function to generate feedback to users
def generate_feedback(credibility_score):
    """
    Generate feedback to users based on credibility score.
    """
    if credibility_score > 80:
        return "The claim is likely TRUE based on the data available."
    elif credibility_score > 50:
        return "The claim is uncertain. Further investigation is needed."
    else:
        return "The claim is likely FALSE based on the data available."

# Endpoint to detect claims using Google Gemini
@app.route('/detect_claim', methods=['POST'])
def detect_claim_route():
    """
    Detect a claim in the text using Google Gemini API.
    """
    data = request.get_json()
    text = data.get('text', '')

    claim_result = detect_claim_using_gemini(text)
    return jsonify({
        "status": "success",
        "claim": claim_result
    })

# Endpoint to verify claim based on knowledge graph and entities
@app.route('/verify_claim', methods=['POST'])
def verify_claim_route():
    """
    Verify a claim using the knowledge graph constructed by Google Gemini.
    """
    data = request.get_json()
    claim = data.get('claim', '')

    matched_entities = fetch_knowledge_graph(claim)  # Match the claim with entities in the knowledge graph
    source_reliability = random.choice([1, 2, 3])  # Mock reliability score (1 = low, 3 = high)
    credibility_score = calculate_credibility_score(matched_entities, source_reliability)

    feedback = generate_feedback(credibility_score)

    return jsonify({
        "status": "success",
        "claim": claim,
        "matched_entities": matched_entities,
        "credibility_score": credibility_score,
        "feedback": feedback
    })

# Endpoint to provide feedback to users
@app.route('/provide_feedback', methods=['POST'])
def provide_feedback():
    """
    Provide feedback to users on claim verification.
    """
    data = request.get_json()
    claim = data.get('claim', '')
    feedback = generate_feedback(random.randint(0, 100))  # Simulate random feedback
    
    return jsonify({
        "status": "success",
        "claim": claim,
        "feedback": feedback
    })

# Main route to check server status
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "message": "Fake News Detection Server is running"
    })

if __name__ == '__main__':
    app.run(debug=True)
