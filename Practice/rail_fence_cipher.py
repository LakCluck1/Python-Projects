import math

def encrypt():
  a = input("\n Write senctence to encrypt: ")
  txt = "".join([i.upper() for i in a.split(" ")])
  
  r1 = [txt[i] for i in range(0,len(txt),2)]
  r2 = [txt[i] for i in range(1,len(txt),2)]
  rails = r1 + r2

  c = [''.join(rails[i:i+5]) for i in range(0, len(rails), 5)]

  return ("\nEncrypted message: \u001b[32m" + " ".join(c)+"\n\u001b[0m")

def decrypt():
  a = input("\nWrite senctence to decrypt: ")
  b = "".join(a.split(" "))
  row_1_len = math.ceil(len(b)/2)
  r1 = (b[:row_1_len])
  r2 = (b[row_1_len:])
    
  plaintext = ""
  for i in range(len(r1)):
    try:
      plaintext += r1[i] + r2[i]
    except:
      plaintext += r1[i]

  return ("\nDecrypted message: \u001b[32m" + plaintext + "\n\u001b[0m")

print("Welcome to the Rail Fence Cipher!\n")
print("Would you like to encrypt or decrypt a message today?\n")
while True:
    while True:
      choice = input("Press e for encrypt or d for decrypt (0 to exit): ").lower()
      if choice == 'e':
        print(encrypt())
      elif choice == 'd': 
        print(decrypt())
      elif choice == '0':
        print("\nBye! Have a great day.")
        break
    break
    