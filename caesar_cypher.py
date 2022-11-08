alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result=[]
continue_game=True

def caesar(text, shift, direction):
    if direction=='decode':
        shift=shift*(-1)
    for x in range(0, len(text)):
        if text[x] in alphabet:
            temp=alphabet.index(text[x])
            new_index=(temp+shift)%26
            result.append(alphabet[new_index])
    print(' '.join(result))
   

while continue_game:
    options=input('Press "start" to begin.\nPress "quit" to exit\n').lower()
    if options=='start':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        result=[]
    elif options=='quit':
        continue_game=False
    else:
        print('Please enter a valid option')
