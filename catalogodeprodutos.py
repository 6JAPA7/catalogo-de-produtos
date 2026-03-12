import tkinter as tk
from tkinter import ttk
import mysql.connector

def criar_input(telae, nome):
        linha = tk.Frame(telae)
        linha.pack(pady=5)
        label = tk.Label(linha, text=nome, fg="black")
        label.pack(side="left")
        input = nome = tk.Entry(linha)
        input.pack(side="left")
        return input

def add_produto():
    def save():
        lista = [id_atual]
        for caixa in caixas:
            lista.append(caixa.get())
        print(f"lista: {lista}")
        
        itens = tuple(lista)
        colunassema = ", ".join(colunas)
        
        
        cmd = f"INSERT INTO new_table ({colunassema}) VALUES {itens};"
        print(cmd)
        print(f"\033[1;31;43mitens: {itens}\033[m")
        db = mysql.connector.connect(host="localhost", user="root", password="Japaa2222", database="new_schema")
        cursor = db.cursor()

        
        cursor.execute(cmd)
        db.commit()
        cursor.close()
        db.close()
        tela_add.destroy()
        
        #atualizar tabela e fechar janela
    
    tela_add = tk.Toplevel()
    tela.title('adicionar produto')
    id_atual = linhas+1
    caixas = []
    for c in colunas[1:]:
        caixa = criar_input(tela_add, c)
        caixas.append(caixa)

    salvar = tk.Button(tela_add, text="confirmar", command=save)
    salvar.pack(side="left")
    cancelar = tk.Button(tela_add, text="cancelar")
    cancelar.pack(side="left")
 
def atualizar_tabela():
    
    table = ttk.Treeview(tela)
    
    table['columns'] = colunas
    table.column('#0', width=0, stretch=tk.NO)
    table.heading('#0', text='', anchor=tk.W)
    for c in table["columns"]:
        
        table.column(c, anchor=tk.W, width=150)
        table.heading(c, text=c, anchor=tk.W)

    for i in range(linhas):
        if i % 2 == 0:
            table.insert(parent='', index=i, values=results[i], tags=('evenrow',))
        else:
            table.insert(parent='', index=i, values=results[i], tags=('oddrow',))


    table.pack(side="left")

    

#pegando dados da tabela mysql
db = mysql.connector.connect(host="localhost", user="root", password="Japaa2222", database="new_schema")
cursor = db.cursor()

query = ("SELECT * FROM new_schema.new_table"
         "")
cursor.execute(query)

results = cursor.fetchall()
colunas = cursor.column_names
cursor.close()

qtd_colunas = len(colunas)


linhas = len(results)


print(f"colunas: {colunas} quantidade de colunas: {qtd_colunas} linhas: {linhas}\n dados da tabela: {results}")

# criando tela inicial
tela = tk.Tk()
tela.title('Catalogo de Produtos')
tela.geometry('560x227')
atualizar_tabela()

add_btn = tk.Button(tela, text="adicionar produto", command=add_produto)
add_btn.pack(side="top")
tela.mainloop()




