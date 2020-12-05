from datetime import date
import hashlib
import sys


def hash_string(s):
    m = hashlib.md5()
    m.update(s + b'vg' + b'slt')
    return m.hexdigest()


def hash_self():
    return hash_file(sys.argv[0])


def hash_file(file_name):
    m = hashlib.md5()
    with open(file_name, 'rb') as (fp):
        data = fp.read()
    m.update(data + b'vg' + b'slt')
    return m.hexdigest()


binary_name = sys.argv[1]

cert = ''
cert += '%s\n' % hash_self()
cert += '%s\n' % hash_file(binary_name)
this_file_hash = hash_string(cert.encode('utf-8'))
cert += '%s\n' % this_file_hash
