import pandas as pd
import os

class DevCorp:
    def __init__(self):
        # Aqui é o SETUP. Só definimos como as coisas SÃO, não o que elas FAZEM.
        
        # Definindo as etiquetas (Colunas) do Caderno de Clientes
        # Isso é uma LISTA de textos.
        self.cols_clientes = ["CPF", "Nome", "VIP"]

        # Definindo as etiquetas do Bloco de Vendas
        # Precisamos do CPF_Cliente para fazer o Link (FK)
        self.cols_vendas = ["ID_Venda", "CPF_Cliente", "Produto", "Valor", "Qtd", "Data"]

        # Criando os nomes dos arquivos.
        self.arq_clientes = "clientes_db.csv"
        self.arq_vendas = "Vendas_relacional.csv"
        print("Sistema inicializado com Sucesso! Colunas definidas.")
        self._carregar_bancos()

    def _carregar_bancos(self):
        if os.path.exists(self.arq_clientes):
            self.clientes = pd.read_csv(self.arq_clientes, dtype={"CPF":str})
            print("Banco de dados Clientes carregado com sucesso!")
        else:
            self.clientes = pd.DataFrame(columns=self.cols_clientes)
            print("Banco de dados Clientes novo criado com sucesso!")

        if os.path.exists(self.arq_vendas):
            self.vendas = pd.read_csv(self.arq_vendas, dtype={"CPF_Cliente": str})
            print("Banco de dados Vendas carregado com sucesso!")
        else:
            self.vendas = pd.DataFrame(columns=self.cols_vendas)
            print("Banco de dados Vendas novo criado com sucesso!")

    def cadastrar_cliente(self, cpf, nome, vip=False):
        if cpf in self.clientes["CPF"].values:
            print(f"❌ Erro: O CPF {cpf} já existe!")
            return
        
        novo_cliente = pd.DataFrame([{
            "CPF": cpf,
            "Nome": nome,
            "VIP": vip
        }])
        
        self.clientes = pd.concat([self.clientes, novo_cliente], ignore_index=True)
        self.clientes.to_csv(self.arq_clientes, index=False)
        print(f"✅ Cliente {nome} cadastrado com sucesso!")
# --- TESTE ---
app = DevCorp()
app.cadastrar_cliente("123", "Fabio", vip=True)
app.cadastrar_cliente("123", "Clone do Fabio") # Tem que dar erro!