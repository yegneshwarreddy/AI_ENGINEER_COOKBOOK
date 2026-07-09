"""
====================================================================
File: 15_agents.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Agents
====================================================================

Description
-----------
Agents are AI systems capable of reasoning, deciding which tools
to use, executing them, observing the results, and producing a
final answer.

Unlike Chains, Agents dynamically decide what action to take.

Used In
-------
✔ AI Assistants
✔ DevOps Agents
✔ AI Copilots
✔ Customer Support
✔ Automation
✔ Multi Tool Systems

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/agents/
"""

####################################################################
# create_react_agent
####################################################################

# Package
# -------
# langgraph-prebuilt

# Install
# -------
# pip install langgraph

from langgraph.prebuilt import create_react_agent

# Purpose
# -------
# Creates a ReAct (Reason + Act) Agent.

# Used In
# -------
# ✔ Modern LangGraph
# ✔ Tool Calling
# ✔ AI Assistants

# Example

# agent = create_react_agent(
#     model=llm,
#     tools=tools
# )

# response = agent.invoke(
#     {
#         "messages":[
#             ("human","List running Docker containers")
#         ]
#     }
# )

# Interview
# ---------
# Q. What is ReAct?
#
# Reason
# ↓
# Think
#
# Act
# ↓
# Execute Tool
#
# Observe
# ↓
# Continue reasoning
#
# Repeat until final answer.


####################################################################
# create_tool_calling_agent
####################################################################

# Package
# -------
# langchain

from langchain.agents import create_tool_calling_agent

# Purpose
# -------
# Creates a tool-calling agent.

# Used In
# -------
# ✔ OpenAI
# ✔ Claude
# ✔ Gemini
# ✔ Groq

# Example

# agent = create_tool_calling_agent(
#     llm,
#     tools,
#     prompt
# )

####################################################################
# AgentExecutor
####################################################################

from langchain.agents import AgentExecutor

# Purpose
# -------
# Executes the agent loop.

# Responsibilities
# ----------------
# ✔ Call LLM
# ✔ Execute Tool
# ✔ Observe Result
# ✔ Repeat
# ✔ Return Final Answer

# Example

# executor = AgentExecutor(
#     agent=agent,
#     tools=tools,
#     verbose=True
# )

####################################################################
# create_openai_tools_agent
####################################################################

from langchain.agents import create_openai_tools_agent

# Purpose
# -------
# Creates an OpenAI Tool Calling Agent.

# Used In
# -------
# ✔ GPT-4
# ✔ GPT-4.1

####################################################################
# create_openai_functions_agent
####################################################################

from langchain.agents import (
    create_openai_functions_agent
)

# Purpose
# -------
# Creates an OpenAI Function Calling Agent.

# Note
# ----
# Older API.
#
# Modern models use Tool Calling.

####################################################################
# OpenAIFunctionsAgent (Legacy)
####################################################################

from langchain.agents.openai_functions_agent.base import (
    OpenAIFunctionsAgent
)

# Purpose
# -------
# Legacy OpenAI Agent.

####################################################################
# AgentAction
####################################################################

from langchain_core.agents import AgentAction

# Purpose
# -------
# Represents a Tool Call.

####################################################################
# AgentFinish
####################################################################

from langchain_core.agents import AgentFinish

# Purpose
# -------
# Represents completion of the agent.

####################################################################
# AgentScratchPad
####################################################################

# Purpose
# -------
# Internal reasoning history.

# Example

# Thought:
# I should inspect Docker.

# Action:
# docker_ps

# Observation:
# nginx container running

# Thought:
# Need logs.

# Action:
# docker_logs

# Observation:
# Port already in use.

# Final Answer:
# Restart container.

####################################################################
# Typical Agent Loop
####################################################################

# User
#   │
#   ▼
# LLM
#   │
#   ▼
# Think
#   │
#   ▼
# Choose Tool
#   │
#   ▼
# Execute Tool
#   │
#   ▼
# Observe Result
#   │
#   ▼
# Need Another Tool?
#
# Yes ───────────────┐
#                    │
#                    ▼
#                Think Again
#
# No
#
# ▼
#
# Final Answer

####################################################################
# Agent vs Chain
####################################################################

# Chain
# -----
# Fixed workflow.

# Prompt
# ↓
# LLM
# ↓
# Output

# Agent
# -----
# Dynamic workflow.

# Think
# ↓
# Tool
# ↓
# Observe
# ↓
# Think Again

####################################################################
# Common Agent Parameters
####################################################################

# tools
# model
# prompt
# verbose
# max_iterations
# return_intermediate_steps

####################################################################
# Agent Methods
####################################################################

# invoke()

# ainvoke()

# stream()

# batch()

####################################################################
# Common Agent Types
####################################################################

# ReAct Agent

# Tool Calling Agent

# OpenAI Tools Agent

# OpenAI Functions Agent

# JSON Agent

# XML Agent

####################################################################
# Real World Examples
####################################################################

# DevOps Agent
#
# Tools:
#
# docker_ps()
#
# docker_logs()
#
# kubectl_get_pods()
#
# kubectl_describe()
#
# restart_container()

###############################################################

# Finance Agent
#
# Tools
#
# Stock Price
#
# News
#
# Calculator
#
# SQL

###############################################################

# Customer Support Agent
#
# CRM Tool
#
# Ticket Tool
#
# Email Tool

###############################################################

# Research Agent
#
# Search Tool
#
# Wikipedia
#
# PDF Loader
#
# Vector DB

####################################################################
# Summary
####################################################################

# create_react_agent()
# --------------------
# ⭐ Modern LangGraph Agent

# create_tool_calling_agent()
# ---------------------------
# Tool Calling

# AgentExecutor
# -------------
# Runs Agent Loop

# create_openai_tools_agent()
# ---------------------------
# GPT Tool Calling

# create_openai_functions_agent()
# -------------------------------
# Legacy

# AgentAction
# -----------
# Tool execution

# AgentFinish
# -----------
# Final response

####################################################################
# Common Interview Questions
####################################################################

# Q. What is an Agent?
#
# An AI system capable of reasoning,
# selecting tools,
# executing them,
# observing results,
# and deciding the next step.

# Q. Difference between Chain and Agent?
#
# Chain
# -----
# Fixed workflow.
#
# Agent
# -----
# Dynamic workflow.

# Q. What is ReAct?
#
# Reason + Act.
#
# Think
# ↓
# Tool
# ↓
# Observe
# ↓
# Think Again

# Q. What is AgentExecutor?
#
# Executes the complete reasoning loop.

# Q. What is AgentScratchPad?
#
# Internal reasoning history used by the
# agent between tool calls.

# Q. Which Agent did you build?
#
# Example Answer:
#
# I built a DevOps AI Agent using LangGraph.
#
# The agent used Docker and Kubernetes tools,
# PostgreSQL memory,
# human approval,
# and Groq/Ollama LLMs.
#
# It could inspect containers,
# fetch logs,
# troubleshoot Kubernetes,
# and execute infrastructure tasks.

####################################################################
# Modern Recommendation
####################################################################

# New Projects
# ------------
# ✔ LangGraph
# ✔ create_react_agent()

# Legacy Projects
# ---------------
# create_tool_calling_agent()

# Avoid New Development
# ---------------------
# OpenAI Functions Agent

####################################################################
# Complete Agent Architecture
####################################################################

#               User
#                 │
#                 ▼
#            Chat Model
#                 │
#          Think / Reason
#                 │
#                 ▼
#         Select Appropriate Tool
#                 │
#                 ▼
#           Execute Tool
#                 │
#                 ▼
#         Observe Tool Result
#                 │
#         Need More Tools?
#        Yes ───────────────► Repeat
#                 │
#                No
#                 │
#                 ▼
#          Generate Final Answer

####################################################################
# End of LangChain Cookbook
####################################################################