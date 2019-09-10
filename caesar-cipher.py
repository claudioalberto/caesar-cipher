import sys

ALPHABET = 'abcdefghijklmnopqrstuvxywz'
KEY = 13

def cipher(message, dir):
  message_temp = ''
  for m in message:
    if m in ALPHABET:
      c_index = ALPHABET.index(m)
      message_temp += ALPHABET[(c_index + (dir * KEY)) % len(ALPHABET)]
    else:
      message_temp += m
  return message_temp


def encrypt(message):
  return cipher(message, 1)

def decrypt(message):
  return cipher(message, -1)

def main():
  command = sys.argv[1].lower()
  message = sys.argv[2].lower()
  if command == 'encrypt':
    print(encrypt(message))
  elif command == 'decrypt':
    print(decrypt(message))
  else:
    print(command + ' -> ERROR: Command not found')

if __name__ == '__main__':
  main()