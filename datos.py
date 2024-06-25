text = 'Pedro Chic'
shift =3
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index =alfabeto.find(char)
    print(char, index)
    nuevo_index =index+shift
    nuevo_char =alfabeto[nuevo_index]
    print(nuevo_char)