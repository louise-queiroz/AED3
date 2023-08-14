import gmpy2
from Crypto.PublicKey import RSA

f = open("keypublic.txt", "r")
key = RSA.importKey(f.read())
print(key.n,"\n")
print(key.e)

e = 65537
p = 4988586550946572698837659323141005331783499412890195822279 
q = 4738700273445489960492041313631971343000359635005034483771
phi = 23639416453077017681888680330686094847437910791660054821871867983903494224484348871927719237876545168189380395428060

x = gmpy2.invert(e, phi)
print("d:",x)

dP = x % (p - 1)
print("dP:", dP)

dQ = x % (q - 1)
print("dQ:", dQ)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("O inverso multiplicativo não existe")
    else:
        return x % m

qINV = mod_inverse(q, p)
print("qINV:", qINV)
