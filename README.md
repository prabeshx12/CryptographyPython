<h1>This will be about Cryptography, Networking and Security</h1>

<h2>Day 1</h2>
<h3>Substitution Cipher</h3>
<h4>
-> Caesar Cipher(+3) --> A becomes D, B becomes E and so on.<br>

<h3>Morse Code</h3>
<h4>
-> WIll change numbers letters into dots(.) and dashes(_).</h4>

<h2>Day 2</h2>
<h3>Hashing Algorithm</h3>
<h4>
Properties:<br>
-> should be fast but not so fast.<br>
->shouldn't have hash collisions.<br>
->has kind of like avalanche effect. i.e. changing in one bit changes the whole hash value. 

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
-> receiver uses the private key(d, n) to decrypt the Ciphertext C into Message M using the formular: <i> M = C<sup>d</sup> mod n</i>.<br>


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
1. Message Hashing: It is done using any hashing algorithms such as SHA-1 or SHA-256. This hash value is denoted by <i>H(m)</i>


2. Signature Generation: <br>
    Select a random integer <i>k</i> (form a range([1, q - 1] where q is small prime divisor of p - 1.) determined by the parameters of DSA).<br><br>

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
