# Fundamentals for Penetration Testing Interviews

### Resources:
- [ازاي لقيت وظيفة كمختبر اختراق ؟ | Penetration Tester](https://youtu.be/XiYmof1ag5I)
- [Penetration Testing Interview Questions](https://youtu.be/qWy25Czi-vM?si=CmJGABO64k8F12zX)

---

## 1. Introduction to Web Concepts

### How does the browser work?
1.  You enter a website address (URL) or click a link.
2.  The browser sends a request to the website’s server.
3.  The server responds by sending the webpage’s data (HTML, CSS, JavaScript, images, etc.).
4.  The browser processes this data and displays the webpage.
5.  You can interact with the page by clicking, scrolling, or entering information.

#### Clients and Servers
- Computers connected to the internet are called **clients** and **servers**.
- **Clients** are the typical web user's internet-connected devices (e.g., your computer, phone) and the software on those devices (e.g., web browsers).
- **Servers** are computers that store webpages, sites, or apps. When a client wants to access a webpage, a copy of the webpage code is downloaded from the server to the client.

#### The other parts of the toolbox
- **Your internet connection**: Allows you to send and receive data on the internet.
- **TCP/IP**: **Transmission Control Protocol** and **Internet Protocol** are communication protocols that define how data should travel across the internet.
- **DNS**: The **Domain Name System** is like an address book for websites. It translates a human-readable domain name (like `google.com`) into an IP address.
- **HTTP**: **Hypertext Transfer Protocol** is an application protocol that defines a language for clients and servers to speak to each other.
- **Files**: A website is made up of many different files, including:
    - **Code**: HTML, CSS, and JavaScript.
    - **Assets**: Images, music, video, Word documents, and PDFs.

#### So what happens, exactly?
1.  The browser goes to the DNS server and finds the real address of the server that the website lives on.
2.  The browser sends an HTTP request message to the server, asking it to send a copy of the website to the client.
3.  If the server approves the request, it sends a "200 OK" message and starts sending the website's files in small chunks called data packets.
4.  The browser assembles the chunks into a complete web page and displays it.

#### DNS Explained
- Real web addresses are IP addresses (e.g., `192.0.2.172`), not memorable strings.
- DNS matches the web address you type (e.g., "mozilla.org") to the website's real IP address.

#### Packets Explained
- When data is sent across the web, it is sent in thousands of small chunks called packets.
- This is done for efficiency and reliability. If a small chunk is lost, it's easier to replace than an entire file.

### Components of a URL
- **URL (Uniform Resource Locator):** Specifies both the identity and the location of a resource (How and Where).
- **URI (Uniform Resource Identifier):** A more comprehensive term covering both URLs and URNs.
- **URN (Uniform Resource Name):** Focuses only on uniquely identifying a resource, not on where it is located.

![URI-URL-URN-1.png](URI-URL-URN-1.png)

A URL consists of several parts:
- **Protocol:** `https` - The method for exchanging data.
- **Domain Name:** `developer.mozilla.org` - The address of the server.
- **Path:** `/en-US/` - The specific resource on the server.

#### Absolute URLs vs. Relative URLs
- **An absolute URL** provides the complete path to a resource (e.g., `https://developer.mozilla.org/en-US/docs/Learn`).
- **A relative URL** specifies a location relative to the current page's URL (e.g., `../css/style.css`).

---

## 2. HTTP Protocol

### What does API mean?
- **API** stands for **Application Programming Interface**.
- It is a set of rules and contracts that allows different software components to communicate.
- **API penetration testing** is a security assessment process where security professionals simulate attacks on an API to identify vulnerabilities.

### HTTP Methods
HTTP methods (or verbs) are instructions sent by a client to a server to perform an action on a resource.

- **GET:** Retrieves data from a server.
- **POST:** Sends data to a server to create a new resource.
- **PUT:** Replaces an existing resource with a new one.
- **PATCH:** Updates only part of an existing resource.
- **DELETE:** Deletes a specific resource.
- **HEAD:** Similar to GET, but without the response body.
- **OPTIONS:** Describes the communication options for the target resource.
- **CONNECT:** Starts a two-way communication (a tunnel) with the requested resource.
- **TRACE:** Performs a message loop-back test.

### HTTP Headers
HTTP headers are key-value pairs sent with requests and responses, providing essential information.

#### Handled by Default by the Browser:
- **Content Negotiation:** `Accept`, `Accept-Encoding`, `Accept-Language`, `User-Agent`.
- **Caching:** `Cache-Control`, `If-Modified-Since`, `If-None-Match`.
- **Connection Management:** `Connection`.
- **Security & Origin:** `Origin`, `Referer`.
- **Cookies:** `Cookie`.

#### Handled by the Developer:
- **Security Headers:** `Content-Security-Policy` (CSP), `Strict-Transport-Security` (HSTS), `X-Frame-Options`.
- **CORS Headers:** `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`.
- **Caching Headers:** `Cache-Control`, `Expires`, `ETag`, `Last-Modified`.
- **Content and Encoding:** `Content-Type`, `Content-Encoding`, `Content-Length`.
- **Authentication:** `Authorization`, `WWW-Authenticate`.
- **Custom Headers:** Application-specific headers.

### HTTP Basics (Request and Response)
An HTTP request might look like this:
```http
GET /en-US/ HTTP/2
Host: developer.mozilla.org
```

A response might look like this:
```http
HTTP/2 200
date: Tue, 11 Feb 2025 11:13:30 GMT
content-type: text/html

<!doctype html> ...
```

### HTTP Status Codes
- **200 OK:** The request was successful.
- **301 Moved Permanently:** The requested resource has been permanently moved.
- **400 Bad Request:** The server can't process the request.
- **403 Forbidden:** The client does not have access rights to the content.
- **404 Not Found:** The server cannot find the requested resource.
- **503 Service Unavailable:** The server is not ready to handle the request.

---

## 3. Networking Fundamentals

### What happens when you plug in an Ethernet cable and go to google.com?
1.  **Connecting the Ethernet Cable:** The operating system initializes the network interface and obtains an IP address via DHCP.
2.  **DNS Lookup:** The browser resolves `google.com` to an IP address.
3.  **TCP Handshake:** The browser initiates a TCP three-way handshake with Google’s server.
4.  **TLS Handshake:** If using HTTPS, a TLS handshake follows to establish a secure connection.
5.  **HTTP Request:** The browser sends an HTTP GET request to `google.com`.
6.  **Server Response:** Google’s server responds with the HTML content and linked resources.
7.  **Rendering the Page:** The browser processes the content and displays the webpage.

### TCP vs. UDP

| Feature             | TCP (Transmission Control Protocol)                               | UDP (User Datagram Protocol)                                      |
| ------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Connection Type** | Connection-oriented; establishes a connection.                    | Connectionless; sends data without establishing a connection.     |
| **Reliability**     | Reliable; ensures data is delivered in order and without errors.  | Unreliable; no guarantee of delivery or order.                    |
| **Speed**           | Slower due to overhead.                                           | Faster with minimal overhead.                                     |
| **Use Cases**       | Web browsing (HTTP/HTTPS), email (SMTP), file transfers (FTP).    | Streaming media, online gaming, VoIP, DNS.                        |

---

## 4. Programming & System Concepts

### Class vs. Object
| Element      | Class                               | Object                                |
| ------------ | ----------------------------------- | ------------------------------------- |
| **Definition** | A blueprint or template.            | An actual instance created from a class. |
| **Memory**     | Does not occupy memory.             | Occupies memory.                      |
| **Example**    | `class Car:`                        | `my_car = Car()`                      |

### Inheritance
- An OOP concept where a new class (child/subclass) inherits properties and methods from an existing class (parent/superclass).
- This allows for code reuse and extension.

### Python Libraries
- **`re`**: Python’s built-in regular expression library for pattern matching in text.
- **`BeautifulSoup`**: A third-party library for parsing HTML and XML documents, commonly used for web scraping.
- **`requests`**: A third-party HTTP library for simplifying HTTP requests and handling responses.

### `chmod` in Linux
- `chmod` is a Linux command used to **change file or directory permissions**.
- `+x` adds the **execute** permission. `chmod +x filename` makes the file executable.

---

## 5. Penetration Testing Fundamentals

### Vulnerability vs. Threat vs. Risk
- **Vulnerability:** A weakness in a system that can be exploited.
- **Threat:** Any potential danger or attacker that can exploit a vulnerability.
- **Risk:** The likelihood of a threat exploiting a vulnerability and the impact of that event.
  **Risk = Likelihood × Impact**

### CIA and DAD Models
- **CIA Triad (Confidentiality, Integrity, Availability):**
    - **Confidentiality:** Preventing unauthorized disclosure of information (e.g., using encryption).
    - **Integrity:** Ensuring data is not altered or tampered with.
    - **Availability:** Ensuring authorized users can access data when needed (e.g., using a load balancer).
- **DAD Triad (Disclosure, Alteration, Denial):** Represents the threats to the CIA principles.
    - **Disclosure:** Unauthorized access to data (violates Confidentiality).
    - **Alteration:** Unauthorized modification of data (violates Integrity).
    - **Denial:** Preventing authorized access (violates Availability).

### Security Concepts
- **Least Privilege:** Each user should have the minimum privileges necessary to perform their job.
- **Zero Trust:** Never trust any request by default, even from internal users. Every access request must be authenticated and authorized.
- **Attack Surface:** The sum of all points where an attacker could try to enter or extract data.

#### How to Minimize Attack Surface
1.  **Implement Zero Trust Architecture.**
2.  **Enforce the Principle of Least Privilege.**
3.  **Regularly Patch and Update Systems.**
4.  **Conduct Continuous Vulnerability Assessments.**
5.  **Segment Your Network.**
6.  **Disable Unnecessary Services and Remove Unused Applications.**
7.  **Implement Strong Authentication (MFA).**
8.  **Encrypt Sensitive Data.**
9.  **Educate and Train Employees.**
10. **Implement Attack Surface Reduction (ASR) Rules.**

### Hacking Methodology
1.  **Reconnaissance (Information Gathering):** Gathering information about the target.
2.  **Scanning/Enumeration:** Scanning the target for open ports, services, and vulnerabilities.
3.  **Gaining Access:** Exploiting a vulnerability to gain access.
4.  **Maintaining Access (Persistence):** Installing backdoors or other mechanisms to maintain access.
5.  **Covering Tracks (Reporting):** Removing evidence of the attack and reporting the findings.

### Penetration Test Types
- **Black Box:** The tester has no prior knowledge of the target.
- **Gray Box:** The tester has limited information about the target.
- **White Box:** The tester has full knowledge of the internal workings of the target.

---

## 6. Common Web Vulnerabilities

### OWASP Top Ten 2021
1.  **A01: Broken Access Control**
2.  **A02: Cryptographic Failures**
3.  **A03: Injection** (XSS, SQLi, etc.)
4.  **A04: Insecure Design**
5.  **A05: Security Misconfiguration**
6.  **A06: Vulnerable and Outdated Components**
7.  **A07: Identification and Authentication Failures**
8.  **A08: Software and Data Integrity Failures**
9.  **A09: Security Logging and Monitoring Failures**
10. **A10: Server-Side Request Forgery (SSRF)**

### Vulnerability Explanations

#### Cross-Site Scripting (XSS)
- **Explanation:** Injecting client-side scripts (usually JavaScript) into web pages viewed by other users.
- **Types:**
    - **Reflected XSS:** The script is reflected off the web server in a response.
    - **Stored XSS:** The script is permanently stored on the server.
    - **DOM-based XSS:** The vulnerability is in the client-side code.

#### Cross-Site Request Forgery (CSRF)
- **Explanation:** Tricking a victim into submitting a malicious request to a web application they are already authenticated to.
- **Mitigation:** Use of anti-CSRF tokens.

#### Server-Side Request Forgery (SSRF)
- **Explanation:** An attacker induces the server-side application to make HTTP requests to an arbitrary domain.
- **Impact:** Can be used to scan internal networks or access restricted services.

#### SQL Injection (SQLi)
- **Explanation:** Inserting malicious SQL statements into an entry field for execution.
- **Types:**
    - **In-band SQLi:** Error-based and Union-based.
    - **Inferential (Blind) SQLi:** Boolean-based and Time-based.
    - **Out-of-band SQLi:** Data exfiltration via external channels.

#### Local File Inclusion (LFI)
- **Explanation:** An attacker includes local files on the server by exploiting flawed input validation.
- **Impact:** Can expose sensitive information or lead to Remote Code Execution (RCE).

#### Insecure Direct Object Reference (IDOR)
- **Explanation:** An application uses user-supplied input to directly access an object without proper authorization checks.
- **Impact:** Allows attackers to bypass authorization and access or modify resources.

#### Authentication, Authorization, and Accounting (AAA)
- **Authentication:** "Who are you?" - Verifying identity.
- **Authorization:** "What can you access?" - Determining permissions.
- **Accounting:** "What did you do?" - Tracking user activities.

#### Other Key Vulnerabilities
- **Content Security Policy (CSP):** A security layer that helps to detect and mitigate certain types of attacks, including XSS and data injection.
- **Rate Limiting:** Controls the amount of traffic a user can send to a server to prevent brute-force and DoS attacks.
- **Host Header Injection:** An attacker manipulates the `Host` header to trick the server into performing unauthorized actions.
- **Clickjacking:** Tricking a user into clicking on a hidden webpage element.
- **File Upload Vulnerabilities:** Exploiting file upload functionality to upload malicious files.
    - **Best Practices:** Whitelist extensions, check MIME types, rename files, store outside the webroot, scan for viruses, and limit file size.
- **Session Hijacking:** An attacker gains unauthorized access to a user's active session by stealing their session token.
- **Open Redirect:** A vulnerability that allows an attacker to redirect users to a malicious site.
- **CORS (Cross-Origin Resource Sharing) Misconfiguration:** Exploiting vulnerabilities in how web applications handle cross-domain requests.

---
## 7. Mobile (Android) Pentesting
- **Insecure Logging:** Sensitive information being logged.
- **Insecure Data Storage:** Sensitive data stored insecurely on the device (e.g., in `SharedPreferences`).
- **SQL Injection:** In local databases.
- **LFI through WebView:** Local File Inclusion vulnerabilities in WebViews.
- **XSS in WebView:** Cross-Site Scripting in WebViews.

---
## 8. Interview Questions (Summary List)
- Difference between authorization and authentication.
- Define the least privilege concept.
- What is CSP?
- What is IDOR?
- How can we exploit file upload vulnerabilities?
- LFI and path traversal.
- Username enumeration.
- Rate limit.
- Host header injection.
- XSS and its types.
- Cryptographic failures.
- Client-side vs. server-side validation in file uploads.
- What is CSRF and its mitigation (mention SameSite attribute)?
- What is the difference between HEAD, PUT, GET, POST?
- SQLi types and talk in-details about each one.
- SSRF possible attacks and mitigation.
- What are cookies and talk about session management.
- Talk about business logic vulnerabilities.
- Broken access control vulnerabilities.
- What is session fixation?
- What is a JWT token and possible attacks?
- If you deployed a network Linux machine, what kill chain would you follow?
- What does nmap do by default? What do the flags `-Pn`, `-A`, `-sn` do?
- What is a TCP full scan and talk about types of port scanning in detail.
- What is banner grabbing?
- Explain Android possible attacks.
