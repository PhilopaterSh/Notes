#### sudo arp-scan -l
Scan all ip in same network

### fping
fping -ag ~~192.168.127.129/24~~ 2>/dev/null





# Info about http request  

| 🛠️ **Tool** | 📌 **Main Function**                                           | ⚙️ **Example Syntax**                                                 |
| ------------ | -------------------------------------------------------------- | --------------------------------------------------------------------- |
| `whatweb`    | Identifies technologies used by websites (e.g. PHP, WordPress) | `whatweb -v http://example.com`                                       |
| `wget`       | Checks server response without downloading the content         | `wget --server-response --max-redirect=5 --spider http://example.com` |
| `curl`       | Sends detailed HTTP request and displays headers + response    | `curl -v -k http://example.com`                                       |

# Scan website automatic 
| `nikto` | Scans web applications for vulnerabilities and misconfigurations | `nikto -h http://example.com` or `nikto -host http://example.com` |
| ------- | ---------------------------------------------------------------- | ----------------------------------------------------------------- |
| `nmap`  | Scans ports and HTTP services on a host                          | `nmap -p 80,443 --script http-enum example.com`                   |
| nuclei  |                                                                  | `nuclei -u http-enum example.com -t ~/nuclei-templates`           |



-----------
### searchsploit
