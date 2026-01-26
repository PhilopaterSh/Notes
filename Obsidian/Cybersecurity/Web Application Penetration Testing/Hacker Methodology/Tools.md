
| Tools       | command                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------- |
| feroxbuster | feroxbuster -u =="http://" ==                                                                |
| dirsearch   | dirsearch -u  =="http://" ==                                                                 |
| sublist3r   | sublist3r -d =="http://" ==-e Baidu,Yahoo,Bing,Ask,Netcraft,ThreatCrowd                      |
| Dirb        |                                                                                              |
| gau         | go install github.com/lc/gau/v2/cmd/gau@latest   <br>sudo cp ~/go/bin/gau /usr/local/bin<br> |

### Msfconsole
search exploit , search auxiliary
use #
options
set
run / exploit
### feroxbuster
feroxbuster -u host

### dirsearch
dirsearch -u host
### whatweb

### Curl
curl -x post url | jq .

### sublist3r
sublist3r -d evil.com -e Baidu,Yahoo,Bing,Ask,Netcraft,ThreatCrowd
#### sudo arp-scan -l
Scan all ip in same network

#### Dirb
https://github.com/Philopater0/Ph.Sh_Dirb.git

#### OWASP ZAP
sudo apt update --fix-missing
sudo apt install zaproxy
zaproxy
#### Clean url

[**Enum4linux**](https://github.com/CiscoCXSecurity/enum4linux)

[PimpMyKali (PMK) v 2.0 Release - TCM Security](https://tcm-sec.com/pimpmykali-pmk-v-2-0-release/)

#### Wpscan
[Sign Up | WPScan](https://wpscan.com/register/)
 wpscan --url https://yallanal3b.com --enumerate p,t,u --random-user-agent --api-token 83FZYiQaaHJ500ogR1nxQG9x0H3Y6Kx9WGcNqJmxxlU

### **📌 كيفية إعداد `proxychains` واستخدامه**
لتغير ال IP وتجنب الحظر المستمر

#### **🛠 1. تثبيت `proxychains` و Tor**

`sudo apt update && sudo apt install proxychains tor -y`

#### **📌 2. تعديل إعدادات `proxychains`**
sudo nano /etc/proxychains.conf`

ثم:

1. **قم بتعطيل `strict_chain` وتفعيل `dynamic_chain`** لتجنب المشاكل إذا تعطل أحد البروكسيات.
    
2. **أضف سيرفرات بروكسي SOCKS5 (مثل Tor)** في نهاية الملف:
    `socks5  127.0.0.1 9050`
    

**لحفظ التعديلات:** اضغط `CTRL + X` ثم `Y` ثم `Enter`.

---

#### **🚀 3. تشغيل Tor**

ابدأ تشغيل **Tor** ليعمل كخادم `SOCKS5`:
`sudo systemctl start tor`

تأكد من أنه يعمل:
`sudo systemctl status tor`

#### 

proxychains sudo nmap -p- -sS -sC -sV -O -A --script=default --badsum -T2 -oN evasive_scan.txt yallanal3b.com

proxychains sudo nmap -p- -T4 --script=http-vuln* yallanal3b.com -oN nmap_vulns_yallanal3b.txt

sudo apt clean
sudo apt autoclean
sudo apt update && sudo apt upgrade -y

 sublist3r -d yallanal3b.com --engines Baidu,Yahoo,Google,Bing,Ask,Netcraft,ThreatCrowd,SSL -o subdomains_fixed.txt
cat subdomains_fixed.txt | while read domain; do proxychains sudo nmap -p- -sS -sC -sV -O -A --script=default -oN "$domain.txt" "$domain"; done


---
### Nessus
