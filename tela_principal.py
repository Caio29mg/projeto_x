import tkinter as tk
from tkinter import messagebox
from tela_abertura import TelaInicial

def projetoX():
    window = tk.Tk() 
    window.geometry("800x600")  
    window.title("The Math Game") 
    window.resizable(False, False) 
    window.continua_jogo = tk.BooleanVar(value=False)
    window.running = True


    def on_close():
        if messagebox.askyesno("Confirmação", "Você realmente deseja sair do jogo?"):
            window.correndo = False
            window.continue_game.set(True)
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)  

    return window

window = projetoX()
tela_inicial = TelaInicial(window)
tela_inicial.frameTelaInicio()

try:
    window.mainloop()
except Exception as e:
    print(f"Erro durante a execução: {e}")
