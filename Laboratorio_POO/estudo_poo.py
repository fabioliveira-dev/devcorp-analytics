from time import sleep

class Sushiman():
    def __init__(self, nome, tam_uniforme, sapato):
        self.nome = nome.strip().capitalize()
        self.tam_uniforme = tam_uniforme.strip().upper()
        self.sapato = int(sapato)

    def trabalhar(self):
        print(f'O Sushiman {self.nome} está fazendo Uramaki de Salmão!')
        sleep(1)
        print(f'Agora o Sushiman {self.nome} está cortando Sashimi de Atum!')
funcionario_1 = Sushiman('fabio', 'gg', 42)
print(f"O Funcionário {funcionario_1.nome} usa uniforme {funcionario_1.tam_uniforme} e calça nº {funcionario_1.sapato}")
sleep(1)
funcionario_1.trabalhar()
