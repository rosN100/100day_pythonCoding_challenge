import caesar_cipher_logo
print(caesar_cipher_logo.logo)
# method 1
# input_msg = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
# message = input("Type your message\n")
# shift_number = int(input("Type the shift number\n"))
# def encode(message,shift_number):
#     encoded_result = ''
#     for letter in message:
#         num = ord(letter) + shift_number
#         encoded_result += chr(num)
#     print(f"Here is the encoded result: {encoded_result}")
#
# def decode(message,shift_number):
#     decoded_result = ''
#     for letter in message:
#         num = ord(letter) - shift_number
#
#         decoded_result += chr(num)
#     print(f"Here is the encoded result: {decoded_result}")
# if input_msg == 'encode':
#     encode(message,shift_number)
# elif input_msg == 'decode':
#     decode(message,shift_number)

#----------------------------------------
# method 2
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
#
# input_msg = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
# message = input("Type your message\n")
# shift_number = int(input("Type the shift number\n"))
#
# def encrypt(message,shift_number):
#     encoded_result = ""
#     for letter in message:
#         shifted_position = alphabet.index(letter) + shift_number
#         shifted_position %= len(alphabet)
#         encoded_result +=alphabet[shifted_position]
#     print(f"Here is the encoded result: {encoded_result}")
#
# def decrypt(message,shift_number):
#     decoded_result = ""
#     for letter in message:
#         shifted_position = alphabet.index(letter) - shift_number
#         shifted_position %= len(alphabet)
#         decoded_result +=alphabet[shifted_position]
#     print(f"Here is the encoded result: {decoded_result}")
# if input_msg == 'encode':
#      encrypt(message,shift_number)
# elif input_msg == 'decode':
#      decrypt(message,shift_number)

# into a single function - cypher - final code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']


def cypher(message,shift_number,direction):
    result = ""
    shifted_position = 0
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            if direction == 'encode':
                shifted_position = alphabet.index(letter) + shift_number
            elif direction == 'decode':
                shifted_position = alphabet.index(letter) - shift_number
            shifted_position %= len(alphabet)
            result +=alphabet[shifted_position]
    print(f"Here is the {direction}d result: {result}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    message = input("Type your message\n")
    shift_number = int(input("Type the shift number\n"))
    cypher(message,shift_number,direction)

    restart = input("Type 'yes' if you want to go again. otherwise say 'no'. \n ").lower()
    if restart == 'no':
        should_continue = False
        print("goodbye!")