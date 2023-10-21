import tkinter as tk
import ttkbootstrap as ttkb
import json
import time
from tkinter import messagebox, Scrollbar, scrolledtext



class MainWindow:
    def __init__(self):
        self.JanelaPrincipal = ttkb.Window(themename='superhero')
        self.JanelaPrincipal.title('Data Structure Algorithm')
        self.JanelaPrincipal.geometry('780x350')
        self.JanelaPrincipal.resizable(False, False)

        self.TituloJanelaPrincipal = ttkb.Label(self.JanelaPrincipal, text="Organizador de Dados", font=('Gothic',30), style="info")
        self.TituloJanelaPrincipal.place(x=140, y=10)

        # Reinicializa o vetor a cada execução
        self.vetor = []

        # Carrega os valores do vetor a partir do arquivo JSON, se existir
        self.carregar_vetor()

        # Elementos gráficos
        self.CampoTextoVariavel = ttkb.Entry(self.JanelaPrincipal, font=('Gothic',12), style="success")
        self.CampoTextoVariavel.place(x=35, y=140, width=200)

        # FrameVetor será utilizado em várias partes, então é definido como atributo da classe
        self.FrameVetor = ttkb.Frame(self.JanelaPrincipal, style='warning', width=450, height=300)

        # Botões e outros elementos gráficos
        self.configurar_elementos_gui()

    def carregar_vetor(self):
        try:
            with open('vetor.json', 'r') as arquivo:
                self.vetor = json.load(arquivo)
            if len(self.vetor) > 1:
                messagebox.showinfo('Sucesso!',"Vetor carregado com sucesso!!")
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def salvar_vetor(self):
        with open('vetor.json', 'w') as arquivo:
            json.dump(self.vetor, arquivo)

    def fecha_app(self):
        self.JanelaPrincipal.destroy()

    def configurar_elementos_gui(self):

        # Botão para abrir métodos de ordenação: Quick e Merge - Hash - Grafos
        self.OrdenacaoDeDados = ttkb.Button(self.JanelaPrincipal, text='Processar Dados', style='warning', width=20, command=self.abre_menu_ordenacao)
        self.OrdenacaoDeDados.place(x=50, y=300)

        # Campo de inserção de valores dentro do vetor
        self.InsereVariavelVetor = ttkb.Label(self.JanelaPrincipal, text='Valor a ser inserido no vetor', font=('Gothic',14), style="info")
        self.InsereVariavelVetor.place(x=30, y=100)

        self.BotaoInsereVariavel = ttkb.Button(self.JanelaPrincipal, text='Inserir', style='success-outline', width=12, command=self.inserir_valor)
        self.BotaoInsereVariavel.place(x=250, y=140)

        self.BotaoObservarVetor = ttkb.Button(self.JanelaPrincipal, text='Olhar Vetor', style='warning-outline', width=15, command=self.abre_janela_observar_vetor)
        self.BotaoObservarVetor.place(x=450, y=140)

        self.BotaoRecriarVetor = ttkb.Button(self.JanelaPrincipal, text='Redefinir Vetor', style='danger-outline', width=15, command=self.redefinir_vetor)
        self.BotaoRecriarVetor.place(x=610, y=140)

        # Botões adicionais para outros métodos de ordenação
        self.TelaFundoOrdenacao = ttkb.LabelFrame(self.JanelaPrincipal,text='Métodos de Ordenação', style='success', width=625,height=70)
        self.TelaFundoOrdenacao.place(x=30,y=270)
        
        self.OrdenacaoDeDados = ttkb.Button(self.JanelaPrincipal, text='Quick - Merge', style='warning',width=20)
        self.OrdenacaoDeDados.place(x=40,y=295)
        
        self.OrdenacaoHash = ttkb.Button(self.JanelaPrincipal, text='Hash Table', style='success',width=20)
        self.OrdenacaoHash.place(x=250, y=295)
        
        self.OrdenacaoGrafo = ttkb.Button(self.JanelaPrincipal, text='Grafos', style='info', width=20, state='pressed')
        self.OrdenacaoGrafo.place(x=460,y=295)
        
        
        # ----------- FECHA APP
        self.FechaApp = ttkb.Button(self.JanelaPrincipal, text='Sair', style='danger-outline',width=10, command=self.fecha_app)
        self.FechaApp.place(x=665,y=305)
        #-----------------


    def abre_janela_observar_vetor(self):
        JanelaVetor = ttkb.Toplevel()
        JanelaVetor.title('Vetor')
        JanelaVetor.geometry('550x300')
        JanelaVetor.resizable(False, False)

        def fecha_janela():
            JanelaVetor.destroy()
                

        TextoVetor = ttkb.Label(JanelaVetor,text='Vetor atual',style='warning',font=('Garamond',14))
        TextoVetor.place(x=20,y=10)

        LB_vetor = tk.Listbox(JanelaVetor, selectmode=tk.SINGLE, font=("Arial",12), exportselection=False,height=10, width=30)
        LB_vetor.place(x=20, y=40)
        
        # Adiciona os valores do vetor ao frame
        for i, valor in enumerate(self.vetor):        
            LB_vetor.insert(tk.END, f" INDEX[{i}] = {valor}")
            
        # Adiciona uma barra de rolagem vertical
        scrollbar = ttkb.Scrollbar(JanelaVetor, orient="vertical", command=LB_vetor.yview,style='primary')
        scrollbar.place(x=350, y=40, height=245)

        LB_vetor.configure(yscrollcommand=scrollbar.set)            
        
        
        BotaoExcluir = ttkb.Button(JanelaVetor, text='Excluir', style='danger-outline', width=10,command= lambda: self.excluir_selecionado(LB_vetor))
        BotaoExcluir.place(x=420, y=40)

        BotaoVoltar = ttkb.Button(JanelaVetor, text='Voltar', style='primary-outline', width=10, command=fecha_janela)
        BotaoVoltar.place(x=420, y=250)
        
    def excluir_selecionado(self, listbox_vetor):
            # Obtém o índice do item selecionado na Listbox
        selected_index = listbox_vetor.curselection()

        if selected_index:
            # Converte a tupla para int
            selected_index = int(selected_index[0])

            # Remove o item do vetor
            del self.vetor[selected_index]

            # Atualiza a Listbox
            listbox_vetor.delete(0, tk.END)
            for i, valor in enumerate(self.vetor):
                listbox_vetor.insert(tk.END, f" INDEX[{i}] = {valor}")

            # Salva as alterações no vetor
            self.salvar_vetor()
        else:
            messagebox.showinfo("Seleção", "Selecione um item para excluir.")


    def redefinir_vetor(self):
        self.vetor = []
        self.salvar_vetor()  # Salva a redefinição do vetor
        self.atualizar_frame_vetor()
        messagebox.showinfo("Sucesso!","Vetor redefinido com sucesso!!")

    def inserir_valor(self):
        valor = self.CampoTextoVariavel.get()
        try:
            valor = int(valor)
            self.vetor.append(valor)
            self.salvar_vetor()  # Salva o vetor após cada inserção
            self.atualizar_frame_vetor()
            self.CampoTextoVariavel.delete(0, ttkb.END)
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido.")

    def atualizar_frame_vetor(self):
        # Limpa o frame
        for widget in self.FrameVetor.winfo_children():
            widget.destroy()

        # Adiciona os valores do vetor ao frame
        for i, valor in enumerate(self.vetor):
            ttkb.Label(self.FrameVetor, text=f"Vetor[{i}] = {valor}").pack()

    def abre_menu_ordenacao(self):
        # Adicione aqui a lógica para abrir o menu de ordenação
        print("Abrir menu de ordenação")
        
    # Métodos de ordenação
    def quick_sort(self):
        # Implemente aqui o algoritmo Quick Sort
        pass

    def merge_sort(self):
        # Implemente aqui o algoritmo Merge Sort
        pass

    def hash_table(self):
        # Implemente aqui a lógica para a tabela de hash
        pass

    def grafo(self):
        # Implemente aqui a lógica para o grafo
        pass
    
if __name__ == "__main__":
    app = MainWindow()
    app.JanelaPrincipal.mainloop()