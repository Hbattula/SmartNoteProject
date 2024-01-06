from cryptography.fernet import Fernet

# Generate a key for encryption (for simplicity, in-memory key)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text
