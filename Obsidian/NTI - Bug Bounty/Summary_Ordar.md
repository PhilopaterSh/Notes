# Bug Bounty Learning Resources

A curated list of resources, tools, and notes for bug bounty hunting.

## 1. General Learning & Methodology

- **OWASP WSTG (Web Security Testing Guide)**
  - [Main Page](https://owasp.org/www-project-web-security-testing-guide/stable/)
  - [Web Application Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/)
  - ![[Pasted image 20250913121651.png]]

- **MITRE ATT&CK**
  - [Homepage](https://attack.mitre.org/)
  - ![[Pasted image 20250913122359.png]]

- **NahamSec's Recon Methodology**
  > When it comes down to recon, it is usually divided into two main pillars. The first one being `asset discovery` and the second one being `content discovery`. The goal of asset discovery is to find as many assets that we can hack on (domains, subdomains, IP addresses). Content discovery is where you look for content to hack on (Google Dorking, brute forcing files/directories, scraping JS files, crawling).

## 2. Learning Platforms & Communities

### Notion
- [NTI Boot camp](https://cold-pyramid-f00.notion.site/NTI-Boot-camp-2436a7a7d31380e8981bc14fcf9c0a08?authuser=0)
- [POCs (Proof of Concepts)](https://www.notion.so/POC-1bd6a7a7d3138018a752e762825052ca)
- [Business Logic Vulnerabilities](https://www.notion.so/Business-Logic-Vulnerabilities-25ac1516b2bb806b99f2cd2e422af2a7)
- [Android Pentesting Notes (A0xTrojan)](https://www.notion.so/Android-Pentesting-A0xTrojan-17b90050c67180d8a453fb4dfb6cfd2c?authuser=0)

### YouTube Channels & Videos
- **Daoud Youssef**
  - [Channel Link](https://www.youtube.com/@daoudyoussef7999/videos)
  - [How to approach a bug bounty program](https://youtu.be/LgnT7Hsh4lE)
  - [How To Fail In Bug Bounty](https://youtu.be/RGS8jP3s4p4)
  - [Recon Mega Course Introduction](https://youtu.be/k57PNXnpzRI?list=PL4S940IsHJYXCmx361_ft5LwOgpLLYRlR)
  - [How to search for CVE POC for outdated Tech](https://youtu.be/t4KE-p2eCbY)
- **NahamSec**
  - [Channel Link](https://www.youtube.com/@NahamSec)
  - [Free Recon Course and Methodology](https://youtu.be/evyxNUzl-HA)
  - [JS Files Bug Bounty 1](https://youtu.be/fQoxjBwQZUA?si=A1AnQz_GvG6vQ5XV)
  - [JS Files Bug Bounty 2](https://youtu.be/FWPXWBh4EFw?si=HU3lSJMyvi-SBVh8)
- **Orwa Atyat**
  - [Channel Link](https://www.youtube.com/@orwaatyat2958?authuser=0)
- **Specific Topics**
  - [Puny-Code, 0-Click Account Takeover](https://youtu.be/4CCghc7eUgI)
  - [Art of VirusTotal Hacking](https://www.youtube.com/watch?v=Xosa-1o-01M&authuser=0)
  - [Finding Admin Panels & Leaked credentials with GitHub Dorks](https://www.youtube.com/watch?v=3sfe8U-f_zk&authuser=0)
  - [Information Disclosure Part 1](https://www.youtube.com/watch?v=zfpOg3P7gpo&authuser=0)
  - [Information Disclosure Part 2](https://www.youtube.com/watch?v=F5q5oimkJ9k&authuser=0)
  - [Tips & Tricks for Information Disclosure](https://www.youtube.com/watch?v=ODhLUi24DxQ&authuser=0)

### Articles & Writeups
- **Medium / Freedium / GitBook**
  - [Bug Bounty Insights: 10 Key Findings (ZeroClick Account Takeover)](https://medium.com/@maakthon/bug-bounty-insights-10-key-findings-zeroclick-account-takeover-part-5-a6acb3dce5e7?authuser=0)
  - [How to Discover EXIF Metadata Leaks from Images](https://freedium.cfd/https://medium.com/h7w/how-to-discover-exif-metadata-leaks-from-images-easy-p4-p3-bugs-44cf6b1cb875?authuser=0)
  - [How I Escalated Simple HTML Injection to SSRF via PDF Rendering](https://ahmed-tarek.gitbook.io/security-notes/pentesting/write-ups/how-i-escalated-simple-html-injection-to-ssrf-via-pdf-rendering)
  - [10 Google Dorks for Sensitive Data](https://freedium.cfd/https://infosecwriteups.com/10-google-dorks-for-sensitive-data-9454b09edc12)
- **HackerOne Reports**
  - [H1 Report 446238](https://hackerone.com/reports/446238?authuser=0)
  - [H1 Report 3099978](https://hackerone.com/reports/3099978?authuser=0)

### Forums & Socials
- [Bug Bounty Forum](https://bugbountyforum.com/)
- [Telegram: Daily Bounty Writeups](https://t.me/dailybountywriteup?authuser=0)
- [LinkedIn Post Example](https://www.linkedin.com/posts/abdelrahman-tamer-6a932924a_cybersecurity-cyber-share-activity-7238217097640636416-M31i?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAD2g5qEBCi2mx4g5MOSmzmul3ThyB9VkAZI&authuser=0)

### Mind Maps
- [Xmind Web Applications Map](https://xmind.app/mindmap/web-applications/rueGCH/?from=gallery&authuser=0)

## 3. Core Concepts & Vulnerabilities

### Punycode & IDN Homograph Attacks
- **Resource**: [The Most Underrated 0-Click Account Takeover Using Punycode](https://freedium.cfd/https://infosecwriteups.com/the-most-underrated-0-click-account-takeover-using-punycode-idn-attacks-c0afdb74a3dc?utm_source=chatgpt.com)
- **Tool**: [Punycode converter](https://www.punycoder.com/)
- **Attack Vectors**:
    - `FORGOT PASSWORD SECTION`
    - `OAUTH PROVIDER EMAIL TRUST`
    - `OAUTH PROVIDER REDIRECT URL`
- **Related Technique: Gmail Trick**
    - Gmail ignores dots `.` and plus signs `+` in email addresses.
    - e.g., `test.email@gmail.com`, `testemail@gmail.com`, and `test+1@gmail.com` all go to the same inbox.
    - > ده مش Punycode، لكنه يفيدك في **اختبار كيف التطبيقات تتعامل مع تعدد أشكال نفس الإيميل**.

### HTTP Request Smuggling
- [PortSwigger Academy](https://portswigger.net/web-security/request-smuggling)

### Cross-Site Scripting (XSS)
- [OWASP XSS Page](https://owasp.org/www-community/attacks/xss/)
- **XSS Challenges:**
  - [Google's XSS Challenge (Easier)](https://xss-game.appspot.com/)
  - [prompt.ml (Harder)](http://prompt.ml/0)
  - [More Challenges (Google Search)](https://www.google.com/search?q=XSS+Challenges&*&ie=utf-8&oe=utf-8)

### Android Pentesting
- **Courses**
    - [Android Development for Beginners - Part 1](https://www.youtube.com/watch?v=fis26HvvDII)
    - [Android Development for Beginners - Part 2](https://www.youtube.com/watch?v=RcSHAkpwXAQ)
- **Resources**
    - [Sallam's GitBook on Android AppSec](https://sallam.gitbook.io/sec-88/android-appsec?authuser=0)
    - [YouTube Playlist](https://www.youtube.com/watch?v=hf5mOFtdsz0&list=PL4S940IsHJYWhhYOpBk6Y-U9nTQq2omae)
    - [Video Link](https://youtu.be/QwwLSyRzNwo?si=_WPVvlfNI1fS6cV2)

## 4. Tools

### Tool Aggregators & Installers
- **Project Discovery Tools Manager (pdtm)**
  - [GitHub Link](https://github.com/projectdiscovery/pdtm)

### Reconnaissance & Discovery
- **Subdomain Enumeration**
  - `subfinder`
  - `assetfinder`
  - `findomain`
  - `massdns`
  - `altdns`
  - `dnscan`
  - `Knockpy`
  - `Sublist3r`
- **Content Discovery**
  - `Waymore`
  - `katana`
  - `SecretFinder`
- **General Recon**
  - `theHarvester`
  - `enumall`
- **GitHub Secret Scanners**
  - `Gitrob`
  - `git-all-secrets`
  - `TruffleHog`
  - `git-secrets`
  - `repo-supervisor`

### Exploiting & Scanning
- **XSS Scanners**
  - `XSS-Radar`
  - `XSSHunter`
  - `domxssscanner`
  - `XSSer`
  - `BruteXSS`
  - `XSStrike`

## 5. Online Resources & Search Engines

### Hacking Search Engines
- [Recon-Engine](https://ahmed-0-3del.github.io/Recon-Engine/)
- [Hunter.how](https://hunter.how/)
- [FOFA.info](https://en.fofa.info/)
- [ZoomEye](https://www.zoomeye.ai/)
- [Censys](https://search.censys.io/)
- [Shodan](https://www.shodan.io/)
- [Quake](https://quake.360.net/quake/#/index)
- [BeVigil (Mobile Apps)](https://bevigil.com/)
- [FullHunt](https://fullhunt.io/search/?query=mgm.mo)

### Dorking & Cheatsheets
- **Google Dorks**
  - [TakSec Cheatsheet](https://taksec.github.io/google-dorks-bug-bounty/?authuser=0)
  - [VeryLazyTech Cheatsheet](https://verylazytech.github.io/index.html)
  - [GitHub Repo: TakSec/google-dorks-bug-bounty](https://github.com/TakSec/google-dorks-bug-bounty/)
- **GitHub Dorks**
  - [Der Benji Cheatsheet](https://benjitrapp.github.io/memories/2022-09-04-github-dorks/)
  - [mr-koanti Cheatsheet](https://mr-koanti.github.io/github.html?authuser=0#)
  - **Tips & Notes:**
    - > First step: don't forget to filter by recently updated code.
    - `path:/wp-config.php` -> Finds WordPress credentials.
    - **Keywords**: `org:`, `language:PHP`, `Passwords`, `Pss`, `Pwd`, `PW`, `Token`, `Secret`, `Privet`
    - **Reporting Leaked Internal Data**:
      - > Write *internal data leaked via github*. You must mention this data is internal so you can't test it.
      - > 1. Use lowercase filters.
      - > 2. Check the date of the repository.
      - > 3. Verify the user works for the company.
      - > 4. Don't add `.com` to searches.
      - > 5. Use negative filters: `NOT net.com NOT about.test`
- **Shodan Dorks**
  - [mr-koanti Cheatsheet](https://mr-koanti.github.io/shodan)
  - `Ssl.cert.subject.CN:`

### Vulnerability & Threat Intel
- [VirusTotal](https://www.virustotal.com/)
- [OTX AlienVault](https://otx.alienvault.com/)
- [Exploit-DB](https://www.exploit-db.com/)
- [HuntDB (Real-Time Intel)](https://huntdb.com/)
- [ThreatCrowd](https://ci-www.threatcrowd.org/)
- [ThreatBook](https://i.threatbook.io/research)
- [NVD](https://nvd.nist.gov/vuln-metrics/cvss#)
- [CVExploits](https://cvexploits.io/)

### Other Useful Websites
- [Wayback Machine](https://web.archive.org/)
- [SecurityTrails](https://securitytrails.com/)
- [urlscan.io](https://urlscan.io/)
- [Robtex](https://www.robtex.com/)
- [RapidDNS](https://rapiddns.io/)
- [Intelx.io](https://intelx.io/tools?tab=domain)
- [Netcraft](https://searchdns.netcraft.com/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3-0?authuser=0)

### Browser Extensions
- [Apollo.io](https://chromewebstore.google.com/detail/apolloio-free-b2b-phone-n/alhgpfoeiimagjlnfekdhkjlkiomcapa?authuser=0)
- [Findsomething](https://addons.mozilla.org/en-US/firefox/addon/findsomething/?authuser=0)

## 6. Key Technologies

### Large Language Models (LLMs)
- [LM Studio](https://lmstudio.ai/)
- [Ollama](https://ollama.com/)
- **Gemini CLI**
  - [Codelab](https://codelabs.developers.google.com/gemini-cli-hands-on?hl=ar#0)
  - **Windows Install:**
    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    choco install nodejs --version=22.19.0 -y
    npm install -g @google/gemini-cli
    gemini
    ```

### AI Frameworks
- **LangChain**
  - [Tutorials](https://langchain-ai.github.io/langgraph/tutorials/workflows/#building-blocks-the-augmented-llm)
- **Crew AI**
  - [Homepage](https://www.crewai.com/open-source)

## 7. Recommended Reading
- *Web Hacking 101* by Peter Yaworski

## 8. Bug Bounty Platforms

| Platform      | Sign up     | Program Type       |
|---------------|-------------|--------------------|
| HackerOne     | Public      | Public and private |
| Zerocopter    | Invite only | Private            |
| Bugcrowd      | Public      | Public and private |
| Synack        | Invite only | Private            |
| Cobalt        | Public      | Public and private |
| Bountyfactory | Public      | Public and private |
| BugBountyHQ   | Public      | Public and private |
| Intigriti     | Public      | Public and private |
