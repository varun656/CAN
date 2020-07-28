import tea

key = '0123456789abcdef'
message = 'Sample message for encryption and decryption.'
cipher = tea.encrypt(message, key)
print(cipher)