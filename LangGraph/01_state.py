"""
====================================================================
File: 01_state.py
Repository: AI-Engineer-Cookbook
Topic: LangGraph State
====================================================================

Description
-----------
State is the heart of every LangGraph application.

Every Node reads the current State,
modifies it,
and returns an updated State.

Think of State as a shared dictionary that travels
through the graph.

Without State,
LangGraph cannot function.

Official Documentation
----------------------
https://langchain-ai.github.io/langgraph/
"""

####################################################################
# TypedDict
####################################################################

# Package
# -------
# typing

from typing import TypedDict

# Purpose
# -------
# Defines the structure of the graph state.

# Why TypedDict?
# --------------
# ✔ Type Safety
# ✔ Autocomplete
# ✔ Better Readability
# ✔ Easier Debugging

# Example

# class State(TypedDict):
#
#     question: str
#     answer: str

####################################################################
# Basic State Example
####################################################################

from typing import TypedDict

class State(TypedDict):

    question: str
    answer: str

# Example State

# {
#     "question":"What is Docker?",
#     "answer":""
# }

####################################################################
# State Flow
####################################################################

# Initial State
#
# {
#     "question":"Explain Kubernetes",
#     "answer":""
# }

#
# Node 1
#
# Reads
#
# question
#
# Writes
#
# answer
#
#
# Updated State
#
# {
#     "question":"Explain Kubernetes",
#     "answer":"Kubernetes is..."
# }

####################################################################
# Multiple Variables
####################################################################

class AgentState(TypedDict):

    question: str

    documents: list

    answer: str

    retry_count: int

    tool_output: str

    next_node: str

# Purpose
# -------
# Real applications usually contain
# many state variables.

####################################################################
# State with Messages
####################################################################

from langchain_core.messages import AnyMessage

class ChatState(TypedDict):

    messages: list[AnyMessage]

# Used In
# -------
# ✔ Chatbots
# ✔ AI Assistants
# ✔ Multi-turn Conversations

####################################################################
# State with Annotated
####################################################################

from typing import Annotated

from operator import add

class ConversationState(TypedDict):

    messages: Annotated[list, add]

# Purpose
# -------
# Automatically appends new messages
# instead of replacing them.

# Without Annotated
#
# Old Messages
# ↓
# Replaced

# With Annotated
#
# Old Messages
# +
# New Messages

####################################################################
# Complex Production State
####################################################################

class DevOpsState(TypedDict):

    user_query: str

    docker_logs: str

    kubernetes_output: str

    tool_result: str

    llm_response: str

    retry_count: int

    approval_required: bool

    approved: bool

    final_answer: str

# Example
#
# {
#   "user_query":"Restart nginx container",
#   "docker_logs":"",
#   "tool_result":"",
#   "approved":False
# }

####################################################################
# State Lifecycle
####################################################################

# User
#   │
#   ▼
#
# Initial State
#
#   │
#   ▼
#
# Node 1
#
# Reads State
#
# Updates State
#
# Returns State
#
#   │
#   ▼
#
# Node 2
#
# Reads Updated State
#
# Updates Again
#
# Returns
#
#   │
#   ▼
#
# Final State

####################################################################
# Rules
####################################################################

# ✔ Every Node receives State.

# ✔ Every Node returns State.

# ✔ Nodes should not modify
#    global variables.

# ✔ State is immutable in concept.
#    Return updated values.

####################################################################
# Example Node
####################################################################

# def chatbot(
#     state: State
# ):
#
#     question = state["question"]
#
#     answer = llm.invoke(question)
#
#     return {
#         "answer":answer
#     }

####################################################################
# Common State Variables
####################################################################

# messages

# question

# answer

# documents

# tool_output

# current_step

# next_node

# retry_count

# user_id

# session_id

# memory

####################################################################
# State vs Variables
####################################################################

# Python Variables
#
# x = 10
#
# Exists only inside function.

#
# LangGraph State
#
# Shared by
#
# Every Node
#
# Every Edge
#
# Entire Graph

####################################################################
# State Diagram
####################################################################

#              Graph State
#
#     ┌─────────────────────────────┐
#     │                             │
#     │ question                    │
#     │ answer                      │
#     │ messages                    │
#     │ tool_result                 │
#     │ retry_count                 │
#     │ documents                   │
#     │                             │
#     └─────────────────────────────┘
#
#              ▲
#              │
#
#     Every Node Reads/Writes

####################################################################
# Best Practices
####################################################################

# ✔ Keep State small.

# ✔ Store only useful data.

# ✔ Avoid duplicate values.

# ✔ Use TypedDict.

# ✔ Use meaningful variable names.

# ✔ Store messages separately.

####################################################################
# Common Mistakes
####################################################################

# ❌ Huge State

# ❌ Duplicate variables

# ❌ Global variables

# ❌ Missing return statement

# ❌ Returning wrong keys

####################################################################
# Common Interview Questions
####################################################################

# Q. What is State?
#
# Shared data passed between every node.

# Q. Why use TypedDict?
#
# Type Safety
# Better readability
# IDE support

# Q. Can multiple nodes access State?
#
# Yes.
#
# Every node receives the current State.

# Q. Can nodes modify State?
#
# Yes.
#
# They return updated values.

# Q. What happens if a node
# doesn't update anything?
#
# The previous values remain unchanged.

####################################################################
# Real Project Example
####################################################################

# In my DevOps AI Agent,
# the State contained:
#
# user_query
#
# docker_logs
#
# kubernetes_output
#
# approval_required
#
# approved
#
# final_answer
#
# Every node updated only
# the fields it was responsible for.

####################################################################
# Summary
####################################################################

# TypedDict
# ---------
# Defines State schema

# State
# -----
# Shared data

# Node
# ----
# Reads State

# Node
# ----
# Updates State

# Node
# ----
# Returns State

# Graph
# -----
# Passes updated State to next node

####################################################################
# Key Takeaway
####################################################################

# Everything in LangGraph revolves around State.
#
# No State
# →
# No Graph
#
# Understand State first,
# and the rest of LangGraph becomes much easier.