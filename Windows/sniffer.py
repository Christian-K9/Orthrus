import subprocess
import socket
import time
import os

reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"

snort_location = r"C:\Users\Administrator"

def run(cmd):
    subprocess.run(cmd, check=True)

    #install snort
def install():

    #Snort File Location
    global snort_location

    answer = None
    print(f"{yellow} File Location of Snort: {snort_location}")
    answer = input(f"Change File Location? (y/n) : {reset}")
    if answer == "y":
        snort_location = input(r"Enter File Location: ")


    npcap_location = r"C:\Users\Administrator\npcap.exe"

    print(f"{yellow} File Location of npcap: {npcap_location}")
    answer = input(f"Change File Location? (y/n) : {reset}")
    if answer == "y":
        npcap_location = input(r"Enter File Location")

    #Install Snort
    # #Invoke-WebRequest -Uri "https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz" -Headers @{ "User-Agent" = "Mozilla/5.0" } -OutFile "script.tar.gz"
    print("Creating Snort Folder")
    snort_file = os.path.join(snort_location, "Snort_Tar")
    tar_file = os.path.join(snort_file, "snort.tar.gz")
    print(f"Snort File: {snort_file}")
    subprocess.run(["mkdir", snort_file], shell=True)
    print(f"{yellow} Installing Snort... {reset}")
    print(f"{yellow} Outputting Snort to {snort_file}")
    run(["powershell", "-Command", "Invoke-WebRequest", "-Uri", "https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz",
        "-Headers", "@{ 'User-Agent' = 'Mozilla/5.0' }", "-OutFile", tar_file])
    print(f"{yellow} Checking If Snort File Exist... {reset}")
    if os.path.exists(snort_file):
        print(f"{green} File Exists {reset}")
    else:
        print(f"{red} Error: File {snort_file} Does not Exists. Check File Permissions {reset}")
        exit()
    #uncompress snort
    print("Uncompressing Snort File...")
    subprocess.run(["tar", "-xvzf", tar_file, "-C", snort_location])
    snort_location = os.path.join(snort_location, "snort-2.9.20")
    #Install npcap
    #Invoke-WebRequest -Uri "https://npcap.com/dist/npcap-1.87.exe" -Headers @{ "User-Agent" = "Mozilla/5.0" } -OutFile "script.py"
    run(["powershell", "-Command", "Invoke-WebRequest", "-Uri", "https://npcap.com/dist/npcap-1.87.exe",
        "-Headers", "@{ 'User-Agent' = 'Mozilla/5.0' }", "-OutFile", npcap_location])

    print(f"{yellow} Checking If npcap File Exist... {reset}")
    if os.path.exists(npcap_location):
        print(f"{green} File Exists {reset}")
    else:
        print(f"{red} Error: File {snort_location} Does not Exists. Check File Permissions {reset}")
        exit()

def install_alternate():

    #Snort File Location
    global snort_location

    answer = None
    print(f"{yellow} File Location of Snort: {snort_location}")
    answer = input(f"Change File Location? (y/n) : {reset}")
    if answer == "y":
        snort_location = input(r"Enter File Location: ")


    npcap_location = r"C:\Users\Administrator\npcap.exe"

    print(f"{yellow} File Location of npcap: {npcap_location}")
    answer = input(f"Change File Location? (y/n) : {reset}")
    if answer == "y":
        npcap_location = input(r"Enter File Location")

    #Install Snort
    # #Invoke-WebRequest -Uri "https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz" -Headers @{ "User-Agent" = "Mozilla/5.0" } -OutFile "script.tar.gz"
    print("Creating Snort Folder")
    snort_file = os.path.join(snort_location, "Snort_Tar")
    exe_file = os.path.join(snort_file, "snort.exe")
    print(f"Snort File: {snort_file}")
    subprocess.run(["mkdir", snort_file], shell=True)
    print(f"{yellow} Installing Snort... {reset}")
    print(f"{yellow} Outputting Snort to {snort_file}")
    run(["powershell", "-Command", "Invoke-WebRequest", "-Uri", "https://www.snort.org/downloads/snort/Snort_2_9_20_Installer.x64.exe",
        "-Headers", "@{ 'User-Agent' = 'Mozilla/5.0' }", "-OutFile", exe_file])
    print(f"{yellow} Checking If snort File Exist... {reset}")
    if os.path.exists(exe_file):
        print(f"{green} File Exists {reset}")
    else:
        print(f"{red} Error: File {snort_location} Does not Exists. Check File Permissions {reset}")
        exit()
    print("Waiting For User To Start Splunk. Press Any Key When Ready")
    response = input()
    print(f"Default Snort Location: {snort_location}\Snort")
    answer = input("Change File Location (y/n): ")
    if answer == "y":
        snort_location = input(r"New File Location: ")
    else:
        snort_location = r"C:\Users\Administrator\Snort"
    print(f"New File Location: {snort_location}")

def download_rules():
    #Download Snort Rules Files
    #https://rules.emergingthreats.net/open/snort-2.9.0/rules/emerging-dns.rules
    rules_location = os.path.join(snort_location, "snort-2.9.20", "rules")
    subprocess.run(["mkdir", rules_location], shell=True)
    rules = ["dns", "exploit", "malware", "policy", "web_server"]
    for i in rules:
        print(f"Downloading Rule For {i}")
        rule_url = r"https://rules.emergingthreats.net/open/snort-2.9.20/rules"
        rule = i + ".rules"
        rule_wr = f"{rule_url}/emerging-{i}.rules"
        print(f"Downloading Rule {rule_wr}")
        rule_file = os.path.join(snort_location, "snort-2.9.20", "rules", f"{i}.rules")
        print(f"Outputting To {rule_file}")
        run(["powershell", "-Command", "Invoke-WebRequest", "-Uri", rule_wr,
        "-Headers", "@{ 'User-Agent' = 'Mozilla/5.0' }", "-OutFile", rule_file])

def configure():
    #Change Snort Config File
    print("Updating Snort File")
    conf = os.path.join(snort_location, "etc", "snort.conf")
    print(f"Configuration File: {conf}")
    temp = conf + ".tmp"
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    with open(conf, 'r') as f_in, open(temp, 'w') as f_out:
        for line in f_in:
            if "ipvar HOME_NET" in line:
                f_out.write(f"ipvar HOME_NET {ip_address}\n")
            else:
                f_out.write(line)
    os.remove(conf)
    os.rename(temp, conf)

#add snort log files to splunk
def add_monitors():
    red = "\033[91m"
    application = os.path.join(snort_location, "bin", "snort.exe")
    print("Adding IIS logs monitor...")
    iis_path = os.path.join(snort_location, "log")
    if os.path.isdir(iis_path):
        run([
            application, "add", "monitor",
            iis_path,
            "-index", "main",
            "-sourcetype", "iis"
        ])
    else:
        print(red + "Error: IIS logs path does not exist")
        time.sleep(3)

#activate snort
def activate():
    #snort -l snort_path -L alerts.log -i <interface>
    interface = 0
    application = os.path.join(snort_location, "bin", "snort.exe")
    result = subprocess.run([application, "-W"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    for line in lines:
        if "disabled" not in line and (line != lines[0] and line != lines[1]):
            parts = line.split()
            if parts[0].isdigit():
                interface = str(parts[0])
                print(f"Sniffing Packets On Interface {interface}")
            break

    log_path = os.path.join(snort_location, "log")
    run([application, "-l", log_path, "-L", "alerts.log", "-i", interface])

install_alternate()
download_rules()
configure()
add_monitors()
activate()