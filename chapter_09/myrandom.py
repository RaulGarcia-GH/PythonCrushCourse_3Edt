# myrandom.py
import os
import struct

class MyRandom:
    def __init__(self, seed=None):
        if seed is None:
            # Use 4 bytes of OS randomness for nondeterministic seeding
            seed = struct.unpack("I", os.urandom(4))[0]
        self.state = seed & 0xffffffff

    def _lcg(self):
        a = 1664525
        c = 1013904223
        m = 2**32
        self.state = (a * self.state + c) % m
        return self.state

    def random(self):
        return self._lcg() / 2**32

    def randint(self, a, b):
        return a + int(self.random() * (b - a + 1))

    def choice(self, seq):
        if not seq:
            raise IndexError("Cannot choose from empty sequence")
        return seq[self.randint(0, len(seq) - 1)]

    def shuffle(self, seq):
        for i in range(len(seq) - 1, 0, -1):
            j = self.randint(0, i)
            seq[i], seq[j] = seq[j], seq[i]
        return seq


# Create a default RNG with unpredictable seed
_default = MyRandom()

def seed(x):
    _default.state = x & 0xffffffff

def random():
    return _default.random()

def randint(a, b):
    return _default.randint(a, b)

def choice(seq):
    return _default.choice(seq)

def shuffle(seq):
    return _default.shuffle(seq)
