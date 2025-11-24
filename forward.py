import subprocess
import time

SPLUNK_PATH = r"C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe"

indexer = input("What is the Server IP?:")

def run(cmd):
    subprocess.run(cmd, check=True)

def add_forward_server():
    run([SPLUNK_PATH, "remove", "forward-server", indexer])
    run([SPLUNK_PATH, "add", "forward-server", indexer, "-auth", "admin:windows"])

def add_monitors():
    run([SPLUNK_PATH, "add", "monitor",
        r"C:\inetpub\logs\LogFiles\W3SVC1",
        "-index", "main",
        "-sourcetype", "iis"])

    run([SPLUNK_PATH, "add", "monitor",
        r"C:\Windows\System32\winevt\Logs",
        "-index", "main",
        "-sourcetype", "WinEventLog"])

def restart_splunk():
    run([SPLUNK_PATH, "restart"])

def show_status():
    time.sleep(5)
    run([SPLUNK_PATH, "list", "forward-server"])
    run([SPLUNK_PATH, "list", "monitor"])

if __name__ == "__main__":
    add_forward_server()
    add_monitors()
    restart_splunk()
    show_status()
