import tkinter as tk
from tkinter import messagebox

class Veiculo:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano

class GestorDeVeiculos:
    def __init__(self):
        self.veiculos = []
        self.janela = tk.Tk()
        self.janela.title("Gestor de Veículos")

        # Campos para inserção de dados
        tk.Label(self.janela, text="Placa:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_placa = tk.Entry(self.janela)
        self.entrada_placa.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.janela, text="Modelo:").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_modelo = tk.Entry(self.janela)
        self.entrada_modelo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.janela, text="Ano:").grid(row=2, column=0, padx=5, pady=5)
        self.entrada_ano = tk.Entry(self.janela)
        self.entrada_ano.grid(row=2, column=1, padx=5, pady=5)

        # Botões
        tk.Button(self.janela, text="Adicionar Veículo", command=self.adicionar_veiculo).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(self.janela, text="Listar Veículos", command=self.listar_veiculos).grid(row=4, column=0, columnspan=2, pady=5)

        self.janela.mainloop()

    def adicionar_veiculo(self):
        placa = self.entrada_placa.get().strip().upper()
        modelo = self.entrada_modelo.get().strip()
        ano = self.entrada_ano.get().strip()

        if not placa or not modelo or not ano:
            messagebox.showwarning("Entrada Inválida", "Por favor, preencha todos os campos.")
            return

        if not ano.isdigit() or int(ano) < 1886 or int(ano) > 2100:
            messagebox.showwarning("Ano Inválido", "Por favor, insira um ano válido (1886 - 2100).")
            return

        novo_veiculo = Veiculo(placa, modelo, ano)
        self.veiculos.append(novo_veiculo)
        messagebox.showinfo("Sucesso", f"Veículo {placa} adicionado com sucesso!")
        self.limpar_campos()

    def listar_veiculos(self):
        if not self.veiculos:
            messagebox.showinfo("Lista Vazia", "Nenhum veículo cadastrado.")
            return

        lista = "\n".join([f"Placa: {v.placa}, Modelo: {v.modelo}, Ano: {v.ano}" for v in self.veiculos])
        messagebox.showinfo("Veículos Cadastrados", lista)

    def limpar_campos(self):
        self.entrada_placa.delete(0, tk.END)
        self.entrada_modelo.delete(0, tk.END)
        self.entrada_ano.delete(0, tk.END)

if __name__ == "__main__":
    GestorDeVeiculos()
