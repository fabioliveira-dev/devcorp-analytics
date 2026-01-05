# -------------------------------------------------------------------------
# Autor: Fabio de Oliveira
# Data: 30/12/2025
# Versão: 1.0
# Descrição: Script de calculo para faturamento.
# -------------------------------------------------------------------------
import boot_system
import locale
import json
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# --- CONFIGURAÇÕES ---
versao = "1.1"
catalogo = {"mouse": 25.00, "teclado": 150.00, "monitor": 899.00}
vendas_do_dia = []
faturamento_total = 0

# --- FUNÇÕES (AS NOVAS FERRAMENTAS) ---
def obter_numero(mensagem):
    """
    Fica num looping infinito até o usuário digitar um numero valido!
    aceita inteiros e float(com ponto ou virgula)
    """
    while True:
        try:
            valor_input = input(mensagem)
            #tratamento universal: troca virgula por ponto
            valor = float(valor_input.replace(',','.'))
            return valor # se deu certo, devolve o numero e encerra o looping e a função.
        except ValueError:
            print("❌ Erro: Digite apenas números válidos!")

def obter_validacao_sn(mensagem):
    """
    Faz a validação se o usuario vai ou não continuar usando o script.
    fica no looping até o usuário digitar a opção válida!
    """
    while True:
        resp = input(mensagem).strip().lower()
        if resp == 's' or resp == 'n':
            return resp # devolve o valor digitado ja tratado.
        print("❌ Opção inválida...")
        
print(f" --- Calculadora V{versao} ---")
print("--- INICIANDO VENDAS ---")

# verificar se existe o produto no "Dicionario" catalogo ou se precisa ser adicionado.
while True:
    produto = input("Digite o nome do produto: ")
    if not produto.strip():
        print("Entrada inválida: Você não digitou nada ou apenas espaços.")
        continue

    chave = produto.lower()

    if chave in catalogo:
        print(f"✅ Produto {chave} existente no catalogo. Preço R${catalogo[chave]:n}")
        valor_unitario = catalogo[chave]
    else:
        print(f"Produto não cadastrado!") 
        # Chamamos a função
        valor_unitario = obter_numero("Digite o Valor do Produto R$: ")
        catalogo[chave] = valor_unitario # Atualiza o dicionário    
    
    # definir quantidade(função)   
    qtd = int(obter_numero("Quantas unidades: "))

    # salvando os dados
    total_item = valor_unitario*qtd
    vendas_do_dia.append((produto, qtd, valor_unitario, total_item))

    # continuar ou encerrar(função)   
    if obter_validacao_sn("Cadastrar outro item [S/N]: ") == 'n':
        break

# relatório final
print('='*40)
print(' --- EXTRATO DETALHADO --- ')
for item in vendas_do_dia:
    # UNPACKING (Desempacotando a tupla)
    nome, quantidade, val_item, val_total = item
    print(f'{nome} (x{quantidade}) - R$ {val_item:n}')
    faturamento_total += val_total

# --- GRAVAÇÃO EM ARQUIVO (PERSISTÊNCIA) ---
print("💾 Salvando relatório no disco...")

# 1. Abrimos o arquivo em modo 'w' (Write)
# Dica: encoding='utf-8' garante que o 'R$' e acentos não fiquem bugados no Windows
with open("faturamento_hoje.txt", "w", encoding='utf-8') as arquivo:

    # 2. Escrevemos o cabeçalho
    arquivo.write("=== RELATÓRIO DE VENDAS (DevCorp) ===\n")
    arquivo.write(f"Versão do Sistema: {versao}\n")
    arquivo.write("-------------------------------------\n")

    # 3. Escrevemos item por item (Reaproveitando a lista vendas_do_dia)
    for item in vendas_do_dia:
        nome, qtd, val_unit, val_total = item
        # Note o \n no final de cada linha!
        arquivo.write(f"Item: {nome} | Qtd: {qtd} | Total: R$ {val_total:.2f}\n")
    
    arquivo.write("-------------------------------------\n")
    arquivo.write(f"FATURAMENTO TOTAL: R$ {faturamento_total:.2f}\n")
    with open("faturamento_hoje.json", 'w', encoding='utf-8') as arquivo:
        json.dump(vendas_do_dia, arquivo, indent=4, ensure_ascii=False)
        

print(f"✅ Arquivo 'faturamento_hoje.txt e csv' gerados com sucesso!")
with open("faturamento_hoje.json", 'r', encoding='utf-8') as arquivo:
    vendas_csv = json.load(arquivo)
    print(vendas_csv)
# Finalização do programa.
print("=====================================================================================")
print(" --- Fim da Operação! --- ")
print(f" --- {boot_system.sis_nome} --- ")
print("===============================================")