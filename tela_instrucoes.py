import tkinter as tk
from utilitario import resetaTela
from tela_jogo import TelaJogo

class TelaInstrucoes:
    def __init__(self, window):
        self.window = window

    def frameTelaInstrucoes(self):
        resetaTela(self.window)
        self.window.title("The Math Game")

        titulo = tk.Label(self.window, text="Instruções do Jogo", font=("Arial", 24))
        titulo.pack(pady=50)

        texto = tk.Label(
            self.window,
            text="Clique na operação que corresponde ao resultado entre os dois números mostrados.\nOperações: |+|-|x|÷|"
        )
        texto.pack(pady=10)

        botao_play = tk.Button(
            self.window,
            text="Jogar",
            font=("Arial", 16),
            width=10,
            height=2,
            command=self.abrirTelaJogo
        )

        botao_play.pack(pady=20)

        rodape = tk.Label(
            self.window,
            text="Desenvolvido por: \nCaio e André (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)
        
    def abrirTelaJogo(self):
        from logica_jogo import DadosOperacionais
        from tela_jogo import TelaJogo

        tela_jogo = TelaJogo(self.window)
        DadosOperacionais.iniciaJogo(tela_jogo, self.window)

