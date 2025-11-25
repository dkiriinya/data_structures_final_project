**Alert Priority Queue System**
===============================

A Python-based simulation of a Priority Queue system designed to manage and process alerts based on severity and arrival time. This project demonstrates the implementation of a Min-Heap data structure to handle critical events in real-time scenarios, such as emergency weather systems, hospital triage, and network traffic prioritization.

**📌 Overview**
---------------

In many real-world systems, processing items strictly by "First-In-First-Out" (FIFO) is insufficient. Critical events (like a nuclear plant failure or a cardiac arrest) must take precedence over routine logs.

This project implements a **Priority Queue** where:

1.  **Severity Rules:** Lower numbers indicate higher priority (e.g., Severity 1 is more critical than Severity 5).
    
2.  **Time Stability:** If two alerts have the same severity, the one that arrived first is processed first (FIFO logic applied within priority tiers).
    

**📂 Project Structure**
------------------------

To run the project successfully, ensure your files are organized as follows:

project\_root/│├── classes/│   ├── \_\_init\_\_.py       (optional, makes folder a package)│   ├── alert\_class.py│   └── alert\_priority\_queue.py│├── scripts/│   ├── \_\_init\_\_.py       (optional)│   └── scenarios.py│├── main.py└── README.md

**🚀 Features**
---------------

*   **Custom Comparator Logic:** The Alert class overrides the \_\_lt\_\_ (less than) operator to sort primarily by severity and secondarily by timestamp.
    
*   **Efficient Sorting:** Uses Python's heapq module (Binary Heap) for $O(\\log n)$ insertion and extraction.
    
*   **Real-time Simulation:** Includes time.sleep() delays to simulate real-world arrival times.
    
*   **Multiple Use Cases:** Demonstrates flexibility across different domains (Weather, Healthcare, Networking).
    

**🛠️ Installation & Usage**
----------------------------

1.  **Clone or Download** the repository.
    
2.  **Navigate** to the project root directory.
    
3.  **Run the main script**:
    

python main.py

**🧪 Simulation Scenarios**
---------------------------

The main.py script executes four distinct simulations defined in scripts/scenarios.py:

### **1\. Emergency Weather Stress Test**

*   **Concept:** Simulates a system under heavy load.
    
*   **Action:** Floods the queue with 10 low-priority (Severity 5) traffic updates, then inserts a single Severity 1 "Nuclear Plant Shutdown" alert.
    
*   **Result:** The critical alert jumps to the front of the line immediately.
    

### **2\. Priority Logic Check**

*   **Concept:** Validates the sorting algorithm.
    
*   **Action:** Inserts alerts of all severity levels (1-5) in a randomized order.
    
*   **Result:** The system processes them in strict numerical order (1, 2, 3, 4, 5).
    

### **3\. Hospital Triage System**

*   **Concept:** Medical emergency room logic.
    
*   **Action:** Patients arrive with conditions ranging from "Ankle Fracture" (Sev 4) to "Cardiac Arrest" (Sev 1).
    
*   **Result:** Life-threatening conditions are treated before stable fractures or routine check-ups.
    

### **4\. Network QoS (Quality of Service)**

*   **Concept:** Data packet prioritization.
    
*   **Action:** Mixes bulk downloads (Sev 5) with real-time VoIP packets (Sev 1).
    
*   **Result:** Voice data is processed immediately to prevent lag, while bulk downloads wait.
    

**🧩 Technical Implementation**
-------------------------------

### **The Alert Class (alert\_class.py)**

The core logic resides in the comparison method:

def \_\_lt\_\_(self, other):    # Priority: first by severity, then by timestamp    return (self.severity, self.timestamp) < (other.severity, other.timestamp)

### **The Priority Queue (alert\_priority\_queue.py)**

Utilizes heapq.heappush and heapq.heappop. Because the Alert class defines how it compares to other alerts, the heap automatically maintains the correct order without complex sorting algorithms.

**🔮 Future Improvements**
--------------------------

*   Add a GUI to visualize the queue in real-time.
    
*   Implement thread locking for safe concurrent access.
    
*   Add persistent storage (database) for logs.