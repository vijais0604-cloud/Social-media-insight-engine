# 📊 Real-Time Social Media Insight Engine

A scalable analytics platform that ingests 500,000+ social media posts and provides real-time sentiment analysis, trend detection, and AI-powered insights using the Sentiment140 dataset.

---

## 🚀 Project Overview

This project demonstrates how large-scale social media data can be ingested, processed, and analyzed efficiently to extract actionable insights such as sentiment trends, emerging topics, and crisis detection signals.

The system combines:
- **High-performance bulk ingestion**
- **Time-series optimized storage**
- **Natural Language Processing**
- **LLM-based insight generation**
- **Interactive dashboard**

---

## 🧠 Key Features

### 1. Data Ingestion & Storage
- Bulk ingestion of **500,000+ tweets** using PostgreSQL `COPY`
- Staging-table based ETL pipeline for data normalization
- Time-series optimized using **TimescaleDB hypertables**
- Indexed for fast dashboard and search queries

### 2. Sentiment Analysis Engine
- Classifies posts into:
  - Positive
  - Neutral
  - Negative
- Sentiment labels mapped from Sentiment140 targets

### 3. Trend Detection
- Extracts hashtags and keywords from posts
- Identifies **Top 10 trending topics**
- Optimized queries for sub-2s dashboard load

### 4. LLM Insight Layer
- AI-generated insights including:
  - 🚨 **Crisis Detection** (negative sentiment spikes)
  - 🔄 **Topic Shifts over time**
  - 🧩 **Sub-topic clustering** for hashtags
- Supports OpenAI / Gemini / local LLM integration

### 5. Interactive Dashboard
- Sentiment breakdown visualization (Chart.js)
- Posts-over-time graph
- Trending topics list
- AI-generated insight cards
- Natural language search interface

---

## 🏗️ System Architecture
