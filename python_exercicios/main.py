from calculadora import Calculadora, SelecionaOpcao


print("Calculadora")
a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))

opcao = int(input("""
Selecione a opção
0. Sair
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
Opção: """))

calculadora = Calculadora(a,b)

selecionaOpcao = SelecionaOpcao(opcao)

if opcao == 1:
    print(f'O resultado da soma é: {calculadora.soma(a,b):.0f}')

elif opcao == 2:
    print(f'O resultado da subtração é: {calculadora.subtracao(a,b):.0f}')

elif opcao == 3:
    print(f'O resultado da multiplicacão é: {calculadora.multiplicacao(a,b):.0f}')

elif opcao == 4:
    print(f'O resultado da divisão é: {calculadora.divisao(a,b):.0f}')






