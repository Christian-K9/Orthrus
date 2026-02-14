import subprocess
import socket
import os

reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"

def run(cmd):
    subprocess.run(cmd, check=True)

#Snort File Location
snort_location = r"C:\Users\Administrator\Snort"

answer = None
print("f{yellow} File Location of Snort: f{snort_location}")
answer = input("Change File Location? (y/n) : f{reset}")
if answer == "y":
    snort_location = input("Enter File Location")

npcap_location = r"C:\Users\Administrator\npcap.exe"

print("f{yellow} File Location of npcap: f{npcap_location}")
answer = input("Change File Location? (y/n) : f{reset}")
if answer == "y":
    npcap_location = input("Enter File Location")

#Install Snort
# #Invoke-WebRequest -Uri "https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz" -Headers @{ "User-Agent" = "Mozilla/5.0" } -OutFile "script.tar.gz"

compressed_file = snort_location + ".tar.gz"
run(["powershell", "-Command", "Invoke-WebRequest", "-Uri", "https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz",
     "-Headers", "@{ 'User-Agent' = 'Mozilla/5.0' }", "-OutFile", compressed_file])
#uncompress snort
run("tar", "-xvzf", snort_location)

#Install npcap
#Invoke-WebRequest -Uri "https://npcap.com/dist/npcap-1.87.exe" -Headers @{ "User-Agent" = "Mozilla/5.0" } -OutFile "script.py"
run(["powershell", "-Command", "Invoke-WebRequest", "-Uri", "https://npcap.com/dist/npcap-1.87.exe",
     "-Headers", "@{ 'User-Agent' = 'Mozilla/5.0' }", "-OutFile", npcap_location])

#Change Snort Config File
conf = "f{snort_location}\etc\snort.conf"
original = 'snort.conf'
temp = 'snort_temp.conf'
hostname = socket.gethostname()
ip_address = socket.gethostbyname()

with open(original, 'r') as f_in, open(temp, 'w') as f_out:
    for line in f_in:
        if "ipvar HOME_NET" in line:
            f_out.write("ipvar HOME_NET f{ip_address}")
        else:
            f_out.write(line)
os.remove(original)
os.rename(temp, original)

#activate snort
#snort -l snort_path -L alerts.log -i <interface>
interface = 0
application = "f{snort_location}\Snort\bin\snort.exe"
result = subprocess.run([application, "-W"], capture_output=True, text=True)
lines = result.stdout.splitlines()
for line in lines:
    if "disabled" not in line and (line != lines[0] and line != lines[1]):
        parts = line.split()
        if parts[0].isdigit():
            interface = parts[0]
            print("Sniffing Packets On Interface f{interface}")
        break

run([application, "-l", "f{snort_location}\log]", "-L", "alerts.log", "-i", interface])