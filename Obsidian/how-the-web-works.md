# 🌐 How the Web Works

## 1. How Does the Browser Work?

1. You enter a website address (URL) or click a link.
2. The browser sends a request to the website’s server.
3. The server responds with the webpage’s data (HTML, CSS, JavaScript, images, etc.).
4. The browser processes this data and renders the webpage.
5. You can interact with the page by clicking, scrolling, or entering information.

---

## 2. Clients and Servers  
🔗 [MDN: Clients and Servers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#clients_and_servers)

- **Clients** are internet-connected devices (like your computer or phone) and web-accessing software (usually browsers like Chrome or Firefox).
- **Servers** store web content. When a client requests a page, the server sends the webpage code for the browser to render.

---

## 3. Other Parts of the Toolbox  
🔗 [MDN: Toolbox Overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#the_other_parts_of_the_toolbox)

- **Internet Connection**: Enables data transmission.
- **TCP/IP**: Protocols that control how data travels.
- **DNS (Domain Name System)**: Translates domain names into IP addresses.
- **HTTP (Hypertext Transfer Protocol)**: Defines communication between client and server.
- **Files**:
  - **Code**: HTML, CSS, JavaScript.
  - **Assets**: Images, videos, PDFs, etc.

---

## 4. What Happens When You Type a URL?  
🔗 [MDN: So What Happens Exactly](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#so_what_happens_exactly)

1. Browser queries DNS to find the server IP.
2. Sends an HTTP request to the server.
3. Server responds with a `200 OK` and sends data in **packets**.
4. Browser assembles the page and displays it.

---

## 5. DNS Explained  
🔗 [MDN: DNS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#dns_explained)

- Web addresses like `mozilla.org` are linked to **IP addresses** (e.g., `192.0.2.172`).
- DNS servers resolve human-readable addresses to machine-readable IPs.
- You can also access sites directly via their IP addresses.

---

## 6. Packets Explained  
🔗 [MDN: Packets](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#packets_explained)

- Data is broken into **small packets** for transmission.
- Advantages:
  - Faster, even with occasional loss or corruption.
  - Packets can take different routes, improving speed and efficiency.

---

## 7. HTTP Basics  
🔗 [MDN: HTTP Overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#http_basics)

### Example HTTP Request
```
GET /en-US/ HTTP/2
Host: developer.mozilla.org
```

### Example HTTP Response
```
HTTP/2 200
date: Tue, 11 Feb 2025 11:13:30 GMT
content-type: text/html
...
<!doctype html> ... (HTML content)
```

- `200`: Success.
- HTTP headers include `date`, `expires`, `server`, etc.
- The body contains HTML content of the page.

---

## 8. Common HTTP Status Codes  
🔗 [MDN: Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

| Code | Meaning |
|------|---------|
| `200` | Success |
| `301` | Moved permanently (redirect) |
| `400` | Bad request (invalid format) |
| `403` | Forbidden (unauthorized access) |
| `404` | Not found (wrong URL or deleted page) |
| `503` | Server unavailable (temporary issue) |

---

## 9. URLs (Uniform Resource Locators)  
🔗 [MDN: What is a URL?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)

![URL Structure](mdn-url-all.png)

### Absolute vs Relative URLs  
🔗 [MDN: Absolute vs Relative](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL#absolute_urls_vs._relative_urls)

- **Absolute URL**: Includes protocol, domain, and full path.
  - Example: `https://example.com/images/logo.png`
- **Relative URL**: Path relative to the current page.
  - Example: `images/logo.png`
