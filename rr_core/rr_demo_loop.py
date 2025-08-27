from rr_core_loop import recursive_rehearsal

# Minimal fragment class to support reinterpretation and audit logging
class Fragment:
    def __init__(self, id, text):
        self.id = id
        self.text = text
        self.flags = []
        self.audit_trail = []

# Ambient fragments for poetic rehearsal with contradiction vectors
fragments = [
    Fragment("frag_001", "vector agency_conflict in silence"),
    Fragment("frag_002", "She contradicts herself with vector identity_drift"),
    Fragment("frag_003", "vector epistemic_tension echoes through memory")
]

compost_log = []
recursive_rehearsal(fragments, compost_log)

print("\n🧾 Final Compost Log:")
for entry in compost_log:
    print(entry)
