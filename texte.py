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

def generate_sentence():
    sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    display_text(sentence + separation)

def generate_paragraph():
    paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris iaculis porttitor congue. Vestibulum mauris nibh, convallis et risus sit amet, eleifend accumsan tellus. Sed quis feugiat lorem, non porta diam. Mauris vitae felis at risus tincidunt tempus. Morbi aliquet felis magna, et dignissim turpis porta et. Donec fringilla odio euismod diam viverra, a placerat arcu eleifend. Nulla a lorem pellentesque, consectetur dolor id, semper massa."
    display_text(paragraph + separation)

def generate_text():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris iaculis porttitor congue. Vestibulum mauris nibh, convallis et risus sit amet, eleifend accumsan tellus. Sed quis feugiat lorem, non porta diam. Mauris vitae felis at risus tincidunt tempus. Morbi aliquet felis magna, et dignissim turpis porta et. Donec fringilla odio euismod diam viverra, a placerat arcu eleifend. Nulla a lorem pellentesque, consectetur dolor id, semper massa. Pellentesque dapibus imperdiet dui ornare ultrices. Nullam eget feugiat erat, eu tincidunt libero. Nulla tempus dolor eu ultricies pharetra. Cras neque sem, lobortis sit amet nisl at, rhoncus facilisis ex. Nunc at mollis nibh. Ut vel magna ligula. Phasellus vel diam vulputate, posuere quam ut, molestie dui. Maecenas neque mauris, lacinia quis vulputate dignissim, ultricies a nulla. Pellentesque fringilla, velit ut vestibulum faucibus, quam lorem efficitur elit, sed hendrerit lorem purus fringilla lacus. Fusce pretium finibus molestie. In at pharetra elit. Mauris arcu libero, ornare vel ligula eget, congue laoreet justo. Sed finibus imperdiet vestibulum. Morbi in placerat tortor, aliquam vulputate neque. Donec ultricies justo vitae massa varius, ac facilisis diam sagittis. Nullam consequat elit ac nunc tincidunt, eget condimentum risus consequat. Suspendisse non pretium ex. In nisi arcu, pretium non volutpat sed, aliquam quis leo. Aliquam consequat blandit nulla nec rhoncus. Suspendisse risus neque, dictum ut consequat a, ultricies et sapien. Nam id congue magna. Curabitur lacinia vitae tellus id pretium. Nulla facilisi. Maecenas sed magna sem. Cras ac lacus metus. Integer lobortis eros sit amet nisl tristique pretium. Nunc tristique est vitae posuere elementum. Fusce tincidunt at diam non venenatis. Cras fermentum mi metus, ac fringilla ligula viverra mollis. Ut eget dictum velit. Morbi volutpat in est at luctus. Praesent vestibulum velit nec orci malesuada, ut auctor tortor cursus. Nunc tempor volutpat sem at elementum. Nam nec metus ultricies, rhoncus purus nec, tincidunt purus. Nullam ullamcorper molestie volutpat. Nam viverra libero id dui pellentesque, eu gravida felis laoreet. Nulla sed fermentum quam. Duis id lectus sem. Maecenas volutpat ligula eget hendrerit lacinia. Sed laoreet non est quis semper. "
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
