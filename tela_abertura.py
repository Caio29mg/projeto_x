import tkinter as tk
from utilitario import resetaTela
from tela_instrucoes import TelaInstrucoes

class TelaInicial:
    def __init__(self,window):
        self.window = window
        resetaTela(self.window)
        window.title("The Math Game")
    
    def frameTelaInicio(self):
        titulo = tk.Label(self.window, text="Bem-vindo ao \nThe Math Game!", font=("Arial",30))
        titulo.pack(pady=50)

        botao_play = tk.Button(
            self.window,
            text="Play",
            font=('Arial',16),
            width=10,
            height=2,
            command=self.abrirInstrucoes
        )
        botao_play.pack(pady=20)

        rodape = tk.Label(
            self.window,
            text="Desenvolvido por Caio e André \nSenai Betim CETEM 2025.",
            font=("Arial",8)
        )
        rodape.pack(side="bottom",pady=10)
        
    def abrirInstrucoes(self):
        telaInstrucoes = TelaInstrucoes(self.window)
        telaInstrucoes.frameTelaInstrucoes()