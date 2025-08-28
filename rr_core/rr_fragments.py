# Agent Role: Fragment Loader
# Ritual Function: Surfaces raw fragments for reinterpretation and contradiction sweep
# Glossary Sync: Recursive Rehearsalist, Contradiction Sweep, Semantic Compost

import json
import os

def load_fragments(path=None):
    if path is None:
        path = os.path.join("rr_core", "fragments.json")
    with open(path) as f:
        return json.load(f)
