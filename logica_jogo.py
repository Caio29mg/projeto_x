import tkinter as tk
import random
from tkinter import messagebox

class DadosOperacionais:
    @staticmethod
    def iniciaJogo(tela_jogo_instancia, window):
        window.pontos = 0
        window.running = True

        if not hasattr(window, 'continua_jogo'):
            window.continua_jogo = tk.BooleanVar()

        contador = 1
        max_partidas = 20

        while contador <= max_partidas:
            window.partida_atual = contador
            tela_jogo_instancia.frameTelaJogo()

            window.continua_jogo.set(False)
            window.wait_variable(window.continua_jogo)

            if not window.running:
                messagebox.showinfo("Jogo encerrado", f"Você saiu do jogo com {window.pontos} pontos.")
                return

            contador += 1

        from tela_fimJogo import FinalJogo
        tela_fim = FinalJogo(window, window.pontos)
        tela_fim.frameTelaFim()


    @staticmethod
    def iniciaTempo():
        m = 0
        s = 0
        h = 0
        return m, s, h

class DadosFuncionais:
    @staticmethod
    def gerarNumeros():
        return random.randint(0, 9), random.randint(0, 9)

    @staticmethod
    def selecionaOperador():
        return random.choice(["+", "-", "*", "/"])

    @staticmethod
    def calculaResultado(a, b, operador):
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            return round(a / (b if b != 0 else 1), 2)

