#Resolução das atividades da aula 07.Hora da prática: a função print()

#   Exercícios
#1- Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura')
print("\n")

#2- Imprima a frase: Meu nome é {nome} e tenho {idade} anos| em que nome idade precisam ser valores armazenados em 
# variáveis.
nome = "Almir"
idade = 39
print(f"Meu nome é {nome} e tenho {idade} anos de idade.")
print("\n")

""""
3- Imprima a palavra 'ALURA' de modo que cada letra fique em uma linha, como mostrado a seguir:
A
L
U
R
A
"""
print("""
    A
    L
    U
    R
    A
    """)
print("\n")


""""
4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma 
variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
"""
pi = 3.14159
print(f"O valor arredondado de pi é: {pi:.2f}")
print("\n")