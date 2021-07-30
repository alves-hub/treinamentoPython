arquivo = open("arquivo.txt")

linha = arquivo.readlines() # Primeira linha 
textoCompleto = arquivo.read() # texto completo



print(linha[1])

for linhas in linha:
	print(linhas)