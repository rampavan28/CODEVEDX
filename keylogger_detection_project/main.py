from process_monitor import get_running_processes
from detector import detect_suspicious
from logger import log_alert

def load_suspicious_list():
    with open("suspicious_processes.txt", "r") as file:
        return file.read().splitlines()

def main():
    print("=== Keylogger Detection System ===")

    processes = get_running_processes()
    suspicious_list = load_suspicious_list()

    found = detect_suspicious(processes, suspicious_list)

    if found:
        print("⚠ Suspicious Processes Detected!")
        for proc in found:
            msg = f"Suspicious process: {proc['name']} (PID: {proc['pid']})"
            print(msg)
            log_alert(msg)
    else:
        print("✅ System is safe. No suspicious processes found.")

if __name__ == "__main__":
    main()