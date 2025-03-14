def calcular_area_quadrado(x1, y1, x2, y2):
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    area = distancia**2
    return area

def calcular_area_triangulo(x1, y1, x2, y2, x3, y3):
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    return area
