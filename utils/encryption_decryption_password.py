from cryptography.fernet import Fernet

def encrypt_password(password, key):
#     Encrypt the given password using the provided key.
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
#     Decrypt the encrypted password using the provided key.
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password
