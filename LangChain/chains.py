"""
====================================================================
File: 14_chains.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Chains
====================================================================

Description
-----------
Chains connect multiple LangChain components together.

Examples:

Prompt
   │
   ▼
LLM
   │
   ▼
Parser

or

Retriever
     │
     ▼
Documents
     │
     ▼
Prompt
     │
     ▼
LLM
     │
     ▼
Answer

Modern LangChain uses LCEL (| operator)
instead of many legacy chain classes.

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/chains/
"""

####################################################################
# create_stuff_documents_chain
####################################################################

# Package
# -------
# langchain

# Install
# -------
# pip install langchain

from langchain.chains.combine_documents import (
    create_stuff_documents_chain
)

# Purpose
# -------
# Combines retrieved documents into one prompt
# before sending them to the LLM.

# Used In
# -------
# ✔ RAG
# ✔ Chatbots
# ✔ Question Answering

# Example

# chain = create_stuff_documents_chain(
#     llm,
#     prompt
# )

# Interview
# ---------
# Q. What does "Stuff" mean?
#
# It stuffs all retrieved documents
# into one prompt.


####################################################################
# create_retrieval_chain
####################################################################

from langchain.chains import create_retrieval_chain

# Purpose
# -------
# Complete Retrieval-Augmented Generation chain.

# Used In
# -------
# ✔ Modern RAG
# ✔ Production

# Example

# retrieval_chain = create_retrieval_chain(
#     retriever,
#     document_chain
# )

# response = retrieval_chain.invoke(
#     {
#         "input":"Explain Docker"
#     }
# )


####################################################################
# create_history_aware_retriever
####################################################################

from langchain.chains import create_history_aware_retriever

# Purpose
# -------
# Uses previous conversation
# to rewrite the current question.

# Used In
# -------
# ✔ Chatbots
# ✔ AI Assistants

# Example

# history_retriever = create_history_aware_retriever(
#     llm,
#     retriever,
#     prompt
# )


####################################################################
# create_retrieval_chain Flow
####################################################################

# User
#   │
#   ▼
# Retriever
#   │
#   ▼
# Retrieved Documents
#   │
#   ▼
# Stuff Documents Chain
#   │
#   ▼
# LLM
#   │
#   ▼
# Final Answer


####################################################################
# LLMChain (Legacy)
####################################################################

from langchain.chains import LLMChain

# Purpose
# -------
# Legacy prompt + LLM chain.

# Status
# ------
# Deprecated

# Modern Replacement
# ------------------
# prompt | llm

# Old Example

# chain = LLMChain(
#     prompt=prompt,
#     llm=llm
# )

# Modern Example

# chain = prompt | llm


####################################################################
# RetrievalQA (Legacy)
####################################################################

from langchain.chains import RetrievalQA

# Purpose
# -------
# Old RAG chain.

# Status
# ------
# Deprecated

# Modern Replacement
# ------------------
# create_retrieval_chain()

# Interview
# ---------
# Older tutorials still use RetrievalQA.


####################################################################
# SequentialChain (Legacy)
####################################################################

from langchain.chains import SequentialChain

# Purpose
# -------
# Executes multiple chains sequentially.

# Status
# ------
# Mostly replaced by LCEL.


####################################################################
# SimpleSequentialChain (Legacy)
####################################################################

from langchain.chains import SimpleSequentialChain

# Purpose
# -------
# Simple sequential execution.

# Status
# ------
# Deprecated in favor of RunnableSequence.


####################################################################
# TransformChain
####################################################################

from langchain.chains import TransformChain

# Purpose
# -------
# Applies Python transformations
# inside a chain.


####################################################################
# Router Chains (Legacy)
####################################################################

from langchain.chains.router import MultiPromptChain

# Purpose
# -------
# Routes questions to different prompts.

# Modern Replacement
# ------------------
# RunnableBranch
# LangGraph


####################################################################
# ConversationChain (Legacy)
####################################################################

from langchain.chains import ConversationChain

# Purpose
# -------
# Simple chatbot.

# Modern Replacement
# ------------------
# LangGraph


####################################################################
# Common Chain Methods
####################################################################

# invoke()

# ainvoke()

# batch()

# stream()


####################################################################
# Modern LCEL Chain
####################################################################

# prompt
#      │
#      ▼
# llm
#      │
#      ▼
# parser

# Code

# chain = prompt | llm | parser


####################################################################
# Modern RAG Pipeline
####################################################################

# Documents
#      │
#      ▼
# Splitter
#      │
#      ▼
# Embeddings
#      │
#      ▼
# Vector DB
#      │
#      ▼
# Retriever
#      │
#      ▼
# create_stuff_documents_chain()
#      │
#      ▼
# create_retrieval_chain()
#      │
#      ▼
# Answer


####################################################################
# Summary
####################################################################

# create_retrieval_chain()
# ------------------------
# ⭐ Modern RAG

# create_stuff_documents_chain()
# ------------------------------
# Combine retrieved docs

# create_history_aware_retriever()
# --------------------------------
# Chat history

# LLMChain
# --------
# Legacy

# RetrievalQA
# -----------
# Legacy

# ConversationChain
# -----------------
# Legacy

# SequentialChain
# ---------------
# Legacy


####################################################################
# Common Interview Questions
####################################################################

# Q. What is a Chain?
#
# A sequence of components
# connected together.

# Q. What replaced LLMChain?
#
# LCEL

# Example
#
# prompt | llm

# Q. What replaced RetrievalQA?
#
# create_retrieval_chain()

# Q. What does Stuff Documents Chain do?
#
# It combines retrieved documents
# into a single prompt.

# Q. Which chain did you use?
#
# Example Answer
#
# I used create_retrieval_chain()
# with create_stuff_documents_chain()
# for my RAG application.

####################################################################
# Version Notes
####################################################################

# LangChain v1.x prefers:

# LCEL
# RunnableSequence
# create_retrieval_chain()

# instead of older Chain classes.