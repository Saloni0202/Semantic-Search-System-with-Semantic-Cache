# Semantic-Search-System-with-Semantic-Cache

## Overview

This project implements a lightweight **Semantic Search System** using the **20 Newsgroups dataset**. The system converts text into vector embeddings and stores them in a vector database for efficient similarity search. A **semantic cache** is implemented to reuse results of similar queries and improve response time.

The system is exposed through a **FastAPI service** that allows users to query documents, view cache statistics, and clear the cache.

## Features

* Semantic search using transformer embeddings
* Vector similarity search using FAISS
* Semantic caching using cosine similarity
* FastAPI REST API for querying and cache management
* Uses the 20 Newsgroups dataset for document search
* 

## Project Structure

Trademarkia
│
├── app
│   ├── api
│   │   └── routes.py
│   │
│   ├── cache
│   │   └── semantic_cache.py
│   │
│   ├── clustering
│   │   └── fuzzy_cluster.py
│   │
│   ├── data
│   │   └── dataset_loader.py
│   │
│   ├── embeddings
│   │   ├── embedder.py
│   │   └── vector_store.py
│
├── models
│   └── request_models.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Components

### 1. Embedding Model

The project uses the **SentenceTransformer model `all-MiniLM-L6-v2`** to convert text documents into vector embeddings. These embeddings capture the semantic meaning of the text.

### 2. Vector Database

Embeddings are stored in **FAISS**, which allows fast similarity search across thousands of documents.

### 3. Semantic Cache

A semantic cache is implemented to detect similar queries using **cosine similarity** between embeddings. If a similar query has already been processed, the cached result is returned instead of performing another vector search.

### 4. FastAPI Service

The system exposes REST endpoints to interact with the semantic search engine.

---

## API Endpoints

### POST /query

Search for a document using a natural language query.

Request Body:

```
{
  "query": "What is space exploration?"
}
```

Response:

```
{
  "query": "...",
  "cache_hit": false,
  "matched_query": null,
  "similarity_score": 0,
  "result": "...",
  "dominant_cluster": 0
}
```

---

### GET /cache/stats

Returns statistics about the semantic cache.

Example Response:

```
{
  "total_entries": 10,
  "hit_count": 3,
  "miss_count": 7,
  "hit_rate": 0.3
}
```

---

### DELETE /cache

Clears all cached query results.

Response:

```
{
  "message": "Cache cleared"
}
```

---

## Installation

### 1. Clone the Repository

```
git clone <repository-link>
cd Trademarkia
```

### 2. Create Virtual Environment

```
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```
.\venv\Scripts\Activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 4. Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## Dataset

This project uses the **20 Newsgroups dataset** from Scikit-learn, which contains approximately 18,000 newsgroup posts across 20 different topics.

---

## Technologies Used

* Python
* FastAPI
* SentenceTransformers
* FAISS
* Scikit-learn
* NumPy

---

## Future Improvements

* Add advanced clustering techniques for topic grouping
* Improve cache eviction strategies
* Add evaluation metrics for search quality
* Deploy the API using Docker

---

## Author

Developed as part of a **Semantic Search System assignment**.
