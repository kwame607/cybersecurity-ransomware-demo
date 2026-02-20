# cybersecurity-ransomware-demo
Python-based ransomware simulator created for cybersecurity learning and defensive research purposes.
# Ransomware Simulation (Educational Project)

## Overview

This project is a controlled ransomware simulation built with Python to demonstrate how file encryption-based attacks operate. It was created strictly for cybersecurity education, awareness, and defensive research purposes.

The goal of this project is to help students and security enthusiasts understand:

* How symmetric encryption works
* How ransomware targets files
* The importance of backups and key management
* Why endpoint protection and monitoring matter

---

## Features

* File encryption using Fernet (symmetric cryptography)
* Controlled target directory (test folder only)
* Key generation and secure storage
* Decryption functionality for recovery
* Clear simulation output messages

---

## Technologies Used

* Python 3
* `cryptography` library (Fernet)
* File handling & OS operations

---

## How It Works

1. The program scans a designated test folder.
2. Files are encrypted using a generated symmetric key.
3. The key is saved locally for demonstration purposes.
4. A decryption mode restores the files using the saved key.

This mimics the workflow of real ransomware in a safe and controlled lab environment.

---

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

Run the encryption simulation:

```
python Crazy.py
```
