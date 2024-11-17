# AI-Powered Web Search and Information Extraction Agent

This project is an AI agent that reads data from a CSV file or Google Sheet, performs web searches for specific information based on a user-defined query, and leverages a language model (LLM) to extract structured information. The extracted data is displayed in a Streamlit dashboard and can be downloaded as a CSV or uploaded back to a Google Sheet.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Workflow](#workflow)
- [File Structure](#file-structure)
- [License](#license)

## Features

- **CSV and Google Sheets Input**: Upload a CSV file or connect to a Google Sheet for data input.
- **Dynamic Query Input**: Define custom queries with placeholders for dynamic information extraction (e.g., "Get the email of {company}").
- **Automated Web Search**: Perform web searches for each entity using a search API (e.g., SerpAPI).
- **LLM-based Information Extraction**: Use an LLM (e.g., OpenAI's GPT) to extract structured information from search results.
- **Data Display and Export**: View results in a table, download as CSV, or upload to Google Sheets.
- **Optional Features**: Advanced query templates, error handling, and Google Sheets output integration.

## Tech Stack

- **Frontend/Dashboard**: Streamlit
- **Data Handling**: pandas for CSV, Google Sheets API for Sheets
- **Web Search API**: SerpAPI, ScraperAPI, or similar (requires API key)
- **LLM API**: OpenAI's GPT or Groq (requires API key)
- **Backend**: Python (agent handling and API integration)

## To run code in console

- streamlit run app.py

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AsmeetaaDutta/ai-agent-project.git
   cd ai-agent-project
