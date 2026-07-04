"""
====================================================================
File: 06_document_loaders.py
Repository: AI-Engineer-Cookbook
Topic: LangChain Document Loaders
====================================================================

Description
-----------
Document Loaders load data from different sources into LangChain
Document objects.

Every RAG pipeline starts with a Document Loader.

Used In
-------
✔ RAG
✔ Chatbots
✔ Search Engines
✔ Knowledge Bases
✔ AI Assistants

Official Documentation
----------------------
https://python.langchain.com/docs/integrations/document_loaders/
"""

####################################################################
# TextLoader
####################################################################

# Package
# -------
# langchain-community

# Install
# -------
# pip install langchain-community

from langchain_community.document_loaders import TextLoader

# Purpose
# -------
# Loads plain text (.txt) files.

# Example

# loader = TextLoader("notes.txt")
# documents = loader.load()

# Methods
# -------
# load()
# lazy_load()

# Used In
# -------
# ✔ TXT Files
# ✔ Notes
# ✔ Logs


####################################################################
# PyPDFLoader
####################################################################

from langchain_community.document_loaders import PyPDFLoader

# Purpose
# -------
# Loads PDF files page by page.

# Example

# loader = PyPDFLoader("book.pdf")
# docs = loader.load()

# Used In
# -------
# ✔ Research Papers
# ✔ Books
# ✔ Documentation


####################################################################
# DirectoryLoader
####################################################################

from langchain_community.document_loaders import DirectoryLoader

# Purpose
# -------
# Loads all supported files from a folder.

# Example

# loader = DirectoryLoader(
#     "./documents"
# )

# docs = loader.load()

# Used In
# -------
# ✔ RAG
# ✔ Bulk Ingestion


####################################################################
# CSVLoader
####################################################################

from langchain_community.document_loaders import CSVLoader

# Purpose
# -------
# Loads CSV files.

# Example

# loader = CSVLoader(
#     file_path="employees.csv"
# )

# docs = loader.load()


####################################################################
# JSONLoader
####################################################################

from langchain_community.document_loaders import JSONLoader

# Purpose
# -------
# Loads JSON documents.

# Example

# loader = JSONLoader(
#     file_path="data.json",
#     jq_schema="."
# )

# docs = loader.load()


####################################################################
# Docx2txtLoader
####################################################################

from langchain_community.document_loaders import Docx2txtLoader

# Purpose
# -------
# Loads Microsoft Word documents.

# Example

# loader = Docx2txtLoader(
#     "resume.docx"
# )

# docs = loader.load()


####################################################################
# UnstructuredPDFLoader
####################################################################

from langchain_community.document_loaders import (
    UnstructuredPDFLoader
)

# Purpose
# -------
# Extracts text from complex PDFs.

# Used In
# -------
# ✔ OCR
# ✔ Tables
# ✔ Images

# Example

# loader = UnstructuredPDFLoader(
#     "report.pdf"
# )


####################################################################
# UnstructuredWordDocumentLoader
####################################################################

from langchain_community.document_loaders import (
    UnstructuredWordDocumentLoader
)

# Purpose
# -------
# Loads Word documents using Unstructured.


####################################################################
# UnstructuredMarkdownLoader
####################################################################

from langchain_community.document_loaders import (
    UnstructuredMarkdownLoader
)

# Purpose
# -------
# Loads Markdown files.

# Example

# loader = UnstructuredMarkdownLoader(
#     "README.md"
# )


####################################################################
# WebBaseLoader
####################################################################

from langchain_community.document_loaders import WebBaseLoader

# Purpose
# -------
# Loads webpages.

# Example

# loader = WebBaseLoader(
#     "https://python.langchain.com"
# )

# docs = loader.load()

# Used In
# -------
# ✔ Web Scraping
# ✔ Website RAG


####################################################################
# SeleniumURLLoader
####################################################################

from langchain_community.document_loaders import SeleniumURLLoader

# Purpose
# -------
# Loads JavaScript-rendered webpages.

# Used In
# -------
# ✔ Dynamic Websites


####################################################################
# BSHTMLLoader
####################################################################

from langchain_community.document_loaders import BSHTMLLoader

# Purpose
# -------
# Loads local HTML files.


####################################################################
# GitLoader
####################################################################

from langchain_community.document_loaders import GitLoader

# Purpose
# -------
# Loads an entire Git repository.

# Example

# loader = GitLoader(
#     clone_url="https://github.com/..."
# )


####################################################################
# NotionDBLoader
####################################################################

from langchain_community.document_loaders import NotionDBLoader

# Purpose
# -------
# Loads data from Notion databases.


####################################################################
# ConfluenceLoader
####################################################################

from langchain_community.document_loaders import ConfluenceLoader

# Purpose
# -------
# Loads Atlassian Confluence pages.


####################################################################
# S3FileLoader
####################################################################

from langchain_community.document_loaders import S3FileLoader

# Purpose
# -------
# Loads files stored in AWS S3.


####################################################################
# AzureBlobStorageFileLoader
####################################################################

from langchain_community.document_loaders import (
    AzureBlobStorageFileLoader
)

# Purpose
# -------
# Loads files from Azure Blob Storage.


####################################################################
# GoogleDriveLoader
####################################################################

from langchain_community.document_loaders import GoogleDriveLoader

# Purpose
# -------
# Loads files from Google Drive.


####################################################################
# YoutubeLoader
####################################################################

from langchain_community.document_loaders import YoutubeLoader

# Purpose
# -------
# Loads YouTube transcripts.

# Example

# loader = YoutubeLoader.from_youtube_url(
#     "https://youtube.com/watch?v=xxxx"
# )


####################################################################
# OutlookMessageLoader
####################################################################

from langchain_community.document_loaders import (
    OutlookMessageLoader
)

# Purpose
# -------
# Loads Outlook email files.


####################################################################
# UnstructuredEmailLoader
####################################################################

from langchain_community.document_loaders import (
    UnstructuredEmailLoader
)

# Purpose
# -------
# Loads .eml email files.


####################################################################
# EverNoteLoader
####################################################################

from langchain_community.document_loaders import EverNoteLoader

# Purpose
# -------
# Loads Evernote notebooks.


####################################################################
# OneNoteLoader
####################################################################

from langchain_community.document_loaders.onenote import (
    OneNoteLoader
)

# Purpose
# -------
# Loads Microsoft OneNote pages.


####################################################################
# NotebookLoader
####################################################################

from langchain_community.document_loaders import NotebookLoader

# Purpose
# -------
# Loads Jupyter Notebook (.ipynb) files.


####################################################################
# Summary
####################################################################

# Local Files
# -----------
# TextLoader
# PyPDFLoader
# CSVLoader
# JSONLoader
# Docx2txtLoader
# NotebookLoader

# Office Documents
# ----------------
# Word
# Outlook
# OneNote

# Web
# ---
# WebBaseLoader
# SeleniumURLLoader
# BSHTMLLoader

# Cloud
# -----
# S3FileLoader
# AzureBlobStorageFileLoader
# GoogleDriveLoader

# Enterprise
# ----------
# NotionDBLoader
# ConfluenceLoader

# Media
# -----
# YoutubeLoader

####################################################################
# Common Interview Questions
####################################################################

# Q. What does a Document Loader return?
#
# A list of LangChain Document objects.

# Q. What is inside a Document object?
#
# page_content
# metadata

# Example
#
# Document(
#     page_content="Docker is...",
#     metadata={
#         "source":"book.pdf",
#         "page":3
#     }
# )

# Q. Which loader did you use in your project?
#
# Example Answer:
#
# I used PyPDFLoader for simple PDFs.
# For complex PDFs containing tables and images,
# I used Unstructured and Docling.

# Q. Why use DirectoryLoader?
#
# It loads multiple files from a directory automatically,
# making bulk ingestion easy for RAG pipelines.