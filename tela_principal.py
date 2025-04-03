import tkinter as tk
from tkinter import messagebox

def projetoX():
    window = tk.tk()
    window.tela("800x600")
    window.titulo("The Math Game")
    window.redimensionavel(False, False)

    window.continue_game = tk.BooleanVar(value=False)
    window.correndo = True

    def on_close():
        if messagebox.askyesno("Confirmação", "Você realmente deseja sair do jogo?"):
            window.correndo = False
            window.continue_game.set(True)
            window.destroy()

    window.protocolo("WM_DELETE_WINDOW", on_close)

    return window

window = projetoX()

try:
    window.mainloop()
except Exception as e:
    print(f"Erro durante a execução: {e}")
    

