📀 Advanced Disk Scheduling Simulator :
A Python-based graphical simulator for visualizing and comparing popular disk scheduling algorithms such as FCFS, SSTF, SCAN, and C-SCAN.
The tool provides an interactive environment with real-time plotted head movements, performance metrics, and a clean Tkinter-based UI.

📌 Features
✔ Interactive GUI
 •Input disk size, head position, and request queue.
 •Select algorithms and direction of head movement (for SCAN & C-SCAN).
 •Clear and intuitive layout.

✔ Real-Time Visualization
 •Matplotlib-powered graph showing head movement.
 •Arrow annotations displaying direction between track transitions.
 •Track labels displayed for clarity.

✔ Multiple Algorithms Supported
 •FCFS (First Come First Serve)
 •SSTF (Shortest Seek Time First)
 •SCAN (Elevator Algorithm)
 •C-SCAN (Circular SCAN)

✔ Detailed Metrics Output
 •Total head movement
 •Average seek distance per request
 •Throughput
 •Request servicing order including initial head

📂 Project Structure
📁 Advanced-Disk-Scheduling-Simulator
│
├── main.py            # Main application code with GUI + algorithms
├── README.md          # Project documentation
└── requirements.txt   # Dependencies (optional)

🚀 Getting Started
1. Install Requirements
You only need matplotlib since Tkinter comes pre-installed with most Python versions.
pip install matplotlib

2. Run the Application
python main.py

🖥️ How It Works

1.User enters:
 •Disk size
 •Initial head position
 •Request sequence
 •Algorithm to use

2.Simulator computes:
 •Head movement order
 •Seek distance
 •Performance metrics
 
3.Visualization plots the path of the disk head across tracks—similar to tracking the path of an elevator moving between floors based on queued requests.

📘 Example Algorithms Explained

FCFS
Processes requests in the order they appear.
Real-life example: Cars at a toll booth served one by one.

SSTF
Picks the request closest to the current head position.
Real-life example: A delivery worker visiting the nearest customer first.

SCAN
Head moves in one direction servicing requests, then reverses like an elevator.

C-SCAN
Moves in one direction, jumps back to start, and continues servicing.

📊 Outputs You Receive
 •Sequence of serviced tracks
 •Graph showing head movement
 •Total seek distance
 •Average seek per request
 •Throughput summary

🧰 Technologies Used
 •Python
 •Tkinter (GUI)
 •Matplotlib (visualization)

📄 License
You can add MIT, Apache, or your preferred license here.

🤝 Contributions
Issues, improvements, and PRs are welcome.
