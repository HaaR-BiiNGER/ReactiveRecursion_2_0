from echo_logic import EchoLogic
from drift_detection import detect_drift, detect_contradiction

def recursive_rehearsal(fragments, compost_log, max_cycles=5):
    echo = EchoLogic()
    for cycle in range(max_cycles):
        print(f"\n🌀 Cycle {cycle + 1}")
        for frag in fragments:
            original_text = frag.text  # Preserve pre-mutation state
            reinterpretation = echo.reinterpret(frag)
            contradiction = detect_contradiction(original_text, reinterpretation.text)
            drift = detect_drift(original_text, reinterpretation.text)

            if drift:
                frag.flags.append("drift_detected")
                frag.audit_trail.append({
                    "cycle": cycle + 1,
                    "event": "drift",
                    "note": "Semantic mutation detected"
                })

            compost_log.append({
                "original": original_text,
                "reinterpretation": reinterpretation.text,
                "contradiction": contradiction,
                "drift": drift,
                "cycle": cycle + 1
            })

            print(f"🔍 Fragment: {original_text}")
            print(f"↪ Reinterpreted: {reinterpretation.text}")
            if contradiction:
                print(f"⚠️ Contradiction: {contradiction}")
            if drift:
                print(f"🌪️ Drift: {drift}")
    return compost_log
