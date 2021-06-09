'''Nesse exercício você vai praticar: Funções; condições
Problema: Você trabalha em uma madeireira e lida com os
pedidos dos clientes. Você tem três pedidos para realizar
no dia e o seu gerente pediu para você selecionar o maior
pedido para fazer a primeira entrega. Cada pedido é uma
lista com os códigos dos produtos que devem ser entregues.
Por ser essa uma situação corriqueira você deve criar uma
função que automatiza esse processo. (Não utilize a função max() do python)
Dica: Crie as variáveis em listas e depois uma função que compare as variáveis'''

lista_1 = ['Sabado','Domingo','Segunda','Terça','Sabado','Domingo','Segunda','Terça','Terça']
lista_2 = ['Sabado','Domingo','Segunda','Terça','Sabado','Domingo','Segunda','Terça','Terça']
lista_3 = ['Sabado','Domingo','Segunda','Terça','Sabado','Domingo','Segunda','Segunda','Terça']

tamanho_1 = len(lista_1)
tamanho_2 = len(lista_2)
tamanho_3 = len(lista_3)

if tamanho_1 > tamanho_2 and tamanho_1 > tamanho_3:
    print('lista 1')
elif tamanho_2 > tamanho_1 and tamanho_2 > tamanho_3:
    print('Lista 2')
elif tamanho_3 > tamanho_2 and tamanho_3 > tamanho_1:
    print('Lista 3')
elif tamanho_1 == tamanho_2 and tamanho_1 == tamanho_3:
    print('listas 1, 2 e 3')
elif tamanho_1 == tamanho_3 and tamanho_1 > tamanho_2:
    print('listas 1 e 3')
elif tamanho_1 == tamanho_2 and tamanho_1 > tamanho_3:
    print('listas 1 e 2')
elif tamanho_2 == tamanho_3 and tamanho_2 > tamanho_1:
    print('listas 2 e 3')
elif tamanho_3 == tamanho_1 and tamanho_3 > tamanho_2:
    print('listas 2 e 3')