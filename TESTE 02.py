"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2
valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence
ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""


print('-=-'*28)
print('Sequência de Fibonacci')
print('-=-'*28)
n = int(input('Insira um número para gerar uma  sequência de Fibonnaci: '))
n1 = 0
n2 = 1
print('-=-'*28)
print(f'{n1} -> {n2}',end = '')
cont1 = 3

while cont1 <= n:
   n3 = n1 + n2
   print('-> {}'.format(n3), end = '')
   n1 = n2
   n2 = n3
   cont1 += 1
print('-> FIM')