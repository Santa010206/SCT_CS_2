from PIL import Image
import numpy as np
import os

def encrypt_image(image_path):
    # Load image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Generate random key with same shape as image
    key = np.random.randint(0, 256, size=img_array.shape, dtype=np.uint8)

    # Encrypt using XOR
    encrypted_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_array)

    # Save encrypted image and key
    encrypted_img.save("encrypted_image.png")
    np.save("key.npy", key)

    print("Image encrypted successfully. Encrypted image saved as 'encrypted_image.png'")
    print("Encryption key saved as 'key.npy'")


def decrypt_image(encrypted_image_path, key_path="key.npy"):
    # Load encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_img)

    # Load saved key
    if not os.path.exists(key_path):
        print("Key file not found!")
        return
    key = np.load(key_path)

    # Ensure shape matches
    if key.shape != encrypted_array.shape:
        print("Key shape does not match image shape.")
        return

    # Decrypt using XOR
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    decrypted_img = Image.fromarray(decrypted_array)

    # Save decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully. Decrypted image saved as 'decrypted_image.png'")


def main():
    print("Image Encryption & Decryption")

    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice == 'e':
        image_path = input("Enter the path of the image to encrypt: ")
        encrypt_image(image_path)

    elif choice == 'd':
        encrypted_path = input("Enter the path of the encrypted image: ")
        decrypt_image(encrypted_path)

    else:
        print("Invalid choice. Use 'e' for encrypt or 'd' for decrypt.")


if __name__ == "__main__":
    main()
