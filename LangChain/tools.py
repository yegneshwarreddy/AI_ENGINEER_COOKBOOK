"""
====================================================================
File: 10_tools.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Tools
====================================================================

Description
-----------
Tools allow LLMs and Agents to interact with external systems.

A Tool is simply a Python function wrapped in a format that
LangChain Agents can understand and invoke.

Used In
-------
✔ Agents
✔ LangGraph
✔ MCP
✔ RAG
✔ Automation
✔ APIs

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/tools/
"""

####################################################################
# tool Decorator
####################################################################

# Package
# -------
# langchain-core

# Install
# -------
# pip install langchain

from langchain_core.tools import tool

# Purpose
# -------
# Converts a Python function into a LangChain Tool.

# Used In
# -------
# ✔ Agents
# ✔ LangGraph
# ✔ Tool Calling

# Example

# @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers."""
#     return a * b

# Interview Questions
# -------------------
# Q. What is a Tool?
#
# A Python function that an LLM can call to
# perform external actions.

####################################################################
# StructuredTool
####################################################################

from langchain_core.tools import StructuredTool

# Purpose
# -------
# Creates a tool with structured input arguments.

# Used In
# -------
# ✔ Multiple Parameters
# ✔ Validation
# ✔ APIs

# Example

# def add(a: int, b: int):
#     return a + b
#
# tool = StructuredTool.from_function(add)

####################################################################
# BaseTool
####################################################################

from langchain_core.tools import BaseTool

# Purpose
# -------
# Parent class for all LangChain tools.

# Used In
# -------
# ✔ Custom Tool Development

# Example

# class MyTool(BaseTool):
#     name = "calculator"
#     description = "Performs calculations."

####################################################################
# Tool
####################################################################

from langchain_core.tools import Tool

# Purpose
# -------
# Creates a tool manually.

# Example

# search_tool = Tool(
#     name="Search",
#     func=search_function,
#     description="Search the internet."
# )

####################################################################
# ToolException
####################################################################

from langchain_core.tools import ToolException

# Purpose
# -------
# Exception raised during tool execution.

# Used In
# -------
# ✔ Error Handling

####################################################################
# InjectedToolArg
####################################################################

from langchain_core.tools import InjectedToolArg

# Purpose
# -------
# Injects hidden arguments into tools.
#
# Usually used internally by LangGraph.

####################################################################
# InjectedToolCallId
####################################################################

from langchain_core.tools import InjectedToolCallId

# Purpose
# -------
# Gives access to the Tool Call ID.

# Used In
# -------
# ✔ ToolMessage
# ✔ LangGraph

####################################################################
# Runnable as Tool
####################################################################

# Any Runnable can become a Tool.

# Example

# tool = runnable.as_tool()

####################################################################
# Common Tool Methods
####################################################################

# invoke()
# ainvoke()
# batch()
# abatch()

####################################################################
# Example Tool
####################################################################

# @tool
# def get_weather(city: str):
#     """
#     Returns weather information.
#     """
#
#     return f"Weather in {city} is 30°C"

####################################################################
# Tool Schema
####################################################################

# LangChain automatically creates a schema
# from the function signature.

# Example

# @tool
# def divide(
#     a: int,
#     b: int
# ) -> float:
#
#     """Divide two numbers."""
#
#     return a / b

####################################################################
# Tool Calling Flow
####################################################################

# User
#   │
#   ▼
# Agent
#   │
#   ▼
# Tool
#   │
#   ▼
# Python Function
#   │
#   ▼
# Result
#   │
#   ▼
# LLM
#   │
#   ▼
# Final Answer

####################################################################
# Best Practices
####################################################################

# ✔ Keep tools small.
# ✔ One responsibility per tool.
# ✔ Write meaningful descriptions.
# ✔ Use type hints.
# ✔ Handle exceptions.
# ✔ Return clean outputs.

####################################################################
# Summary
####################################################################

# tool
# ----
# Decorator for creating tools.

# StructuredTool
# --------------
# Tool with structured input.

# Tool
# ----
# Manual tool creation.

# BaseTool
# --------
# Parent class.

# ToolException
# -------------
# Error handling.

# InjectedToolArg
# ---------------
# Hidden arguments.

# InjectedToolCallId
# ------------------
# Tool Call ID.

####################################################################
# Common Interview Questions
####################################################################

# Q. What is a Tool?
#
# A Python function exposed to an LLM.

# Q. Difference between Tool and StructuredTool?
#
# Tool
# ----
# Simple wrapper.
#
# StructuredTool
# --------------
# Uses structured schemas and validation.

# Q. Why use @tool decorator?
#
# It automatically generates:
#
# ✔ Name
# ✔ Description
# ✔ JSON Schema
# ✔ Parameters

# Q. Can an Agent call multiple tools?
#
# Yes.
#
# Modern Agents can call one or many tools
# depending on the task.

# Q. Which tools did you build?
#
# Example Answer:
#
# Docker Tool
# Kubernetes Tool
# SQL Tool
# Search Tool
# Calculator Tool
# Weather Tool
#
# In my DevOps Agent project, I built custom
# Docker and Kubernetes tools that allowed the
# agent to inspect containers, fetch logs,
# list pods, and describe Kubernetes resources.