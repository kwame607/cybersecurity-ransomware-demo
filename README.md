# cybersecurity-ransomware-demo

## Overview

This project is a **controlled ransomware simulation** built with Python to demonstrate how file-encryption attacks operate. It was created strictly for **educational and cybersecurity research purposes**.

The goal of this project is to help students and security enthusiasts understand:

* How symmetric encryption works
* How ransomware targets files
* The importance of backups and key management
* Defensive strategies against malware

---

## Features

* File encryption and decryption using **Fernet symmetric encryption**
* Operates only inside a **safe test folder** (`test_folder`)
* Secure storage of encryption key (`secret.key`)
* Recovery simulation using a **recovery password**
* Clear terminal messages for educational purposes

---

## Technologies Used

* Python 3
* `cryptography` library (Fernet)
* File handling and OS operations

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ransomware-simulator.git
cd ransomware-simulator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Encryption (Simulated Ransomware)

```bash
python crazy.py
```

* Encrypts files inside the `test_folder`
* Generates `secret.key` for decryption

### Decryption (Recovery Simulation)

```bash
python xena.py
```

* Prompts for the **recovery password**
* Decrypts files inside `test_folder` using `secret.key`

⚠ **Important:** Always run inside `test_folder`. Do **not** run on important files or your system directories.

---

## Educational Purpose & Disclaimer

This project is strictly for:

* Cybersecurity education
* Security research
* Ethical hacking practice
* Awareness demonstrations

The author is **not responsible** for misuse or damage caused by improper use of this code.

---

## Learning Outcomes

By working with this project, you can learn:

* Practical application of encryption in cybersecurity
* How ransomware attacks function at a technical level
* The importance of defensive security strategies

---

## Author

Kwame Emmanuel Adom (CRAZY)


```
python Crazy.py
```
