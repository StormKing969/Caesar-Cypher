lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(clear_text):
	cyphertext = " "
	for char in clear_text:
		if char in lowercase_alphabet:
			new_position1 = (lowercase_alphabet.find(char) + 13) % 26
			cyphertext += lowercase_alphabet[new_position1]
		elif char in uppercase_alphabet:
			new_position2 = (uppercase_alphabet.find(char) + 13) % 26
			cyphertext += uppercase_alphabet[new_position2]
		else:
			cyphertext += char
	return cyphertext

def decrypt(text):
	message = " "
	for char in text:
		if char in lowercase_alphabet:
			new_position1 = (lowercase_alphabet.find(char) - 13) 
			message += lowercase_alphabet[new_position1]
		elif char in uppercase_alphabet:
			new_position2 = (uppercase_alphabet.find(char) - 13)
			message += uppercase_alphabet[new_position2]
		else:
			message += char
	return message

while True:
	wish = input("Do you want to Encrypt, Decrypt or Quit: ")
	wish = wish.lower()
	while wish == "encrypt":
		clear_text = input("Clear Message: ")
		print("Secret Message: ", encrypt(clear_text))
		print()
		desire1 = input("Press y to keep encrypting, n to exit encryption: ")
		if desire1 == "n":
			break
	while wish == "decrypt":
		text = input("Secret Message: ")
		print("Clear Message: ", decrypt(text))
		print()
		desire2 = input("Press y to keep decrypting, n to exit decryption: ")
		if desire2 == "n":
			break
	if wish == "quit":
		break

