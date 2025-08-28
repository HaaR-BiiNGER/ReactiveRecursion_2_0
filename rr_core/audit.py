# rr_core/audit.py

class DriftLogger:
    def log(self, message):
        print(f"🪶 Drift log: {message}")

class GovernanceTrigger:
    def __init__(self, threshold):
        self.threshold = threshold
