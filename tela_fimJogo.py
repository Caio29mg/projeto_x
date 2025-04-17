import tkinter as tk
from utilitario import resetaTela
from tela_jogo import TelaJogo
from logica_jogo import DadosOperacionais

class FinalJogo:
    def __init__(self, window, pontos):
        self.window = window
        self.pontos = pontos

    def frameTelaFim(self):
        resetaTela(self.window)
        self.window.title("Fim de Jogo")

        # Título
        titulo = tk.Label(
            self.window,
            text="Fim do Jogo!",
            font=("Arial", 28),
            fg="green"
        )
        titulo.pack(pady=40)

        # Pontuação final
        pontuacao = tk.Label(
            self.window,
            text=f"Você fez {self.pontos} pontos!",
            font=("Arial", 20)
        )
        pontuacao.pack(pady=20)

        # Botões
        botoes_frame = tk.Frame(self.window)
        botoes_frame.pack(pady=40)

        botao_reiniciar = tk.Button(
            botoes_frame,
            text="Jogar Novamente",
            font=("Arial", 14),
            width=15,
            height=2,
            command=self.reiniciarJogo
        )
        botao_reiniciar.grid(row=0, column=0, padx=20)

        botao_sair = tk.Button(
            botoes_frame,
            text="Sair",
            font=("Arial", 14),
            width=10,
            height=2,
            command=self.sairDoJogo
        )
        botao_sair.grid(row=0, column=1, padx=20)

        # Rodapé
        rodape = tk.Label(
            self.window,
            text="Desenvolvido por Caio e André\nSenai Betim 2025",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def reiniciarJogo(self):
        tela_jogo = TelaJogo(self.window)
        DadosOperacionais.iniciaJogo(tela_jogo, self.window)

    def sairDoJogo(self):
        self.window.destroy()
