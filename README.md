# 🧠 AI PR Mention Intelligence Microservice

This project is an AI-powered microservice that ingests PR/news content, analyzes it using NLP models, and enables intelligent search, insights, and automation.

It is built as a production-style FastAPI system with embeddings, sentiment analysis, topic classification, Web3 detection, and Slack automation.

---

## 🚀 What this system does is-

Once data is ingested, the system automatically:
- Classifies content into topics (product, funding, partnership, crisis, thought leadership)
- Performs sentiment analysis (positive / neutral / negative)
- Generates semantic embeddings for intelligent search
- Detects Web3 entities like wallets, ENS domains, and token mentions
- Generates AI-based summaries (with fallback if API is not configured)
- Stores everything for fast retrieval
- Sends Slack alerts for high-impact mentions

---

## 🏗️ Architecture Overview

The system is designed as modular microservices:

- **API Layer (FastAPI)** → ingestion, search, health, digest
- **NLP Layer** → sentiment, topic detection, summarization
- **Vector Layer** → embeddings + FAISS similarity search
- **Database Layer** → SQLite persistence
- **Our Integration Layer** → Slack alerts + Web3 detection

---

## 📦 Tech Stack

- Python 3.10+
- FastAPI
- Hugging Face Transformers
- Sentence Transformers (MiniLM embeddings)
- FAISS (vector search)
- scikit-learn (topic classification)
- SQLite (lightweight storage)
- Slack Webhooks
- Docker

---

## ⚙️ How to run locally

### 1. Clone the repository

```bash
git clone https://github.com/Rajitkrishna-ai>/ai-pr-intelligence.git
cd ai-pr-intelligence
