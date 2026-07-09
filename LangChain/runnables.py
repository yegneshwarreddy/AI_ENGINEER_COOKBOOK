"""
====================================================================
File: 11_runnables.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Runnables (LCEL)
====================================================================

Description
-----------
Runnables are the core building blocks of modern LangChain.

Everything in LangChain is a Runnable:
✔ LLMs
✔ Prompt Templates
✔ Output Parsers
✔ Retrievers
✔ Chains

They can all be connected together using the "|" operator.

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/runnables/
"""

####################################################################
# RunnableLambda
####################################################################

# Package
# -------
# langchain-core

# Install
# -------
# pip install langchain

from langchain_core.runnables import RunnableLambda

# Purpose
# -------
# Converts a normal Python function into a Runnable.

# Used In
# -------
# ✔ Data Processing
# ✔ Pre-processing
# ✔ Post-processing

# Example

# def uppercase(text):
#     return text.upper()

# runnable = RunnableLambda(uppercase)

# result = runnable.invoke("langchain")

# Output
# ------
# LANGCHAIN

####################################################################
# RunnablePassthrough
####################################################################

from langchain_core.runnables import RunnablePassthrough

# Purpose
# -------
# Passes the input unchanged.

# Used In
# -------
# ✔ RAG
# ✔ Parallel Pipelines
# ✔ LCEL

# Example

# runnable = RunnablePassthrough()

# runnable.invoke("Hello")

# Output
# ------
# Hello

####################################################################
# RunnableParallel
####################################################################

from langchain_core.runnables import RunnableParallel

# Purpose
# -------
# Runs multiple Runnables simultaneously.

# Used In
# -------
# ✔ Parallel Retrieval
# ✔ Multiple LLM Calls
# ✔ Speed Optimization

# Example

# chain = RunnableParallel(
#     summary=summarizer,
#     keywords=keyword_generator
# )

####################################################################
# RunnableSequence
####################################################################

from langchain_core.runnables import RunnableSequence

# Purpose
# -------
# Executes multiple Runnables one after another.

# Used In
# -------
# ✔ Pipelines
# ✔ RAG
# ✔ AI Workflows

# Example

# chain = prompt | llm | parser

# Equivalent

# chain = RunnableSequence(
#     prompt,
#     llm,
#     parser
# )

####################################################################
# RunnableBranch
####################################################################

from langchain_core.runnables import RunnableBranch

# Purpose
# -------
# Executes different branches based on conditions.

# Used In
# -------
# ✔ Conditional Workflows
# ✔ Routing

# Example

# branch = RunnableBranch(
#     (
#         lambda x: x["language"] == "python",
#         python_chain
#     ),
#     default_chain
# )

####################################################################
# RunnableAssign
####################################################################

from langchain_core.runnables import RunnableAssign

# Purpose
# -------
# Adds extra fields to the current input.

# Used In
# -------
# ✔ LangGraph
# ✔ LCEL
# ✔ Data Enrichment

####################################################################
# RunnableMap
####################################################################

from langchain_core.runnables import RunnableMap

# Purpose
# -------
# Maps multiple runnables to different keys.

# Note
# ----
# RunnableMap is essentially an alias of RunnableParallel
# in modern LangChain.

####################################################################
# RunnableConfig
####################################################################

from langchain_core.runnables import RunnableConfig

# Purpose
# -------
# Configuration object passed during execution.

# Common Parameters
# -----------------
# tags
# metadata
# callbacks
# configurable

####################################################################
# RunnableSerializable
####################################################################

from langchain_core.runnables import RunnableSerializable

# Purpose
# -------
# Base class for serializable runnables.

####################################################################
# Common Methods
####################################################################

# invoke()
# -------
# Runs a single input.

# batch()
# ------
# Runs multiple inputs.

# stream()
# -------
# Streams output.

# ainvoke()
# --------
# Async invoke.

# abatch()
# --------
# Async batch.

# astream()
# ---------
# Async streaming.

####################################################################
# LCEL Operator
####################################################################

# The "|" operator connects Runnables.

# Example

# chain = prompt | llm | parser

# Execution Flow
#
# Prompt
#    │
#    ▼
# LLM
#    │
#    ▼
# Output Parser
#    │
#    ▼
# Final Output

####################################################################
# Parallel Example
####################################################################

# chain = RunnableParallel(
#     summary=summarizer,
#     sentiment=sentiment_chain,
#     keywords=keyword_chain
# )

####################################################################
# Batch Example
####################################################################

# results = chain.batch(
#     [
#         {"question":"What is Docker?"},
#         {"question":"What is Kubernetes?"}
#     ]
# )

####################################################################
# Streaming Example
####################################################################

# for chunk in chain.stream(
#     {"question":"Explain AI"}
# ):
#     print(chunk)

####################################################################
# Async Example
####################################################################

# result = await chain.ainvoke(
#     {
#         "question":"Explain RAG"
#     }
# )

####################################################################
# Summary
####################################################################

# RunnableLambda
# --------------
# Python function

# RunnablePassthrough
# -------------------
# Identity function

# RunnableParallel
# ----------------
# Parallel execution

# RunnableSequence
# ----------------
# Sequential execution

# RunnableBranch
# --------------
# Conditional routing

# RunnableAssign
# --------------
# Add new fields

# RunnableMap
# -----------
# Parallel mapping

# RunnableConfig
# --------------
# Runtime configuration

####################################################################
# Common Interview Questions
####################################################################

# Q. What is a Runnable?
#
# A standard interface representing anything
# that can process an input and produce an output.

# Q. Why did LangChain introduce Runnables?
#
# To provide one consistent interface for
# prompts, LLMs, retrievers, tools, parsers,
# and chains.

# Q. What does the "|" operator do?
#
# It pipes the output of one Runnable into
# the next Runnable.

# Q. Difference between invoke() and batch()?
#
# invoke()
# --------
# One input.
#
# batch()
# -------
# Multiple inputs.

# Q. Difference between RunnableParallel and RunnableSequence?
#
# RunnableSequence
# ----------------
# Executes one after another.
#
# RunnableParallel
# ----------------
# Executes simultaneously.

####################################################################
# Typical LCEL Pipeline
####################################################################

# User Question
#       │
#       ▼
# PromptTemplate
#       │
#       ▼
# Chat Model
#       │
#       ▼
# Output Parser
#       │
#       ▼
# Final Response
#
# LCEL Code
#
# chain = prompt | llm | parser
#
# response = chain.invoke(
#     {
#         "question":"Explain Kubernetes"
#     }
# )