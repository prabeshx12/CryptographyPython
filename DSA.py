# simple code implementation for Digital Signature Algorithm(DSA).
def modular_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


# key generation
p = 23  # a small prime number for p
q = 11  # a small prime divisor of p-1 for q
g = 2   # generator g such that g^q mod p = 1
x = 6   # private key, a random number between 1 and q-1
y = pow(g, x, p)  # public key

print("Key Generation:")
print(f"p = {p}, q = {q}, g = {g}, x (private key) = {x}, y (public key) = {y}")

# Signing
message = "Test"
H_m = sum(ord(c) for c in message)  # Simple hash of the message (sum of ASCII values)
k = 3  # Randomly chosen k value between 1 and q-1

# Calculate r = (g^k mod p) mod q
r = pow(g, k, p) % q

# Calculate s = k^(-1) * (H(m) + x * r) mod q
k_inv = modular_inverse(k, q)
s = (k_inv * (H_m + x * r)) % q

print("\nSigning:")
print(f"Message: {message}")
print(f"H(m) (hash of message): {H_m}")
print(f"r = {r}, s = {s}")

# Step 3: Verification
w = modular_inverse(s, q)  # w = s^(-1) mod q
u1 = (H_m * w) % q  # u1 = H(m) * w mod q
u2 = (r * w) % q  # u2 = r * w mod q

# Compute v = (g^u1 * y^u2 mod p) mod q
v = (pow(g, u1) * pow(y, u2)) % p % q

print("\nVerification:")
print(f"w = {w}, u1 = {u1}, u2 = {u2}")
print(f"v = {v}")

# Check if v == r
if v == r:
    print("The signature is valid!")
else:
    print("The signature is invalid.")