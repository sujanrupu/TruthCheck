from explainable_ai import explain_model

def generate_feedback(claim):
    explanation = explain_model(claim)
    return {"claim": claim, "explanation": explanation}
