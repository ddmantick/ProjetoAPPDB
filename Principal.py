import tkinter as tk
from tkinter import messagebox

class Janela1:
    def __init__(self, master=None):
      self.widget1 = Frame(master)
      self.widget1.pack()
      self.msg = Label(self.widget1, text='Informe os Dados')
      self.msg["font"]=("Verdana","20", "italic", "bold")
      self.msg.pack()
      self.sair = Button(self.widget1)
      self.sair["text"] = "Sair"
      self.sair["font"] = ("calibri", "20")
      self.sair["width"] = 15
      self.sair["command"] = self.widget1.quit
      self.sair.pack()

# Funções para os botões
def mostrar_usuarios():
    messagebox.showinfo("Usuários", "Não deu certo carmona kkk")

def mostrar_cidades():
    messagebox.showinfo("Cidades", "Não deu certo carmona")

def mostrar_clientes():
    messagebox.showinfo("Clientes", "não deu certo Carmona")

def fechar_janela():
    root.destroy()

# Criação da janela principal
root = tk.Tk()
root.title("Interface de Botões")

# Criação dos botões
botao_usuarios = tk.Button(root, text="Usuários", command=mostrar_usuarios)
botao_usuarios.pack(pady=10)

botao_cidades = tk.Button(root, text="Cidades", command=mostrar_cidades)
botao_cidades.pack(pady=10)

botao_clientes = tk.Button(root, text="Clientes", command=mostrar_clientes)
botao_clientes.pack(pady=10)

botao_fechar = tk.Button(root, text="Fechar", command=fechar_janela)
botao_fechar.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()