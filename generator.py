import re

# Technology-specific follow-up templates
TECH_FOLLOWUPS = {
    "redis": "How did you handle cache invalidation when the underlying data changed?",
    "cache": "What caching strategy did you use, and how did you decide on TTL values?",
    "docker": "How did you manage environment variables and secrets in your Docker setup?",
    "kubernetes": "How did you handle scaling and load balancing in your Kubernetes setup?",
    "rest api": "How did you handle authentication and rate limiting in your API?",
    "fastapi": "How did you structure error handling and validation in your FastAPI app?",
    "postgresql": "How did you optimize your PostgreSQL queries for performance?",
    "mysql": "How did you handle indexing and query optimization in MySQL?",
    "mongodb": "How did you design your schema for MongoDB given it's schema-less?",
    "sql": "Can you explain how you optimized a slow-running SQL query?",
    "hash map": "How did you handle collisions in your hash map implementation?",
    "hashmap": "How did you handle collisions in your hash map implementation?",
    "binary search": "What was the time complexity of your binary search, and how did you handle edge cases like duplicates?",
    "linked list": "How did you handle edge cases like an empty list or single node?",
    "recursion": "How did you handle the base case and avoid stack overflow for large inputs?",
    "machine learning": "How did you evaluate your model's performance, and what metrics did you use?",
    "random forest": "How did you tune the hyperparameters of your Random Forest model?",
    "neural network": "How did you choose the architecture and avoid overfitting?",
    "index": "What type of index did you use, and why was it suitable for your use case?",
    "thread": "How did you handle synchronization issues between threads?",
    "async": "How did you handle error propagation in your asynchronous code?",
    "queue": "How did you handle scenarios where the queue becomes full or empty?",
    "load balancer": "How did you handle session persistence across multiple servers?",
    "microservice": "How did your services communicate with each other, and how did you handle failures?",
    "jwt": "How did you handle token expiration and refresh in your authentication flow?",
    "oop": "Can you give an example of how you applied polymorphism or inheritance in a real project?",
}

GENERIC_FALLBACKS = [
    "Could you provide more detail about your answer?",
]


def generate_follow_up(answer: str) -> dict:
    answer = answer.strip()

    # Edge case: empty or too short answer
    if not answer or len(answer.split()) < 3:
        return {"follow_up": "Could you provide more detail about your answer?"}

    answer_lower = answer.lower()

    # Check for known technology/concept keywords
    for keyword, follow_up in TECH_FOLLOWUPS.items():
        if keyword in answer_lower:
            return {"follow_up": follow_up}

    # Try to extract a meaningful noun phrase as a fallback topic
    words = re.findall(r'\b[a-zA-Z]{4,}\b', answer)
    topic = words[-1] if words else "this"

    return {
        "follow_up": f"Can you walk me through how '{topic}' was implemented and what challenges you faced?"
    }