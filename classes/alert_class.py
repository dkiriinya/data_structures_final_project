import time

# Alert class
class Alert:
    def __init__(self, severity, message):
        self.severity = severity       # Lower number = higher priority
        self.timestamp = time.time()   # Capture arrival time
        self.message = message

    def __lt__(self, other):
        # Priority: first by severity, then by timestamp
        return (self.severity, self.timestamp) < (other.severity, other.timestamp)

    def __str__(self):
        # Format the time for better readability
        return f"[Severity: {self.severity}] {self.message} (Time: {time.strftime('%H:%M:%S', time.localtime(self.timestamp))})"