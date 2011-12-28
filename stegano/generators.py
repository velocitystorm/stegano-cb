#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Stéganô - Stéganô is a basic Python Steganography module.
# Copyright (C) 2010-2011  Cédric Bonhomme - http://cedricbonhomme.org/
#
# For more information : http://bitbucket.org/cedricbonhomme/stegano/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2011/12/28 $"
__license__ = "GPLv3"

import itertools

def fermat():
    """
    Generate the n-th Fermat Number.
    """
    n = 0
    while True:
        n += 1
        yield pow(2, pow(2, n)) + 1

def mersenne():
    """
    Generate 2^n-1.
    """
    n = 0
    while True:
        n += 1
        yield pow(2, n) - 1

def eratosthenes():
    """
    Generate the prime numbers with the sieve of Eratosthenes.
    """
    d = {}
    for i in itertools.count(2):
        if i in d:
            for j in d[i]:
                d[i + j] = d.get(i + j, []) + [j]
            del d[i]
        else:
            d[i * i] = [i]
            yield i

def eratosthenes_composite():
    """
    Generate the composite numbers with the sieve of Eratosthenes.
    """
    p1 = 3
    for p2 in eratosthenes():
        for n in range(p1 + 1, p2):
            yield n
        p1 = p2

def carmichael():
    for m in eratosthenes_composite():
        for a in range(2, m):
            if pow(a,m,m) != a:
                break
        else:
            yield m

def ackermann(m, n):
    """
    Ackermann number.
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

def fibonacci():
    """
    A generator for Fibonacci numbers, goes to next number in series on each call.
    This generator start at 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, ...
    See: http://oeis.org/A000045
    """
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def syracuse(l=15):
    n = 0
    while True:
        yield syracuse_gen(n, l)
        n += 1
        
def syracuse_gen(n, l=15):
    if n == 0:
        return l
    if n % 2 == 0:
        return syracuse_gen(n-1)/2
    elif n % 2 == 1:
        return 3*syracuse_gen(n-1)+1

        
if __name__ == "__main__":
    # Point of entry in execution mode.
    f = fibonacci()
    for x in range(13):
        print f.next(), # 0 1 1 2 3 5 8 13 21 34 55 89 144