import subprocess
import sys

def install_packageg(package, installer):
    try:
        subprocess.check_call(["sudo", installer, "install", "-y", package])
    except subprocess.CalledProcessError as e:
        print("Error Installing: " + package)


machines = {"debian": 'splunkforwarder-10.0.1-c486717c322b-linux-amd64.deb "https://download.splunk.com/products/universalforwarder/releases/10.0.1/linux/splunkforwarder-10.0.1-c486717c322b-linux-amd64.deb"',
            "ubuntu": 'splunkforwarder-10.0.1-c486717c322b-linux-amd64.deb "https://download.splunk.com/products/universalforwarder/releases/10.0.1/linux/splunkforwarder-10.0.1-c486717c322b-linux-amd64.deb"',
            "centOS": 'splunkforwarder-10.0.1-c486717c322b-linux-amd64.deb "https://download.splunk.com/products/universalforwarder/releases/10.0.1/linux/splunkforwarder-10.0.1-c486717c322b-linux-amd64.deb"',
            "fedora": 'splunkforwarder-10.0.1-c486717c322b.x86_64.rpm "https://download.splunk.com/products/universalforwarder/releases/10.0.1/linux/splunkforwarder-10.0.1-c486717c322b.x86_64.rpm"',
            "windows": 'splunkforwarder-10.0.1-c486717c322b-windows-x64.msi "https://download.splunk.com/products/universalforwarder/releases/10.0.1/windows/splunkforwarder-10.0.1-c486717c322b-windows-x64.msi"'
}

print("Which Machine Are You Using?")
for i in machines:
    print("-",i)

machine_type = input()
for i in machines:
    if machine_type == i:
        
