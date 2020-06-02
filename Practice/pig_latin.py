import re 

def wordtopig(w):
    if w[0].lower() in 'aieou':
        return w + 'way'
    else:
        if w == w.capitalize():
          return (w[1:len(w)] +'ay').capitalize()
        else: 
          return (w[1:len(w)] +'ay')


def texttopig(t):
  for i in set(re.findall(r'\w+', t)):
    t = t.replace(i,wordtopig(i))
  return t


while True:
  a = input("Write your text to convert to Pig Latin!\n\n")
  if len(a) == 0:
    a = input("Please try again!")
  print("______\n")
  print(texttopig(a))
  if input("\nPress Enter to try again, or 0 to quit.\n") == '0':
    print("Thank you for playing!")
    break