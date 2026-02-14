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
print(f"{yellow} Installing Snort... {reset}")
compressed_file = snort_location + ".tar.gz"
run(["powershell", "-Command", "Invoke-WebRequest", "-Uri", "https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz",
     "-Headers", "@{ 'User-Agent' = 'Mozilla/5.0' }", "-OutFile", compressed_file])
print(f"{yellow} Checking If Snort File Exist... {reset}")
if os.path.exists(compressed_file):
    print(f"{green} File Exists {reset}")
else:
    print(f"{red} Error: File {snort_location} Does not Exists. Check File Permissions {reset}")
    exit
#uncompress snort
print("Uncompressing Snort File...")
run("tar", "-xvzf", compressed_file)

#Install npcap
#Invoke-WebRequest -Uri "https://npcap.com/dist/npcap-1.87.exe" -Headers @{ "User-Agent" = "Mozilla/5.0" } -OutFile "script.py"
run(["powershell", "-Command", "Invoke-WebRequest", "-Uri", "https://npcap.com/dist/npcap-1.87.exe",
     "-Headers", "@{ 'User-Agent' = 'Mozilla/5.0' }", "-OutFile", npcap_location])

print(f"{yellow} Checking If npcap File Exist... {reset}")
if os.path.exists(npcap_location):
    print(f"{green} File Exists {reset}")
else:
    print(f"{red} Error: File {snort_location} Does not Exists. Check File Permissions {reset}")
    exit

#Change Snort Config File
print("Updating Snort File")
conf = f"{snort_location}\etc\snort.conf"
original = 'snort.conf'
temp = 'snort_temp.conf'
hostname = socket.gethostname()
ip_address = socket.gethostbyname()

with open(original, 'r') as f_in, open(temp, 'w') as f_out:
    for line in f_in:
        if "ipvar HOME_NET" in line:
            f_out.write(f"ipvar HOME_NET {ip_address}")
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

run([application, "-l", f"{snort_location}\log]", "-L", "alerts.log", "-i", interface])