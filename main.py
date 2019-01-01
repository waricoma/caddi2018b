# -*- coding: utf-8 -*-
import sympy
import functools

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)

N, P = map(int, raw_input().split())

pfs = sympy.factorint(P)
print pfs

aaa = functools.reduce(gcd, [12, 15, 17, 20])
print aaa

print str(N) + " " + str(P)
