"""
while + while (laços internos)
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'1{linha=} {coluna=}')
        coluna += 1

    linha += 1