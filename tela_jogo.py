import tkinter as tk
from utilitario import resetaTela
from logica_jogo import DadosFuncionais, DadosOperacionais

class TelaJogo:
    def __init__(self, window):
        self.window = window
        self.operador_correto = None
        self.num1 = None
        self.num2 = None
        self.resultado = None

    def frameTelaJogo(self): 
        resetaTela(self.window)
        self.window.title("The Math Game")

        # Geração dos dados do jogo
        self.num1, self.num2 = DadosFuncionais.gerarNumeros()
        self.operador_correto = DadosFuncionais.selecionaOperador()
        self.resultado = DadosFuncionais.calculaResultado(self.num1, self.num2, self.operador_correto)

        # Cabeçalho
        cabecalho = tk.Frame(self.window)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Partida:").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, text=f"{self.window.partida_atual}/20").grid(row=0, column=1, padx=10)

        tk.Label(cabecalho, text="Pontuação:").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, text=str(self.window.pontos)).grid(row=0, column=3, padx=10)

        botao_parar = tk.Button(cabecalho, text="Parar", font=("Arial", 10), command=self.pararJogo)
        botao_parar.grid(row=0, column=4, padx=10)

        # Números da conta
        numeros_frame = tk.Frame(self.window)
        numeros_frame.pack(pady=40)

        tk.Label(numeros_frame, text=str(self.num1), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="?", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text=str(self.num2), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="=", font=("Arial", 32)).pack(side="left", padx=10)
        tk.Label(numeros_frame, text=str(self.resultado), font=("Arial", 32)).pack(side="left", padx=10)

        # Botões de operação
        operacoes_frame = tk.Frame(self.window)
        operacoes_frame.pack(pady=30)

        operadores_mapeados = {"+": "+", "-": "-", "x": "*", "÷": "/"}

        for texto_botao, operador_real in operadores_mapeados.items():
            botao = tk.Button(
                operacoes_frame,
                text=texto_botao,
                font=("Arial", 16),
                width=5,
                height=2,
                command=lambda op=operador_real: self.processarResposta(op)
            )
            botao.pack(side="left", padx=10)

        # Rodapé
        rodape = tk.Label(
            self.window,
            text="Desenvolvido por: \nCaio e André (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def processarResposta(self, resposta):
        if resposta == self.operador_correto:
            self.window.pontos += 199
        else:
            self.window.pontos += 0

        self.window.continua_jogo.set(True)

    def pararJogo(self):
        self.window.running = False
        self.window.continua_jogo.set(True)
