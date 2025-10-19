import subprocess
import sys

splunk_path = r"C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe"
splunk_server = input("What Is the Splunk Server IP?: ")
AUTH = "admin:", input("What Is The Admin Password?: ")

subprocess.run([splunk_path, "add", "forward-server", splunk_server])

subprocess.run([splunk_path, "add", "monitor", "WinEventLog://Application"])
subprocess.run([splunk_path, "add", "monitor", "WinEventLog://Systen"])
subprocess.run([splunk_path, "add", "monitor", "WinEventLog://Security"])

subprocess.run(["net", "stop", "splunkforwarder"])
subprocess.run(["net", "start", "splunkforwarder"])