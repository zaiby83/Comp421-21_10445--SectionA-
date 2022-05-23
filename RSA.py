## First we import our modules: random and sympy.

import random
import sympy

## e define our function gcd() which will take two integers: a and b.
## Recall that the GCD in Math is short for Greatest Common Divisor and is
## also called the Highest Common Factor or HCF. This is the largest positive integer that would
## divide both numbers without leaving a fraction.
## This function simply takes two integers a and b and returns the GCD.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a   


## The multplicative_inverse() function is used to calculate the Multiplicative
## Inverse which is part of our private key.

## The Multiplicative Inverse is defined as a number which when multiplied by the
## original number gives the product as 1.

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y
        
    if temp_phi == 1:
        return d + phi

## The generate_keypair() function does just that: generate our public and private keys.
## It is the core component of the RSA algorithm.

def generate_keypair(p, q):
    n = p*q
    phi = ((p-1)*(q-1))

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi) 

    return ((e, n), (d, n))

## The encrypt() function will accept the tuple pk (which is our public key) and the plaintext to be encrypted.
## Recall that the public key was generated in generate_keypair() and contains both integer e (used also as the key) and
## integer n (the modulus).


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


## The decrypt() function will accept the tuple pk
## (which is our private key) and the encrypted ciphertext.

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)





## We will generate our two random primes p and q, both between 1 and 100, at runtime.
## These values will passed to generate_keypair() and will generate and return our public and private key,
## as previously described.


p = sympy.randprime(1, 100)
q = sympy.randprime(1, 100)

public, private = generate_keypair(p, q)

message = input("Type message: ")

encrypted_msg = encrypt(public, message)

print(f"{encrypted_msg}")

print (f"Decrypted Message is : {decrypt(private,encrypted_msg)}")

