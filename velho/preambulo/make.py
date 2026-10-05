#!/usr/bin/env python3

import glob, sys, os

target = sys.argv[1] if len(sys.argv) > 1 else next(iter(glob.glob("desafio*.tex")), None)

if not target:
    print("Ficheiro não encontrado!\nUse 'python script.py [nome do ficheiro]' ou nomeie o relatório 'desafio[nº].tex'")
    sys.exit(1)

keep_logs = "--keep-logs" if "logs" in sys.argv else ""

os.system(f"tectonic -X compile {target} -Z search-path=auxiliares/biblatex/ {keep_logs}")
