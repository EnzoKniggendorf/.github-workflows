from mymodule import calcular_area_quadrado, calcular_area_triangulo

def test_calcular_area_quadrado():
    assert calcular_area_quadrado(0, 0, 1, 0) == 1
    assert calcular_area_quadrado(0, 0, 2, 0) == 4

def test_calcular_area_triangulo():
    assert calcular_area_triangulo(0, 0, 0, 1, 1, 0) == 0.5
    assert calcular_area_triangulo(1, 1, 2, 2, 3, 3) == 0
