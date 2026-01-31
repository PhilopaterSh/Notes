from bs4 import BeautifulSoup
import re

file_path = "D:\\Notes-main\\Notes-main\\Obsidian\\Cybersecurity Fundamentals (Midterm).html"

# The 30 questions provided by the user as raw text
new_questions_raw_text = """
Question 1
Correct
Mark 0.50 out of 0.50
Flag question
Question text
Which of the four main subsystems in the Von Neumann Model is responsible for where calculation and logical operations take place?
Question 1Select one:

a.
Control Unit (CU)

b.
Memory

c.
Arithmetic Logic Unit (ALU)

d.
Input/Output
Feedback
The correct answer is: Arithmetic Logic Unit (ALU)
Question 2
Correct
Mark 0.50 out of 0.50
Flag question
Question text
In a private network, IP addresses are usually in which of the following ranges?
Question 2Select one:

a.
192.168.x.x

b.
8.8.x.x

c.
172.32.x.x

d.
1.1.x.x
Feedback
The correct answer is: 192.168.x.x
Question 3
Correct
Mark 0.50 out of 0.50
Flag question
Question text
Which device connects multiple networks and routes packets between them?
Question 3Select one:

a.
Hub

b.
Switch

c.
Router

d.
Access Point
Feedback
The correct answer is: Router
Question 4
Correct
Mark 0.50 out of 0.50
Flag question
Question text
In a typical LAN, what device is responsible for connecting multiple devices and forwarding data based on MAC addresses?
Question 4Select one:

a.
Router

b.
Switch

c.
Hub

d.
Firewall
Feedback
The correct answer is: Switch
Question 5
Correct
Mark 0.50 out of 0.50
Flag question
Question text
A financial company notices repeated login attempts from unusual locations every 39 seconds. What is the most likely cause?
Question 5Select one:

a.
Random user errors

b.
Automated bot attacks

c.
Insider employee mistakes

d.
Routine software updates
Feedback
The correct answer is: Automated bot attacks
Question 6
Correct
Mark 0.50 out of 0.50
Flag question
Question text
A web server is flooded with thousands of fake requests, making it unavailable to legitimate users. What type of attack is this?
Question 6Select one:

a.
SQL Injection

b.
Denial of Service (DoS)

c.
Phishing

d.
Insider threat
Feedback
The correct answer is: Denial of Service (DoS)
Question 7
Correct
Mark 0.50 out of 0.50
Flag question
Question text
The memory that holds the Basic Input Output System (BIOS), which is responsible for testing all the PC hardware at startup, is:
Question 7Select one:

a.
RAM

b.
Cache Memory

c.
Read Only Memory (ROM)

d.
Main Memory
Feedback
The correct answer is: Read Only Memory (ROM)
Question 8
Correct
Mark 0.50 out of 0.50
Flag question
Question text
The initial concept of a computer as a “Data Processor” is considered insufficient for modern computers because:
Question 8Select one:

a.
It only accepts digital input.

b.
It cannot process data fast enough.

c.
It assumes the computer can ONLY perform a single specific task.

d.
It doesn’t account for output data.
Feedback
The correct answer is: It assumes the computer can ONLY perform a single specific task.
Question 9
Correct
Mark 0.50 out of 0.50
Flag question
Question text
A Man-in-the-Middle (MITM) attack is most dangerous because it allows the attacker to:
Question 9Select one:

a.
Crash the server immediately

b.
Intercept and manipulate confidential communications

c.
Delete system files remotely

d.
Only access public websites
Feedback
The correct answer is: Intercept and manipulate confidential communications
Question 10
Correct
Mark 0.50 out of 0.50
Flag question
Question text
Which condition makes MITM attacks easier to perform?
Question 10Select one:

a.
Open or unsecured Wi-Fi

b.
Strong encryption

c.
Updated software

d.
Closed networks
Feedback
The correct answer is: Open or unsecured Wi-Fi
Question 11
Correct
Mark 0.50 out of 0.50
Flag question
Question text
A Man-in-the-Middle (MITM) attack occurs when:
Question 11Select one:

a.
The attacker destroys the server

b.
The attacker secretly intercepts communication between two parties

c.
The attacker only blocks network traffic

d.
The attacker installs antivirus software
Feedback
The correct answer is: The attacker secretly intercepts communication between two parties
Question 12
Correct
Mark 0.50 out of 0.50
Flag question
Question text
Which of the following is a major impact of MITM attacks?
Question 12Select one:

a.
Improved encryption

b.
Faster internet speed

c.
Theft of sensitive information

d.
Reduced network traffic
Feedback
The correct answer is: Theft of sensitive information
Question 13
Correct
Mark 0.50 out of 0.50
Flag question
Question text
Which step involves scanning for weaknesses like open Wi-Fi networks or outdated software?
Question 13Select one:

a.
Step 1: Vulnerability Scanning

b.
Step 2: Phishing or Redirection

c.
Step 3: Decryption

d.
Step 4: Analysis
Feedback
The correct answer is: Step 1: Vulnerability Scanning
Question 14
Correct
Mark 0.50 out of 0.50
Flag question
Question text
Which OS technique uses two or more CPUs or cores to run processes in true parallel, dividing the workload for faster execution?
Question 14Select one:

a.
Multithreading

b.
Multitasking

c.
Parallel Processing

d.
Multiprocessing
Feedback
The correct answer is: Multiprocessing
Question 15
Correct
Mark 0.50 out of 0.50
Flag question
Question text
In a Cross-Site Scripting (XSS) attack, what information do malicious scripts often steal?
Question 15Select one:

a.
The computer's serial number

b.
Session cookies and user credentials

c.
The Wi-Fi router password

d.
The server's power supply status
Feedback
The correct answer is: Session cookies and user credentials
Question 16
Incorrect
Mark 0.00 out of 0.50
Flag question
Question text
A Denial of Service (DoS) attack always requires saturating the victim’s network bandwidth to be effective.
Question 16Answer
True 
False
Feedback
The correct answer is 'False'.
Question 17
Correct
Mark 0.50 out of 0.50
Flag question
Question text
A Denial of Service condition cannot occur unless the attacker generates traffic volumes significantly higher than legitimate users.
Question 17Answer
True
False 
Feedback
The correct answer is 'False'.
Question 18
Incorrect
Mark 0.00 out of 0.50
Flag question
Question text
Deploying a load balancer guarantees protection against all forms of Denial of Service attacks by evenly distributing traffic.
Question 18Answer
True 
False
Feedback
The correct answer is 'False'.
Question 19
Correct
Mark 0.50 out of 0.50
Flag question
Question text
Shrew attacks are easier to detect than ICMP floods because their traffic patterns are more periodic and predictable.
Question 19Answer
True
False 
Feedback
The correct answer is 'False'.
Question 20
Correct
Mark 0.50 out of 0.50
Flag question
Question text
A SYN Flood attack succeeds only if the attacker completes the TCP three-way handshake with the victim.
Question 20Answer
True
False 
Feedback
The correct answer is 'False'.
Question 21
Correct
Mark 0.50 out of 0.50
Flag question
Question text
In a Cross-Site Scripting (XSS) MITM scenario, the primary vulnerability exists within the user's browser configuration rather than the web application's code.

Question 21Answer
True
False 
Feedback
The correct answer is 'False'.
Question 22
Incorrect
Mark 0.00 out of 0.50
Flag question
Question text
A session cookie stolen via an MITM attack can allow an attacker to bypass Multi-Factor Authentication (MFA) if the session was not already established

Question 22Answer
True 
False
Feedback
The correct answer is 'False'.
Question 23
Correct
Mark 0.50 out of 0.50
Flag question
Question text
During a host-based DNS Poisoning attack, the attacker systematically modifies the victim's local hosts file to achieve static redirection that bypasses external DNS queries.

Question 23Answer
True 
False
Feedback
The correct answer is 'True'.
Question 24
Correct
Mark 0.50 out of 0.50
Flag question
Question text
In the Von Neumann Model, the Arithmetic Logic Unit (ALU) is responsible for all calculation and logical operations.
Question 24Answer
True 
False
Feedback
The correct answer is 'True'.
Question 25
Correct
Mark 0.50 out of 0.50
Flag question
Question text
Application software is classified as system software because it controls hardware operations and manages memory.
Question 25Answer
True
False 
Feedback
The correct answer is 'False'.
Question 26
Incorrect
Mark 0.00 out of 0.50
Flag question
Question text
The Control Unit (CU) of a computer is responsible for performing arithmetic and logical operations.
Question 26Answer
True 
False
Feedback
The correct answer is 'False'.
Question 27
Correct
Mark 0.50 out of 0.50
Flag question
Question text
The transition to the Programmable Data Processor primarily required adding a monitor as the crucial element.
Question 27Answer
True
False 
Feedback
The correct answer is 'False'.
Question 28
Incorrect
Mark 0.00 out of 0.50
Flag question
Question text
Multithreading is identical to parallel processing because threads always run simultaneously on multiple cores.
Question 28Answer
True 
False
Feedback
The correct answer is 'False'.
Question 29
Incorrect
Mark 0.00 out of 0.50
Flag question
Question text
Parallel processing refers to using multiple CPUs or cores to execute processes simultaneously for faster execution.
Question 29Answer
True
False 
Feedback
The correct answer is 'True'.
Question 30
Incorrect
Mark 0.00 out of 0.50
Flag question
Question text
Personal computers are generally considered dedicated embedded systems because they perform single dedicated tasks.

Question 30Answer
True 
False
Feedback
The correct answer is 'False'.
"