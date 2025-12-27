## Install kali WSL in Windows
### Requirements:
- Windows 10 (version 2004 or later) or Windows 11.
- Internet connection.
- WSL enabled.
```
wsl --install
wsl --update
wsl --set-default-version 2
```
Windows PowerShell --> run as administrator
```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Hyper-V-All /all /norestart
```
or 
```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
#### Set WSL version to 2:
To upgrade Kali to WSL 2
```
wsl --set-version kali-linux 2
wsl -l -v
```

#### Run this command in **PowerShell** or **Command Prompt**:
`wsl --terminate .......`
#### If you're inside the **.......** terminal, you can simply type:
`exit`
#### Shut Down All WSL Instances:
`wsl --shutdown`

####
#### Try Resetting WSL
- This will reinstall **Kali Linux** in WSL.
```
wsl --shutdown
wsl --unregister kali-linux
wsl --install kali-linux
```
#### wsl --install -d kali-linux --name kali-new
`wsl --install -d kali-linux --name kali-new`
#### To set **Kali Linux** as your default WSL distribution
`wsl --setdefault kali-linux`
### 🔧 **Complete Kali Linux Setup & Optimization Script for WSL**

`sudo nano /etc/apt/sources.list`
```
# See: https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/
#deb http://http.kali.org/kali kali-last-snapshot main contrib non-free non-free-firmware
deb http://http.kali.org/kali kali-rolling main non-free contrib
# Additional line for source packages
#deb-src http://http.kali.org/kali kali-last-snapshot main contrib non-free non-free-firmware
```
#### 🐉 **Post-Install Kali Linux WSL Setup Script (Tools, Fixes, and Win-KeX)**
```
sudo wget https://archive.kali.org/archive-keyring.gpg -O /usr/share/keyrings/kali-archive-keyring.gpg

sudo dpkg --configure -a
sudo apt autoremove -y
sudo apt autoclean
sudo apt clean

sudo rm -rf /var/lib/apt/lists/*
sudo rm -rf /var/log/*

sudo apt remove --purge python3-jwt -y

sudo apt update --allow-releaseinfo-change
sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt --fix-broken install -y
sudo apt install -f --fix-missing -y

sudo apt install -y kali-linux-default
sudo apt install -y kali-linux-headless
sudo apt install -y kali-tools-top10
sudo apt install -y kali-win-kex --fix-missing
sudo apt install -y libclang-cpp19 python3-fs samdump2
sudo apt install -y openssh-server

sudo systemctl enable ssh.service --now
systemctl status ssh

lsb_release -a
sudo systemctl status
sudo journalctl -xe
sudo fsck -f /

free -h
top
htop

apt list --broken
apt-cache policy [package-name]

dpkg -l | grep -E "(kali-linux-headless|kali-tools-top10)" | head -5

df -h
du -sh /var/cache/apt/archives/

history -c


```

- On Window’s command prompt: `wsl -d kali-linux kex --win -s`
### Check Kali is installed properly
`lsb_release -a`

### لتشغيل GUI ل kali علشان نستخدم
- **تشغيل Win-KeX** (وضع نافذة مع الصوت):

```WSl
kex --win -s
```
- أو لتجربة الوضع السلس (Seamless Mode):
```WSl
kex --sl -s
```

- وإذا أردت الوضع المحسّن (Enhanced Session Mode):
```WSl
kex --esm --ip -s
```
