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