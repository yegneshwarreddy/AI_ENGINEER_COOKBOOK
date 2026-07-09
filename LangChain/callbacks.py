"""
====================================================================
File: 13_callbacks.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Callbacks
====================================================================

Description
-----------
Callbacks allow you to monitor, log, stream and trace everything
that happens inside a LangChain application.

Callbacks are useful for:

✔ Streaming Responses
✔ Logging
✔ Monitoring
✔ Debugging
✔ LangSmith Tracing
✔ Token Usage
✔ Observability

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/callbacks/
"""

####################################################################
# BaseCallbackHandler
####################################################################

# Package
# -------
# langchain-core

# Install
# -------
# pip install langchain

from langchain_core.callbacks import BaseCallbackHandler

# Purpose
# -------
# Parent class for all callback handlers.

# Used In
# -------
# ✔ Custom Logging
# ✔ Monitoring
# ✔ Analytics

# Example

# class MyHandler(BaseCallbackHandler):
#
#     def on_llm_start(self, *args, **kwargs):
#         print("LLM Started")
#
#     def on_llm_end(self, *args, **kwargs):
#         print("LLM Finished")


####################################################################
# StreamingStdOutCallbackHandler
####################################################################

# Package
# -------
# langchain

from langchain.callbacks.streaming_stdout import (
    StreamingStdOutCallbackHandler
)

# Purpose
# -------
# Streams generated tokens directly to the terminal.

# Used In
# -------
# ✔ CLI Chatbots
# ✔ Streaming
# ✔ Debugging

# Example

# callback = StreamingStdOutCallbackHandler()

# llm = ChatOpenAI(
#     streaming=True,
#     callbacks=[callback]
# )


####################################################################
# FileCallbackHandler
####################################################################

from langchain.callbacks.file import FileCallbackHandler

# Purpose
# -------
# Saves callback events into a log file.

# Example

# callback = FileCallbackHandler(
#     "logs.txt"
# )


####################################################################
# StdOutCallbackHandler
####################################################################

from langchain.callbacks.stdout import StdOutCallbackHandler

# Purpose
# -------
# Prints callback events to the terminal.

# Used In
# -------
# ✔ Debugging
# ✔ Development


####################################################################
# CallbackManager
####################################################################

from langchain_core.callbacks import CallbackManager

# Purpose
# -------
# Manages multiple callback handlers.

# Example

# manager = CallbackManager(
#     [
#         StdOutCallbackHandler(),
#         StreamingStdOutCallbackHandler()
#     ]
# )


####################################################################
# AsyncCallbackManager
####################################################################

from langchain_core.callbacks import AsyncCallbackManager

# Purpose
# -------
# Async version of CallbackManager.

# Used In
# -------
# ✔ FastAPI
# ✔ Async Applications


####################################################################
# Common Callback Events
####################################################################

# on_chain_start()

# on_chain_end()

# on_llm_start()

# on_llm_end()

# on_tool_start()

# on_tool_end()

# on_agent_action()

# on_agent_finish()

# on_retriever_start()

# on_retriever_end()

# on_retry()

# on_text()

# on_chat_model_start()


####################################################################
# Custom Callback Example
####################################################################

# class Logger(BaseCallbackHandler):
#
#     def on_llm_start(self, *args, **kwargs):
#         print("LLM Started")
#
#     def on_llm_end(self, *args, **kwargs):
#         print("LLM Finished")
#
#     def on_tool_start(self, *args, **kwargs):
#         print("Tool Started")
#
#     def on_tool_end(self, *args, **kwargs):
#         print("Tool Finished")


####################################################################
# LangSmith Tracing
####################################################################

# Install
# -------
# pip install langsmith

# Purpose
# -------
# LangSmith automatically records:
#
# Prompt
# Response
# Tokens
# Latency
# Errors
# Tool Calls
# Agent Steps
# Graph Execution

# Environment Variables

# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_API_KEY=xxxxxxxx
# LANGCHAIN_PROJECT=my-project


####################################################################
# Streaming Flow
####################################################################

# User
#   │
#   ▼
# Prompt
#   │
#   ▼
# LLM
#   │
#   ▼
# Callback
#   │
#   ▼
# Stream Tokens
#   │
#   ▼
# User


####################################################################
# Common Use Cases
####################################################################

# ✔ Logging

# ✔ Streaming Tokens

# ✔ Monitoring

# ✔ Token Counting

# ✔ Cost Calculation

# ✔ Debugging

# ✔ LangSmith

# ✔ Performance Metrics


####################################################################
# Summary
####################################################################

# BaseCallbackHandler
# -------------------
# Parent class

# CallbackManager
# ---------------
# Multiple callbacks

# AsyncCallbackManager
# --------------------
# Async callbacks

# StreamingStdOutCallbackHandler
# ------------------------------
# Streams tokens

# StdOutCallbackHandler
# ---------------------
# Terminal logging

# FileCallbackHandler
# -------------------
# File logging


####################################################################
# Common Interview Questions
####################################################################

# Q. What are Callbacks?
#
# Callback functions executed whenever
# an event occurs inside LangChain.

# Q. Why use callbacks?
#
# Logging
# Streaming
# Monitoring
# Debugging

# Q. What is StreamingStdOutCallbackHandler?
#
# Streams tokens as they are generated.

# Q. Which callback did you use?
#
# Example Answer:
#
# I used StreamingStdOutCallbackHandler
# during local development.
#
# For production, I used LangSmith
# tracing to monitor prompts,
# responses, latency,
# token usage and errors.

####################################################################
# Best Practices
####################################################################

# ✔ Use LangSmith in production.

# ✔ Stream responses whenever possible.

# ✔ Log errors.

# ✔ Track latency.

# ✔ Track token usage.

# ✔ Build custom callbacks for monitoring.

####################################################################
# Version Notes
####################################################################

# Modern LangChain recommends
# LangSmith for observability instead
# of writing large custom callback systems.