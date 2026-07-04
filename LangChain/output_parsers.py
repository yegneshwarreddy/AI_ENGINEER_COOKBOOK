"""
====================================================================
File: 04_output_parsers.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Output Parsers
====================================================================

Description
-----------
Output Parsers convert raw LLM responses into structured formats
such as strings, JSON, lists, dictionaries, or Pydantic objects.

They are commonly used in:
✔ RAG
✔ Agents
✔ APIs
✔ Structured Output
✔ LangGraph

Official Documentation
----------------------
https://python.langchain.com/docs/concepts/output_parsers/
"""

####################################################################
# StrOutputParser
####################################################################

# Package
# -------
# langchain-core

# Install
# -------
# pip install langchain

from langchain_core.output_parsers import StrOutputParser

# Purpose
# -------
# Converts the LLM response into a plain string.

# Used In
# -------
# ✔ Chatbots
# ✔ RAG
# ✔ APIs
# ✔ Summarization

# Example

# parser = StrOutputParser()

# chain = prompt | llm | parser

# result = chain.invoke(
#     {"question": "What is Docker?"}
# )

# Interview Questions
# -------------------
# Q. Why use StrOutputParser?
#
# It extracts only the text response from the LLM.

# Documentation
# -------------
# https://python.langchain.com/docs/


####################################################################
# JsonOutputParser
####################################################################

from langchain_core.output_parsers import JsonOutputParser

# Purpose
# -------
# Parses the LLM response into a JSON object.

# Used In
# -------
# ✔ APIs
# ✔ Structured Outputs
# ✔ Automation
# ✔ Agents

# Example

# parser = JsonOutputParser()

# chain = prompt | llm | parser

# Output
# ------
# {
#   "name":"John",
#   "age":25
# }

# Interview Questions
# -------------------
# Q. Why use JsonOutputParser?
#
# It ensures machine-readable responses.


####################################################################
# PydanticOutputParser
####################################################################

from langchain_core.output_parsers import PydanticOutputParser

# Purpose
# -------
# Parses responses directly into Pydantic models.

# Used In
# -------
# ✔ FastAPI
# ✔ APIs
# ✔ Production AI Systems

# Example

# from pydantic import BaseModel

# class Person(BaseModel):
#     name: str
#     age: int

# parser = PydanticOutputParser(
#     pydantic_object=Person
# )

# Interview Questions
# -------------------
# Q. Why use PydanticOutputParser?
#
# It validates the LLM output automatically.


####################################################################
# CommaSeparatedListOutputParser
####################################################################

from langchain_core.output_parsers import (
    CommaSeparatedListOutputParser
)

# Purpose
# -------
# Converts comma-separated text into a Python list.

# Example

# parser = CommaSeparatedListOutputParser()

# Output
# ------
# Python, Java, Go

# becomes

# [
#     "Python",
#     "Java",
#     "Go"
# ]

# Used In
# -------
# ✔ Skills Extraction
# ✔ Tags
# ✔ Keyword Generation


####################################################################
# ListOutputParser
####################################################################

from langchain_core.output_parsers.list import ListOutputParser

# Purpose
# -------
# Base class for list parsers.

# Used In
# -------
# ✔ Custom Output Parsers


####################################################################
# BaseOutputParser
####################################################################

from langchain_core.output_parsers import BaseOutputParser

# Purpose
# -------
# Base class for all output parsers.

# Used In
# -------
# ✔ Custom Parser Development

# Example

# class MyParser(BaseOutputParser):
#
#     def parse(self, text):
#         return text.upper()


####################################################################
# OutputFixingParser
####################################################################

from langchain.output_parsers import OutputFixingParser

# Purpose
# -------
# Automatically fixes invalid LLM outputs.

# Used In
# -------
# ✔ JSON Validation
# ✔ APIs
# ✔ Production Systems

# Example

# fixing_parser = OutputFixingParser.from_llm(
#     parser=parser,
#     llm=llm
# )

# Interview Questions
# -------------------
# Q. Why use OutputFixingParser?
#
# It retries and repairs malformed outputs.


####################################################################
# RetryOutputParser
####################################################################

from langchain.output_parsers import RetryOutputParser

# Purpose
# -------
# Automatically retries parsing if parsing fails.

# Used In
# -------
# ✔ Production
# ✔ APIs
# ✔ Automation

# Interview Questions
# -------------------
# Q. Difference between RetryOutputParser and OutputFixingParser?
#
# RetryOutputParser
# -----------------
# Generates a new answer.
#
# OutputFixingParser
# ------------------
# Repairs the existing answer.


####################################################################
# Summary
####################################################################

# StrOutputParser
# ---------------
# Plain text

# JsonOutputParser
# ----------------
# JSON object

# PydanticOutputParser
# --------------------
# Pydantic Model

# CommaSeparatedListOutputParser
# ------------------------------
# Python List

# BaseOutputParser
# ----------------
# Parent class

# OutputFixingParser
# ------------------
# Repairs invalid output

# RetryOutputParser
# -----------------
# Regenerates output if parsing fails