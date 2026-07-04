"""
====================================================================
File: 01_chat_models.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Chat Models
====================================================================

Description
-----------
This file contains the most commonly used Chat Models in LangChain.

Whenever you need to connect an LLM, open this file and copy the
required import and initialization code.

Official Documentation
----------------------
https://python.langchain.com/

"""

import os

####################################################################
# ChatOllama
####################################################################

# Package
# -------
# langchain-ollama

# Install
# -------
# pip install langchain-ollama

from langchain_ollama import ChatOllama

# Purpose
# -------
# Runs Large Language Models locally through Ollama.

# When to Use
# -----------
# ✔ Local Development
# ✔ No API Cost
# ✔ Offline Applications
# ✔ Privacy Sensitive Applications

# Example

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0
)

# Important Parameters
# --------------------
# model
# temperature
# num_ctx
# top_p
# top_k
# num_predict
# repeat_penalty

# Interview Questions
# -------------------
# Q. Why use ChatOllama instead of Ollama Python package?
#
# ChatOllama integrates directly with LangChain,
# allowing Prompt Templates, Tools, Agents,
# Memory and Chains.

# Documentation
# -------------
# https://python.langchain.com/docs/integrations/chat/ollama/


####################################################################
# ChatGroq
####################################################################

# Package
# -------
# langchain-groq

# Install
# -------
# pip install langchain-groq

from langchain_groq import ChatGroq

# Purpose
# -------
# Connects LangChain to Groq Cloud LLMs.

# When to Use
# -----------
# ✔ Extremely Fast Inference
# ✔ Production Applications
# ✔ API Hosted Models

# Example

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Popular Models
# --------------
# llama-3.3-70b-versatile
# deepseek-r1-distill-llama-70b
# mixtral-8x7b
# gemma2-9b-it

# Important Parameters
# --------------------
# model
# temperature
# max_tokens
# timeout
# max_retries

# Interview Questions
# -------------------
# Q. Why is Groq so fast?
#
# Groq uses its own custom hardware called LPUs
# (Language Processing Units), optimized for
# LLM inference.

# Documentation
# -------------
# https://python.langchain.com/docs/integrations/chat/groq/


####################################################################
# ChatOpenAI
####################################################################

# Package
# -------
# langchain-openai

# Install
# -------
# pip install langchain-openai

from langchain_openai import ChatOpenAI

# Purpose
# -------
# Connects LangChain to OpenAI GPT models.

# When to Use
# -----------
# ✔ GPT Models
# ✔ Function Calling
# ✔ Production APIs
# ✔ Reasoning Models

# Example

llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0
)

# Popular Models
# --------------
# gpt-4.1
# gpt-4.1-mini
# gpt-4o
# gpt-4o-mini
# o3
# o4-mini

# Important Parameters
# --------------------
# model
# temperature
# max_tokens
# timeout
# max_retries

# Interview Questions
# -------------------
# Q. Difference between ChatOpenAI and OpenAI?
#
# ChatOpenAI is designed for chat-based LLMs
# using the Chat Completions API.

# Documentation
# -------------
# https://python.langchain.com/docs/integrations/chat/openai/


####################################################################
# ChatGoogleGenerativeAI
####################################################################

# Package
# -------
# langchain-google-genai

# Install
# -------
# pip install langchain-google-genai

from langchain_google_genai import ChatGoogleGenerativeAI

# Purpose
# -------
# Connects LangChain to Google's Gemini models.

# When to Use
# -----------
# ✔ Gemini Models
# ✔ Long Context Applications
# ✔ Multimodal Tasks
# ✔ Google AI Studio

# Example

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro"
)

# Popular Models
# --------------
# gemini-2.5-pro
# gemini-2.5-flash
# gemini-2.0-flash

# Important Parameters
# --------------------
# model
# temperature
# max_output_tokens
# top_p
# top_k

# Interview Questions
# -------------------
# Q. What is Gemini?
#
# Gemini is Google's family of Large Language Models
# supporting text, images, audio and code.

# Documentation
# -------------
# https://python.langchain.com/docs/integrations/chat/google_generative_ai/


####################################################################
# ChatAnthropic
####################################################################

# Package
# -------
# langchain-anthropic

# Install
# -------
# pip install langchain-anthropic

from langchain_anthropic import ChatAnthropic

# Purpose
# -------
# Connects LangChain to Anthropic Claude models.

# When to Use
# -----------
# ✔ Claude Models
# ✔ Long Context
# ✔ Coding Assistants
# ✔ Enterprise AI

# Example

llm = ChatAnthropic(
    model="claude-4-sonnet"
)

# Popular Models
# --------------
# claude-4-opus
# claude-4-sonnet
# claude-3.7-sonnet

# Important Parameters
# --------------------
# model
# temperature
# max_tokens

# Interview Questions
# -------------------
# Q. Why do many companies choose Claude?
#
# Claude is known for strong reasoning,
# coding performance and very large context windows.

# Documentation
# -------------
# https://python.langchain.com/docs/integrations/chat/anthropic/


####################################################################
# ChatMistralAI
####################################################################

# Package
# -------
# langchain-mistralai

# Install
# -------
# pip install langchain-mistralai

from langchain_mistralai import ChatMistralAI

# Purpose
# -------
# Connects LangChain to Mistral AI hosted models.

# Example

llm = ChatMistralAI(
    model="mistral-large-latest"
)

# Popular Models
# --------------
# mistral-large-latest
# ministral-8b
# codestral

# Documentation
# -------------
# https://python.langchain.com/docs/integrations/chat/mistralai/


####################################################################
# Summary
####################################################################

# Local Models
# ------------
# ChatOllama

# Cloud Models
# ------------
# ChatOpenAI
# ChatGroq
# ChatGoogleGenerativeAI
# ChatAnthropic
# ChatMistralAI