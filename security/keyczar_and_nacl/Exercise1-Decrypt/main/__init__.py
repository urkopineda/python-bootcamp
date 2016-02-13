"""

This exercise decrypts the content located at /crypted_text/texto_cifrado_paso2_keyczar.base64 using a symmetric key
located at ./primary_key. Then, writes the result at ./decrypted_text/texto_descifrado_ejercicio1.base64 in base64
encoding.

Author: Urko Pineda

"""
from keyczar import keyczar
import os
import binascii


def main():
    current_location = get_current_location()
    ### READ ###
    binary_text = decrypt_text(current_location + '/primary_key/', current_location +
                                                                   '/crypted_text/texto_cifrado_paso2_keyczar.base64')
    ascii_text = binascii.b2a_base64(binary_text)
    print 'Decrypted text (Binary): %s' % binary_text
    print 'Decrypted text (ASCII): %s' % ascii_text
    ### WRITE ###
    encoded_text = binary_text.encode('base64')
    create_file(current_location + '/decrypted_text/', 'texto_descifrado_ejercicio1.base64', encoded_text)


def get_current_location():
    return os.path.dirname(os.path.realpath(__file__))


def decrypt_text(pk_location, cipher_location):
    crypter = keyczar.Crypter.Read(pk_location)
    return crypter.Decrypt(read_file(cipher_location))


def read_file(location):
    f = open(location, 'r')
    cipher_text = f.read()
    f.close()
    return cipher_text


def create_file(location, name, content):
    f = open(location + name, 'w+')
    f.write(content)
    f.close()
    return f


if __name__ == '__main__':
    main()

