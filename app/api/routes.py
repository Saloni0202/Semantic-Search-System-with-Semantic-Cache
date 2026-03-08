from fastapi import APIRouter, Request
from models.request_models import QueryRequest
import numpy as np

router = APIRouter()


@router.post("/query")
def query_api(request: Request, data: QueryRequest):

    query = data.query

    embedder = request.app.state.embedder
    vector_store = request.app.state.vector_store
    cache = request.app.state.cache
    texts = request.app.state.texts

    query_embedding = embedder.embed([query])[0]

    hit, entry, score = cache.lookup(query_embedding)

    if hit:

        return {
            "query": query,
            "cache_hit": True,
            "matched_query": entry["query"],
            "similarity_score": float(score),
            "result": entry["result"],
            "dominant_cluster": entry["cluster"]
        }

    distances, indices = vector_store.search(
        np.array([query_embedding]), k=1
    )

    doc_index = int(indices[0][0])

    result = texts[doc_index]

    dominant_cluster = 0

    cache.add(query, query_embedding, result, dominant_cluster)

    return {
        "query": query,
        "cache_hit": False,
        "matched_query": None,
        "similarity_score": 0,
        "result": result,
        "dominant_cluster": dominant_cluster
    }


@router.get("/cache/stats")
def cache_stats(request: Request):

    cache = request.app.state.cache

    return cache.stats()


@router.delete("/cache")
def clear_cache(request: Request):

    cache = request.app.state.cache
    cache.clear()

    return {"message": "Cache cleared"}