from app.utils.database import query_knowledge_graph

def verify_claim(claim):
    # NER-based structured query generation
    entities = extract_entities(claim)
    graph_results = query_knowledge_graph(entities)
    
    # Semantic matching logic (e.g., Sentence-BERT)
    verified_result = semantic_matching(claim, graph_results)
    return {"claim": claim, "verified_result": verified_result}
