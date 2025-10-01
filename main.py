from lib import cuadrado, rectangulo, triangulo, circunferencia
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado=4
print(f"El area de un {cuadrado.get_identificador()} de lado {lado} es: {cuadrado.get_area(lado)} \
      y el perimetro es: {cuadrado.get_perimetro(lado)}")

base = 4 
altura = 2
print(rectangulo.get_identificador())
print(f"El area de un {rectangulo.get_identificador()} de base {base} y altura {altura} es: {rectangulo.get_area(base, altura)} \
      y el perimetro es: {rectangulo.get_perimetro(base, altura)}")
base = 4
altura = 6
print(triangulo.get_identificador())
print(f"El area de un {triangulo.get_identificador()} de base {base} y altura {altura} es: {triangulo.get_area(base, altura)} \
      y el perimetro es: {triangulo.get_perimetro(base, altura)}")

radio = 3
print(f"El area de una circunferencia de radio 3 es {circunferencia.get_area(radio)}")