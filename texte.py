'''
import lorem

separation = "\n\n\n*** --------- ***\n\n"

# On génère une phrase de Lorem Ipsum
phrase = lorem.sentence()
print(phrase + separation)

# On génère un paragraphe de Lorem Ipsum
paragraphe = lorem.paragraph()
print(paragraphe + separation)

# On génère un texte avec un nombre spécifique de paragraphes
texte = lorem.text()
print(texte + separation)
'''

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import lorem

def generate_sentence():
    sentence = lorem.sentence()
    display_text(sentence + separation)

def generate_paragraph():
    paragraph = lorem.paragraph()
    display_text(paragraph + separation)

def generate_text():
    text = lorem.text()
    display_text(text + separation)

def display_text(text):
    text_area.configure(state='normal')
    text_area.insert(tk.END, text)
    text_area.configure(state='disabled')

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Générateur de Lorem Ipsum")

# Création d'une zone de texte déroulante pour afficher le résultat
text_area = ScrolledText(root, width=60, height=20, state='disabled')
text_area.pack(pady=10)

# Séparation visuelle pour les résultats
separation = "\n\n\n*** --------- ***\n\n"

# Création des boutons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

btn_sentence = tk.Button(button_frame, text="Générer une phrase", command=generate_sentence)
btn_sentence.pack(side=tk.LEFT, padx=5)

btn_paragraph = tk.Button(button_frame, text="Générer un paragraphe", command=generate_paragraph)
btn_paragraph.pack(side=tk.LEFT, padx=5)

btn_text = tk.Button(button_frame, text="Générer du texte", command=generate_text)
btn_text.pack(side=tk.LEFT, padx=5)

# Lancer l'application
root.mainloop()
