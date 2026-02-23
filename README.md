# CODECRAFT_CS_01

# 🔐 Caesar Cipher Encryption Tool

A Python-based implementation of the classical Caesar Cipher algorithm that allows users to encrypt and decrypt text using a shift value.

## 📌 Project Overview

This project demonstrates a basic substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

It supports:
- Encryption
- Decryption
- Case sensitivity (uppercase/lowercase preserved)
- Non-alphabet characters unchanged



## 🛠 Technologies Used

- Python 3
- Built-in functions (`ord()`, `chr()`)



## 🚀 How It Works

Encryption Formula:

C = (P + shift) mod 26

Decryption Formula:

P = (C - shift) mod 26
