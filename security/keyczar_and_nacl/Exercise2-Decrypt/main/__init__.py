"""

This exercise uses the result of the exercise 1 located at ./decrypted_text/texto_descifrado_ejercicio1.base64
to decrypt the cipher text at ./crypted_text/texto_cifrado_paso2_nacl.base64. Then, uses the keys located at
./pp_keys to encrypt the decrypted message using public / private key. Finally, writes the encrypted text in
base64 at ./crypted_text/texto_cifrado_ejercicio2.base64

Author: Urko Pineda

"""
import nacl.utils
import nacl.secret
from nacl.public import PrivateKey, PublicKey, Box
import os


def main():
    current_location = get_current_location()
    # READ TEXT
    key = read_file(current_location + '/decrypted_text/texto_descifrado_ejercicio1.base64')
    box = nacl.secret.SecretBox(key)
    text = read_file(current_location + '/crypted_text/texto_cifrado_paso2_nacl.base64')
    print 'Encrypted text is: "%s", length is: "%i"' % (text, len(text))
    decrypted_text = box.decrypt(text)
    print 'Decrypted text is: "%s"' % decrypted_text
    # GET KEYS
    my_public_key = PublicKey(read_file(current_location + '/pp_keys/pkAlumno.base64'))
    my_private_key = PrivateKey(read_file(current_location + '/pp_keys/skAlumno.base64'))
    iarenaza_public_key = PublicKey(read_file(current_location + '/pp_keys/pkTutor.base64'))
    # ENCRYPT
    box = Box(my_private_key, iarenaza_public_key)
    nonce = nacl.utils.random(Box.NONCE_SIZE)
    encrypted_text = box.encrypt(decrypted_text, nonce)
    print 'Encrypted text is: "%s", length is: "%i"' % (encrypted_text, len(encrypted_text))
    # WRITE FILE
    create_file(current_location + '/crypted_text/', 'texto_cifrado_ejercicio2.base64', encrypted_text.encode('base64'))


def get_current_location():
    return os.path.dirname(os.path.realpath(__file__))


def read_file(location):
    f = open(location, 'r')
    cipher_text = f.read()
    f.close()
    return cipher_text.decode('base64')


def create_file(location, name, content):
    f = open(location + name, 'w+')
    f.write(content)
    f.close()
    return f


if __name__ == '__main__':
    main()

