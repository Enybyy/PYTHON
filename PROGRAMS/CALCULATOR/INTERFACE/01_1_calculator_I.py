import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora en Python")

        # Pantalla para mostrar la ecuación y el resultado
        self.equation_line = tk.Entry(master, font=("Arial", 18))
        self.equation_line.grid(row=0, column=0, columnspan=4)

        # Botones numéricos y operaciones
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        row, col = 1, 0
        for button_text in buttons:
            tk.Button(master, text=button_text, font=("Arial", 14), command=lambda text=button_text: self.on_button_click(text)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.equation_line.get())
                self.equation_line.delete(0, tk.END)
                self.equation_line.insert(0, str(result))
            except Exception:
                self.equation_line.delete(0, tk.END)
                self.equation_line.insert(0, "Error")
        elif text == "C":
            self.equation_line.delete(0, tk.END)
        else:
            self.equation_line.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
