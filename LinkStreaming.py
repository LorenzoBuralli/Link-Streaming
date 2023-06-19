import tkinter as tk
import subprocess

__author__ = "Ryan119"
__version__ = "1.0"

def run_script_1():
    subprocess.Popen(['python', 'Cinema.py'])

def run_script_2():
    subprocess.Popen(['python', 'Cinema2.py'])

def run_script_3():
    subprocess.Popen(['python', 'RisultatiLive.py'])

root = tk.Tk()
root.title("Link Streaming")
root.configure(bg="black")  # Imposta il colore di sfondo su nero
root.resizable(False, False)  # Disabilita il ridimensionamento della finestra

button_font = ("Comic Sans MS", 12)  # Imposta il font Comic Sans per i pulsanti
button_width = 20  # Imposta la larghezza dei pulsanti

button1 = tk.Button(root, text="Cinema", command=run_script_1, font=button_font, width=button_width)
button1.configure(bg="black", fg="white")  # Imposta il colore di sfondo su nero e il testo su bianco
button1.pack(pady=10)

button2 = tk.Button(root, text="Cinema 2", command=run_script_2, font=button_font, width=button_width)
button2.configure(bg="black", fg="white")  # Imposta il colore di sfondo su nero e il testo su bianco
button2.pack(pady=10)

button3 = tk.Button(root, text="Risultati Live", command=run_script_3, font=button_font, width=button_width)
button3.configure(bg="black", fg="white")  # Imposta il colore di sfondo su nero e il testo su bianco
button3.pack(pady=10)

signature = tk.Label(root, text=f"Author: {__author__}\nVersion: {__version__}", bg="black", fg="white")
signature.pack(pady=10)

root.mainloop()

