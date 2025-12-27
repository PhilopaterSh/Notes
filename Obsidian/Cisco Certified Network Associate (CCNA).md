 تصنيف الأجهزة الشبكية وفق نموذج OSI كما يُدرّس في منهج CCNA، مع ذكر الوصف والملاحظات الإضافية لكل جهاز:

| **Device**                     | **OSI Layer**                                                                             | **Description**                                                                                     | **Additional Notes**                                                                    |
| ------------------------------ | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Repeater**                   | Physical Layer (Layer 1)                                                                  | Amplifies or regenerates signals over a long distance without processing the data.                  | Used to extend the reach of a network; works only with electrical/optical signals.      |
| **Hub**                        | Physical Layer (Layer 1)                                                                  | Broadcasts incoming signals to all ports without filtering or processing data.                      | Does not use MAC addresses; simply repeats signals, leading to potential collisions.    |
| **Bridge**                     | Data Link Layer (Layer 2)                                                                 | Connects and filters traffic between two LAN segments using MAC addresses.                          | Reduces collision domains by segmenting network traffic.                                |
| **Switch**                     | Data Link Layer (Layer 2)                                                                 | Forwards frames within a LAN based on MAC addresses stored in its Content Addressable Memory (CAM). | Considered the "brain" of the LAN; limits broadcast traffic by segmenting the network.  |
| **Wireless Access Point (AP)** | Data Link Layer (Layer 2)                                                                 | Provides wireless connectivity for devices to access the LAN.                                       | May incorporate additional security features for wireless communications.               |
| **Router**                     | Network Layer (Layer 3)                                                                   | Routes packets between different networks using IP addresses.                                       | Uses routing tables and protocols to determine the best path for data delivery.         |
| **Multilayer Switch**          | Data Link Layer (Layer 2) / Network Layer (Layer 3)                                       | Combines the functionalities of a switch and a router, performing both switching and routing.       | Often used in enterprise networks to enhance performance and reduce routing complexity. |
| **Firewall**                   | Primarily Network Layer (Layer 3) and sometimes Transport/Application Layers (Layers 4-7) | Inspects and filters traffic based on security policies to block unauthorized access.               | Can integrate deep packet inspection (DPI) and intrusion prevention capabilities.       |
| **VPN Gateway**                | Network Layer (Layer 3) and above                                                         | Establishes secure, encrypted tunnels for data between remote users or networks over the Internet.  | Often integrated with routers or firewalls to secure remote connectivity.               |
| **AAA Server**                 | Application Layer (Layer 7)                                                               | Manages authentication, authorization, and accounting for network access.                           | Used to enforce security policies and monitor network access.                           |

#### OSI Model (Open Systems Interconnection Model) VS TCP/IP Model (Transmission Control Protocol/Internet Protocol)
| **OSI Model** | **TCP/IP Model**                | **Data Unit**                             |
| ------------- | ------------------------------- | ----------------------------------------- |
| Application   | Application                     | Data                                      |
| Presentation  | — (Integrated into Application) | — (Data handled at the Application layer) |
| Session       | — (Integrated into Application) | — (Data handled at the Application layer) |
| Transport     | Transport                       | Segment (for TCP) / Datagram (for UDP)    |
| Network       | Internet                        | Packet                                    |
| Data Link     | Network Interface / Link        | Frame                                     |
| Physical      | Network Interface / Link        | Bits                                      |
### Classes rang IP Addresses
|**Class**|**Range**|**Default Subnet Mask**|**Number of Networks**|**Number of Hosts per Network**|
|---|---|---|---|---|
|**Class A**|1.0.0.0 to 126.0.0.0|255.0.0.0|128|16,777,214|
|**Class B**|128.0.0.0 to 191.255.0.0|255.255.0.0|16,384|65,534|
|**Class C**|192.0.0.0 to 223.255.255.0|255.255.255.0|2,097,152|254|
|**Class D**|224.0.0.0 to 239.255.255.255|Not applicable|Reserved for multicast|Not applicable|
|**Class E**|240.0.0.0 to 255.255.255.255|Not applicable|Reserved for future use|Not applicable|
- **Class D:**  
        تُخصص لعناوين البث المتعدد (Multicast) ولا تستخدم لتعيين عناوين مضيفين عاديين.
- **Class E:**  
        مخصصة للاستخدامات التجريبية أو المستقبلية ولا تُستخدم في الشبكات العامة. 
- **Class A و Class B و Class C** تعتبر جميعها جزءاً من نظام التصنيف الكلاسيكي (Classful).
#### **CIDR (Classless Inter-Domain Routing):**

- مع ظهور CIDR، أصبح من الممكن تخصيص عناوين IP بنظام "غير كلاسيكي" (Classless)، مما يعني أنه لم يعد يُلزم بتقسيم العناوين وفق الفئات الثابتة A، B، C.
- يُتيح CIDR استخدام قناع شبكة بطول متغير (VLSM)، مما يساعد على تحسين استخدام العناوين وتقليل الهدر.
### ### IPv4 Unicast vs. IPv6 Unicast

| **Aspect**              | **IPv4 Unicast**                                            | **IPv6 Unicast**                                                           |
| ----------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Address Length**      | 32 bits                                                     | 128 bits                                                                   |
| **Broadcast Support**   | Supports broadcast addresses (one-to-all communication)     | No broadcast; multicast is used instead                                    |
| **Address Types**       | Public Unicast, Private Unicast                             | Global Unicast, Link-Local, Unique Local                                   |
| **Routing & Structure** | Uses traditional routing methods (Classful/CIDR addressing) | Employs fully integrated CIDR addressing with enhanced routing scalability |
| **Communication Type**  | Direct one-to-one communication between devices             | Direct one-to-one communication between devices                            |
- **IPv4 Unicast** uses 32-bit addresses and supports broadcast communication, meaning that in addition to unicast, it can send data to all hosts within a network.
- **IPv6 Unicast** uses 128-bit addresses, which allows for a vastly larger address space. It does not support traditional broadcasting; instead, multicast is used for functions that require one-to-all or one-to-many communications.
- IPv6 introduces more flexible address types (such as Global, Link-Local, and Unique Local) and is designed with more advanced routing mechanisms to improve scalability and efficiency in modern networks.
### NAT (Network Address Translation)
**التعريف:** هي تقنية تُستخدم لترجمة عناوين IP الخاصة (الخاصة بالشبكة الداخلية) إلى عناوين IP عامة عند خروج حركة المرور إلى الإنترنت، والعكس بالعكس.
#### **أنواع NAT**

- **Static NAT:**  
    تقوم بترجمة عنوان IP خاص إلى عنوان IP عام ثابت (واحد لواحد).
- **Dynamic NAT:**  
    تقوم بترجمة عناوين IP الخاصة إلى مجموعة من العناوين العامة المتوفرة (تُختار من قائمة عناوين عامة بشكل ديناميكي).
- **PAT (Port Address Translation) أو NAT Overload:**  
    يقوم بترجمة عدة عناوين خاصة إلى عنوان IP عام واحد باستخدام أرقام منافذ مختلفة لتمييز الاتصالات.
##### Private IP --To-- Public
### RIP (Routing Information Protocol)
- **التعريف:**  
    RIP هو بروتوكول توجيه من نوع distance vector يُستخدم لتبادل معلومات التوجيه بين أجهزة التوجيه (routers) في الشبكات الصغيرة أو المتوسطة.
- **الميزة الأساسية:**  
    يعتمد على عدد القفزات (hops) كمعيار لتحديد أفضل مسار؛ حيث أن الحد الأقصى لعدد القفزات هو 15 (أي أن الشبكات التي تتطلب أكثر من 15 قفزة تُعتبر غير قابلة للوصول).

#### ب. **الإصدارات الرئيسية**

- **RIP v1:**
    - لا يدعم VLSM (التقسيم الفرعي بطول متغير).
    - يستخدم البث (broadcast) لإرسال تحديثات التوجيه.
- **RIP v2:**
    - يدعم VLSM ويتيح توجيه أفضل في الشبكات التي تتطلب تقسيمًا فرعيًا.
    - يستخدم الإرسال المتعدد (multicast) لتقليل الازدحام.
    - يدعم المصادقة (authentication) لتعزيز الأمان.

## OSPF (Open Shortest Path First)

- **التعريف:**  
    OSPF هو بروتوكول توجيه من نوع link-state، يُستخدم في الشبكات الأكبر والأكثر تعقيدًا. يقوم ببناء خريطة كاملة للشبكة (topology) ويستخدم خوارزمية Dijkstra لحساب أقصر مسار.
- **المزايا:**
    - يدعم تقسيم الشبكة إلى مناطق (Areas) مما يحسن من الأداء ويقلل من حجم المعلومات التي يجب تبادلها بين أجهزة التوجيه.
    - يدعم VLSM ويتميز بسرعة التقارب (convergence).

#### ب. **المفاهيم الأساسية في OSPF**

- **المناطق (Areas):**  
    تُقسم الشبكة إلى مناطق، حيث يُعد Area 0 (المنطقة الأساسية أو Backbone) هو المحور الرئيسي الذي ترتبط به باقي المناطق.
- **LSA (Link State Advertisement):**  
    الرسائل التي تُرسلها أجهزة التوجيه للإعلان عن حالتها وحالة الروابط المتصلة بها.
- **Cost (التكلفة):**  
    يستخدم معيار التكلفة (عادةً يعتمد على عرض النطاق الترددي) لتحديد أفضل مسار للوصول إلى الشبكة الوجهة.
### VLSM (Variable Length Subnet Mask)
- **المفهوم الأساسي:**  
    VLSM تعني "قناع الشبكة الفرعي بطول متغير"، وهي تقنية تتيح تقسيم شبكة IP (مثلاً شبكة 192.168.1.0/24) إلى عدة أقسام فرعية بأحجام مختلفة بحسب الحاجة.
- **الفكرة:**  
    بدلاً من استخدام قناع شبكة ثابت (Fixed Length Subnet Mask) لجميع الأقسام الفرعية، يتيح VLSM تعيين أقنعة فرعية مختلفة لكل قسم وفقاً لعدد الأجهزة (المضيفين) المطلوب داخل كل قسم.

### SSH vs Telnet
| **Feature**                | **SSH**                                                    | **Telnet**                                           |
| -------------------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| **Encryption**             | Encrypted (provides secure communication)                  | Unencrypted (plain text communication)               |
| **Security**               | Secure against eavesdropping and man-in-the-middle attacks | Insecure and vulnerable to eavesdropping             |
| **Authentication**         | Supports password, public key, and other methods           | Typically uses username and password authentication  |
| **Port Number**            | Default port 22                                            | Default port 23                                      |
| **Protocol**               | TCP/IP                                                     | TCP/IP                                               |
| **Functionality**<br>      | Secure remote login, file transfer, tunneling              | Remote terminal access                               |
| **Use Cases**              | Secure system administration, secure file transfers        | Simple remote terminal access, mainly legacy systems |
| **Data Integrity**         | Ensures data integrity and confidentiality                 | No data integrity checks                             |
| **Performance**            | Slightly higher overhead due to encryption                 | Lower overhead, but insecure                         |
| **Common Implementations** | OpenSSH, PuTTY, SecureCRT                                  | Telnet client built into most operating systems      |
### AAA (Authentication, Authorization, and Accounting)
- **Authentication (التحقق):**  
    تأكيد هوية المستخدم قبل السماح له بالوصول إلى الجهاز.
    
- **Authorization (التفويض):**  
    تحديد الصلاحيات التي يمتلكها المستخدم (ما يمكنه فعله على الجهاز).
    
- **Accounting (التسجيل):**  
    تسجيل الأنشطة والإجراءات التي يقوم بها المستخدم.

### VPN (Virtual Private Networks) and Proxy
#### أ. **VPN وصول عن بُعد (Remote Access VPN):**

- **الاستخدام:**  
    يُستخدم للسماح للمستخدمين الفرديين (مثل الموظفين أو العملاء) بالاتصال بشبكة الشركة من مواقع خارجية.
- **الآلية:**  
    يقوم المستخدم بإنشاء نفق VPN من جهازه الشخصي (مثل الكمبيوتر المحمول أو الهاتف الذكي) إلى خادم VPN في الشبكة الداخلية، حيث يتم التحقق من الهوية وتشفير الاتصال.

#### ب. **VPN بين المواقع (Site-to-Site VPN):**

- **الاستخدام:**  
    يُستخدم لربط شبكات أو مواقع جغرافية مختلفة مثل فروع شركة موزعة في مناطق مختلفة.
- **الآلية:**  
    يتم إنشاء نفق VPN بين أجهزة توجيه (Routers) أو جدران حماية (Firewalls) في كل موقع، بحيث تصبح الشبكات المرتبطة تبدو كأنها شبكة واحدة متكاملة.

#### ج. **VPN عبر SSL/TLS:**

- **الاستخدام:**  
    يعتمد على بروتوكولات SSL/TLS (المستخدمة عادةً في تأمين الاتصالات على الويب) لإنشاء نفق آمن.
- **المزايا:**  
    يُستخدم عادةً في تطبيقات الوصول عن بُعد عبر متصفح الويب، مما يُسهّل عملية الوصول دون الحاجة لتثبيت برامج عميلة (Client).

- **VPN** يُستخدم لتأمين حركة المرور عبر نفق مشفر شامل يعمل على مستوى الجهاز، مما يوفر حماية متكاملة للاتصالات عن بُعد وربط الشبكات معاً.
- **Proxy** يعمل كوسيط لتصفية الطلبات وتحسين الأداء، ويُستخدم عادة على مستوى التطبيقات مثل تصفح الويب، ولكنه لا يوفر تشفيراً شاملاً لكل حركة المرور.

### ACLs (Access Control Lists)
تعمل على السماح أو منع مرور حزم البيانات بناءً على معايير محددة مثل عنوان المصدر، وعنوان الوجهة، وبروتوكول الاتصال، وأرقام المنافذ
Filter allow or block 
Source, Destination, Type Protocol, Port number
#### أنواع ACLs
  1. ACLs قياسية (Standard ACLs)
      **التركيز:**  تقتصر على فحص عنوان IP المصدر فقط، دون النظر إلى عنوان الوجهة أو البروتوكولات المستخدمة

1. ACLs موسعة (Extended ACLs)
    **التركيز:**  تستطيع فحص عدة معايير منها:
    - عنوان IP المصدر.
    - عنوان IP الوجهة.
    - نوع البروتوكول (TCP، UDP، ICMP، إلخ).
    - أرقام المنافذ (مثل 80 لـ HTTP، 443 لـ HTTPS، إلخ).
2. ACLs المسماة (Named ACLs)
    **التركيز:**  
    بدلاً من استخدام الأرقام لتحديد ACL، يمكنك إعطاء ACL اسمًا مما يسهل عملية التوثيق والإدارة.
### Firewalls
تُستخدم لحماية الشبكات باستخدام قواعد ACLs، حيث يمكن اعتبارها نوعًا من الفحص الأساسي (Packet Filtering). وقد يتم الإشارة إلى:

- **جدران الحماية القائمة على الفحص الأساسي stateless (Packet-Filtering Firewalls) :**  
    تفحص رؤوس الحزم (Headers) اعتمادًا على معايير مثل عناوين IP والمنافذ، وتقرر السماح أو الرفض.
    
- **مفاهيم الجدران النارية القائمة على الحالة  stateful (Stateful Inspection) :**  
    تُتابع حالة الاتصال وتقوم بتقييم كل حزمة ضمن سياق الجلسة
- **Proxy Firewall – جدار الحماية الوكيل** : 
جدار الحماية الوكيل (Proxy Firewall) هو نوع متقدم من جدران الحماية يعمل كوسيط بين المستخدمين والإنترنت. عندما يطلب جهاز داخل الشبكة الوصول إلى موقع أو خدمة خارجية، يقوم البروكسي بفحص الطلب أولاً، ثم يرسله إلى الوجهة المستهدفة نيابةً عن المستخدم. يتم استخدامه لتعزيز الأمان والخصوصية من خلال إخفاء عناوين IP الداخلية ومراقبة حركة المرور بشكل دقيق. 
##### **الفرق بين Proxy Firewall و Traditional Firewall**

|الميزة|Proxy Firewall|Traditional Firewall|
|---|---|---|
|**طريقة العمل**|يعمل كوسيط، يمنع الاتصال المباشر|يسمح بالاتصال المباشر مع تصفية على مستوى المنافذ|
|**مستوى الحماية**|أعلى (لأنه يعزل الشبكة بالكامل)|أقل مقارنةً بالبروكسي|
|**الأداء**|أبطأ بسبب فحص كل طلب|أسرع لأن الفحص يتم على مستوى الحزم فقط|
|**إخفاء الهوية**|نعم، يخفي عناوين IP الداخلية|لا، يمرر الاتصالات مباشرة|
|**التحكم في المحتوى**|قوي جدًا (يدعم فلترة المواقع والتطبيقات)|محدود (يعتمد على قواعد المنافذ والعناوين)|
#### Next-Generation Firewall (NGFW) – جدار الحماية من الجيل التالي

- **التعريف:**  
    جدار الحماية من الجيل التالي (NGFW) هو جدار حماية متقدم يتجاوز الوظائف التقليدية (مثل الفحص الأساسي لحزم البيانات وفحص الحالة) ليقدم قدرات أمان شاملة تتضمن التعرف على التطبيقات، وإجراء الفحص العميق للحزم (DPI)، والتكامل مع نظم الكشف والوقاية من التطفل (IDS/IPS)، بالإضافة إلى دعم تحليل حركة المرور المشفرة.
#####  Deep Packet Inspection (DPI) – الفحص العميق للحزم

- **التعريف:**  
    الفحص العميق للحزم (DPI) هو تقنية تُستخدم لتحليل محتوى الحزم المارة عبر الشبكة، وليس فقط فحص رؤوس الحزم (Header) كما في الفحص التقليدي. يقوم DPI بفحص البيانات المُحملة داخل كل حزمة لتحديد طبيعتها، والتحقق من تطبيقات معينة، والبحث عن توقيعات هجمات أو محتوى غير مرغوب فيه.
#### IPS (Intrusion Prevention System) vs IDS (Intrusion Detection System)

| **Feature**           | **IPS**                                          | **IDS**                                                             |
| --------------------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| **Purpose**           | Prevents attacks                                 | Detects attacks                                                     |
| **Action**            | Proactively blocks malicious activity            | Monitors and alerts on suspicious activity                          |
| **Deployment**        | Inline (directly in the communication path)      | Out-of-band (parallel to the communication path)                    |
| **Response Time**     | Immediate                                        | After detection                                                     |
| **Configuration**     | Requires careful tuning to avoid false positives | Typically generates fewer false positives, but more false negatives |
| **Impact on Network** | Can cause latency                                | Minimal impact on network performance                               |
| **Complexity**        | Higher complexity, requires constant updates     | Relatively simpler to deploy and maintain                           |
| **Examples**          | Cisco Firepower, Palo Alto Networks              | Snort, OSSEC                                                        |
1. **اكتشاف التوقيعات (Signature-Based Detection):** يقوم برصد توقيعات كل وحدة بيانات (بيلود)، وفي حالة العثور على شيء مشابه لما هو مخزن لديه، يصدر تنبيهًا.
2. **اكتشاف الشذوذ (Anomaly Detection):** يتعلم سلوك النظام اليومي، وعند اكتشاف أي اختلافات أو سلوك غير معتاد، يصدر تنبيهًا.

### STP (Spanning Tree Protocol)
- **ما هو STP؟**  
    هو بروتوكول يُستخدم لمنع حدوث الحلقات (loops) في شبكات السويتش (Layer 2) ذات الهيكلية المتكررة (Redundant Topologies).
- **الغرض الأساسي:**  
    الحفاظ على شبكة خالية من الحلقات التي قد تؤدي إلى ازدحام مرور البيانات وتدهور أداء الشبكة.
### CIA (Confidentiality, Integrity, Availability)
- **Confidentiality (السرية):**
    - **المقصود:** حماية المعلومات بحيث لا يتم الوصول إليها من قبل أفراد غير مصرح لهم.
    - **التطبيق:** استخدام التشفير، التحكم في الوصول، سياسات كلمات المرور.
- **Integrity (السلامة):**
    - **المقصود:** ضمان أن تكون البيانات دقيقة وغير معدلة أو مشوهة أثناء النقل أو التخزين.
    - **التطبيق:** استخدام آليات التحقق مثل التجزئة (Hashing) والتوقيعات الرقمية.
- **Availability (التوافر):**
    - **المقصود:** ضمان أن تكون المعلومات والخدمات متاحة للمستخدمين المصرح لهم عند الحاجة.
    - **التطبيق:** تصميم الشبكات بنظام النسخ الاحتياطي (Redundancy)، واستخدام تقنيات التوازن (Load Balancing) وآليات الاستجابة للطوارئ.
### DHCP Snooping
- **ما هو DHCP Snooping؟**  
    هو ميزة أمان تُستخدم على مستوى السويتش لمنع هجمات الـ DHCP (مثل DHCP spoofing) التي قد تُتيح لجهاز غير مصرح به توزيع عناوين IP غير صحيحة للمستخدمين.
- **الغرض الأساسي:**  
    حماية عملية توزيع عناوين IP عبر الشبكة من خلال التحقق من مصادر خوادم DHCP الموثوقة.
### Dynamic ARP Inspection (DAI)
#### 1. تعريف DAI

- **Dynamic ARP Inspection (DAI)** هو ميزة أمان تُستخدم على مستوى السويتش (Layer 2) لحماية الشبكة من هجمات ARP مثل ARP spoofing أو ARP poisoning.
- تعمل DAI على التحقق من صحة رسائل ARP (طلب واستجابة) عن طريق مقارنة معلوماتها مع جدول الربط (binding table) الذي يتم إنشاؤه بواسطة ميزة **DHCP Snooping**.
#### 2. الهدف والوظيفة

- **الهدف الرئيسي:**  
    منع المهاجمين من إرسال رسائل ARP مزيفة تُستخدم لتغيير جداول ARP على الأجهزة داخل الشبكة، مما يؤدي إلى اعتراض حركة المرور (Man-in-the-Middle) أو انتحال شخصية أجهزة أخرى.
### MPLS (Multiprotocol Label Switching)
- **ا هو MPLS؟**  
    MPLS أو "التحويل متعدد البروتوكولات باستخدام الملصقات" هو تقنية تُستخدم في شبكات الاتصالات لتسريع عملية التوجيه وتسهيل إدارة حركة المرور عن طريق إضافة ملصقات (Labels) قصيرة إلى حزم البيانات.
- **الفكرة الأساسية:**  
    بدلاً من الاعتماد على بحث جداول التوجيه التقليدية (التي تستخدم عناوين IP كاملة)، تقوم MPLS بتوجيه الحزم باستخدام ملصقات محددة تُحدِّد مسارًا محددًا (Label Switched Path - LSP) عبر الشبكة.

### Attacks
#### 1. هجوم VLAN (VLAN Attack)
- **VLAN Hopping:**
    - **الوصف:**  
        يقوم المهاجم بمحاولة تجاوز حدود الـ VLAN عبر تقنيات مثل **Double Tagging** أو **Switch Spoofing**.
#### 2. هجمات DHCP (DHCP Attack)

- **DHCP Starvation Attack:**
    - **الوصف:**  
        يقوم المهاجم بإرسال عدد ضخم من طلبات DHCP باستخدام عناوين MAC مزيفة بهدف استنفاد جميع عناوين IP المتاحة على خادم DHCP، مما يمنع الأجهزة الشرعية من الحصول على عناوين.
- **DHCP Spoofing Attack:**
    - **الوصف:**  
        يقوم المهاجم بتشغيل خادم DHCP غير مصرح به في الشبكة لتوزيع إعدادات شبكة مزورة (مثل عنوان البوابة الافتراضية) على الأجهزة، مما يمكنه من اعتراض حركة المرور أو إعادة توجيهها.
#### 3. هجمات ARP (ARP Attack)

- **ARP Spoofing / ARP Poisoning:**
    - **الوصف:**  
        يقوم المهاجم بإرسال رسائل ARP مزورة تربط بين عنوان IP معين وعنوان MAC خاطئ (عادة ما يكون عنوان المهاجم)، مما يؤدي إلى تغيير جداول ARP على الأجهزة داخل الشبكة.  
        ينتج عن ذلك اعتراض حركة المرور (Man-in-the-Middle) أو تعطيل الاتصال.
#### 4. هجوم انتحال العناوين (Address Spoofing Attack)

- **الوصف:**  
    يقوم المهاجم بتزوير عناوين IP أو MAC في حزم البيانات ليتظاهر بأنه جهاز موثوق به داخل الشبكة.  
    يُستخدم هذا النوع من الهجمات لتجاوز ضوابط الأمان أو لشن هجمات مثل هجمات الحرمان من الخدمة (DoS) أو هجمات man-in-the-middle.
#### 5. هجوم STP (STP Attack)

- **STP Manipulation:**
    - **الوصف:**  
        يقوم المهاجم بإرسال رسائل BPDU (Bridge Protocol Data Units) مزورة تحتوي على Bridge ID منخفض لجعل جهاز غير مصرح به يصبح الـ Root Bridge في شبكة STP.  
        يؤدي ذلك إلى إعادة تنظيم مسارات التبديل داخل الشبكة، مما قد يسبب اضطرابات في حركة المرور، ويتيح للمهاجم إعادة توجيه أو اعتراض البيانات.
        
#### 6. هجمات الإغراق (Flooding Attacks):

- **MAC Flooding:**
    - **الوصف:** يرسل المهاجم عددًا ضخمًا من الإطارات المزيفة التي تحمل عناوين MAC مختلفة إلى السويتش، مما يؤدي إلى ملء جدول CAM ودفع السويتش إلى تحويل جميع الحزم إلى جميع المنافذ (Flooding).
- **ICMP Flooding (Ping Flood):**
    - **الوصف:** إرسال عدد كبير من طلبات Ping (ICMP Echo Requests) إلى جهاز مستهدف بهدف استنزاف موارده والتسبب في بطء أدائه أو توقفه.
#### 7. هجوم التضخيم Amplification Attack

- **التعريف:**  
    هجوم التضخيم (Amplification Attack) هو نوع من هجمات الحرمان من الخدمة (DoS) يعتمد على استغلال بروتوكولات معينة لتحويل طلب صغير الحجم إلى ردود بيانات كبيرة، بحيث تُضاعف كمية البيانات المرسلة إلى الهدف.
**الهدف:**  
استنزاف موارد الشبكة أو الجهاز المستهدف مما يؤدي إلى تعطل الخدمات.
#### 8. هجوم التنصت (Sniffing Attack)

- **التعريف:**  
    التنصت هو أسلوب يُستخدم فيه المهاجم لمراقبة حركة مرور البيانات على الشبكة (أي "التقاط" الحزم) بهدف جمع معلومات حساسة مثل كلمات المرور، أو بيانات الجلسات، أو معلومات التكوين. يُعتبر التنصت هجومًا سلبيًا؛ إذ لا يقوم المهاجم بتعديل أو تعطيل حركة المرور بل يلتقطها لمراقبتها.

#### مصطلحات:
- **الثغرة الأمنية (Vulnerability):** هي نقطة ضعف يمكن استغلالها.
- **التهديد (Threat):** يمثل المصدر أو الحدث المحتمل الذي يستغل الثغرات.
- **المخاطر (Risk):** تتحدد من خلال احتمال وقوع التهديد وتأثيره عند استغلال الثغرة.
- **الاستغلال (Exploitation):** هو عملية استغلال المهاجم للثغرة للوصول إلى النظام.
- **ثغرة اليوم صفر (Zero-Day):** هي ثغرة غير معروفة حتى يتم استغلالها ولا يتوفر لها تحديث أمني عند اكتشافها.
### جدول أرقام المنافذ (Port Numbers) لأهم الخدمات

| **Service**   | **Port Number** | **Protocol** | **Description**                    |
| ------------- | --------------- | ------------ | ---------------------------------- |
| HTTP          | 80              | TCP          | نقل صفحات الويب                    |
| HTTPS         | 443             | TCP          | نقل صفحات الويب الآمن              |
| FTP (Control) | 21              | TCP          | التحكم في نقل الملفات              |
| FTP (Data)    | 20              | TCP          | نقل بيانات الملفات                 |
| SMTP          | 25              | TCP          | إرسال البريد الإلكتروني            |
| DNS           | 53              | TCP/UDP      | نظام أسماء النطاقات                |
| Telnet        | 23              | TCP          | الوصول البعيد النصي                |
| SSH           | 22              | TCP          | الوصول البعيد الآمن                |
| POP3          | 110             | TCP          | استرجاع البريد الإلكتروني (POP3)   |
| IMAP          | 143             | TCP          | استرجاع البريد الإلكتروني (IMAP)   |
| SNMP          | 161             | UDP          | إدارة الشبكات                      |
| LDAP          | 389             | TCP/UDP      | خدمات الدليل                       |
| RDP           | 3389            | TCP          | الوصول لسطح المكتب البعيد          |
| TFTP          | 69              | UDP          | نقل الملفات البسيط                 |
| DHCP Server   | 67              | UDP          | توزيع عناوين IP من الخادم (Server) |
| DHCP Client   | 68              | UDP          | استلام عنوان IP من الخادم (Client) |
| NTP           | 123             | UDP          | بروتوكول الوقت الشبكي              |
![[Network Security.gif]]

## 🔹 **1. 3-Way Handshake** (TCP/IP)

This is used to **establish a TCP connection** between two devices (e.g., client and server).
### ✅ **Steps:**
1. **SYN:** Client sends a synchronization (SYN) request to the server.
2. **SYN-ACK:** Server responds with a SYN-ACK (synchronization + acknowledgment).
3. **ACK:** Client sends back an ACK to confirm.
➡️ **Result:** TCP connection is established.

### 🔐 Use case:
- Any application that uses TCP: web browsing, email, file transfers.

## 🔹 **2. 4-Way Handshake** (Wi-Fi Security – WPA/WPA2)

This is used to **establish a secure session between a client and an access point** (AP) in Wi-Fi networks using WPA/WPA2.
### ✅ **Steps:**
1. **AP sends ANonce** (a random number) to the client.
2. **Client generates PTK** (Pairwise Transient Key) and sends back SNonce and MIC (Message Integrity Code).
3. **AP calculates PTK** and verifies MIC, then sends its own MIC to the client.
4. **Client confirms and installs the keys.**    
➡️ **Result:** Secure encryption keys are exchanged, and the connection is encrypted.
### 🔐 Use case:
- When a device connects to a **WPA/WPA2-protected Wi-Fi network**.

| Feature           | 3-Way Handshake                | 4-Way Handshake                         |
| ----------------- | ------------------------------ | --------------------------------------- |
| Purpose           | Establish TCP connection       | Establish secure Wi-Fi encryption keys  |
| Layers            | Transport Layer (TCP)          | Data Link Layer (Wi-Fi security – WPA2) |
| Steps             | 3 steps (SYN, SYN-ACK, ACK)    | 4 steps (Nonce, SNonce, MIC exchanges)  |
| Protocol involved | TCP                            | WPA2/WPA3 (IEEE 802.11i)                |
| Security focus    | No encryption, just connection | Handles encryption key generation       |

## ✅ **1. Broadcast Domain**

### 🔹 Definition:

A **broadcast domain** is a logical area in a network where a **broadcast message** (like ARP requests or DHCP discover) can be heard by **all devices**.

### 🔊 Example:

When a PC sends a broadcast (e.g., "Who has IP 192.168.1.1?"), **all devices** in the same broadcast domain will hear it.

### 💡 What creates broadcast domains?

- **Routers** **separate** broadcast domains.
    
- **Switches** (by default) **do not** separate broadcast domains (unless you use VLANs).
    

### 📌 Key points:
- All devices in the **same subnet** are in the same broadcast domain.
- Too many devices in a broadcast domain = network **congestion**.    

---

## ✅ **2. Collision Domain**
### 🔹 Definition:
A **collision domain** is an area of the network where **data packets can collide** if sent at the same time.

### 💥 When does a collision happen?
In half-duplex communication (like in old hubs), if **two devices** send data at the same time on the same wire, the signals collide.

### 💡 What creates or breaks collision domains?
- **Switches** separate collision domains per port.
- **Hubs** do **not** separate collision domains (everything is shared).    
- **Routers** also separate collision domains.
### 📌 Key points:
- Each **switch port** = 1 collision domain.
- More collision domains = **better performance**.
---
## 🔻 Key Differences:

|Feature|Broadcast Domain|Collision Domain|
|---|---|---|
|Affected by|Broadcast traffic|Data collision|
|Separated by|Routers (or VLANs on switches)|Switches, routers|
|Shared by|Devices in the same subnet|Devices connected through a hub|
|Goal|Reduce unnecessary broadcast traffic|Prevent data collisions|
|Modern networks use|VLANs to manage|Switches to isolate|