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