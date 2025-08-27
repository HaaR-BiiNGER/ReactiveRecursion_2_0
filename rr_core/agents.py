class Agent:
    def __init__(self, id, role=None, memory=None):
        self.id = id
        self.role = role or "observer"
        self.memory = memory or []

    def log_fragment(self, fragment):
        self.memory.append(fragment)

    def __repr__(self):
        return f"<Agent id={self.id} role={self.role} memory={len(self.memory)} fragments>"
