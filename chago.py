def tipoLista():
    x = list()
    print(type(x))
    print(dir(x))

def promedio():
    nums = [4,7,2,8,2,0,4,1,0]
    print('\n')
    print(f'Elemntos: {len(nums)}')
    print(f'Número maximo: {max(nums)}')
    print(f'Número minimo: {min(nums)}')
    print(f'Suma de los elementos: {sum(nums)}')
    print(f'Promedio: {sum(nums)/len(nums)}')

def cicloWhile():
    total = 0
    contador = 0
    while True:
        num = input("Ingrese un número: ")
        if num == 'done': 
            break

        value = float(num)
        total = total + value
        contador = contador + 1

    average = total / contador
    print(f'Average: {average}')

    numlist = list()
    while True:
        num = input("Ingrese un número: ")
        if num == 'done':
            break

        value = float(num)
        numlist.append(value)

    average = sum(numlist) / len(numlist)
    print(f'Average: {average}')

def listaOrdenada():
    print('\n')
    nums = [4,7,2,8,2,0,4,1,0]
    nums.sort()
    amigos = ['magaliel', 'alberto', 'david', 'kevin', 'charly', 'fernando', 'hector']
    amigos.sort()
    print(amigos)
    print(nums)
    amigos.reverse()
    nums.reverse()
    print(amigos)
    print(nums)

def agregarLista():
    print('\n')
    stuff = list()
    stuff.append('book')
    stuff.append(99)
    print(stuff)
    stuff.append('cookie')
    print(stuff)
    stuff.append('@')
    stuff.append(12)
    stuff.append(4)
    print(stuff)

def estaEnLaLista():
    print('\n')
    stuff = ['book', 'cookie', 99, 12, 4]
    print(12 in stuff)
    print('@' in stuff)
    print('books' in stuff)

def splitline():
    abc = 'Chago UAZ nos obliga a estudiar python e investigar'
    line = 'Los estudiantes de software son los mejores'
    stuff = abc.split()
    line = line.split()
    print(stuff)
    print(len(stuff))
    print(stuff[1])
    print(line)
    print(len(line))
    print(line[3])

    for w in stuff:
        print(w)
    for z in line:
        print(z)

    print('\n')
    line = 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
    words = line.split()
    print(words)
    email = words[1]
    print(email)
    piezas = email.split('@')
    print(piezas)
    print(piezas[1])