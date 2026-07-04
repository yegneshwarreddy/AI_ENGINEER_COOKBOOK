"""
====================================================================
File: 02_prompts.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Prompt Templates
====================================================================

Description
-----------
Prompt Templates help create dynamic prompts by inserting variables
instead of hardcoding text.

They are one of the most commonly used components in LangChain.

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/prompt_templates/

"""

####################################################################
# PromptTemplate
####################################################################

# Package
# -------
# langchain-core

# Install
# -------
# pip install langchain

from langchain_core.prompts import PromptTemplate

# Purpose
# -------
# Used for text-based prompts.

# When to Use
# -----------
# ✔ Simple prompts
# ✔ RAG
# ✔ Summarization
# ✔ Translation
# ✔ Text Generation

# Example

# prompt = PromptTemplate.from_template(
#     "Explain {topic} in simple words."
# )

# formatted_prompt = prompt.invoke(
#     {"topic": "Vector Databases"}
# )

# Output
# ------
# Explain Vector Databases in simple words.

# Important Methods
# -----------------
# from_template()
# format()
# invoke()

# Interview Questions
# -------------------
# Q. Why use PromptTemplate instead of Python f-strings?
#
# PromptTemplate safely manages variables,
# supports LangChain pipelines,
# and integrates with Runnables.

# Documentation
# -------------
# https://python.langchain.com/docs/concepts/prompt_templates/


####################################################################
# ChatPromptTemplate
####################################################################

# Package
# -------
# langchain-core

from langchain_core.prompts import ChatPromptTemplate

# Purpose
# -------
# Creates structured prompts for chat models.

# When to Use
# -----------
# ✔ GPT
# ✔ Claude
# ✔ Gemini
# ✔ Groq
# ✔ Ollama Chat Models

# Example

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are an AI Tutor."),
#         ("human", "{question}")
#     ]
# )

# prompt.invoke(
#     {
#         "question": "Explain Kubernetes."
#     }
# )

# Output
# ------
# System:
# You are an AI Tutor.
#
# Human:
# Explain Kubernetes.

# Important Methods
# -----------------
# from_messages()
# from_template()
# invoke()

# Interview Questions
# -------------------
# Q. Difference between PromptTemplate and ChatPromptTemplate?
#
# PromptTemplate
# --------------
# Produces plain text.
#
# ChatPromptTemplate
# ------------------
# Produces structured chat messages
# (System, Human, AI).

# Documentation
# -------------
# https://python.langchain.com/docs/concepts/prompt_templates/


####################################################################
# MessagesPlaceholder
####################################################################

# Package
# -------
# langchain-core

from langchain_core.prompts import MessagesPlaceholder

# Purpose
# -------
# Inserts conversation history into prompts.

# When to Use
# -----------
# ✔ Chatbots
# ✔ Memory
# ✔ Agents
# ✔ Multi-turn conversations

# Example

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful assistant."),
#         MessagesPlaceholder("history"),
#         ("human", "{question}")
#     ]
# )

# Interview Questions
# -------------------
# Q. Why use MessagesPlaceholder?
#
# It dynamically injects chat history
# into the prompt without rebuilding it.

# Documentation
# -------------
# https://python.langchain.com/docs/concepts/prompt_templates/


####################################################################
# PipelinePromptTemplate
####################################################################

# Package
# -------
# langchain-core

from langchain_core.prompts import PipelinePromptTemplate

# Purpose
# -------
# Combines multiple PromptTemplates
# into one reusable pipeline.

# When to Use
# -----------
# ✔ Complex prompt engineering
# ✔ Multi-stage prompting

# Example

# introduction = PromptTemplate.from_template(
#     "You are an AI assistant."
# )
#
# question = PromptTemplate.from_template(
#     "Question: {question}"
# )
#
# pipeline = PipelinePromptTemplate(
#     final_prompt=question,
#     pipeline_prompts=[
#         ("intro", introduction)
#     ]
# )

# Interview Questions
# -------------------
# Q. When should you use PipelinePromptTemplate?
#
# When prompts are built in multiple reusable stages.

# Documentation
# -------------
# https://python.langchain.com/docs/


####################################################################
# Few-Shot PromptTemplate
####################################################################

# Package
# -------
# langchain-core

from langchain_core.prompts import FewShotPromptTemplate

# Purpose
# -------
# Creates prompts using examples.

# When to Use
# -----------
# ✔ Classification
# ✔ Structured Outputs
# ✔ Better Accuracy

# Example

# examples = [
#     {
#         "question": "2+2",
#         "answer": "4"
#     },
#     {
#         "question": "3+5",
#         "answer": "8"
#     }
# ]

# example_prompt = PromptTemplate.from_template(
#     "Question: {question}\nAnswer: {answer}"
# )

# few_shot = FewShotPromptTemplate(
#     examples=examples,
#     example_prompt=example_prompt,
#     suffix="Question: {input}",
#     input_variables=["input"]
# )

# Interview Questions
# -------------------
# Q. What is Few-Shot Prompting?
#
# Giving the LLM several examples
# before asking the real question.

# Documentation
# -------------
# https://python.langchain.com/docs/


####################################################################
# Summary
####################################################################

# PromptTemplate
# --------------
# Simple text prompts.

# ChatPromptTemplate
# ------------------
# Chat model prompts.

# MessagesPlaceholder
# -------------------
# Conversation history.

# PipelinePromptTemplate
# ----------------------
# Multi-stage prompts.

# FewShotPromptTemplate
# ---------------------
# Example-based prompting.