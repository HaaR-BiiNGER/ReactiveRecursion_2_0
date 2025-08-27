# drift_detection.py

def detect_drift(original_text, reinterpreted_text):
    return original_text.strip() != reinterpreted_text.strip()

def detect_contradiction(original, reinterpreted):
    contradiction_terms = ["contradicts", "conflict", "tension", "disagree", "opposed"]
    for term in contradiction_terms:
        if term in original.lower() or term in reinterpreted.lower():
            return f"Detected contradiction via term: '{term}'"
    return None

