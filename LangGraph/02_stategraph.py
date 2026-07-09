"""
====================================================================
File: 02_stategraph.py
Repository: AI-Engineer-Cookbook
Topic: LangGraph StateGraph
====================================================================

Description
-----------
StateGraph is the main class used to build workflows
in LangGraph.

A StateGraph contains:

✔ State
✔ Nodes
✔ Edges
✔ Conditional Edges
✔ Entry Point
✔ Exit Point

Think of it like a roadmap.

Official Documentation
----------------------
https://langchain-ai.github.io/langgraph/
"""

####################################################################
# StateGraph
####################################################################

# Package
# -------
# langgraph.graph

# Install
# -------
# pip install langgraph

from langgraph.graph import StateGraph

# Purpose
# -------
# Creates a graph that passes a shared State
# between multiple nodes.

# Used In
# -------
# ✔ AI Agents
# ✔ Chatbots
# ✔ RAG
# ✔ Multi-Agent Systems
# ✔ Automation

####################################################################
# END
####################################################################

from langgraph.graph import END

# Purpose
# -------
# Represents the end of graph execution.

# Example
#
# graph.add_edge(
#     "chatbot",
#     END
# )

####################################################################
# START
####################################################################

from langgraph.graph import START

# Purpose
# -------
# Represents the starting point of the graph.

# Example
#
# graph.add_edge(
#     START,
#     "chatbot"
# )

####################################################################
# Basic Graph
####################################################################

from typing import TypedDict

class State(TypedDict):

    question: str

    answer: str

# Create Graph

# graph = StateGraph(State)

####################################################################
# Adding Nodes
####################################################################

# graph.add_node(
#     "chatbot",
#     chatbot
# )

####################################################################
# Adding Edges
####################################################################

# graph.add_edge(
#     START,
#     "chatbot"
# )

# graph.add_edge(
#     "chatbot",
#     END
# )

####################################################################
# Compile Graph
####################################################################

# app = graph.compile()

# Purpose
# -------
# Converts the graph definition into an executable graph.

####################################################################
# Invoke Graph
####################################################################

# response = app.invoke(
#     {
#         "question":"Explain Docker",
#         "answer":""
#     }
# )

####################################################################
# Complete Flow
####################################################################

# graph = StateGraph(State)
#
# graph.add_node("chatbot", chatbot)
#
# graph.add_edge(START, "chatbot")
#
# graph.add_edge("chatbot", END)
#
# app = graph.compile()

####################################################################
# Graph Lifecycle
####################################################################

# Create State
#
#        │
#        ▼
#
# Create Graph
#
#        │
#        ▼
#
# Add Nodes
#
#        │
#        ▼
#
# Connect Nodes
#
#        │
#        ▼
#
# Compile
#
#        │
#        ▼
#
# Invoke
#
#        │
#        ▼
#
# Execution

####################################################################
# Graph Architecture
####################################################################

#               START
#                 │
#                 ▼
#
#            Chatbot Node
#
#                 │
#                 ▼
#
#                END

####################################################################
# Graph with Multiple Nodes
####################################################################

#               START
#
#                 │
#
#                 ▼
#
#          Retrieve Node
#
#                 │
#
#                 ▼
#
#           Generate Node
#
#                 │
#
#                 ▼
#
#           Validate Node
#
#                 │
#
#                 ▼
#
#                END

####################################################################
# Graph with Tool Calling
####################################################################

#             START
#
#               │
#
#               ▼
#
#        Planner Node
#
#               │
#
#               ▼
#
#          Tool Node
#
#               │
#
#               ▼
#
#        Final Response
#
#               │
#
#               ▼
#
#              END

####################################################################
# Common Methods
####################################################################

# add_node()

# add_edge()

# add_conditional_edges()

# compile()

####################################################################
# Compile Options
####################################################################

# app = graph.compile()

#
# With Checkpointer
#
# app = graph.compile(
#     checkpointer=memory
# )

#
# With Interrupt
#
# app = graph.compile(
#     interrupt_before=["approval"]
# )

####################################################################
# StateGraph vs Graph
####################################################################

# Graph
# -----
# Simple graph.

#
# StateGraph
# ----------
# Graph +
# Shared State

####################################################################
# Common Errors
####################################################################

# ❌ Forgot compile()

# ❌ Missing START

# ❌ Missing END

# ❌ Node name typo

# ❌ Wrong State schema

####################################################################
# Best Practices
####################################################################

# ✔ One responsibility per node.

# ✔ Keep State small.

# ✔ Always compile once.

# ✔ Use TypedDict.

# ✔ Name nodes clearly.

####################################################################
# Common Interview Questions
####################################################################

# Q. What is StateGraph?
#
# A workflow engine that executes
# nodes while passing a shared State.

# Q. Why compile()?
#
# compile()
# converts the graph definition
# into an executable application.

# Q. Difference between START and END?
#
# START
# -----
# Entry point.
#
# END
# ---
# Exit point.

# Q. What does add_node() do?
#
# Registers a function as a graph node.

# Q. What does add_edge() do?
#
# Connects two nodes.

# Q. Can a graph have multiple nodes?
#
# Yes.
#
# Most production graphs contain
# many connected nodes.

####################################################################
# Real Project Example
####################################################################

# DevOps Agent
#
#             START
#
#                │
#
#                ▼
#
#          Planner Node
#
#                │
#
#                ▼
#
#         Docker Tool Node
#
#                │
#
#                ▼
#
#      Human Approval Node
#
#                │
#
#                ▼
#
#        Execute Command
#
#                │
#
#                ▼
#
#               END

####################################################################
# Summary
####################################################################

# StateGraph
# ----------
# Main graph builder.

# START
# -----
# Graph entry.

# END
# ---
# Graph exit.

# add_node()
# ----------
# Add node.

# add_edge()
# ----------
# Connect nodes.

# compile()
# ---------
# Build executable graph.

####################################################################
# Key Takeaway
####################################################################

# StateGraph defines the workflow.
#
# State stores the data.
#
# Nodes perform the work.
#
# Edges define where execution goes next.
#
# Together, they form a complete AI workflow.