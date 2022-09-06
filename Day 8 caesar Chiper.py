alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  enc = []
  enc2 = []
  if direction == "decode":
    shift *= -1
  for i in text:

    if i in alphabet:
      enc = alphabet.index(i)
      enc = enc + shift
      enc2.append(alphabet[enc])
    else:
      enc2.append(i)
  
  print(f"The {direction} text is {''.join(enc2)}")

import art
print(art.logo)

question = "yes"
while question == "yes":

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift >= 26:
    shift = shift % 26 
    caesar(text, shift, direction)
  else:
    caesar(text, shift, direction)
  question = input("Type 'yes' if you want to go again. otherwise type 'no'. \n")
  if question == "no":
    print("Good Bye")

