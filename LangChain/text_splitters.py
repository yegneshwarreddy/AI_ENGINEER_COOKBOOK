"""
====================================================================
File: 07_text_splitters.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Text Splitters
====================================================================

Description
-----------
Text Splitters divide large documents into smaller chunks before
creating embeddings.

Chunking improves retrieval quality and reduces token usage.

Used In
-------
✔ RAG
✔ Semantic Search
✔ Vector Databases
✔ Chatbots
✔ AI Search

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/text_splitters/
"""

####################################################################
# RecursiveCharacterTextSplitter
####################################################################

# Package
# -------
# langchain-text-splitters

# Install
# -------
# pip install langchain-text-splitters

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Purpose
# -------
# The most commonly used text splitter.
#
# It recursively splits text using:
# Paragraphs
# ↓
# New Lines
# ↓
# Spaces
# ↓
# Characters

# Used In
# -------
# ✔ RAG
# ✔ PDFs
# ✔ Books
# ✔ Documentation

# Example

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200
# )

# chunks = splitter.split_documents(documents)

# Important Parameters
# --------------------
# chunk_size
# chunk_overlap
# separators
# length_function

# Interview Questions
# -------------------
# Q. Why is RecursiveCharacterTextSplitter preferred?
#
# It preserves context better than fixed-size chunking.

####################################################################
# CharacterTextSplitter
####################################################################

from langchain_text_splitters import CharacterTextSplitter

# Purpose
# -------
# Splits text using a fixed separator.

# Example

# splitter = CharacterTextSplitter(
#     separator="\n",
#     chunk_size=1000,
#     chunk_overlap=100
# )

# chunks = splitter.split_documents(documents)

# Used In
# -------
# ✔ Logs
# ✔ CSV
# ✔ Structured Text

####################################################################
# TokenTextSplitter
####################################################################

from langchain_text_splitters import TokenTextSplitter

# Purpose
# -------
# Splits text based on token count instead of characters.

# Used In
# -------
# ✔ GPT Models
# ✔ Claude
# ✔ Gemini
# ✔ Token-sensitive applications

# Example

# splitter = TokenTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

####################################################################
# MarkdownTextSplitter
####################################################################

from langchain_text_splitters import MarkdownTextSplitter

# Purpose
# -------
# Splits Markdown files while preserving headings.

# Used In
# -------
# ✔ README.md
# ✔ Documentation
# ✔ GitHub Repositories

# Example

# splitter = MarkdownTextSplitter()

####################################################################
# HTMLHeaderTextSplitter
####################################################################

from langchain_text_splitters import HTMLHeaderTextSplitter

# Purpose
# -------
# Splits HTML using heading tags.

# Used In
# -------
# ✔ Websites
# ✔ Documentation

# Example

# headers = [
#     ("h1", "Header 1"),
#     ("h2", "Header 2"),
# ]

# splitter = HTMLHeaderTextSplitter(headers)

####################################################################
# PythonCodeTextSplitter
####################################################################

from langchain_text_splitters import PythonCodeTextSplitter

# Purpose
# -------
# Splits Python code intelligently.

# Used In
# -------
# ✔ Code RAG
# ✔ AI Coding Assistants

# Example

# splitter = PythonCodeTextSplitter()

####################################################################
# Language
####################################################################

from langchain_text_splitters import Language

# Purpose
# -------
# Specifies programming language for code splitting.

# Supported Languages
# -------------------
# PYTHON
# JAVA
# CPP
# GO
# JS
# TS
# RUST
# PHP

####################################################################
# RecursiveCharacterTextSplitter.from_language()
####################################################################

# Example

# splitter = RecursiveCharacterTextSplitter.from_language(
#     language=Language.PYTHON,
#     chunk_size=1000,
#     chunk_overlap=100
# )

####################################################################
# NLTKTextSplitter
####################################################################

from langchain_text_splitters import NLTKTextSplitter

# Purpose
# -------
# Splits text into sentences using NLTK.

# Used In
# -------
# ✔ NLP
# ✔ Research Papers

####################################################################
# SpacyTextSplitter
####################################################################

from langchain_text_splitters import SpacyTextSplitter

# Purpose
# -------
# Splits text using SpaCy NLP.

# Used In
# -------
# ✔ NLP Pipelines
# ✔ Linguistic Analysis

####################################################################
# SentenceTransformersTokenTextSplitter
####################################################################

from langchain_text_splitters import (
    SentenceTransformersTokenTextSplitter
)

# Purpose
# -------
# Splits text using SentenceTransformer tokenizer.

# Used In
# -------
# ✔ BGE
# ✔ MiniLM
# ✔ MPNet

####################################################################
# Summary
####################################################################

# RecursiveCharacterTextSplitter
# ------------------------------
# ⭐ Most Popular
# Best for RAG

# CharacterTextSplitter
# ---------------------
# Fixed separator

# TokenTextSplitter
# -----------------
# Token-based chunking

# MarkdownTextSplitter
# --------------------
# Markdown

# HTMLHeaderTextSplitter
# ----------------------
# HTML

# PythonCodeTextSplitter
# ----------------------
# Code RAG

# NLTKTextSplitter
# ----------------
# Sentence-based

# SpacyTextSplitter
# -----------------
# NLP

####################################################################
# Common Interview Questions
####################################################################

# Q. Why do we split documents?
#
# Large documents exceed the model's context window.
# Chunking makes retrieval faster and more accurate.

# Q. What is chunk_size?
#
# Maximum size of each chunk.

# Q. What is chunk_overlap?
#
# Number of overlapping characters/tokens between chunks.

# Example
#
# Chunk 1:
# ----------
# LangChain is a framework for...

# Chunk 2:
# ----------
# framework for building LLM applications...

# The repeated text helps preserve context.

# Q. Which splitter is used most in production?
#
# RecursiveCharacterTextSplitter

# Q. Which splitter did you use in your project?
#
# Example Answer:
#
# I used RecursiveCharacterTextSplitter
# with chunk_size=500 and chunk_overlap=100
# because it preserved semantic context while
# maintaining good retrieval quality.

####################################################################
# Recommended Chunk Sizes
####################################################################

# Small Documents
# ---------------
# chunk_size = 300
# overlap = 50

# General PDFs
# ------------
# chunk_size = 500
# overlap = 100

# Large Books
# -----------
# chunk_size = 1000
# overlap = 200

# Code Files
# ----------
# chunk_size = 200
# overlap = 20

# Research Papers
# ---------------
# chunk_size = 800
# overlap = 150