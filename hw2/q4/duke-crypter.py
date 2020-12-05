#!/usr/bin/python3
"""
Syntax:
  To encrypt:  ./duke-crypter -e <input_file> <output_file>
  To decrypt:  ./duke-crypter -d <input_file> <output_file>
 
prompt for the secret key, echo the typed keys as normal

it may write to stderr or stdout

successful 
return 0

fail 
provided secret key is not correct
cipher text is determined to have been tampered with
any other error occurs  (file not found, etc.)

ciphertext file include some form of signature of the plaintext, such as SHA-2 or SHA-3
use an encryption algorithm that includes built-in integrity verification.

self grading
python3 cryptotest.pyc <your_encryption_program>
"""

from sys import argv, exit

from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256


def fail():
    print("Syntax: \nTo encrypt:  ./duke-crypter.py -e < input_file > <output_file > \nTo decrypt:  ./duke-crypter.py -d < input_file > <output_file > ")
    exit(2)


if len(argv) != 4:
    fail()
elif argv[1] != '-e' and argv[1] != '-d':
    fail()


in_file = argv[2]
ou_file = argv[3]

tmp = input()
h_obj = SHA3_256.new()
h_obj.update(tmp.encode("utf8"))
key = h_obj.digest()


if argv[1] == '-e':
    try:
        with open(in_file) as i:
            data = i.read()
        cipher = AES.new(key, AES.MODE_EAX)

        ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf8"))
        file_out = open(ou_file, "w+b")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
        file_out.close()

        exit(0)
    except Exception as e:
        print('Failed: ' + str(e))

        exit(2)

if argv[1] == '-d':
    try:
        file_in = open(in_file, "rb")
        nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
        cipher = AES.new(key, AES.MODE_EAX, nonce)

        data = cipher.decrypt_and_verify(ciphertext, tag)
        with open(ou_file, "wb+") as f:
            f.write(data)

        exit(0)
    except Exception as e:
        print('Failed ' + str(e))
        exit(2)
