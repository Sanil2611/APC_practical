text = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in text:
    if ch.isalpha():
        encrypted = encrypted + chr(ord(ch) + shift)
    else:
        encrypted = encrypted + ch

print("Encrypted:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isalpha():
        decrypted = decrypted + chr(ord(ch) - shift)
    else:
        decrypted = decrypted + ch

print("Decrypted:", decrypted)
