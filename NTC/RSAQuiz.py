
"""
Implement RSA encryption with the given public key modulo, exponent

You have access to the function PowMod(a, n, modulo) which computes a^n mod modulo
using the fast modular exponentiation algorithm from the previous module. 
You also have access to the function ConvertToInt(message) which converts a text message to an integer.

return the integer ciphertext according to RSA encryption algorithm.
"""

def Encrypt(message, modulo, exponent):
  # modulo - n
  # exponent - e

  # the one want to recieve the message need to generate two keys:
  # public key to encrypt: E
  # private key to decrypt: D

  # to generate the keys:
  # 1. generate two big random primes p and q
  # 2. computes n = p * q
  # 3. generates random e coprime with (p - 1)(q - 1)
  # public key E is the pair (n, e)
  # private key D is the pair (p, q)

  # Encryption:
  # 1. convert message m to an integer (needs to be between 0 and n - 1)
  # 2. ciphertext c = m^e mod n - use fast modular exponentiation

  # Decryption:
  # compute d such that c^d ≡ m mod n

  m = ConvertToInt(message)
  c = PowMod(m, exponent, modulo)

  return c

"""
Implement RSA decryption with the given private key p, q, exponent

1. You have access to the function ConvertToStr(m) which converts from integer m to the plaintext message.
2. You also have access to the function InvertModulo(a, n) which takes coprime integers a and n as inputs 
and returns integer b such that ab ≡ 1 mod n. 
3. You also have access to the function PowMod(a, n, modulo) which computes a^n mod modulo 
using fast modular exponentiation.

You need to fix the implementation of the function Decrypt(ciphertext, p, q, exponent) 
to decrypt the message which was encrypted using the public key 
(n = p * q, e = exponent)
"""

def Decrypt(ciphertext, p, q, exponent):
  # Decryption:
  # compute d such that c^d ≡ m mod n
  # c^d ≡ (m^e)^d ≡ m^ed mod n (because c = m^e mod n)
  # we need m^ed ≡ m mod n
  # n = p * q so by Chinese Remainder Theorem it is equivalent to:
  # m^ed ≡ m mod p, m^ed ≡ m mod q (because p and q are coprime)

  # by Fermat's Little Theorem:
  # m^k ≡ m^(k mod (p - 1)) mod p, so this holds if (we need)
  # ed ≡ 1 mod (p - 1), ed ≡ 1 mod (q - 1), if:
  # ed ≡ 1 mod (p - 1)(q - 1)

  # e is coprime with (p - 1)(q - 1)
  # so we can use Extended Euclid's Algorithm to compute such d so that 
  # ed ≡ 1 mod (p - 1)(q - 1)

  # Steps:
  # 1. compute (p - 1)(q - 1)
  # 2. compute d such that ed ≡ 1 mod (p - 1)(q - 1) using Extended Euclid's Algorithm
  # 3. to decrypt ciphertext c, compute c^d mod n using fast modular exponentiation

  d = InvertModulo(exponent, (p - 1) * (q - 1))

  return ConvertToStr(PowMod(ciphertext, d, p * q))

"""
take the ciphertext sent from Alice to the center, 
the public key modulo, exponent and the set of potential messages that Alice could have sent, 
and return the message that Alice encrypted and sent as a string

modular, exponent = public key pair (n, e)
"""

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
  for m in potential_messages:
    if ciphertext == Encrypt(m, modulo, exponent):
      return m
  return "don't know"

"""
Alice is using RSA encryption with a public key modulo, exponent such that 
modulo=p⋅q with one of the primes p and q being less than 1,000,000, 
and you know about it. You want to break the cipher and decrypt her message.

Available function to use: Decrypt(ciphertext,p,q,e)

decipher the ciphertext in case when one of the prime factors of the public modulo is smaller than 1000000.
modular, exponent = public key pair (n, e)
"""

# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/46635266#46635266
from itertools import compress
def rwh_primes1v2(n):
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]


def DecipherSmallPrime(ciphertext, modulo, exponent):
  # try all prime up to 1,000,000 as divisor of the public key n
  # factorize n and decrypt the cipher
  if modulo % 2 == 0:
    small_prime = 2
    big_prime = modulo // 2
    return Decrypt(ciphertext, small_prime, big_prime, exponent)
  
  # for i in range(3, 1000000, 2):
  #   if is_prime(i):
  #     if modulo % i == 0:
  #       small_prime = i
  #       big_prime = modulo // i
  #       return Decrypt(ciphertext, small_prime, big_prime, exponent)

  for i in rwh_primes1v2(1000000):
    if modulo % i == 0:
      small_prime = i
      big_prime = modulo // i
      return Decrypt(ciphertext, small_prime, big_prime, exponent)

  return "don't know"

"""
Alice is using RSA encryption with a public key modulo, exponent such that modulo=p⋅q with ∣p−q∣<5000, 
and you know about it. You want to break the cipher and decrypt her message.

Available function to use: 
Decrypt(ciphertext,p,q,e)
IntSqrt(n): takes integer n and returns the largest integer x such that x^2 ≤ n.

Algorithm:
r = q - p < 5000
p < q 
p < √n < q
√n - p < q - p = r
√n - r < p < √n

Try all integers between √n - r and √n as divisors of n 
modular, exponent = public key pair (n, e)
"""
def DecipherSmallDiff(ciphertext, modulo, exponent):
  bottom_bond = IntSqrt(modulo) - 5000
  upper_bond = IntSqrt(modulo)

  for i in range(bottom_bond, upper_bond+1):
    if modulo % i == 0:
      small_prime = i
      big_prime = modulo // i
      return Decrypt(ciphertext, small_prime, big_prime, exponent)
  return "don't know"

"""
You've discovered that the first prime number pp for the private key was generated with the same algorithm 
and the same random seed by two different senders Alice and Angelina due to insufficient randomness, 
while the second prime q is different for those two private keys. 
You want to break both ciphers and decipher messages from both Alice and Angelina.

Available function to use: 
Decrypt(ciphertext,p,q,e)
DecipherCommonDivisor(first_ciphertext,first_modulo,first_exponent,second_ciphertext,second_modulo,second_exponent).

You need to fix its implementation so that it can decipher both first_ciphertext and second_ciphertext 
in case when first_modulo and second_modulo share a prime factor.

Algorithm:
If the public key n1 and n2 are generated using the same p, but different q,
the GCD(n1, n2) = p
"""

def GCD(a, b):
  if b == 0:
    return a
  return GCD(b, a % b)
  
def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent):
  # Fix this implementation to correctly decipher both messages in case
  # first_modulo and second_modulo share a prime factor, and return
  # a pair (first_message, second_message). The implementation below won't work
  # if the common_prime is bigger than 1000000.
  common_prime = GCD(first_modulo, second_modulo)
  
  q1 = first_modulo // common_prime
  q2 = second_modulo // common_prime
  return (Decrypt(first_ciphertext, common_prime, q1, first_exponent), Decrypt(second_ciphertext, common_prime, q2, second_exponent))

"""
Bob has sent the same messagemessage to Alice and Angelina using two different public keys 
(n1, e=2) and (n2, e=2) with the same exponent e=2. 
Implement Hastad's broadcast attack from the lectures for this case to decipher the message 
using the intercepted ciphertexts first_ciphertext and second_ciphertext.

Available function to use: 
ConvertToStr(m) which converts an integer to a plaintext messagemessage. 
ChineseRemainderTheorem(n1, r1, n2, r2)
IntSqrt(n): takes integer n and returns the largest integer x such that x^2 ≤ n.

Algorithm:
Say if there are 3 persons, and e = 3
Assume GCD(Ni, Nj) = 1
Use Chinese Remainder Theorem to construct c such that 0 <= c < N1N2N3.. and 
c ≡ c1 mod N1, c ≡ c2 mod N2, c ≡ c3 mod N3
c ≡ m^3 mod N1N2N3
0 <= c, m^3 < N1N2N3
c = m^3
decode m by 3√c
"""
def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
  # Fix this implementation
  r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
  # r = m^2 because e = 2
  m = IntSqrt(r)
  return ConvertToStr(m)
