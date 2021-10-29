import random

rango_max = input('Ingresa el rango máximo del número: ')

if rango_max.isdigit():
    rango_max = int(rango_max)

    if rango_max <= 0:
        print('Por favor escribe un número mayor a 0 la próxima vez...')
        quit()
else:
    print('Por favor digite un número la próxima vez...')
    quit()


r_number = random.randint(0,rango_max)

intentos = 0
while True:
    intentos += 1
    num_usuario = input('Adivina el número: ')

    if num_usuario.isdigit():
        num_usuario = int(num_usuario)
    else:
        print('Por favor digite un número la próxima vez...')
        continue

    if num_usuario == r_number:
        print('¡Felicitaciones, adivinaste !')
        break
    else:
        if num_usuario > r_number:
            print('El número que escogiste es mayor al número secreto')
        else:
            print('El número que escogiste es menor al número secreto')

print('Lograste adivinar el número en ', intentos, 'intentos')