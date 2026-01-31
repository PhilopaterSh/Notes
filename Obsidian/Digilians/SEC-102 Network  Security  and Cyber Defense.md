# SEC-102: Network  Security  and Cyber Defense

National Telecommunication Institute (NTI) Cairo,  Egypt  - 2025

Course Overview

This course offers an advanced  exploration  of network security,  building upon foundational cybersecurity  principles.    It  is designed  to  provide  students with  a  deep  understanding of defense-in depth  strategies,  the  mechanics  of network based  attacks,   and  the  practical skills required for effective cyber defense. Through  a combination  of theoretical  instruction and  hands on  labs,  students will learn to detect,  prevent,  and  respond  to intrusions  using enterprise-grade tools and methodologies.  The curriculum covers the entire security lifecycle, from proactive  prevention  to post-incident recovery and system strengthening.

Learning Ob jectives

Upon successful completion of this course, students will be able to:

• Analyze the fundamental  operations  and potential  vulnerabilities  of core networking pro- tocols
• Identify  and explain the  mechanisms  behind  common network  attacks  such as spoofing, session hijacking, and MITM attacks
• Utilize industry standard tools like Wireshark,  Scapy,  Nmap,  and  iptables  for network analysis and defense
• Implement and configure essential network security controls including firewalls and NAT
• Understand layered security strategies  and modern technologies like SIEM and SOAR
• Perform network troubleshooting and security assessments to identify vulnerabilities

Course Assessment
All components  are mandatory and contribute to the final grade.

| Component      | Marks |
| -------------- | ----- |
| Final Exam     | 70    |
| 7th Week Exam  | 15    |
| 12th Week Exam | 15    |
| Total          | 100   |

Course Agenda & Weekly Schedule
## Part 1:  Networking Fundamentals &  Core Security

• Week 1:  Networking Fundamentals
Topics:  Introduction to Networks, OSI vs. TCP/IP Models, IP Addressing (IPv4/IPv6), Network Devices, Switching vs. Routing,  Essential  Network Services (DNS, DHCP)

• Week 2:  Introduction to Network Security
Topics:  Hacker Types  and  Motivations,  The  Hacking Process,  Defense-in-Depth,  Wi-Fi Vulnerabilities

• Week 3:  Traffic Interception and Manipulation
Topics:  Packet  Sniffing Theory, Promiscuous  Mode, Packet  Spoofing Theory, Man-in-the- Middle (MitM)  Attacks,  Python  and Scapy

• Week 4:  MAC Layer Security
Topics:  The MAC Layer, Ethernet Frame Structure, Address Resolution Protocol (ARP), ARP Cache Poisoning

• Week 5:  Network Layer Security
Topics:   IPv4  Header  Analysis,  IP  Fragmentation Attacks,   Routing  Threats, Spoofing Prevention, ICMP Attacks

• Week 6:  Transport Layer Security (UDP & TCP)
Topics:  UDP  Flood Attacks,  Amplification/Reflection Attacks,  TCP  Three-Way  Hand- shake, SYN Flooding, Session Hijacking

• Week 7:  7th Week Exam & Review
Midterm  assessment covering Weeks 1-6

## Part 2:  Advanced Defense &  Practical Applications

• Week 8:  Application Layer Security (DNS)
Topics:  DNS Query Process, DNS Record Types, DNS Cache Poisoning, DNS Amplification, DNSSEC

• Week 9:  Secure Networking Technologies (VPNs)
Topics:  Tunneling  Concepts,  TUNTAP Virtual  Interfaces,  Firewall Bypass Techniques

• Week 10:  Firewall Technologies
Topics:  Netfilter and iptables, Stateful  vs. Stateless  Inspection,  SNAT and DNAT

• Week 11:  Advanced Routing Security (BGP)
Topics:  Autonomous  Systems and Peering,  BGP  Path  Selection, Prefix Hijacking, Route Leaks, RPK

• Week 12:  12th Week Exam & Security Monitoring
Assessment covering Weeks 8-11
Topics:  Security Monitoring,  SIEM Tools (Splunk,  ELK), SOAR

• Week 13:  Practical Application & Case Studies
Topics:  Hands-on  Labs (IDS/IPS, NGFW,  SIEM),  Cyber  Defense Case Studies,  Group
Projects

• Week 14:  Final Exam

Required Tools & Software
• Packet Analysis: Wireshark,  tcpdump
• Network Discovery: Nmap, Advanced IP Scanner
• Packet Crafting: Scapy
• Exploitation: Metasploit
• Web Testing: Burp Suite
• Firewall Management: iptables
• Remote Access: PuTTY
• Command-line Utilities: ping, traceroute, nslookup, dig, netstat

# Week 1  Networking Fundamentals  Chapter 1

##

#Quiz
	1. What does OSI stand for?
	   ==**Open Systems Interconnection**==
	2. How many layers are in the OSI model?
	   ==**7**==
	3. Which layer of the OSI model is responsible for IP addressing?
	   ==**Network**==
	4. A switch operates mainly at which OSI layer?
	   ==**Layer 2**==
	5. A router operates mainly at which OSI layer?
	   ==**a) Layer 3**==
	6. What is the main function of a switch?
	   ==**Forward frames based on MAC addresses**==
	7. What is the main function of a router?
	   ==**Route packets between networks**==
	8. Which OSI layer is responsible for end-to-end reliable communication?
	   ==**Transport**==
	9. Which device **reduces** collision domains but **not broadcast** domains?
	   ==**Switch**==
	10. Which device **increases** collision domains but **decreases broadcast** domains?
	   **==Hub==**
	11. In security context, why is understanding OSI layers important?
	  ==**It allows precise identification of attack points and defense mechanisms.**==
	12. What is the default subnet mask for a Class C IPv4 network? 
	    ==**255.255.255.0**==
	13. Which IP address type is used for one-to-many communication?
	    ==**Multicast**==
	14. What does NAT stand for?
	    ==**Network Address Translation**==
	15. How many usable host addresses are there in a /30 subnet?
	    ==**2**==
	    Host = ((2^h) -2)  = 4 -2 = ===2== 
	16. Which device operates primarily to connect different networks?
	    ==**Router**==
	17. Which command shows the IP configuration on a Windows PC?
	    ==**Ipconfig**==
	18. What is the purpose of a VLAN?
	    ==**Isolate broadcast domains within a switch**==
	19. Which IP address is considered a private IP address?
	    Include:
	    - **==10.0.0.0== to ==10.255.255.255==**
	    - **==172.16.0.0== to ==172.31.255.255==**
	    - **==192.168.0.0== to ==192.168.255.255==**
	20. What is the purpose of a subnet mask?
	    ==**To divide an IP network into smaller networks**==
	21. Which command can test connectivity between two devices on a network?
	    ==**Ping**==


---

#Quiz 
	1. What is the primary purpose of a routing table in a router?
	   ==**To determine the best path for packet forwarding**==
	2. Which of the following entries is typically found in a routing table?
	   ==**Destination network**==
	3. Which metric represents the number of routers a packet must pass through?
	   ==**Hop count**==
	4. Administrative Distance (AD) is used to:
	   ==**Select the best routing protocol source**==
	5. If multiple routes exist to the same destination, the router chooses the route with:
	   ==**Lowest metric value**==
	6. Which command displays the routing table on a Cisco router?
	   ==**Show ip route**==
	7. What does the “next hop” field in a routing table indicate?
	   ==**Next router to forward the packet to**==
	8. Which routing table entry is used when no specific route matches a destination?
	   ==**Default route**==
	9. Which routing table component specifies where the packet leaves the router?
	   ==**Outgoing interface**==
	10. Which layer of the OSI/TCP-IP model is routing mainly associated with?
	    ==**Network layer**==
	11. RIP is classified as which type of routing protocol?
	    ==**Distance Vector**==
	12. What metric does RIP use to select the best path?
	    ==**Hop count**==
	13. What is the maximum hop count allowed in RIP?
	    ==**15**==
	14. Why is RIP considered slow to converge?
	    ==**It sends updates every 30 seconds**==
	15. OSPF calculates the shortest path using which algorithm?
	    ==**SPF (Dijkstra)**==
	16. What is the backbone area in OSPF called?
	    ==**Area 0**==
	17. Which routing protocol supports **unequal-cost load balancing**?
	    ==**EIGRP**==
	18. Which protocol is primarily used to connect **different Autonomous Systems (AS)**?
	    ==**BGP**==
	19. Which routing protocol prioritizes policy and **stability over fast** convergence?
	    ==**BGP**==
	20. Which protocol is known as the “error reporting and diagnostic protocol” of the Internet?
	    ==**ICMP**==





### 
![[Network Security and Cyber Defense (Midterm) Quizzes.html]]