import heapq

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
