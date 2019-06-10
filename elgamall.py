import random
import sympy  # generation of primitive numbers
import hashlib
import numpy as np


in_file = open("tt.txt", "rb")
Data = in_file.read()  # e.g. data[0] - first symbol etc..
hashik = sum(Data)
in_file.close()
hashsh = hashlib.sha1(Data).hexdigest()
print(hashlib.sha1(Data).hexdigest())  # 690de2b90c534314d893070bb7bc3aeae95d09e0

if hashik < 256:
	n = 256
else:
	n = hashik
b = hashik+1000
#P = sympy.randprime(49, 88)  # algorithm below doesnt work for numbers above 88
P = sympy.randprime(400, 700)

x = random.randint(1, P)  # private-key x

Phi = P-1  # eiler function for prime numbers


def factorizing(phi):
	pi = []  # list of prime numbers
	d = 2
	while d * d <= phi:
		if phi % d == 0:
			pi.append(d)
			phi //= d
		else:
			d += 1
	if phi >= 1:
		pi.append(phi)
	return pi


def primit_root(p):  # calculation of primitive root
	Pi = factorizing(Phi)
	for g in range(2, p + 1):
		for k in range(0, len(Pi)):
			q = int(Phi / Pi[k])
			gg = g ** q % p
			if gg == 1:
				break
		if gg != 1:
			result = g
			break
	return result


def crypt_elgamal(data, p, g):
	#x = random.randint(1, p)  # private-key x
	#g = primit_root(p)
	y = g ** x % p  # public-key y
	k = random.randint(1, p)
	#b = [2]
	#b = list(data)
	a = list(data)
	b = np.zeros(len(data), dtype=int)
	for i in range(0, len(a)):
		a[i] = g**k % p
		b[i] = (y**k * data[i]) % p
	return a, b


def decrypt_elgamal(p, a, b):
	r = list(a)
	for i in range(0, len(a)):
		r[i] = (b[i] * a[i] ** (p - 1 - x)) % p
	j = bytes(r)
	return j


def pow_to_low(x,y,z):
	flag = True  # where x-primitive root, y - pow, z - mod
	massiv = []
	for i in range(1, z):
		massiv.append(x ** i % z)
		for j in range(0, len(massiv)):
			if i - 1 != j:
				if massiv[i - 1] == massiv[j]:
					flag = False
					break
		if flag:
			pass
		else:
			del massiv[-1]
			break
	kakoi_po_schetu_v_massive = y % len(massiv)
	fgldkgld = y-len(massiv)
	gnmdfgdf = fgldkgld % len(massiv)
	result = massiv[kakoi_po_schetu_v_massive - 1]
	return kakoi_po_schetu_v_massive


G = primit_root(P)
print(100)
n, o = crypt_elgamal(Data, P, G)
print(102)
h = decrypt_elgamal(P, n, o)
print(104)

f = open('decrypted.jpg', 'wb')
f.write(h)
f.close()





#signature
#hashsh_int = int(hashsh, 16)  # hash
k = random.randint(1, P-1)
r = G**k % P
for o in range(1, P-1):  # multiplicative inverse
	if k*o % P == 1:
		MuIn = o

for s_promej in range(1, P-1):
	if hashik == (x*r + k*s_promej) % (P-1):
		s = s_promej


#r and s all together - signature

#checking signature
l = True
Y = G ** x % P
if 0 < r < P and 0 < s < P-1:
	pass
else:
	l = False
if l:
	pass

if l:
	#test = (Y**r)*(r**s)
	test = Y**pow_to_low(Y, r, P)
	if (Y**pow_to_low(Y, r, P))*(r**pow_to_low(r, s, P)) % P == G**pow_to_low(G, hashik, P) % P:
		l = True
	else:
		l = False
if l:
	print('ALL GOOD!')
else:
	print('WRONG!')

test = (Y**r)*(r**s)



