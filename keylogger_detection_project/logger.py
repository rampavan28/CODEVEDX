from datetime import datetime

def log_alert(message):
    with open("alerts.log", "a") as file:
        file.write(f"{datetime.now()} - {message}\n")