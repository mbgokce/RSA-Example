import sys
import random
import math
from Crypto.Util import number
import string

def gcd(a, b):

    while a != 0:
        a, b = b%a, a
    return b


def modinv(a, m):

    if gcd(a, m) != 1:
    print "No modular inverse!"
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def factor(n):

    sn = int(math.sqrt(n))
    for x in range(2,(sn+1)):
        if n%x == 0:
            break
    y = n/x
    return x,y


alphabet = "0123456789abcdef"
msg = ''.join(random.choice(alphabet) for i in range(7))

p = number.getPrime(20,None)
q = number.getPrime(20,None)
n = p*q
phi = (p-1)*(q-1)

for i in range(3,50):
    if gcd(i,phi) == 1:
        e = i
        break

d = modinv(e, phi)
m = int(msg,16)
c = pow(m,e,n)

print "\nHere's what you need to figure out the encrypted message:\n"
print "e = " + str(e)
print "n = " + str(n)
print "ciphertext = " + str(c)

print "\nNow we'll find cleartext with integer factorization"

P,Q = factor(n)
PHI = (P-1)*(Q-1)
D = modinv(e, PHI)
Message = pow(c,D,n)
MSG = '{:02x}'.format(Message)
print "\nCleantext: " +str(MSG)

if MSG == msg:
    print "\nCongrats!"
else:
    print "\nSomething is wrong with code!"