import tkinter as tk

def resetaTela(window):
    for widget in window.winfo_children():
        widget.destroy()
