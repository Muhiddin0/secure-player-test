from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_text(text, key):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    return decrypted_text

# Example usage
if __name__ == "__main__":
    # Generate a random key (do not hardcode keys in production)
    key = generate_key()

    print(key)

    # Text to be encrypted
    original_text = "This is a secret message."

    # Encrypt the text
    encrypted_text = encrypt_text(original_text, key)
    print("Encrypted Text:", encrypted_text)

    # Decrypt the text
    decrypted_text = decrypt_text(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)
