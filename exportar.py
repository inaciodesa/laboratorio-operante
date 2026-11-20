#!/usr/bin/env python3
"""Gera a versão portátil do Laboratório Operante: um único arquivo HTML, sem dependências externas.
Uso: python3 exportar.py"""
import re, zipfile, pathlib
raiz = pathlib.Path(__file__).parent
fonte = (raiz / 'index.html').read_text(encoding='utf8')
cabeca, corpo = fonte.split('<div class="app">', 1)
cabeca = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n?', '', cabeca)   # sem rede: usa as fontes do sistema
cabeca = re.sub(r'<meta name="claude:[^>]*>\n?', '', cabeca)
html = ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + cabeca + '</head>\n<body>\n<div class="app">' + corpo + '\n</body>\n</html>\n')
assert 'http://' not in html.replace('http://www.w3.org', '') and 'https://' not in html, 'o export não pode depender da rede'
saida = raiz / 'export'; saida.mkdir(exist_ok=True)
(saida / 'laboratorio-operante.html').write_text(html, encoding='utf8')
leia = """LABORATÓRIO OPERANTE
Autora: Alana Campos de Sá

Como usar
1. Abra o arquivo laboratorio-operante.html em qualquer navegador (Chrome, Edge, Firefox, Safari),
   no computador, tablet ou celular. Basta dar dois cliques.
2. Não precisa de internet, instalação nem servidor. Tudo está dentro desse único arquivo.
3. Para guardar o progresso do rato, use a aba "Arquivo e parâmetros": "Salvar ponto" guarda no
   navegador; "Baixar arquivo" gera um .json que pode ser aberto em outro computador.

Licença: domínio público (The Unlicense). Use, copie e modifique sem restrições.

Base: Graham, J., Alloway, T., & Krames, L. (1994). Sniffy, the virtual rat: Simulated operant
conditioning. Behavior Research Methods, Instruments, & Computers, 26(2), 134-141.
"""
(saida / 'LEIA-ME.txt').write_text(leia, encoding='utf8')
docs = raiz / 'docs'; docs.mkdir(exist_ok=True)
(docs / 'index.html').write_text(html, encoding='utf8')   # versão servida pelo GitHub Pages
with zipfile.ZipFile(saida / 'laboratorio-operante.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(saida / 'laboratorio-operante.html', 'laboratorio-operante/laboratorio-operante.html')
    z.write(saida / 'LEIA-ME.txt', 'laboratorio-operante/LEIA-ME.txt')
print('export gerado em', saida)
