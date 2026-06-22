def detect_suspicious(processes, suspicious_list):
    found = []

    for proc in processes:
        for suspect in suspicious_list:
            if suspect.lower() in proc['name'].lower():
                found.append(proc)

    return found