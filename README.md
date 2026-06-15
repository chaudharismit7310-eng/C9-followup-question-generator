# Task C9 — Follow-Up Question Generator

## 📌 Overview
This module generates a context-aware, technical follow-up question based on a candidate's interview answer. It is part of the **AI Voice Interview System (Group C)**.

## 🎯 Objective
- Generate deeper probing questions based on candidate responses
- Avoid generic/repetitive questions
- Remain context-aware to the technology/concept mentioned

## 🛠 Approach
A **hybrid rule-based + keyword detection** approach was used:

1. **Edge case handling**: Empty or very short answers (<3 words) return a clarification prompt
2. **Keyword matching**: The answer is scanned for known technical terms (Redis, FastAPI, hash map, PostgreSQL, Docker, etc.), each mapped to a pre-crafted, specific follow-up question
3. **Fallback logic**: If no keyword matches, the last meaningful noun is extracted and used to generate a generic-but-relevant follow-up

This guarantees **deterministic, explainable, and cost-free** output (no LLM API dependency).

## 📥 Input
```json
{
  "answer": "I used Redis for caching."
}
```

## 📤 Output
```json
{
  "follow_up": "How did you handle cache invalidation when the underlying data changed?"
}
```

## ⚙️ Edge Cases Handled
- Empty answer
- Very short answers (<3 words)
- Off-topic / non-technical answers
- Unknown technical terms (generic fallback)

## 🚀 How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit: `http://127.0.0.1:8000/docs` to test the `/follow-up` endpoint.

## 🧪 Run Tests

```bash
pytest test_followup.py -v
```

## 📊 Sample Outputs

| Input | Output |
|---|---|
| "I used Redis for caching." | "How did you handle cache invalidation when the underlying data changed?" |
| "I built a REST API using FastAPI and PostgreSQL." | "How did you optimize your PostgreSQL queries for performance?" |
| "I used a hash map for O(1) lookup in my solution." | "How did you handle collisions in your hash map implementation?" |
| "I used indexing to speed up database queries." | "What type of index did you use, and why was it suitable for your use case?" |
| "I trained a Random Forest model for classification." | "How did you tune the hyperparameters of your Random Forest model?" |

## 📁 Project Structure
C9_followup_generator/

├── main.py           # FastAPI endpoint

├── generator.py      # Core follow-up generation logic

├── test_followup.py  # Test cases

├── requirements.txt  # Dependencies

├── samples.md        # Sample input/output examples

└── README.md         # This file