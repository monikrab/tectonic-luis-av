#!/usr/bin/env python3
#  |
#  `- Usando esta instrução na primeira linha do ficheiro, o Linux executa-o
#     automaticamente, usando o Python. No Linux, usa 'chmod +x make.py' para
#     fazê-lo executável, e usa './make.py' para o correr.


# Bibliotecas que o script precisa para funcionar (sempre presentes na biblioteca
# padrão do Python)
import glob, sys, os 


# Se o nome do ficheiro LaTeX começar por 'desafio' e acabar com '.tex', é
# automaticamente selecionado, ou seja, 'python make.py' compila o documento diretamente
nome_do_ficheiro = sys.argv[1] if len(sys.argv) > 1 else next(iter(glob.glob("desafio*.tex")), None)


# Se não houver nenhum ficheiro com esse nome ...
if not nome_do_ficheiro:
    # Avisa o utilizador
    print("Ficheiro não encontrado!\nUse 'python script.py [nome do ficheiro]' ou nomeie o relatório 'desafio[nº].tex'")
    # Termina a execução do script
    sys.exit(1)


# Se o professor pedir 'logs', execute o comando com 'logs' no final, por ex.:
# 'python make.py relatorio.tex logs'
escrever_logs = "--keep-logs" if "logs" in sys.argv else ""


# Comando de compilação do documento usando o Tectonic:
#   tectonic   -X compile [nome do ficheiro]  -Z search-path=auxiliares/biblatex
#   |            |                              |  
#   `- Comando   `- Subcomando (compilar)       `- Onde encontrar o BibLaTeX (faz a bibliografia)
#
os.system(f"tectonic -X compile {nome_do_ficheiro} -Z search-path=auxiliares/biblatex/ {escrever_logs}")
