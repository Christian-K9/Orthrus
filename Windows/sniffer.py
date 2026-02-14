import subprocess

reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"

def run(cmd):
    subprocess.run(cmd, check=True)

#Snort File Location
snort_location = "C:\Users\Administrator\Snort"

answer = None
print("f{yellow} File Location of Snort: f{snort_location}")
answer = input("Change File Location? (y/n) : f{reset}")
if answer == "y":
    snort_location = input("Enter File Location")

npcap_location = "C:\Users\Administrator\npcap.exe"

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

#activate snort
#snort -l snort_path -L alerts.log -i <interface