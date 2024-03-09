import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

# INGRESAR APIKEY
api_key = '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'
client = OpenAI(api_key=api_key)

input_text = "Eres un robot erudito"

# DEFINIR FUNCION OBTENER RESPUESTA


def get_response():
    user_input = user_input_text.get("1.0", "end-1c")
    chat_history.insert(tk.END, "Tú: " + user_input + "\n")
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=200
        )
        output_text = response.choices[0].text.strip()
        chat_history.insert(tk.END, "Robot Erudito: " + output_text + "\n")
    except Exception as e:
        chat_history.insert(tk.END, "Error: " + str(e) + "\n")
    user_input_text.delete("1.0", tk.END)

# FUNCION ENTER


def on_enter(event):
    get_response()


# CREAR VENTANA
root = tk.Tk()
root.title("Chatbot - Robot Erudito")

# CCREAR WITGEATS
chat_history = scrolledtext.ScrolledText(root, width=50, height=20)
user_input_text = tk.Text(root, width=50, height=3)
send_button = tk.Button(root, text="Enviar", command=get_response)

# ASOCIAR FUN ENTER
user_input_text.bind("<Return>", on_enter)

# COLOCAR WITGEATS EN WINDS
chat_history.pack()
user_input_text.pack()
send_button.pack()

# INICIAR LOOP
root.mainloop()
