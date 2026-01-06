import pandas as pd
import os
from datetime import datetime

class SistemaVendas:
    def __init__(self):
        """
        O Construtor é como ligar o servidor do Banco de Dados.
        Ele prepara a tabela vazia (DataFrame) com as colunas certas.
        """
        self.arquivo_banco = "vendas_db.csv"
        self.colunas = ["Produto", "Quantidade", "Preco_Unitario", "Total", "Data"]
        
        # Tenta carregar dados antigos (Persistência)
        if os.path.exists(self.arquivo_banco):
            self.db = pd.read_csv(self.arquivo_banco)
            print(f"✅ Banco de Dados carregado! {len(self.db)} registros encontrados.")
        else:
            self.db = pd.DataFrame(columns=self.colunas)
            print("⚠️ Banco de Dados novo criado.")

    def registrar_venda(self, produto, qtd, preco):
        """
        Funciona como um 'INSERT INTO' do SQL.
        Adiciona uma nova linha na nossa tabela.
        """
        total = qtd * preco
        data_hoje = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Cria um mini-dataframe temporário para o novo item
        nova_venda = pd.DataFrame([{
            "Produto": produto,
            "Quantidade": qtd,
            "Preco_Unitario": preco,
            "Total": total,
            "Data": data_hoje
        }])
        
        # Concatena (Cola) no banco principal. 
        # O pd.concat é a forma moderna de adicionar dados no Pandas.
        if self.db.empty:
            self.db = nova_venda
        else:
            self.db = pd.concat([self.db, nova_venda], ignore_index=True)
            
        print(f"💾 Venda registrada: {produto} (R$ {total:.2f})")
        self._salvar_no_disco() # Salva automático (Commit)

    def _salvar_no_disco(self):
        """Salva a memória RAM no HD (Arquivo CSV)"""
        self.db.to_csv(self.arquivo_banco, index=False)

    def gerar_relatorio(self):
        """Funciona como um 'SELECT * FROM' com formatação"""
        print("\n" + "="*40)
        print("📊 RELATÓRIO GERAL DE VENDAS")
        print("="*40)
        
        if self.db.empty:
            print("Nenhuma venda registrada ainda.")
        else:
            print(self.db)
            print("-" * 40)
            print(f"💰 Faturamento Total: R$ {self.db['Total'].sum():.2f}")
            print(f"📦 Total de Itens: {self.db['Quantidade'].sum()}")
        print("="*40 + "\n")

# --- ZONA DE TESTE (Simulando o Usuário) ---
if __name__ == "__main__":
    # 1. Instancia o Sistema (Cria o Objeto)
    app = SistemaVendas()
    
    # 2. Registra Vendas (Simula inputs)
    app.registrar_venda("Sushi Especial", 2, 45.00)
    app.registrar_venda("Coca-Cola", 5, 6.00)
    
    # 3. Pede o Relatório
    app.gerar_relatorio()