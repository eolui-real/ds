import tkinter as tk
from aluno import Aluno

class TelaCadastro:
    def __init__(self, master, voltar_callback):
        # Criando o frame principal da tela
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)  # Preenche todo o espaço da janela

        # Título da tela
        self.label = tk.Label(self.frame, text="Cadastro de Aluno")
        self.label.grid(row=0, column=1, pady=10)

        # Nome
        tk.Label(self.frame, text="Nome:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=1, column=1, padx=5, pady=5)

        # Idade
        tk.Label(self.frame, text="Idade:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.idade_entry = tk.Entry(self.frame)
        self.idade_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botão Cadastrar
        self.botao_cadastrar = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar)
        self.botao_cadastrar.grid(row=3, column=1, pady=10)

        # Botão Voltar
        self.botao_voltar = tk.Button(self.frame, text="Voltar", command=voltar_callback)
        self.botao_voltar.grid(row=4, column=1, pady=10)

        # Lista de alunos
        self.lista_label = tk.Label(self.frame, text="")
        self.lista_label.grid(row=5, column=0, columnspan=2, pady=5)

        self.lista_alunos = []

    def cadastrar(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()

        # Verificando se os campos estão preenchidos corretamente
        if nome and idade.isdigit():
            aluno = Aluno(nome, int(idade))
            self.lista_alunos.append(aluno)

            # Limpando os campos de entrada
            self.nome_entry.delete(0, tk.END)
            self.idade_entry.delete(0, tk.END)

            # Exibindo a lista atualizada de alunos
            self.exibir_lista()

    def exibir_lista(self):
        # Exibindo a lista de alunos cadastrados
        texto = "\n".join(str(a) for a in self.lista_alunos)
        self.lista_label.config(text=texto)


# Função de retorno para o botão Voltar
def voltar():
    print("Voltando...")

# Teste para garantir que a interface seja carregada
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tela de Cadastro")

    # Cria a tela de cadastro
    tela = TelaCadastro(root, voltar)

    # Exibe a janela
    root.mainloop()
