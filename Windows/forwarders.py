import subprocess
import getpass
import time
import os

path = r"C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe"
server = input("What is the Server IP?: ")
port = input("What is the Server Receiving Port?: ")
indexer = f"{server}:{port}"
username = input("Splunk Username: ")
password = getpass.getpass("Enter Splunk Password: ")
login = f"{username}:{password}"

def run(cmd):
    subprocess.run(cmd, check=True)

def set_hostname():
    hostname = input("Enter The Hostname For Splunk: ")
    run([path, "set", "hostname", hostname, "-auth", login], check=True)

def add_forward_server():
    print("Removing Any Existing Forward-Server...")
    run([path, "remove", "forward-server", indexer])
    print("Adding New Forward-Server...")
    run([path, "add", "forward-server", indexer, "-auth", login])

def add_monitors():
    print("Adding IIS logs monitor...")
    iis_path = r"C:\inetpub\logs\LogFiles\W3SVC1"
    if os.path.isdir(iis_path):
        run([
            path, "add", "monitor",
            iis_path,
            "-index", "main",
            "-sourcetype", "iis"
        ])
    else:
        print("IIS logs path does not exist")

    # Windows Event Logs
    event_path = r"C:\Windows\System32\winevt\Logs"
    if os.path.isdir(event_path):
        print("Adding Windows Event Logs...")
        run([
            path, "add", "monitor",
            r"C:\Windows\System32\winevt\Logs\*.evtx",
            "-index", "main",
            "-sourcetype", "WinEventLog"
        ])
    else:
        print("Windows Event Logs directory does not exist")

def restart_splunk():
    print("Restarting Splunk Universal Forwarder...")
    run([path, "restart"])

def show_status():
    print("Waiting 15 seconds for Splunk UF to reconnect...")
    time.sleep(15)
    run([path, "list", "forward-server"])
    run([path, "list", "monitor"])

if __name__ == "__main__":
    add_forward_server()
    set_hostname()
    restart_splunk()
    add_monitors()
    restart_splunk()
    show_status()
