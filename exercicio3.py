#Solicite ao usuário o valor do salário atual (numérico com decimais)
#em seguida solicite o percentual de aumento (numérico com decimais) e
#imprima o valor do salário atualizado.

salario = float(input("Informe o seu salario atual:"))
aumento = float(input("Informe o percentual de aumento:"))
porcentagem = (salario*aumento)/100
Vatualizado = porcentagem + salario

print("O valor do salário atualizado é", Vatualizado)