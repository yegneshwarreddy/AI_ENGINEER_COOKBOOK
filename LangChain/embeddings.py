"""
====================================================================
File: 05_embeddings.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Embeddings
====================================================================

Description
-----------
Embeddings convert text into numerical vectors so that
machines can understand semantic meaning.

Embeddings are the foundation of every RAG application.

Used In
-------
✔ RAG
✔ Vector Databases
✔ Semantic Search
✔ Recommendation Systems
✔ Similarity Search

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/embedding_models/
"""

####################################################################
# HuggingFaceEmbeddings
####################################################################

# Package
# -------
# langchain-huggingface

# Install
# -------
# pip install langchain-huggingface sentence-transformers

from langchain_huggingface import HuggingFaceEmbeddings

# Purpose
# -------
# Generates embeddings locally using HuggingFace models.

# When to Use
# -----------
# ✔ Local Development
# ✔ No API Cost
# ✔ Production
# ✔ RAG

# Example

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# Popular Models
# --------------
# all-MiniLM-L6-v2
# all-mpnet-base-v2
# BAAI/bge-small-en-v1.5
# BAAI/bge-base-en-v1.5
# BAAI/bge-large-en-v1.5
# nomic-ai/nomic-embed-text-v1

# Common Methods
# --------------
# embed_query()
# embed_documents()

# Example

# vector = embeddings.embed_query(
#     "What is Kubernetes?"
# )

# docs = embeddings.embed_documents(
#     [
#         "Docker",
#         "Kubernetes",
#         "LangChain"
#     ]
# )

# Interview Questions
# -------------------
# Q. Difference between embed_query() and embed_documents()?
#
# embed_query()
# Generates one embedding.
#
# embed_documents()
# Generates embeddings for multiple documents.


####################################################################
# OpenAIEmbeddings
####################################################################

# Package
# -------
# langchain-openai

# Install
# -------
# pip install langchain-openai

from langchain_openai import OpenAIEmbeddings

# Purpose
# -------
# Uses OpenAI embedding models.

# When to Use
# -----------
# ✔ Production
# ✔ OpenAI APIs
# ✔ High-quality embeddings

# Example

# embeddings = OpenAIEmbeddings(
#     model="text-embedding-3-small"
# )

# Popular Models
# --------------
# text-embedding-3-small
# text-embedding-3-large

# Common Methods
# --------------
# embed_query()
# embed_documents()


####################################################################
# OllamaEmbeddings
####################################################################

# Package
# -------
# langchain-ollama

# Install
# -------
# pip install langchain-ollama

from langchain_ollama import OllamaEmbeddings

# Purpose
# -------
# Generates embeddings locally through Ollama.

# When to Use
# -----------
# ✔ Offline RAG
# ✔ Local AI Applications

# Example

# embeddings = OllamaEmbeddings(
#     model="nomic-embed-text"
# )

# Popular Models
# --------------
# nomic-embed-text
# mxbai-embed-large

# Common Methods
# --------------
# embed_query()
# embed_documents()


####################################################################
# GoogleGenerativeAIEmbeddings
####################################################################

# Package
# -------
# langchain-google-genai

# Install
# -------
# pip install langchain-google-genai

from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Purpose
# -------
# Generates embeddings using Google's Gemini API.

# Example

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/text-embedding-004"
# )

# Popular Models
# --------------
# models/text-embedding-004


####################################################################
# AzureOpenAIEmbeddings
####################################################################

# Package
# -------
# langchain-openai

from langchain_openai import AzureOpenAIEmbeddings

# Purpose
# -------
# Generates embeddings using Azure OpenAI.

# Example

# embeddings = AzureOpenAIEmbeddings(
#     model="text-embedding-3-small"
# )

# Used In
# -------
# ✔ Enterprise AI
# ✔ Azure AI Search
# ✔ Production


####################################################################
# VoyageAIEmbeddings
####################################################################

# Package
# -------
# langchain-voyageai

# Install
# -------
# pip install langchain-voyageai

from langchain_voyageai import VoyageAIEmbeddings

# Purpose
# -------
# High-quality embeddings for production RAG.

# Example

# embeddings = VoyageAIEmbeddings(
#     model="voyage-large-2"
# )


####################################################################
# FakeEmbeddings
####################################################################

# Package
# -------
# langchain-core

from langchain_core.embeddings import FakeEmbeddings

# Purpose
# -------
# Generates fake vectors for testing.

# Used In
# -------
# ✔ Unit Testing
# ✔ Development

# Example

# embeddings = FakeEmbeddings(
#     size=768
# )


####################################################################
# Embeddings Interface
####################################################################

from langchain_core.embeddings import Embeddings

# Purpose
# -------
# Base class for all embedding models.

# Used In
# -------
# ✔ Custom Embedding Models


####################################################################
# Summary
####################################################################

# HuggingFaceEmbeddings
# ---------------------
# Local embeddings

# OpenAIEmbeddings
# ----------------
# OpenAI API

# AzureOpenAIEmbeddings
# ---------------------
# Azure OpenAI

# OllamaEmbeddings
# ----------------
# Local Ollama embeddings

# GoogleGenerativeAIEmbeddings
# ----------------------------
# Gemini embeddings

# VoyageAIEmbeddings
# ------------------
# Premium production embeddings

# FakeEmbeddings
# --------------
# Testing

# Embeddings
# ----------
# Base interface


####################################################################
# Frequently Asked Interview Questions
####################################################################

# Q. What is an embedding?
#
# A numerical vector representation of text that captures semantic meaning.

# Q. Why don't we store raw text inside a vector database?
#
# Vector databases search using numerical vectors, not plain text.

# Q. What is embedding dimension?
#
# The length of the generated vector.
#
# Example:
#
# [0.23, -0.11, 0.92, ...]
#
# 384 dimensions
# 768 dimensions
# 1024 dimensions
# 1536 dimensions
# 3072 dimensions

# Q. What is cosine similarity?
#
# Measures semantic similarity between two vectors.

# Q. Which embedding model is best for local RAG?
#
# BAAI/bge-large-en-v1.5
# all-mpnet-base-v2
# nomic-embed-text
# mxbai-embed-large

# Q. Which embedding model did you use in your project?
#
# Example Answer:
#
# I used sentence-transformers/all-MiniLM-L6-v2
# because it provides a good balance between
# speed, memory usage and retrieval quality.