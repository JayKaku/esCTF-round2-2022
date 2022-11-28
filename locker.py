# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: hash.py
# Compiled at: 2022-11-14 12:37:46
# Size of source mod 2**32: 1050 bytes
import sys


def substitution(char):
	switch = {
		"a": 1,
		"b": 2,
		"c": 3,
		"d": 4,
		"e": 5,
		"f": 6,
		"g": 7,
		"h": 8,
		"i": 9,
		"j": 10,
		"k": 11,
		"l": 12,
		"m": 13,
		"n": 14,
		"o": 15,
		"p": 16,
		"q": 17,
		"r": 18,
		"s": 19,
		"t": 20,
		"u": 21,
		"v": 22,
		"w": 23,
		"x": 24,
		"y": 25,
		"z": 26,
		"{": 27,
		"}": 28,
		"_": 29,
		"!": 30,
	}
	return switch.get(char, 0)


def hash_(passw):
	hash = 1
	for i in range(len(passw)):
		hash += hash * 9 + 2 ** substitution(passw[i]) % 31

	return hash


print("Enter the passcode :")
password = input()
passcode = "alohamora!"
if password == "alohamora!":
	print("Spells are not allowed.")
else:
	if hash_(password) == hash_(passcode):
		print("Welcome to Hogwards, the flag is esCTF{dummy_flag}")
	else:
		print("UnAuthorized")
# okay decompiling binary.pyc