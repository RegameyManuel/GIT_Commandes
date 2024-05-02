#!/bin/bash

# Demander le nom de l'utilisateur
read -p "Entrez votre nom pour Git: " name
# Demander l'adresse email de l'utilisateur
read -p "Entrez votre adresse email pour Git: " email

# Mise à jour des paquets et installation de Git
sudo apt update
sudo apt install git -y

# Configurer le nom et l'email pour Git
git config --global user.name "$name"
git config --global user.email "$email"

# Vérifier si wget est installé, sinon l'installer
type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)

# Ajouter la clé GPG et le dépôt de GitHub CLI
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Mettre à jour les paquets et installer GitHub CLI
sudo apt update
sudo apt install gh -y

# Authentifier l'utilisateur sur GitHub
gh auth login

echo "Git et GitHub CLI ont été installés et configurés avec succès."

