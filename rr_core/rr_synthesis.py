# Agent Role: Synthesis Engine
# Ritual Function: Detects contradiction overload and generates synthesized fragments
# Glossary Sync: Semantic Compost, Contradiction Sweep, Incarnate 666 777

class SynthesisEngine:
    def __init__(self, registry):
        self.registry = registry

    def synthesize_from_overload(self, threshold=5):
        overload = [r for r in self.registry.get_all() if len(r["vectors"]) >= 2]
        synthesized = []
        for item in overload[:threshold]:
            text = item["text"] + " [synthesized]"
            synthesized.append(text)
        return synthesized
