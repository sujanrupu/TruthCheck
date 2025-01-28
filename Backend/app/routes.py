from flask import Blueprint, request, jsonify
from app.services import knowledge_graph, claim_detection, semantic_verification, feedback

api = Blueprint("api", __name__)

@api.route("/construct_knowledge_graph", methods=["POST"])
def construct_knowledge_graph():
    result = knowledge_graph.construct()
    return jsonify({"message": "Knowledge graph updated successfully", "result": result})

@api.route("/detect_claim", methods=["POST"])
def detect_claim():
    data = request.json
    text = data.get("text")
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    result = claim_detection.detect_claim(text)
    return jsonify(result)

@api.route("/verify_claim", methods=["POST"])
def verify_claim():
    data = request.json
    claim = data.get("claim")
    if not claim:
        return jsonify({"error": "Claim is required"}), 400
    
    result = semantic_verification.verify_claim(claim)
    return jsonify(result)

@api.route("/get_feedback", methods=["POST"])
def get_feedback():
    data = request.json
    claim = data.get("claim")
    if not claim:
        return jsonify({"error": "Claim is required"}), 400

    result = feedback.generate_feedback(claim)
    return jsonify(result)

def register_routes(app):
    app.register_blueprint(api, url_prefix="/api")
