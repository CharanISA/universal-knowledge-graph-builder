# Universal Knowledge Graph Builder

## Overview

Universal Knowledge Graph Builder is a document intelligence application that converts unstructured text into an interactive knowledge graph. The system extracts entities, identifies relationships between concepts, visualizes those relationships as a graph, and allows users to explore document connections through natural-language questions.

## Problem

Large documents often contain important relationships that are difficult to identify manually. Researchers, analysts, and organizations spend significant time connecting information across documents.

This project helps users quickly discover:

* Key entities
* Relationships between concepts
* Dependencies between topics
* Knowledge structures hidden within text

## Features

### Document Ingestion

* Paste text directly into the application
* Process unstructured document content

### Entity Extraction

* Identifies:

  * People
  * Organizations
  * Locations
  * Dates
  * Other named entities

### Relationship Detection

* Finds relationships between entities appearing within the same sentence
* Builds connections automatically

### Interactive Knowledge Graph

* Visualizes entities as nodes
* Visualizes relationships as edges
* Interactive graph exploration

### Natural Language Questions

Examples:

* How is Microsoft related to OpenAI?
* Show all dependencies.
* What connections exist for Google?

## Tech Stack

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask

### NLP

* spaCy

### Graph Processing

* NetworkX

### Visualization

* PyVis

### Version Control

* Git
* GitHub

## System Workflow

1. User submits a document.
2. spaCy extracts entities from the text.
3. Relationships are detected between entities.
4. NetworkX builds a graph structure.
5. PyVis generates an interactive visualization.
6. Users explore connections and ask questions.

## Installation

Clone the repository:

```bash
git clone https://github.com/CharanISA/universal-knowledge-graph-builder.git
```

Navigate to the project:

```bash
cd universal-knowledge-graph-builder
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the spaCy language model:

```bash
python -m spacy download en_core_web_sm
```

Run the application:

```bash
python app.py
```

Open:

```txt
http://127.0.0.1:5000
```

## Example Use Case

Input:

Google developed artificial intelligence tools for cloud computing. OpenAI works with Microsoft to build advanced AI systems.

Output:

* Extracted entities:

  * Google
  * OpenAI
  * Microsoft

* Relationships:

  * OpenAI ↔ Microsoft
  * Google ↔ Artificial Intelligence

* Interactive graph visualization

## Future Improvements

* PDF document support
* DOCX document support
* Neo4j graph database integration
* OpenAI-powered relationship extraction
* Multi-document analysis
* Advanced graph search
* Graph export functionality

## Screenshots

### Home Page

(Add screenshot here)

### Generated Knowledge Graph

(Add screenshot here)

### Relationship Extraction

(Add screenshot here)

### Question Answering

(Add screenshot here)

## Author

Cain Saragadam

Aspiring Software Developer | IT Professional | UI/UX Designer | Data Analyst
