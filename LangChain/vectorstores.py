"""
====================================================================
File: 08_vectorstores.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Vector Stores
====================================================================

Description
-----------
Vector Stores store embeddings and perform similarity search.

Without a Vector Store, RAG applications cannot efficiently
retrieve relevant documents.

Used In
-------
✔ RAG
✔ Semantic Search
✔ Chatbots
✔ AI Search
✔ Recommendation Systems

Official Documentation
----------------------
https://python.langchain.com/docs/integrations/vectorstores/
"""

####################################################################
# Chroma
####################################################################

# Package
# -------
# langchain-chroma

# Install
# -------
# pip install langchain-chroma chromadb

from langchain_chroma import Chroma

# Purpose
# -------
# Local vector database used for development and production.

# When to Use
# -----------
# ✔ Local RAG
# ✔ Fast Prototyping
# ✔ Small & Medium Projects

# Example

# db = Chroma.from_documents(
#     documents=documents,
#     embedding=embeddings,
#     persist_directory="./chroma_db"
# )

# Common Methods
# --------------
# from_documents()
# from_texts()
# add_documents()
# similarity_search()
# similarity_search_with_score()
# as_retriever()
# delete()

# Interview Questions
# -------------------
# Q. Why use Chroma?
#
# Chroma is lightweight, open-source,
# and easy to integrate with LangChain.


####################################################################
# FAISS
####################################################################

# Package
# -------
# langchain-community

# Install
# -------
# pip install faiss-cpu langchain-community

from langchain_community.vectorstores import FAISS

# Purpose
# -------
# Facebook AI Similarity Search.

# When to Use
# -----------
# ✔ Local Search
# ✔ Fast Similarity Search
# ✔ Offline Applications

# Example

# db = FAISS.from_documents(
#     documents,
#     embeddings
# )

# Common Methods
# --------------
# save_local()
# load_local()
# similarity_search()
# merge_from()
# as_retriever()

# Interview Questions
# -------------------
# Q. Does FAISS persist automatically?
#
# No.
# You must explicitly save the index.


####################################################################
# PineconeVectorStore
####################################################################

# Package
# -------
# langchain-pinecone

# Install
# -------
# pip install langchain-pinecone pinecone

from langchain_pinecone import PineconeVectorStore

# Purpose
# -------
# Managed cloud vector database.

# When to Use
# -----------
# ✔ Production
# ✔ Cloud Applications
# ✔ Large Scale Search

# Example

# db = PineconeVectorStore.from_documents(
#     documents,
#     embeddings,
#     index_name="my-index"
# )


####################################################################
# PGVector
####################################################################

# Package
# -------
# langchain-postgres

# Install
# -------
# pip install langchain-postgres

from langchain_postgres import PGVector

# Purpose
# -------
# PostgreSQL extension for vector search.

# When to Use
# -----------
# ✔ Enterprise
# ✔ Existing PostgreSQL Database
# ✔ Production

# Example

# db = PGVector(
#     embeddings=embeddings,
#     collection_name="documents",
#     connection="postgresql://..."
# )

####################################################################
# Azure AI Search
####################################################################

# Package
# -------
# langchain-community

# Install
# -------
# pip install langchain-community

from langchain_community.vectorstores import AzureSearch

# Purpose
# -------
# Azure AI Search with vector capabilities.

# Used In
# -------
# ✔ Enterprise AI
# ✔ Azure Cloud
# ✔ Production RAG

# Example

# db = AzureSearch(
#     azure_search_endpoint="...",
#     azure_search_key="...",
#     index_name="rag-index",
#     embedding_function=embeddings.embed_query
# )

####################################################################
# Milvus
####################################################################

# Package
# -------
# langchain-milvus

# Install
# -------
# pip install langchain-milvus pymilvus

from langchain_milvus import Milvus

# Purpose
# -------
# High-performance open-source vector database.

# Used In
# -------
# ✔ Billion-scale vectors
# ✔ Enterprise AI

####################################################################
# Qdrant
####################################################################

# Package
# -------
# langchain-qdrant

# Install
# -------
# pip install langchain-qdrant qdrant-client

from langchain_qdrant import QdrantVectorStore

# Purpose
# -------
# Open-source vector database.

# Used In
# -------
# ✔ Production
# ✔ Cloud
# ✔ Local Deployment

####################################################################
# Weaviate
####################################################################

# Package
# -------
# langchain-weaviate

# Install
# -------
# pip install langchain-weaviate

from langchain_weaviate import WeaviateVectorStore

# Purpose
# -------
# AI-native vector database.

####################################################################
# Elasticsearch
####################################################################

# Package
# -------
# langchain-elasticsearch

# Install
# -------
# pip install langchain-elasticsearch

from langchain_elasticsearch import ElasticsearchStore

# Purpose
# -------
# Elasticsearch with vector search.

# Used In
# -------
# ✔ Hybrid Search
# ✔ Enterprise Search

####################################################################
# Redis
####################################################################

# Package
# -------
# langchain-redis

# Install
# -------
# pip install langchain-redis

from langchain_redis import RedisVectorStore

# Purpose
# -------
# Redis vector similarity search.

# Used In
# -------
# ✔ High-speed search
# ✔ Session memory
# ✔ AI applications

####################################################################
# LanceDB
####################################################################

# Package
# -------
# langchain-community

from langchain_community.vectorstores import LanceDB

# Purpose
# -------
# Embedded local vector database.

####################################################################
# Methods Every Vector Store Supports
####################################################################

# from_documents()
# from_texts()
# add_documents()
# add_texts()
# similarity_search()
# similarity_search_with_score()
# similarity_search_by_vector()
# max_marginal_relevance_search()
# delete()
# as_retriever()

####################################################################
# Summary
####################################################################

# Local
# -----
# Chroma
# FAISS
# LanceDB

# Enterprise
# ----------
# PGVector
# Azure AI Search
# Elasticsearch

# Cloud
# -----
# Pinecone
# Qdrant
# Weaviate

# High Performance
# ----------------
# Milvus

# Memory + Search
# ---------------
# Redis

####################################################################
# Common Interview Questions
####################################################################

# Q. What is a Vector Store?
#
# A database optimized for storing vector embeddings
# and performing similarity search.

# Q. Difference between FAISS and Chroma?
#
# FAISS
# -----
# Similarity search library.
# Does not automatically persist data.
#
# Chroma
# -------
# Full vector database with metadata support
# and persistence.

# Q. Which Vector DB did you use?
#
# Example Answer:
#
# I used Azure AI Search in production
# and FAISS for local development.
#
# (or)
#
# I used Chroma locally for prototyping.

# Q. Why PGVector?
#
# It allows vector search directly inside PostgreSQL,
# avoiding another database.

# Q. Which Vector DB is best?
#
# Local Development
# -----------------
# Chroma
#
# Enterprise
# ----------
# Azure AI Search
# PGVector
#
# Large Scale
# -----------
# Pinecone
# Milvus
# Qdrant

####################################################################
# Typical RAG Flow
####################################################################

# Documents
#     │
#     ▼
# Text Splitter
#     │
#     ▼
# Embedding Model
#     │
#     ▼
# Vector Store
#     │
#     ▼
# Retriever
#     │
#     ▼
# LLM
#     │
#     ▼
# Final Answer