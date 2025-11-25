# scenarios.py

import time
import random
from classes.alert_priority_queue import AlertPriorityQueue
from classes.alert_class import Alert

# ----------------------------------------------------------------------
# SIMULATION SCENARIOS
# ----------------------------------------------------------------------

def emergency_weather_system_stress_test():
    """
    Simulates system behavior under heavy load with a sudden critical alert. 
    A large number of low-priority alerts are inserted, followed by a single 
    critical alert, which must be extracted immediately. (Corresponds to Slide 11)
    """
    alert_queue = AlertPriorityQueue()
    print("\n\n=== SIMULATION: EMERGENCY WEATHER SYSTEM STRESS TEST ===")

    NUM_LOW_ALERTS = 10
    
    print("\n--- A. Inserting 10 Low Priority Alerts (Severity 5) ---")
    for i in range(NUM_LOW_ALERTS):
        alert_queue.insert_alert(Alert(
            severity=5, 
            message=f"Routine Traffic Update (ID {i+1})"
        ))
        time.sleep(0.01) # Small delay to ensure distinct timestamps

    print("\n--- B. Inserting Critical Alert (Severity 1) ---")
    # This alert is inserted late but must jump to the front.
    alert_queue.insert_alert(Alert(
        severity=1, 
        message="NUCLEAR PLANT SHUTDOWN IMMINENT"
    ))

    print("\n--- C. Processing Alerts by Priority ---")
    # Expected: Sev 1 alert first, then all Sev 5 alerts in FIFO order.
    while not alert_queue.is_empty():
        time.sleep(0.1) 
        alert_queue.process_alert()


def emergency_weather_system_priority_check():
    """
    Tests the strict hierarchical processing of all five severity levels 
    inserted randomly to confirm (1, 2, 3, 4, 5) ordering. (Corresponds to Slide 12)
    """
    alert_queue = AlertPriorityQueue()
    print("\n\n=== SIMULATION: EMERGENCY WEATHER SYSTEM PRIORITY CHECK ===")

    scenarios = [
        (3, "Medium Rainfall Forecast"),
        (5, "Minor Road Maintenance"),
        (1, "DAM BREACH IMMINENT"),
        (4, "High Wind Advisory"),
        (2, "Wildfire Spreading Rapidly"),
        (3, "Second Medium Rainfall Report"), # Additional Sev 3 to test FIFO tie-breaker
    ]
    
    # Shuffle the input order to demonstrate that insertion order doesn't matter
    random.shuffle(scenarios)

    print("\n--- A. Inserting Alerts in Randomized Order ---")
    for severity, message in scenarios:
        alert_queue.insert_alert(Alert(severity, message))
        time.sleep(0.01)
        
    print("\n--- B. Processing Alerts by Priority ---")
    # Expected: Strict 1, 2, 3(oldest), 3(newest), 4, 5
    while not alert_queue.is_empty():
        time.sleep(0.2)
        alert_queue.process_alert()


def hospital_triage_demonstration():
    """
    Simulates patient triage where priority is determined by medical need.
    Severity 1 = Immediate (Life-Threatening), 5 = Non-Urgent. (Corresponds to a new slide)
    """
    triage_queue = AlertPriorityQueue()
    print("\n\n=== SIMULATION: HOSPITAL EMERGENCY TRIAGE ===")
    
    patients = [
        (4, "Patient: Ankle Fracture (Stable)"),
        (1, "Patient: Severe Chest Pain (Critical)"),
        (3, "Patient: High Fever, Dehydration (Urgent)"),
        (2, "Patient: Head Trauma, Unconscious (Immediate)"),
        (1, "Patient: Cardiac Arrest (Critical - Arrived later)"),
        (5, "Patient: Routine Check-up (Non-Urgent)"),
    ]
    
    print("\n--- A. Inserting Patients in Arrival Order ---")
    for severity, message in patients:
        triage_queue.insert_alert(Alert(severity, message))
        time.sleep(0.01)
        
    print("\n--- B. Processing Patients by Triage Priority ---")
    # Expected Order: Both Sev 1s (FIFO), Sev 2, Sev 3, Sev 4, Sev 5.
    while not triage_queue.is_empty():
        time.sleep(0.3)
        triage_queue.process_alert()


def network_prioritization_demonstration():
    """
    Simulates Quality of Service (QoS) for network traffic.
    Severity 1 = Real-Time Voice/Video, 5 = Bulk Download. (Corresponds to a new slide)
    """
    network_queue = AlertPriorityQueue()
    print("\n\n=== SIMULATION: NETWORK PACKET PRIORITIZATION ===")
    
    packets = [
        (5, "Bulk File Download (Low Priority)"),
        (1, "VoIP Call Packet 1 (Real-Time)"),
        (3, "Web Page Request (Standard)"),
        (1, "VoIP Call Packet 2 (Real-Time - Arrived later)"),
        (5, "Backup Data Transfer (Low Priority)"),
        (2, "Remote Desktop Control (High Interactivity)"),
    ]

    print("\n--- A. Inserting Packets in Arrival Order ---")
    for severity, message in packets:
        network_queue.insert_alert(Alert(severity, message))
        time.sleep(0.01)
        
    print("\n--- B. Processing Packets by QoS Priority ---")
    # Expected Order: Both Sev 1s (FIFO), Sev 2, Sev 3, both Sev 5s (FIFO).
    while not network_queue.is_empty():
        time.sleep(0.3)
        network_queue.process_alert()