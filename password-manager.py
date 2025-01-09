import streamlit as st
import hashlib
import json
import os
from cryptography.fernet import Fernet

# File to store passwords
data_file = "passwords.json"
key_file = "key.key"

# Generate or load encryption key
def load_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
    else:
        with open(key_file, "rb") as file:
            key = file.read()
    return key

def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt_message(message, key):
    f = Fernet(key)
    return f.decrypt(message.encode()).decode()

# Load or initialize password storage
def load_passwords():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {}

def save_passwords(data):
    with open(data_file, "w") as file:
        json.dump(data, file)

# Hash the master password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Streamlit App
def main():
    st.title("🔒 Password Manager")

    key = load_key()
    passwords = load_passwords()

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.subheader("Enter Master Password")
        master_password_input = st.text_input("Master Password", type="password")

        # Load or set master password
        if os.path.exists("master_password.txt"):
            with open("master_password.txt", "r") as file:
                saved_master_password = file.read()
        else:
            if master_password_input:
                saved_master_password = hash_password(master_password_input)
                with open("master_password.txt", "w") as file:
                    file.write(saved_master_password)
                st.success("Master password set! Restart the app.")
                st.stop()
            else:
                st.warning("Please set a master password to continue.")
                st.stop()

        if master_password_input and hash_password(master_password_input) == saved_master_password:
            st.session_state["authenticated"] = True
            st.success("Authenticated successfully!")
        elif master_password_input:
            st.error("Invalid master password")
            st.stop()
        else:
            st.stop()

    st.subheader("Manage Your Passwords")

    # Add a new password
    with st.form("add_password"):
        service = st.text_input("Service Name")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Add Password")

        if submitted:
            if service and password:
                encrypted_password = encrypt_message(password, key)
                passwords[service] = encrypted_password
                save_passwords(passwords)
                st.success(f"Password for {service} added successfully!")
            else:
                st.error("Service name and password cannot be empty.")

    # Retrieve a password
    st.subheader("Retrieve a Password")
    service_to_retrieve = st.text_input("Enter Service Name to Retrieve")

    if st.button("Retrieve"):
        if service_to_retrieve in passwords:
            decrypted_password = decrypt_message(passwords[service_to_retrieve], key)
            st.write(f"Password for {service_to_retrieve}: `{decrypted_password}`")
        else:
            st.error("No password found for this service.")

if __name__ == "__main__":
    main()
