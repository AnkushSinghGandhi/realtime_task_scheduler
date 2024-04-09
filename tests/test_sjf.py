from src.sjf_scheduler import SJFScheduler
from src.process import Process

def test_sjf_scheduler():
    # Create some sample processes
    processes = [
        Process("P1", arrival_time=0, burst_time=5, priority=1),
        Process("P2", arrival_time=1, burst_time=3, priority=2),
        Process("P3", arrival_time=2, burst_time=7, priority=3)
    ]
    
    # Initialize the SJF scheduler
    scheduler = SJFScheduler()
    
    # Schedule the processes
    scheduling_output = scheduler.schedule(processes)
    
    # Sort processes by arrival time for consistent comparison
    processes.sort(key=lambda x: x.arrival_time)
    
    # Verify the scheduling output
    expected_output = """Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time
P1\t\t0\t\t5\t\t3\t\t8
P2\t\t1\t\t3\t\t0\t\t3
P3\t\t2\t\t7\t\t6\t\t13
    
Average Waiting Time: 3.0
Average Turnaround Time: 8.0
"""
    assert scheduling_output.strip() == expected_output.strip()
