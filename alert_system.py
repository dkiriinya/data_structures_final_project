import heapq
import time
import AlertPriorityQueue from 

# --- (Alert and AlertPriorityQueue classes remain the same) ---

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


# Min-Heap Priority Queue
class AlertPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert_alert(self, alert):
        heapq.heappush(self.heap, alert)
        print(f"-> Alert inserted: {alert}")

    def process_alert(self):
        if self.heap:
            alert = heapq.heappop(self.heap)
            print(f"<- Processing alert: {alert}")
            return alert
        else:
            print("No alerts to process.")
            return None

    def peek_alert(self):
        if self.heap:
            print(f"Next alert: {self.heap[0]}")
        else:
            print("No alerts in queue.")

    def is_empty(self):
        return len(self.heap) == 0

# -----------------------------------------------------------------
# 🚨 New Demonstration Function
# -----------------------------------------------------------------

def run_demonstration():
    alert_queue = AlertPriorityQueue()
    print("=== Emergency Alert System Demonstration ===")

    # 1. Define Sample Alerts (Severity: 1=Highest, 5=Lowest)
    print("\n--- A. Inserting Initial Alerts ---")
    
    # High Priority
    alert_queue.insert_alert(Alert(severity=1, message="Tornado Warning for County X (IMMEDIATE ACTION)"))
    # Medium Priority
    time.sleep(0.1) # Wait a moment to ensure a distinct timestamp
    alert_queue.insert_alert(Alert(severity=3, message="Severe Thunderstorm Watch in effect"))
    # Low Priority
    time.sleep(0.1)
    alert_queue.insert_alert(Alert(severity=5, message="Air Quality Alert due to smog"))
    # Another High Priority alert, which will be processed second due to later timestamp
    time.sleep(0.1)
    alert_queue.insert_alert(Alert(severity=1, message="Flash Flood Warning in City Y"))
    # Another Medium Priority alert, which will be processed last of the mediums
    time.sleep(0.1)
    alert_queue.insert_alert(Alert(severity=3, message="Dense Fog Advisory tonight"))

    # 2. Process Alerts
    print("\n--- B. Processing Alerts by Priority ---")

    # The system should process 1 (Tornado), then 1 (Flash Flood), then 3, then 3, then 5.
    while not alert_queue.is_empty():
        time.sleep(0.5) # Pause for a moment to simulate real-time processing
        alert_queue.process_alert()
    
    print("\n--- C. Queue Empty ---")
    alert_queue.process_alert() # Should print "No alerts to process."


# -----------------------------------------------------------------
# 🚀 Update the execution block to run the demonstration
# -----------------------------------------------------------------

if __name__ == "__main__":
    run_demonstration()