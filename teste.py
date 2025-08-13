import random
from random import randint

def sorteio(lista_pos):
    
    lista_aux = []
    lista_aux_colec = []
    
    n_obstaculos = random.choices([1, 2], weights = [0.7, 0.3])
    
    # FOR para gerar as posições dos obstáculos
    for i in range(n_obstaculos):
        
        y = random.choice(lista_pos)
        
        lista_aux.append(y)
        
        #README cuidado para não alterar a lista de fora
        lista_pos.remove(y)
    
    status_colec = random.choices([True, False], weights = [0.3, 0.7]) 
    
    if status_colec:
        y = random.choice(lista_pos)

        tipo = random.choices(["saduiche","suco","passagem"], weights = [0.4, 0.3, 0.2])

        lista_aux_colec.append(y)

        lista_pos.remove(y)

        resultado = f'obstáculos: {lista_aux}\n coletável: tipo {tipo} e posição {lista_aux_colec} \n restante {lista_pos}'
    
    else:
        
        resultado = f'obstáculos: {lista_aux}\n não tem coletável \n restante {lista_pos}'
    
    return resultado

letra = input()
while letra != "exit":
    lista_pos = [1, 2, 3]

    print(sorteio(lista_pos))
    letra = input()