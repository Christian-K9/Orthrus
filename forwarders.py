import subprocess
import getpass
import sys

forwarder = "splunkforwarder-10.0.1-c486717c322b-windows-x64.msi"
url = "https://download.splunk.com/products/universalforwarder/releases/10.0.1/windows/splunkforwarder-10.0.1-c486717c322b-windows-x64.msi"

subprocess.run(["wget", "-O", forwarder, url])

splunk_path = r"C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe"
splunk_server = input("What Is the Splunk Server IP?: ")
password = getpass.getpass("What is the Splunk Password: ")

subprocess.run([splunk_path, "add", "forward-server", splunk_server])

subprocess.run([splunk_path, "add", "monitor", "WinEventLog://Application"])
subprocess.run([splunk_path, "add", "monitor", "WinEventLog://Systen"])
subprocess.run([splunk_path, "add", "monitor", "WinEventLog://Security"])

subprocess.run(["net", "stop", "splunkforwarder"])
subprocess.run(["net", "start", "splunkforwarder"])