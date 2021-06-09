

class Funcoes:
    def __init__(self):
        pass

def calc_ano_aposentadoria(x,y):
    anos_aposentadoria = (65-x)
    ano_de_aposentadoria = y + anos_aposentadoria
    if anos_aposentadoria <= 0:
        Mensagem = ('Já pode se aposentar desde ',ano_de_aposentadoria)
    elif anos_aposentadoria >0:
        Mensagem = ('Ainda faltam ',anos_aposentadoria,' anos. Previsão para ',ano_de_aposentadoria)
    else:
        pass
    return Mensagem;

def calc_par_ou_impar(x):
    if (x%2) == 0:
        Mensagem = ('Par')
    else:
        Mensagem = ('Ímpar')
    return Mensagem;

def criar_lista_com_primeiro_e_ultimo_de_outra_lista(lista_paramentro = []):
    lista_nova = []
    tamanho = len(lista_paramentro)
    primeiro = lista_paramentro[0]
    ultimo = lista_paramentro[tamanho-1]
    lista_nova[0] = primeiro
    lista_nova[1] = ultimo
    print(lista_nova)


#Trocar por .index
def criar_lista_sem_duplicados(lista_repetidos = []):
    lista_sem_duplicados = []
    tamanho = len(lista_repetidos)
    qtd_repetidos = 0
    palavra_repetida = ''
    tamanho_atual = 0
    x = 0
    y = 0
    while x < tamanho:
        if lista_repetidos.count(lista_repetidos[x]) == 1:
            lista_sem_duplicados.append(lista_repetidos[x])
            x = x + 1
        else:
            qtd_repetidos = lista_repetidos.count(lista_repetidos[x])
            palavra_repetida = lista_repetidos[x]
            tamanho_atual = tamanho
            tamanho = tamanho - qtd_repetidos + 1
            y = x
            while y < tamanho_atual:
                if palavra_repetida == lista_repetidos[y] and qtd_repetidos > 1:
                    lista_repetidos.remove(lista_repetidos[y])
                    qtd_repetidos = qtd_repetidos - 1
                    tamanho_atual = tamanho_atual - 1
                else:
                    y = y + 1
    print(lista_sem_duplicados)

