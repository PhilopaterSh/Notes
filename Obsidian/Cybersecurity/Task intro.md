### Why sites are hacked?
### HTTP and JavaScript.
### HTTP vs HTTPs.
### SSL Security.
### Hacker methodology.
### Structured Query Language Injection (SQLI).

Here’s a structured overview of each topic. I’ve aimed for an intermediate technical level—let me know if you’d like more depth or examples on any section.

---

## 1. Why Sites Are Hacked

- **Financial Gain**: Stealing credit-card data or deploying ransomware.
- **Data Theft**: Harvesting personal or proprietary information for resale or espionage.
- **Defacement/Political Motives**: Altering content to spread a message or protest.

- **Botnet Recruitment**: Compromised servers become part of distributed attack networks.    
- **Resource Abuse**: Maven for cryptojacking (mining cryptocurrency) or hosting illicit content.
- **Reputation Testing**: “Script kiddies” probing sites for fun or bragging rights.

---

## 2. HTTP and JavaScript

- **HTTP (Hypertext Transfer Protocol)**
        - Text-based request/response protocol over TCP.    
    - Methods: GET (retrieve), POST (submit), PUT, DELETE, etc.
    - Stateless: Each request independent—servers often use cookies or tokens to track sessions.
        
- **JavaScript in HTTP**
    - Executes in the browser after an HTTP response.
    - Can modify or generate HTTP requests dynamically (e.g., via `fetch()` or `XMLHttpRequest`).
    - Client-side validation: Improves UX but never a substitute for server-side checks.
        

---

## 3. HTTP vs. HTTPS

| Feature                | HTTP                            | HTTPS                            |
| ---------------------- | ------------------------------- | -------------------------------- |
| Port                   | 80                              | 443                              |
| Encryption             | None                            | TLS-encrypted channel            |
| Data Integrity         | Vulnerable to tampering         | Built-in integrity checks        |
| Authentication         | None (server trust not proved)  | Server identity via certificates |
| SEO & Browser Warnings | No SEO boost; “Not secure” flag | SEO benefit; padlock icon        |

- **Key Point**: Always serve sensitive pages (login, payment) over HTTPS to protect confidentiality and integrity.
    

---

## 4. SSL/TLS Security

- **Handshake Steps**
    
    1. **Client Hello**: Client proposes TLS version, cipher suites.
    2. **Server Hello + Certificate**: Server selects parameters, sends its X.509 cert.
    3. **Key Exchange**: Client verifies cert, then sends pre-master secret encrypted with server’s public key.
    4. **Session Keys Derived**: Both derive symmetric keys for encryption/MAC.
    5. **Finished Messages**: Verify handshake integrity; secure channel established.
- **Common Pitfalls**
    
    - Using outdated protocols (SSLv3, TLS 1.0/1.1).
    - Self-signed or expired certificates.
    - Weak cipher suites (e.g., RC4, DES).
    - Misconfigured chains (missing intermediates).

---

## 5. Hacker Methodology

1. **Reconnaissance (Footprinting)**
    
    - Passive: WHOIS, public records, Google dorking.
    - Active: Ping sweeps, DNS queries.
2. **Scanning**
    
    - Port scanning (e.g., Nmap SYN scan).
    - Service/version enumeration (e.g., banner grabbing).
3. **Gaining Access**
    
    - Exploiting vulnerabilities (e.g., buffer overflows, SQLi, XSS).     
    - Brute-force or credential-stuffing attacks.
4. **Privilege Escalation**
    
    - Local exploits to gain higher permissions (e.g., SUID binaries on Linux).
    - Misconfigurations (weak ACLs, unpatched services).
5. **Maintaining Access**
    
    - Installing backdoors, web shells, or reverse shells.
    - Creating rogue admin accounts or cron jobs.
6. **Covering Tracks**
    
    - Clearing logs, timestomping, rootkit deployment.
    - Encrypting or exfiltrating data stealthily.

---

## 6. Structured Query Language Injection (SQLi)

- **What It Is**  
    Injecting malicious SQL through input fields to manipulate database queries.

- **Types**
    
    - **In-band (Classic)**: Error-based, UNION-based (data retrieved via same channel).
    - **Blind**: Boolean-based (ask true/false), time-based (delay responses).
    - **Out-of-band**: Using features like `xp_cmdshell` or HTTP callbacks.

- **Example (UNION-based)**
    
    ```sql
    -- Victim code
    query = "SELECT name, email FROM users WHERE id = " + user_input + ";";
    -- If user_input = "1 UNION SELECT username, password FROM admins--"
    -- attackers retrieve admin credentials.
    ```
    
- **Prevention**
    
    - **Parameterized Queries/Prepared Statements**: Separate code from data.
    - **ORMs**: Use frameworks that auto-sanitize inputs.
    - **Whitelist Input Validation**: Only allow known-good patterns.
    - **Least Privilege DB Accounts**: Ensure web app only has necessary rights.
    - **Web Application Firewalls (WAFs)**: Block common SQLi payloads.

---

**Next Steps?**

- Deep-dive into any section (e.g., hands-on SSL tools, Nmap commands, secure coding practices).
    
- Build a simple test lab (e.g., DVWA, bWAPP) to practice SQLi and other exploits safely.
    
- Integrate automated scans (e.g., OWASP ZAP) into your CI/CD pipeline.
    

Let me know where you’d like to go from here!