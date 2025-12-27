# Cybersecurity Influencer
- Tom Hudson (TomNomNom)
	  [LinkedIn](https://www.linkedin.com/in/tom-hudson-01816822)
	  [GitHub](https://github.com/tomnomnom)
	  [Website]((https://tomhudson.co.uk/)
- daoud youssef
    [LinkedIn](https://www.linkedin.com/in/daoud-youssef-yany)
	[YouTube]([daoud youssef - YouTube](https://www.youtube.com/@daoudyoussef7999)
- 
# Notion
- https://cold-pyramid-f00.notion.site/NTI-Boot-camp-2436a7a7d31380e8981bc14fcf9c0a08?authuser=0
- [(1) POC](https://www.notion.so/POC-1bd6a7a7d3138018a752e762825052ca)
- [Business Logic Vulnerabilities](https://www.notion.so/Business-Logic-Vulnerabilities-25ac1516b2bb806b99f2cd2e422af2a7)
- 
# YouTube
- Puny-Code, 0-Click Account Takeover
	- https://youtu.be/4CCghc7eUgI
		- [HTTP Request Smuggling - تهريب طلبات HTTP](https://portswigger.net/web-security/request-smuggling)
			- [What is HTTP request smuggling? Tutorial & Examples | Web Security Academy](https://portswigger.net/web-security/request-smuggling#:~:text=Learn%20how%20to%20perform)
		- _**[Punycode and IDN Homograph Attack]([The Most Underrated 0-Click Account Takeover Using Punycode IDN Attacks | by coffinxp | in InfoSec Write-ups - Freedium](https://freedium.cfd/https://infosecwriteups.com/the-most-underrated-0-click-account-takeover-using-punycode-idn-attacks-c0afdb74a3dc?utm_source=chatgpt.com))**:_Used they encounter ==a== (odd A) different character in ==Gmail== 
		  ![[punycode_gen.py]]
		  - [Punycode converter (IDN converter), Punycode to Unicode](https://www.punycoder.com/)
			- FORGOT PASSWORD SECTION
			- OAUTH PROVIDER EMAIL TRUST				  
			- OAUTH PROVIDER REDIRECT URL
		-  استخدم Gmail Trick:
		    -Gmail بيتجاهل النقط (.) والـ plus (+).
		    - مثال:
	        - `test.email@gmail.com`
	        - `testemail@gmail.com`
	        - `test+1@gmail.com`
		    - كلهم بيوصلوا لصندوق بريد واحد.
			- ده مش Punycode، لكنه يفيدك في **اختبار كيف التطبيقات تتعامل مع تعدد أشكال نفس الإيميل**.
- Recon From Orwa Atyat
	-  https://www.youtube.com/@orwaatyat2958?authuser=0
- Art of VirusTotal Hacking
	- https://www.youtube.com/watch?v=Xosa-1o-01M&authuser=0
		- Tools gathering endpoint form github
			[Way More](https://github.com/xnl-h4ck3r/waymore)  
		  - [orwagodfather/virustotalx: ♥](https://github.com/orwagodfather/virustotalx)
		  ![[Pasted image 20250901234945.png]]
			  - Keywords Tips To Search
			    CTRL + F
			    .zip / .7z / .exe / .tar / .gz / .dll / .iso (backup files)
				token= | apikey= | /resetpassword/ | registration
				== (encoded creds) | .com: | @ | code=
				.aspx | .ashx | .php | .jsp | .cgi | .xml | .txt | .xhtml
				==equal equal That's means something like token or decoded base==
			- 💡 Tip
				Remember. Search for subdomains one by one
				EX:
					_Results of_
					uat-dev.orwa.com
					==when you search it's not the same for==
					uat1-dev.orwa.com
		- 
- I Found Admin Panels & Leaked credentials Using This One GitHub Dork!
	- https://www.youtube.com/watch?v=3sfe8U-f_zk&authuser=0
	- "target" "@target" --> employees "password"
	- The two **main tips** he emphasized were:
		1. **Verify that the leak actually belongs to the company (Scope)**
		    - Not every GitHub repo or file that mentions the company name is truly related to them.
		    - It could be a random user’s test project.
		    - So you must confirm that the repo or account is genuinely tied to the company (e.g., an employee’s repo, or an official repo).
		2. **Check the freshness of the leak (less than 1 year old)**
		    - Old leaks (more than a year) are often useless because the credentials or keys are usually revoked or rotated.
		    - More recent leaks (less than a year) are far more likely to still be valid and worth reporting.
- Information disclosure part 1
	- https://www.youtube.com/watch?v=zfpOg3P7gpo&authuser=0
		- Shodan.io --> org:"Targed" --> More --> in filter choose ==http.title==
			- Search : Apache Tomcat --> (Configuration, Documentation) , Inbox of, phpinfo, wealcome to xmpp, Wamp, Lamp, phpMyAdmin,  Grafana CVEs, GlobalProtect Portal CVEs --> Xss
		- Github --> cheet sheet dorking github 
			  - "Target" "Password"; _Choose ==<> code==_  
		  - EMX File Metadata CVEs in Bugcrowd
			  -
- Information disclosure part 2
	- https://www.youtube.com/watch?v=F5q5oimkJ9k&authuser=0
		- VirsTotal and automatic Tool Orwe
		- js Files Bug Bounty
			- [js Files Bug Bounty - YouTube](https://www.youtube.com/results?search_query=js+Files+Bug+Bounty)
			- NahamSec
				- https://youtu.be/fQoxjBwQZUA?si=A1AnQz_GvG6vQ5XV
			- https://youtu.be/FWPXWBh4EFw?si=HU3lSJMyvi-SBVh8
- Tips & Tricks for Information Disclosure
	- https://www.youtube.com/watch?v=ODhLUi24DxQ&authuser=0
- [Daoud Youssef](https://www.youtube.com/@daoudyoussef7999/videos)
	 - How to approach a bug bounty program
	  https://youtu.be/LgnT7Hsh4lE
	 -  How To Fail In Bug Bounty
	   https://youtu.be/RGS8jP3s4p4
	 -  01. Introduction for recon mega course
	   https://youtu.be/k57PNXnpzRI?list=PL4S940IsHJYXCmx361_ft5LwOgpLLYRlR
	 - how to search for CVE POC for outdated Tech
	   https://youtu.be/t4KE-p2eCbY
		   - [NVD - Vulnerability Metrics](https://nvd.nist.gov/vuln-metrics/cvss#)
		   - [CVExploits](https://cvexploits.io/)
- [NahamSec](https://www.youtube.com/@NahamSec)
	- Free Recon Course and Methodology For Bug Bounty Hunters
		- https://youtu.be/evyxNUzl-HA
			  When it comes down to recon, it is usually divided into two main pillars. The first one being `asset discovery` and the second one being `content discovery`. And these two go hand in and the goal of asset discovery is to find as many assets that we can hack on. are your domains, subdomains, your IP addresses, everything that could be something that we can attack. You can also put something like port scanning and getting the application on running on other ports within this bucket over here. 
			  **Reconnaissance Assets Discovery** 
				  - [projectdiscovery/pdtm:](https://github.com/projectdiscovery/pdtm) 
					   1. namp
					   2. massdns
					   3.  subfinder -d example.com -all
					   4. shuffledns --> [trickus resolvers]([raw.githubusercontent.com/trickest/resolvers/refs/heads/main/resolvers.txt](https://raw.githubusercontent.com/trickest/resolvers/refs/heads/main/resolvers.txt))
					      #WordList 
					   5. WordList : [SecLists]([danielmiessler/SecLists: SecLists is the security tester's companion. It's a collection of multiple types of lists used during security assessments, collected in one place. List types include usernames, passwords, URLs, sensitive data patterns, fuzzing payloads, web shells, and many more.](https://github.com/danielmiessler/SecLists)) [Assetnote Wordlists](https://wordlists.assetnote.io/)
					   6. 
				**Reconnaissance Content Discovery**
				1. Gather Information : This is where you look for content to hack on.
				2. Google Doing or even you go as far as Brute Forcing for files and directory or scraping JavaScript files or just simply crawling the website
- https://youtu.be/UdFzNKkJXQg
- https://youtu.be/7hf-WQ0Idhg
- How to Access 404 files of any server | Information disclosure vulnerability | Bug bounty poc
  https://youtu.be/abk7wT1EMzw
 ```Bash
	curl -s "https://web.archive.org/cdx/search/cdx" --data-urlencode "url=example.com" --data-urlencode "collapse=urlkey" --data-urlencode "output=text" --data-urlencode "fl=original"
	```
	
	```Bash
	cat out.txt | grep -E '\.xls|\.xml|\.xlsx|\.json|\.pdf|\.sql|\.docx|\.doc|\.pptx|\.ppt|\.gz|\.tar|\.tgz|\.bz2|\.log|\.cache|\.swf|\.dat|\.db|\.backup|\.vim|\.conf|\.csv|\.ini|\.bin|\.dll|\.sh|\.tar\.gz|\.bak|\.old|\.zip|\.rar|\.pem|\.key|\.pub|\.asc'
	```
- Github Actions in Recon
	  https://youtu.be/oAUWINBLbcM
	  👉 github.com/SecFathy/CIScanner
- Application Security for Recon part 1
	  https://youtu.be/8fZTdOqoRSI
		  
# Xmind
- https://xmind.app/mindmap/web-applications/rueGCH/?from=gallery&authuser=0

# LinkedIn
- https://www.linkedin.com/posts/abdelrahman-tamer-6a932924a_cybersecurity-cyber-share-activity-7238217097640636416-M31i?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAD2g5qEBCi2mx4g5MOSmzmul3ThyB9VkAZI&authuser=0

# Telegram
- https://t.me/dailybountywriteup?authuser=0

# Medium - Freedium - Writeup
- https://medium.com/@maakthon/bug-bounty-insights-10-key-findings-zeroclick-account-takeover-part-5-a6acb3dce5e7?authuser=0
- https://freedium.cfd/https://medium.com/h7w/how-to-discover-exif-metadata-leaks-from-images-easy-p4-p3-bugs-44cf6b1cb875?authuser=0
- https://hackerone.com/reports/446238?authuser=0
- https://hackerone.com/reports/3099978?authuser=0
- https://codewithvamp.medium.com/cve-2025-0133-reflected-xss-vulnerability-in-palo-alto-globalprotect-gateway-portal-028128f2f5b9?authuser=0
- [How I Escalated Simple HTML Injection to SSRF]([How I Escalated Simple HTML Injection to SSRF via PDF Rendering | Security Notes](https://ahmed-tarek.gitbook.io/security-notes/pentesting/write-ups/how-i-escalated-simple-html-injection-to-ssrf-via-pdf-rendering))
- https://freedium.cfd/https://infosecwriteups.com/10-google-dorks-for-sensitive-data-9454b09edc12
- https://freedium.cfd/https://thegrayarea.tech/5-google-dorks-every-hacker-needs-to-know-fed21022a906
- https://freedium.cfd/https://infosecwriteups.com/uncover-hidden-gems-in-the-cloud-with-google-dorks-8621e56a329d
- https://freedium.cfd/https://infosecwriteups.com/recon-to-master-the-complete-bug-bounty-checklist-95b80ea55ff0
- [Homepage | WriteupDB](https://www.writeup-db.com/)
- [Bug Bounty Hunting Methodology | Pentester Guide by Zishan Ahamed Thandar](https://pentest.zishanhack.com/notes/BugBountyHuntingMethodology.html#port-scan)
- 

# Extensions
- https://chromewebstore.google.com/detail/apolloio-free-b2b-phone-n/alhgpfoeiimagjlnfekdhkjlkiomcapa?authuser=0
- https://addons.mozilla.org/en-US/firefox/addon/findsomething/?authuser=0

# Website
- [Homepage | WriteupDB](https://www.writeup-db.com/)
- Bug Bounty Hunting Methodology
  [Bug Bounty Hunting Methodology | Pentester Guide by Zishan Ahamed Thandar](https://zishanadthandar.github.io/pentest/notes/BugBountyHuntingMethodology.html)
- CVSS_Calculator
	 https://www.first.org/cvss/calculator/3-0?authuser=0
- Bug Bounty Hunting Methodology 2025
	  [Bug-Bounty-Hunting-Methodology-2025](https://github.com/amrelsagaei/Bug-Bounty-Hunting-Methodology-2025?tab=readme-ov-file#1-reconnaissance-and-subdomain-enumeration)
- Recon-Engine
	-  GitHub Dorks Cheatsheet 
		- http://cs.github.com/
		- First step don't forget that move to recently codes
		- [GitHub Dorks Cheatsheet – Der Benji – Father, DevSecOps, Cyber Security enthusiast, agilist with common sense](https://benjitrapp.github.io/memories/2022-09-04-github-dorks/)
		- https://mr-koanti.github.io/github.html?authuser=0#
		- path:/wp-config.php --> WordPress That file stores the database credentials and is present on nearly every WordPress installation
		- org: ,language:PHP, Passwords, Pss, Pwd, PW, Token, Secret, Privet
		- ==In Report== Write *internal data leaked via github* --> you must mention this is data it's internal so you can't test it
			1.  ==*so filter it's use it as a not capital== 
			2. Date for repo
			3. Check the user if he work for them ==if not== 
			4. Don't forget don't add ==.com==
			5. Can wirte this test NOT net.com NOT about.test NOT
			6. check the languages from pages
		- For API validate [streaak/keyhacks: Keyhacks is a repository which shows quick ways in which API keys leaked by a bug bounty program can be checked to see if they're valid.](https://github.com/streaak/keyhacks)
		- https://youtu.be/gFGc0ojrYD4
		- Tools in Github
			- Gitrob [https://github.com/michenriksen/gitrob](https://github.com/michenriksen/gitrob)
			- Git-all-secrets [https://github.com/anshumanbh/git-all-secrets](https://github.com/anshumanbh/git-all-secrets)
			- TruffleHog [https://github.com/dxa4481/truffleHog](https://github.com/dxa4481/truffleHog)
			- Git-secrets [https://github.com/awslabs/git-secrets](https://github.com/awslabs/git-secrets)
			- Repo-supervisor [https://github.com/auth0/repo-supervisor](https://github.com/auth0/repo-supervisor)
	-  Google Dorks
		- [Bug Bounty Search Engine](https://ahmed-0-3del.github.io/Recon-Engine/
		- [Google Dorks for Bug Bounty](https://taksec.github.io/google-dorks-bug-bounty/?authuser=0)
		- [Google Dorks for Bug Bounty - By VeryLazyTech](https://verylazytech.github.io/index.html)
		- https://github.com/TakSec/google-dorks-bug-bounty/
			- Tools in Githhub
				- Goohak [https://github.com/1N3/Goohak/](https://github.com/1N3/Goohak/)
				- GoogD0rker [https://github.com/ZephrFish/GoogD0rker/](https://github.com/ZephrFish/GoogD0rker/)
	- Shodan-Dork
		- [Shodan Dorks](https://mr-koanti.github.io/shodan)
		- Ssl.cert.subject.CN:
- Eexploit-DB
	- [Exploit Database - Exploits for Penetration Testers, Researchers, and Ethical Hackers](https://www.exploit-db.com/)
- Hunter.how
	[Hunter Search Engine](https://hunter.how/)  
- ==[Bug Bounty Forum](https://bugbountyforum.com/)==
	 - [Bug Bounty Forum - resources](https://bugbountyforum.com/resources/) 
	- [Bug Bounty Forum - tools - Index](https://bugbountyforum.com/tools/)
- Iplocation.net
	- [IP Address Lookup | Geolocation](https://www.iplocation.net/ip-lookup?authuser=0)
 
## Website for Subdomains and scan	 
- Wayback Machine
	- https://web.archive.org/?authuser=0
	- [wabarc/wayback: An archiving tool with an IM-style interface that prioritizes privacy and accessibility, integrated with various archival services including Internet Archive, archive.today, Ghostarchive, IPFS, Telegraph, and file systems.](https://github.com/wabarc/wayback?authuser=0)
	- https://web.archive.org/cdx/search/cdx?url=*.example.com/*&collapse=urlkey&output=text&f1=original&
- VirusTotal
	- https://www.virustotal.com/vtapi/v2/domain/report?apikey=&domain=example.com&authuser=0
	- [orwagodfather/virustotalx: ♥](https://github.com/orwagodfather/virustotalx)
- Otx.alienvault.com
	- https://otx.alienvault.com/api/v1/indicators/domain/example.com/url_list?limit=500&page=1
- Cavalier.hudsonrock.com
	[cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-domain?domain=mgm.mo](https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-domain?domain=mgm.mo)

- SecurityTrails.com
	- [SecurityTrails.com](https://securitytrails.com/list/apex_domain)
			- curl "https://api.securitytrails.com/v1/domain/intercom.com/subdomains" -H "apikey: UCMM5xsqVyyoVt51nKCwUIAuJ1lF-IZy"
			- https://www.linkedin.com/posts/rix4uni_bugbounty-bugbountytips-bugbountytip-activity-7382801462315327488-tEKA?utm_source=share&utm_medium=member_desktop&rcm=ACoAADrviuQBQpGGKs9aARtqUeGUo2S5nhYnSJI
			- https://www.linkedin.com/posts/rix4uni_bugbounty-bugbountytips-bugbountytip-activity-7385013307176505344-q2tv?utm_source=share&utm_medium=member_desktop&rcm=ACoAADrviuQBQpGGKs9aARtqUeGUo2S5nhYnSJI
			- https://github.com/rix4uni/haktrailsfree
- FOFA.info
	- [FOFA Search Engine](https://en.fofa.info/)
		- API Key : https://fofa.info/api/v1/search/all?key=a72ac838bf3985c70aefeff2af0978c1&qbase64=bWJvcy5jbG91ZA==
- Netcraft:
	https://searchdns.netcraft.com/?restriction=site+contains&host=&position=limited
- Zoomeye.ai
	- [ZoomEye - Cyberspace Search Engine](https://www.zoomeye.ai/)
		  - API-KEY" = "de03bD9F-Eb2D-38fD7-3583-1e839d9a9d1" } 
			  API-KEY" = "46898369-B379-37E14-d649-6630ac62d89" }
			  API-KEY" = "67616db9-5193-0cda9-576d-8d9a58ab605" } 
			  API-KEY" = "801EA8bC-8bEA-efc05-f024-f9bac59084e" }  
		-  iwr -UseBasicParsing -Headers @{ "API-KEY" = "de03bD9F-Eb2D-38fD7-3583-1e839d9a9d1" } "https://api.zoomeye.ai/domain/search?q=lieferando.de&page=1" | ConvertFrom-Json | Select-Object -ExpandProperty list | Select-Object -ExpandProperty name
		- curl.exe -s -H "API-KEY: de03bD9F-Eb2D-38fD7-3583-1e839d9a9d1" "https://api.zoomeye.ai/domain/search?q=lieferando.de&page=1" | ConvertFrom-Json | Select-Object -ExpandProperty list | Select-Object -ExpandProperty name
- urlscan.io
	- https://urlscan.io/
		API Key : 019912bb-87ad-711c-8d30-22de19331622
- Censys.io
	- https://search.censys.io/
- subdomains.whoisxmlapi.com
	- [syfe.com | Subdomains Lookup | WhoisXML API](https://subdomains.whoisxmlapi.com/lookup-report/mw56qldr2o)
- Domain Digger Tools
	- [Subdomain Search for syfe.com - Domain Digger](https://digger.tools/lookup/syfe.com/subdomains)
- Real-Time Vulnerability Intelligence
		- [HuntDB - Real-Time Vulnerability Intelligence Platform](https://huntdb.com/)
- pentest-tools.com
	- [Free Subdomain Finder Report (Light)](https://pentest-tools.com/information-gathering/find-subdomains-of-domain/scans/XqbxbBzSQrLGNtCf)
- Threatcrowd.org
	- [Threat Crowd | Threatcrowd.org Open Source Threat Intelligence](https://ci-www.threatcrowd.org/)
		- https://ci-www.threatcrowd.org/searchApi/v2/ip/report/?ip=
		- https://ci-www.threatcrowd.org/searchApi/v2/file/report/?resource=
		- https://ci-www.threatcrowd.org/searchApi/v2/domain/report/?domain=
- ~~Threatminer.org~~
	- https://www.threatminer.org/domains.php?q=
- Subdomainfinder
  [Subdomain Finder scan of "" - C99.nl](https://subdomainfinder.c99.nl/scans/2025-09-05/)
- Intelx.io
  [Tools - Intelligence X](https://intelx.io/tools?tab=domain)
- Threatbook
  [ThreatBook Intelligence｜ThreatBook CTI](https://i.threatbook.io/research)
- Crt.sh
  [crt.sh | Certificate Search](https://crt.sh/)
- Robtex
  [Welcome to Robtex!](https://www.robtex.com/)
- quake
  [360网络空间测绘 — 因为看见，所以安全](https://quake.360.net/quake/#/index
- bevigil
  [BeVigil - World's first & only security search engine for mobile apps](https://bevigil.com/)
- fullhunt
  [Search Results | FullHunt](https://fullhunt.io/search/?query=mgm.mo)
- rapiddns
	[RapidDNS Rapid DNS Information Collection - Home](https://rapiddns.io/)
- THC.org --> (VPS) 
		[The Hacker’s Choice | Founded in 1995 | Segfault](https://www.thc.org/)
- - WebGoat (by OWASP) is an intentionally vulnerable website. You can mess with many vulnerabilities in it, including XSS: https://github.com/WebGoat/WebGoat/wiki


- # DNS Discovery Tools
	- Sublist3r   https://github.com/aboul3la/Sublist3r
		git clone https://github.com/aboul3la/Sublist3r.git
		cd Sublist3r
		sudo apt install python3-venv
		python3 -m venv sublist3r-env
		source sublist3r-env/bin/activate
		cd ~/Desktop/Sublist3r
		pip install -r requirements.txt
		- python3 sublist3r.py -d example.com
	- enumall     https://github.com/jhaddix/domain/
			git clone https://github.com/jhaddix/domain.git
			cd domain
			git clone https://github.com/lanmaster53/recon-ng.git --branch v4.9.6 
			cd recon-ng
			sudo apt install python3-venv
			python3 -m venv venv
			source venv/bin/activate
			pip install -r REQUIREMENTS
			cd ..
			git clone https://github.com/infosec-au/altdns.git 
			cd altdns
			sudo apt install python3-venv
			python3 -m venv venv
			source venv/bin/activate
			pip install -r requirements.txt
			cd ..
			cp config_sample.py config.py
			nano config.py
			sudo apt install pipx
			pipx ensurepath
			pipx install 2to3
			sudo apt update --fix-missing
			sudo apt install -y build-essential zlib1g-dev libncurses-dev libgdbm-dev \
			libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
			sudo rm -rf /var/lib/apt/lists/*
			sudo apt clean
			sudo apt update
			cd /usr/src
			sudo curl -O https://www.python.org/ftp/python/3.11.7/Python-3.11.7.tgz
			sudo tar -xf Python-3.11.7.tgz
			cd Python-3.11.7
			sudo ./configure --enable-optimizations
			sudo make -j$(nproc)
			sudo make altinstall
			python3.11 -m lib2to3 -w /home/kali/Desktop/domain/enumall.py
			python3.11 -m pip install pyyaml
			python3.11 -m pip install requests
			rm -rf ~/Desktop/domain/recon-ng
			pip3.11 install dnspython lxml xlsxwriter PyPDF2 dicttoxml pycryptodome
		- python3.11 enuall.py example.com			
	- massdns     https://github.com/blechschmidt/massdns
			mkdir MassDNS && cd MassDNS
			git clone https://github.com/blechschmidt/massdns
			cd massdns
			sudo apt update
			sudo apt install git make
			sudo apt install wget https://raw.githubusercontent.com/blechschmidt/massdns/master/lists/resolvers.txt
		- ./bin/massdns
	- altdns  https://github.com/infosec-au/altdns
	- brutesubs   https://github.com/anshumanbh/brutesubs
		  git clone https://github.com/anshumanbh/brutesubs.git
		  cd brutesubs
		  cp sample-env .env
		  sudo docker-compose build
		  sudo docker-compose up
	- dns-parallel-prober     https://github.com/lorenzog/dns-parallel-prober
		    git clone https://github.com/lorenzog/dns-parallel-prober.git
		    cd dns-parallel-prober
		    sudo apt install python3-virtualenv
			python3 -m virtualenv venv
			source venv/bin/activate
			pip install -r requirements.txt
			sudo apt update && sudo apt install -y python3-dnspython python3-progressbar
			- ```# Setup (run once)
			source venv/bin/activate
			# FAST VERSION - Use this for your 3.4M wordlist (recommended)
			python3 simple_dns_enum.py example.com -w subdomains.txt -o results.txt -t 300 --timeout 1 -n 8.8.8.8 1.1.1.1
			# ORIGINAL FIXED VERSION - Now works properly
			python3 dns-queue.py example.com 100 out.txt -i subdomains.txt -f -n 8.8.8.8```
		- python3 dns-queue.py example.com 100 out.txt -i subdomains.txt	
	- dnscan  https://github.com/rbsec/dnscan
		    git clone https://github.com/rbsec/dnscan.git
			cd dnscan
			sudo apt install python3-dnspython
			sudo apt install python3-venv
			python3 -m venv venv
			source venv/bin/activate
			pip install dnspython
			sudo apt install pipx
			pipx install dnspython
			sudo apt install build-essential libssl-dev libffi-dev python3-dev
			pip install packaging cryptography
		- python3 dnscan.py -d syfe.com -w subdomains.txt
		- python3 dnscan.py -d syfe.com -w subdomains.txt -6
		- python3 dnscan.py -d syfe.com -w subdomains.txt && python3 dnscan.py -d syfe.com -w subdomains.txt -6
		  python3 dnscan.py -l mgm_domains.txt -o "/home/kali/Desktop/Tools Recon/dnscan/mgm_results.txt" 
	- Knockpy     https://github.com/guelfoweb/knock
		  sudo apt install python3-pip git -y
		  git clone https://github.com/guelfoweb/knock.git 
		  cd knock
		  python3 -m venv knockenv                                                                                            
		  source knockenv/bin/activate
		  pip install .
		  sudo apt install pipx
		 -  python knockpy.py -d syfe.com
	- subfinder 
		sudo apt install -y subfinder &>/dev/null
		- subfinder -d example.com -silent
		- subfinder–d mars.com -all --recursive
		- ~/.config/subfinder/provider-config.yaml
		- subfinder -up 
	- assetfinder 
		go install github.com/tomnomnom/$tool@latest >> "$LOGFILE" 2>&1
        sudo cp ~/go/bin/$tool /usr/local/bin/ >> "$LOGFILE" 2>&1
	    - assetfinder --subs-only example.com
	- findomain
		sudo apt install findomain
		- findomain -t syfee.com  
	- Waymore [https://github.com/xnl-h4ck3r/waymore](https://github.com/xnl-h4ck3r/waymore) 
		sudo apt install python3 python3-pip
		pipx install git+https://github.com/xnl-h4ck3r/waymore.git
		pipx upgrade waymore
		==Add APIs==
		- nano ~/.config/waymore/config.yml
		- waymore -i syfe.com -mode B  
	- Secretfinder
		  git clone https://github.com/m4ll0k/SecretFinder.git
		  cd SecretFinder
		  pip3 install -r requirements.txt
		  python3 SecretFinder.py -h
		  python3 SecretFinder.py -i https://example.com/1.js -o results.html
		  python3 SecretFinder.py -i https://syfe.com -e -r '\.zip|\.7z|\.exe|\.tar|\.gz|\.dll|\.iso|token=|apikey=|/resetpassword/|registration|==|\.com:|@|code=|\.aspx|\.ashx|\.php|\.jsp|\.cgi|\.xml|\.txt|\.xhtml' -o ../Syfe/SecretFinder.html
	- katana
		  sudo apt install golang-go
		  go install github.com/projectdiscovery/katana/cmd/katana@latest
		  sudo cp ~/go/bin/katana /usr/local/bin/
		  katana -h
	- theHarvester
		- nano /etc/theHarvester/api-keys.yaml
		- `theHarvester -d mgm.mo -b crtsh,rapiddns -l 100 -f mgm_results.html`
	- Findomain
		  [Findomain:](https://github.com/Findomain/Findomain)
		  `sudo apt install findomain`
		``` Bash
		  git clone https://github.com/findomain/findomain.git
		  cd findomain
		  cargo build --release
		  sudo cp target/release/findomain /usr/bin/
		  findomain
		  ```
		  
- # Exploiting & Scanning
	- ### **XSS**
		  XSS-Radar   https://github.com/bugbountyforum/XSS-Radar
			1. XSSHunter   https://github.com/mandatoryprogrammer/xsshunter
			2. xsshunter_client    https://github.com/mandatoryprogrammer/xsshunter_client
			3. domxssscanner   https://github.com/yaph/domxssscanner
			4. XSSer   https://github.com/epsylon/xsser
			5. BruteXSS    https://github.com/rajeshmajumdar/BruteXSS
			6. XSStrike    https://github.com/UltimateHackers/XSStrike
			7. XSS'OR  http://xssor.io/
			8. [s0md3v/XSStrike: Most advanced XSS scanner.](https://github.com/s0md3v/XSStrike)


# Read this book
- Peter Yaworsk wrote the book Web Hacking 101

# Cross Site Scripting (XSS)
- [Cross Site Scripting (XSS) | OWASP Foundation](https://owasp.org/www-community/attacks/xss/)
- https://www.google.com/search?q=Cross-Site+Scripting&ie=utf-8&oe=utf-8
- XSS Challenges - websites that are built with mini challenges to find the XSS vulnerability. This is great because you know it's vulnerable, but you have to overcome obstacles. You will find these obstacles in the real world.
    - Easier: Google's XSS Challenge: https://xss-game.appspot.com/
    - Harder: Challenges made by some of the best: http://prompt.ml/0
    - More: There are hundreds of them, seek them out: https://www.google.com/search?q=XSS+Challenges&*&ie=utf-8&oe=utf-8
# Platforms
| ==**Platform**== | ==**Sign up**== | ==**Type of programs**== |
| ---------------- | --------------- | ------------------------ |
| HackerOne        | Public          | Public and private       |
| Zerocopter       | Invite only     | Private                  |
| Bugcrowd         | Public          | Public and private       |
| Synack           | Invite only     | Private                  |
| Cobalt           | Public          | Public and private       |
| Bountyfactory    | Public          | Public and private       |
| BugBountyHQ      | Public          | Public and private       |
| Intigriti        | Public          | Public and private       |

![[Pasted image 20250913123031.png]]
## OWASP WSTG
https://owasp.org/www-project-web-security-testing-guide/stable/
![[Pasted image 20250913121651.png]]
 [WSTG - Stable | OWASP Foundation | Web_Application_Security_Testing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/)
## MITRE ATT&CK
https://attack.mitre.org/
![[Pasted image 20250913122359.png]]

## LLM
https://lmstudio.ai/
https://ollama.com/
![[Pasted image 20250913122620.png]]
https://youtu.be/9GTt0hxmnxs
[wormgpt/WormGPT Prompt at main · ChillHackLab/wormgpt](https://github.com/ChillHackLab/wormgpt/tree/main/WormGPT%20Prompt)
### #Gemini_CLI -->  [Gemini CLI](https://codelabs.developers.google.com/gemini-cli-hands-on?hl=ar#0)
	Linux
		node -v
		sudo apt update
		sudo apt install nodejs npm
		sudo npm install -g @google/gemini-cli
		gemini
	Windows powerShell
		Set-ExecutionPolicy Bypass -Scope Process -Force
		iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
		choco install nodejs --version=22.19.0 -y
		Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
		npm update -g
		npm install -g @google/gemini-cli
		gemini
		
## LangChain
https://langchain-ai.github.io/langgraph/tutorials/workflows/#building-blocks-the-augmented-llm
![[Pasted image 20250913122943.png]]

## Crew AI
https://www.crewai.com/open-source
![[Pasted image 20250913123123.png]]



![[Pasted image 20250913123659.png]]


# Android #Mobile_Android_Pentest
- Android Development for Beginners - Full Course Part 1    
  [![](https://www.gstatic.com/youtube/img/watch/yt_favicon_ringo2.png) • Android Development for Beginners - Full C...](https://www.youtube.com/watch?v=fis26HvvDII)   
- Android Development for Beginners - Full Course Part 2    
- [![](https://www.gstatic.com/youtube/img/watch/yt_favicon_ringo2.png) • Android Development for Beginners - Full C...](https://www.youtube.com/watch?v=RcSHAkpwXAQ)
- [OWASP Mobile Top 10 | OWASP Foundation](https://owasp.org/www-project-mobile-top-10/)
- https://sallam.gitbook.io/sec-88/android-appsec?authuser=0
- https://www.notion.so/Android-Pentesting-A0xTrojan-17b90050c67180d8a453fb4dfb6cfd2c?authuser=0
- https://youtu.be/QwwLSyRzNwo?si=_WPVvlfNI1fS6cV2
- https://www.youtube.com/watch?v=hf5mOFtdsz0&list=PL4S940IsHJYWhhYOpBk6Y-U9nTQq2omae
- 

