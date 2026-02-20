#!/usr/bin/python3

"""
Ransomware Simulation - Decryption Script
Educational use only.
Decrypts files inside the test_folder directory using the saved key.
"""

import os
from cryptography.fernet import Fernet

TARGET_FOLDER = "test_folder"
KEY_FILE = "secret.key"
RECOVERY_PASSWORD = "demo"   

def load_key():
    if not os.path.exists(KEY_FILE):
        print("[Error] Encryption key not found.")
        return None
    
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def get_files(folder):
    files = []
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files

def decrypt_files(files, key):
    fernet = Fernet(key)

    for file in files:
        with open(file, "rb") as f:
            data = f.read()

        try:
            decrypted_data = fernet.decrypt(data)
        except:
            print(f"[Skipped] {file} (already decrypted or invalid)")
            continue

        with open(file, "wb") as f:
            f.write(decrypted_data)

        print(f"[Decrypted] {file}")

def main():
    print("\n[Simulation] File Recovery Mode")

    # Check target folder
    if not os.path.exists(TARGET_FOLDER):
        print("[Error] test_folder not found.")
        return

    # Password simulation
    user_input = input("Enter recovery password: ")

    if user_input != RECOVERY_PASSWORD:
        print("[Access Denied] Incorrect recovery password.")
        return

    key = load_key()
    if key is None:
        return

    files = get_files(TARGET_FOLDER)

    if not files:
        print("[Info] No files found in test_folder.")
        return

    decrypt_files(files, key)

    print("\n[Simulation Complete] Files successfully decrypted.")

if __name__ == "__main__":
    main()