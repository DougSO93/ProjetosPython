'''Nesse exercício você vai praticar: Lógica de programação Python

Problema: Você foi contratado(a) para fazer um serviço para o INSS
(Instituto Nacional do Seguro Social) do Brasil. O trabalho consiste
em criar um programa que diga a pessoa o ano que ela poderá se aposentar.
Você deve perguntar a pessoa, o nome, a idade e criar uma mensagem dizendo
em qual ano ela irá aposentar. Considere que todas as pessoas podem se aposentar
aos 65 anos de idade.

Dica: Utilize a função input() para interagir com a pessoa.'''
import ClasseFuncoes as funcoes
import Ex1ClassePessoa as ClassePessoa

nome_pessoa = str(input(print('Informe o nome da pessoa: ')))
idade_pessoa = int(input(print('Informe a idade da pessoa:')))
ano_base = int(input(print('Informe o ano base: ')))

print(ClassePessoa.set_nm_pessoa(ClassePessoa,nome_pessoa))
print(ClassePessoa.set_idade_pessoa(ClassePessoa,idade_pessoa))
print(funcoes.calc_ano_aposentadoria(idade_pessoa,ano_base))