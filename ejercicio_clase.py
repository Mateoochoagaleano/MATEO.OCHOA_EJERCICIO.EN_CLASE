import os


class Lote:
    os.system('cls')
    def _init_(self, frente, fondo, tipo):
        self.frente = frente
        self.fondo = fondo
        self.m2 = frente * fondo
        self.tipo = tipo

    def calcular_valor(self):
        os.system('cls')
        if self.tipo == 1:
            valor_m2 = 25000
            permiso_construccion = 0.45
        elif self.tipo == 2:
            valor_m2 = 60000
            permiso_construccion = 0.75
        elif self.tipo == 3:
            valor_m2 = 35000
            permiso_construccion = 0.15
        else:
            return 'Tipo de lote no válido'

        valor_total = self.m2 * valor_m2
        valor_permiso = valor_total * permiso_construccion
        return valor_total, valor_permiso

lotes = []

def fnt_agregar():
    os.system('cls')
    frente = float(input('Ingrese la medida del frente del lote en metros: '))
    fondo = float(input('Ingrese la medida del fondo del lote en metros: '))
    tipo = int(input('Ingrese el tipo de lote (1 - Urbano, 2 - Comercial, 3 - Campestre): '))
    lote = Lote(frente, fondo, tipo)
    lotes.append(lote)
    print('lote agregado.')

def fnt_mostrar(tipo):
    os.system('cls')
    if tipo == 'a':
        print('Lotes Urbanos:')
    elif tipo == 'b':
        print('Lotes Comerciales:')
    elif tipo == 'c':
        print('Lotes Campestres:')
    else:
        print('Tipo de lote no válido')
        return

    for index, lote in enumerate(lotes):
        os.system('cls')
        if lote.tipo == int(tipo):
            print(f'Lote {index + 1}:')
            print(f'Medidas: {lote.frente}m * {lote.fondo}m')
            print(f'Área: {lote.m2}m²')
            valor_total, valor_permiso = lote.calcular_valor()
            print(f'Valor total del lote: ${valor_total}')
            print(f'Valor del permiso de construcción: ${valor_permiso}')
            print()

while True:
    os.system('cls')
    print('   Menú   ')
    print('1. Agregar un nuevo lote')
    print('2. Mostrar lotes')
    print('3. Salir')
    opcion = input('que quieres hacer bro: ')

    if opcion == '1':
        fnt_agregar()
    elif opcion == '2':
        tipo_lote = input("Seleccione el tipo de lote (a - Urbano, b - Comercial, c - Campestre): ")
        fnt_mostrar(tipo_lote)
    elif opcion == '3':
        break
    else:
        print('ERROR...')
