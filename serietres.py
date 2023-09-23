import argparse
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_rectangulo(base, altura):
    return base * altura

def main():
    parser = argparse.ArgumentParser(description='Calcula áreas de múltiples figuras')
    parser.add_argument('figuras', type=str, help='Especifique las figuras y sus datos separados por "|"')
    
    args = parser.parse_args()
    figuras_datos = args.figuras.split('|')
    
    for figura in figuras_datos:
        figura_info = figura.split()
        tipo = figura_info[0]
        datos = [float(d) for d in figura_info[1].split(',')]
        
        if tipo == 'circulo':
            area = calcular_area_circulo(datos[0])
            print(f'Área del círculo con radio {datos[0]}: {area:.2f}')
        elif tipo == 'triangulo':
            area = calcular_area_triangulo(datos[0], datos[1])
            print(f'Área del triángulo con base {datos[0]} y altura {datos[1]}: {area:.2f}')
        elif tipo == 'rectangulo':
            area = calcular_area_rectangulo(datos[0], datos[1])
            print(f'Área del rectángulo con base {datos[0]} y altura {datos[1]}: {area:.2f}')
        else:
            print(f'Tipo de figura no válido: {tipo}')

if __name__ == "__main__":
    main()
