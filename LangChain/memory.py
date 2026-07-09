"""
====================================================================
File: 12_memory.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Memory
====================================================================

Description
-----------
Memory enables LLM applications to remember previous interactions.

Traditional LangChain Memory stores conversation history.

Modern LangChain applications usually use LangGraph Checkpointers
instead of legacy memory classes.

Used In
-------
✔ Chatbots
✔ AI Assistants
✔ Agents
✔ Customer Support
✔ Multi-turn Conversations

Official Documentation
----------------------
https://python.langchain.com/docs/
"""

####################################################################
# ConversationBufferMemory (Legacy)
####################################################################

# Package
# -------
# langchain

# Install
# -------
# pip install langchain

from langchain.memory import ConversationBufferMemory

# Purpose
# -------
# Stores the complete conversation history.

# Used In
# -------
# ✔ Simple Chatbots
# ✔ Tutorials
# ✔ Legacy Projects

# Example

# memory = ConversationBufferMemory(
#     return_messages=True
# )

# Important Parameters
# --------------------
# return_messages
# memory_key
# input_key
# output_key

# Interview Questions
# -------------------
# Q. What is ConversationBufferMemory?
#
# Stores the entire conversation without removing messages.

####################################################################
# ConversationBufferWindowMemory (Legacy)
####################################################################

from langchain.memory import ConversationBufferWindowMemory

# Purpose
# -------
# Stores only the last K conversations.

# Used In
# -------
# ✔ Reduce Token Usage
# ✔ Chatbots

# Example

# memory = ConversationBufferWindowMemory(
#     k=5
# )

# Important Parameters
# --------------------
# k
# return_messages

####################################################################
# ConversationSummaryMemory (Legacy)
####################################################################

from langchain.memory import ConversationSummaryMemory

# Purpose
# -------
# Summarizes old conversations using an LLM.

# Used In
# -------
# ✔ Long Conversations
# ✔ AI Assistants

# Example

# memory = ConversationSummaryMemory(
#     llm=llm
# )

####################################################################
# ConversationSummaryBufferMemory (Legacy)
####################################################################

from langchain.memory import ConversationSummaryBufferMemory

# Purpose
# -------
# Combines summarization and buffer memory.

# Used In
# -------
# ✔ Long-term conversations

####################################################################
# ConversationTokenBufferMemory (Legacy)
####################################################################

from langchain.memory import ConversationTokenBufferMemory

# Purpose
# -------
# Maintains memory based on token count.

# Used In
# -------
# ✔ GPT Models
# ✔ Token Management

####################################################################
# VectorStoreRetrieverMemory (Legacy)
####################################################################

from langchain.memory import VectorStoreRetrieverMemory

# Purpose
# -------
# Stores conversation inside a vector database.

# Used In
# -------
# ✔ Semantic Memory
# ✔ AI Assistants

####################################################################
# CombinedMemory (Legacy)
####################################################################

from langchain.memory import CombinedMemory

# Purpose
# -------
# Combines multiple memory objects.

# Used In
# -------
# ✔ Complex Applications

####################################################################
# ReadOnlySharedMemory (Legacy)
####################################################################

from langchain.memory import ReadOnlySharedMemory

# Purpose
# -------
# Read-only memory wrapper.

####################################################################
# ChatMessageHistory
####################################################################

from langchain_core.chat_history import BaseChatMessageHistory

# Purpose
# -------
# Base interface for chat history storage.

# Used In
# -------
# ✔ Custom Memory
# ✔ LangGraph

####################################################################
# InMemoryChatMessageHistory
####################################################################

from langchain_core.chat_history import (
    InMemoryChatMessageHistory
)

# Purpose
# -------
# Stores chat history in RAM.

# Example

# history = InMemoryChatMessageHistory()

####################################################################
# Common Memory Methods
####################################################################

# save_context()

# load_memory_variables()

# clear()

####################################################################
# Memory Flow
####################################################################

# User
#   │
#   ▼
# LLM
#   │
#   ▼
# Memory
#   │
#   ▼
# Store Conversation
#   │
#   ▼
# Future Questions

####################################################################
# Modern LangChain Recommendation
####################################################################

# Instead of:
#
# ConversationBufferMemory
#
# Modern Applications Prefer:
#
# LangGraph Checkpointer
#
# Example
#
# MemorySaver
# PostgreSQL Checkpointer
# Redis Checkpointer

####################################################################
# Summary
####################################################################

# ConversationBufferMemory
# ------------------------
# Entire conversation

# ConversationBufferWindowMemory
# ------------------------------
# Last K messages

# ConversationSummaryMemory
# -------------------------
# LLM generated summary

# ConversationSummaryBufferMemory
# -------------------------------
# Buffer + Summary

# ConversationTokenBufferMemory
# -----------------------------
# Token-based memory

# VectorStoreRetrieverMemory
# --------------------------
# Semantic Memory

# CombinedMemory
# --------------
# Multiple memories

# InMemoryChatMessageHistory
# --------------------------
# RAM storage

####################################################################
# Common Interview Questions
####################################################################

# Q. What is Memory?
#
# Memory stores previous conversations so
# the LLM can maintain context.

# Q. Why not always use ConversationBufferMemory?
#
# Because the conversation keeps growing,
# increasing token usage and cost.

# Q. Which memory is best?
#
# Small Chatbot
# -------------
# ConversationBufferMemory
#
# Long Conversations
# ------------------
# ConversationSummaryMemory
#
# Production AI Systems
# ---------------------
# LangGraph Checkpointer
# PostgreSQL
# Redis

# Q. What did you use in your project?
#
# Example Answer:
#
# I used PostgreSQL to persist conversation
# history and LangGraph checkpoints to
# maintain state across sessions.
#
# This is more scalable than the legacy
# memory classes.

####################################################################
# Version Notes
####################################################################

# ⚠ Legacy APIs
# -------------
# Most classes in langchain.memory are
# considered legacy.
#
# Modern LangChain applications typically
# use LangGraph persistence instead.