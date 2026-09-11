import os, subprocess

#Mostrar o diretorio atual
print(f"Diretório Atual:",os.getcwd())

# #Mostra o processo atual
print(f"Processo Atual:",os.getpid())

#Abrir bloco de notas
subprocess.run("notepad")

#Abrir Calculadora
subprocess.run("calc")

#Abrir Explorador de Arquivos
subprocess.run("explorer")

#Criar um arquivo
with open("arquivo_aula.txt", "w") as arquivo:
    arquivo.write("Sistemas da Informação 4° Periodo, Sistemas Operacionais")