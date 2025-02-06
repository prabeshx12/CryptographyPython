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