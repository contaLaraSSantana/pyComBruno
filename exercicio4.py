#Crie um programa e declare uma constante PI (use 4 casas após a vírgula).
#Dados o raio e a altura, calcular e apresentar do volume de uma lata de óleo
#utilizando a fórmula fórmula: volume = PI * r2 * altura

PI= 3.1415
r = float(input("Informe o raio:"))
a = float(input("Informe a altura:"))
v = PI * (r**2) * a

print("O volume da lata de óleo é de", v)