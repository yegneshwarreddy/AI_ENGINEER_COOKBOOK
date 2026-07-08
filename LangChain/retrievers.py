"""
====================================================================
File: 09_retrievers.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Retrievers
====================================================================

Description
-----------
Retrievers fetch the most relevant documents from a vector database
or other data source based on the user's query.

They are one of the core components of every RAG pipeline.

Used In
-------
✔ RAG
✔ Chatbots
✔ AI Search
✔ Question Answering
✔ Agents

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/retrievers/
"""

####################################################################
# Vector Store Retriever
####################################################################

# Purpose
# -------
# Converts any Vector Store into a Retriever.

# Example

# retriever = vectorstore.as_retriever()

# Common Parameters
# -----------------
# search_type
# search_kwargs

# Example

# retriever = vectorstore.as_retriever(
#     search_type="similarity",
#     search_kwargs={
#         "k":4
#     }
# )

# Search Types
# ------------
# similarity
# mmr
# similarity_score_threshold

# Interview Questions
# -------------------
# Q. Why convert a Vector Store into a Retriever?
#
# Retrievers provide a standard interface for fetching
# relevant documents regardless of the underlying
# vector database.

####################################################################
# BaseRetriever
####################################################################

from langchain_core.retrievers import BaseRetriever

# Purpose
# -------
# Parent class of all retrievers.

# Used In
# -------
# ✔ Custom Retrievers

# Example

# class MyRetriever(BaseRetriever):
#     pass

####################################################################
# MultiQueryRetriever
####################################################################

# Package
# -------
# langchain

# Install
# -------
# pip install langchain

from langchain.retrievers.multi_query import MultiQueryRetriever

# Purpose
# -------
# Generates multiple versions of the user's question
# before searching.

# Used In
# -------
# ✔ Better Recall
# ✔ Production RAG

# Example

# retriever = MultiQueryRetriever.from_llm(
#     retriever=vectorstore.as_retriever(),
#     llm=llm
# )

# Interview Questions
# -------------------
# Q. Why use MultiQueryRetriever?
#
# Different wording may retrieve different documents.
# Multiple queries improve recall.

####################################################################
# ContextualCompressionRetriever
####################################################################

from langchain.retrievers import ContextualCompressionRetriever

# Purpose
# -------
# Compresses retrieved documents before
# sending them to the LLM.

# Used In
# -------
# ✔ Reduce Tokens
# ✔ Faster Responses
# ✔ Better Context

# Example

# compression_retriever = ContextualCompressionRetriever(
#     base_retriever=retriever,
#     base_compressor=compressor
# )

####################################################################
# EnsembleRetriever
####################################################################

from langchain.retrievers import EnsembleRetriever

# Purpose
# -------
# Combines multiple retrievers.

# Used In
# -------
# ✔ Hybrid Search
# ✔ Enterprise Search

# Example

# ensemble = EnsembleRetriever(
#     retrievers=[retriever1, retriever2],
#     weights=[0.6,0.4]
# )

####################################################################
# ParentDocumentRetriever
####################################################################

from langchain.retrievers import ParentDocumentRetriever

# Purpose
# -------
# Stores small chunks but returns the
# complete parent document.

# Used In
# -------
# ✔ Long PDFs
# ✔ Books
# ✔ Documentation

####################################################################
# SelfQueryRetriever
####################################################################

from langchain.retrievers.self_query.base import SelfQueryRetriever

# Purpose
# -------
# Uses an LLM to automatically build metadata filters.

# Used In
# -------
# ✔ Metadata Search
# ✔ Enterprise Search

# Example

# User:
# Show documents after 2024.

# Automatically generates metadata filter.

####################################################################
# TimeWeightedVectorStoreRetriever
####################################################################

from langchain.retrievers import TimeWeightedVectorStoreRetriever

# Purpose
# -------
# Prioritizes recently added documents.

# Used In
# -------
# ✔ Memory
# ✔ AI Assistants

####################################################################
# MergerRetriever
####################################################################

from langchain.retrievers import MergerRetriever

# Purpose
# -------
# Merges results from multiple retrievers.

####################################################################
# RePhraseQueryRetriever
####################################################################

from langchain.retrievers.re_phraser import RePhraseQueryRetriever

# Purpose
# -------
# Rewrites the user's question before retrieval.

# Used In
# -------
# ✔ Better Search Quality

####################################################################
# BM25Retriever
####################################################################

# Package
# -------
# langchain-community

from langchain_community.retrievers import BM25Retriever

# Purpose
# -------
# Traditional keyword search.

# Used In
# -------
# ✔ Hybrid Search
# ✔ Exact Keyword Search

# Example

# retriever = BM25Retriever.from_documents(
#     documents
# )

####################################################################
# TFIDFRetriever
####################################################################

from langchain_community.retrievers import TFIDFRetriever

# Purpose
# -------
# TF-IDF based retriever.

# Used In
# -------
# ✔ Classical Information Retrieval

####################################################################
# MultiVectorRetriever
####################################################################

from langchain.retrievers.multi_vector import MultiVectorRetriever

# Purpose
# -------
# Stores multiple embeddings for
# a single document.

####################################################################
# Common Retrieval Methods
####################################################################

# invoke()

# Example

# docs = retriever.invoke(
#     "Explain Docker."
# )

####################################################################
# Common Search Types
####################################################################

# similarity
# mmr
# similarity_score_threshold

####################################################################
# Search Parameters
####################################################################

# k
# ----
# Number of documents to retrieve.

# score_threshold
# ----------------
# Minimum similarity score.

# fetch_k
# --------
# Number of candidate documents.

####################################################################
# Summary
####################################################################

# BaseRetriever
# -------------
# Parent class

# VectorStoreRetriever
# --------------------
# Most commonly used

# MultiQueryRetriever
# -------------------
# Multiple questions

# ContextualCompressionRetriever
# ------------------------------
# Compresses retrieved documents

# EnsembleRetriever
# -----------------
# Combines retrievers

# ParentDocumentRetriever
# -----------------------
# Small chunks
# Large document output

# SelfQueryRetriever
# ------------------
# Metadata filtering

# BM25Retriever
# -------------
# Keyword Search

# TFIDFRetriever
# --------------
# Classical Retrieval

####################################################################
# Common Interview Questions
####################################################################

# Q. Difference between Vector Store and Retriever?
#
# Vector Store
# ------------
# Stores embeddings.
#
# Retriever
# ----------
# Fetches relevant documents.

# Q. What does k mean?
#
# Number of documents returned.

# Q. What is MMR?
#
# Maximum Marginal Relevance.
#
# It balances:
#
# Relevance
# +
# Diversity

# Q. Why use ContextualCompressionRetriever?
#
# It reduces token usage by removing
# irrelevant content before sending
# documents to the LLM.

# Q. Which retriever did you use in your project?
#
# Example Answer:
#
# I used VectorStoreRetriever with
# similarity search and k=4.
#
# Later I added ContextualCompressionRetriever
# with a reranker to improve retrieval quality.

####################################################################
# Typical Retrieval Flow
####################################################################

# User Query
#      │
#      ▼
# Retriever
#      │
#      ▼
# Vector Database
#      │
#      ▼
# Top-K Documents
#      │
#      ▼
# LLM
#      │
#      ▼
# Final Answer