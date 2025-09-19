#!/usr/bin/env python3
import csv
import subprocess

CSV_FILE = "hosts_from_pdns.csv"  # مسیر فایل CSV خروجی از zone
TIMEOUT = 1  # ثانیه برای ping

def ping_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", str(TIMEOUT), ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

def main():
    with open(CSV_FILE) as f:
        reader = csv.DictReader(f)
        print(f"{'HOSTNAME':30} {'IP':15} STATUS")
        print("-"*55)
        for row in reader:
            hostname = row['hostname']
            ip = row['ip']
            status = "UP" if ping_host(ip) else "DOWN"
            print(f"{hostname:30} {ip:15} {status}")

if __name__ == "__main__":
    main()

