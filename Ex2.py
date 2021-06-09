'''Nesse exercício você vai praticar: Lógica de Programação Python; condições if e else
Problema: Você precisa criar um robô que é capaz de responder ao usuário se determinado
número é par ou ímpar. Você deve pedir a pessoa para digitar um número aleatório e responder
com uma mensagem dizendo: "O número inserido é par" ou "O número inserido é ímpar"
Dica: Utilize a função input() para interagir com a pessoa'''
import ClasseFuncoes as funcoes

numero = int(input(print('Informe o número: ')))
print(funcoes.calc_par_ou_impar(numero))