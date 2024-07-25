# test_bot.py

import pytest
from your_bot_module import encrypt, decrypt

def test_encryption():
    password = "test_password"
    message = "This is a test message."
    encrypted_message = encrypt(message, password)
    assert encrypted_message != message

def test_decryption():
    password = "test_password"
    message = "This is a test message."
    encrypted_message = encrypt(message, password)
    decrypted_message = decrypt(encrypted_message, password)
    assert decrypted_message == message

def test_incorrect_decryption():
    password = "test_password"
    incorrect_password = "wrong_password"
    message = "This is a test message."
    encrypted_message = encrypt(message, password)
    with pytest.raises(Exception):
        decrypt(encrypted_message, incorrect_password)
