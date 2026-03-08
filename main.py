from fastapi import FastAPI
from app.api.routes import router

from app.data.dataset_loader import load_dataset
from app.embeddings.embedder import Embedder
from app.embeddings.vector_store import VectorStore
from app.cache.semantic_cache import SemanticCache

app = FastAPI(title="Semantic Search System")

print("Loading dataset...")

texts = load_dataset()

print("Generating embeddings...")

embedder = Embedder()

embeddings = embedder.embed(texts)

vector_store = VectorStore(embeddings.shape[1])
vector_store.add(embeddings)

cache = SemanticCache()

app.state.texts = texts
app.state.embedder = embedder
app.state.vector_store = vector_store
app.state.cache = cache

app.include_router(router)