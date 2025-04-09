import tkinter as tk
from tkinter import ttk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador Minimalista")
        self.root.geometry("200x150")  # Tamaño pequeño y minimalista
        self.root.resizable(False, False)  # No redimensionable
        self.root.configure(bg="#f5f5f5")  # Fondo gris claro

        # Variable para el contador
        self.count = 0

        # Estilo para los botones
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14), padding=5)
        style.configure("TLabel", background="#f5f5f5", font=("Arial", 24, "bold"))

        # Etiqueta para mostrar el contador
        self.label = ttk.Label(root, text=f"{self.count:04d}", style="TLabel")
        self.label.pack(pady=20)

        # Frame para los botones
        button_frame = ttk.Frame(root, style="TFrame")
        button_frame.pack()

        # Botón para incrementar
        self.increment_button = ttk.Button(button_frame, text="+", command=self.increment)
        self.increment_button.pack(side=tk.LEFT, padx=5)

        # Botón para reiniciar
        self.reset_button = ttk.Button(button_frame, text="C", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def increment(self):
        self.count += 1
        self.label.config(text=f"{self.count:04d}")

    def reset(self):
        self.count = 0
        self.label.config(text=f"{self.count:04d}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
