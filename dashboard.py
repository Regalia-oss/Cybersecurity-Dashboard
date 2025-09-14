# dashboard.py
import tkinter as tk
from tkinter import scrolledtext
import psutil
import random
from datetime import datetime

# ------------------ Helper Functions ------------------

def log_event(message):
    """Append event to the dashboard log"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    dashboard_log.insert(tk.END, f"[{timestamp}] {message}\n")
    dashboard_log.yview(tk.END)

# Password Strength simulation
def check_password_strength():
    password = password_entry.get()
    length = len(password)
    special = any(not c.isalnum() for c in password)
    score = 0
    if length >= 8:
        score += 1
    if special:
        score += 1
    log_event(f"Password Strength Checked: Score {score}/2")

# CPU Monitor
def monitor_cpu():
    usage = psutil.cpu_percent(interval=0.5)
    cpu_label.config(text=f"CPU Usage: {usage}%")
    if usage > 80:
        log_event(f"High CPU Usage Detected: {usage}%")
    root.after(2000, monitor_cpu)

# Port Scanner Simulation
def scan_ports():
    target = "127.0.0.1"
    open_ports = [22, 80]  # simulated open ports
    log_event(f"Port Scan of {target}: Open ports {open_ports}")

# Encryption Simulation
def encrypt_text():
    text = encrypt_entry.get()
    encrypted = "".join([chr((ord(c)+3)%256) for c in text])  # simple Caesar for demo
    log_event(f"Encrypted Text: {encrypted}")

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Cybersecurity Dashboard")
root.geometry("700x500")

# Password Section
tk.Label(root, text="Password Strength Checker").grid(row=0, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, width=20)
password_entry.grid(row=1, column=0, padx=10)
tk.Button(root, text="Check Strength", command=check_password_strength).grid(row=2, column=0, pady=5)

# Encryption Section
tk.Label(root, text="Encrypt Text (Caesar)").grid(row=0, column=1, padx=10, pady=5)
encrypt_entry = tk.Entry(root, width=20)
encrypt_entry.grid(row=1, column=1, padx=10)
tk.Button(root, text="Encrypt", command=encrypt_text).grid(row=2, column=1, pady=5)

# CPU Usage
cpu_label = tk.Label(root, text="CPU Usage: 0%")
cpu_label.grid(row=3, column=0, columnspan=2, pady=10)
monitor_cpu()  # start CPU monitoring loop

# Dashboard Log
tk.Label(root, text="Event Log").grid(row=4, column=0, columnspan=2)
dashboard_log = scrolledtext.ScrolledText(root, width=80, height=15)
dashboard_log.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Port Scan Button
tk.Button(root, text="Simulate Port Scan", command=scan_ports).grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
