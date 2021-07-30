# mudando caixa da string

seq = "QWERTYU"
SEQ2 = "qwertyu"
seq3 = "jeff alves"

print(seq)
print("era maiusculo: ",seq.lower()) # minusculo
print("era minusculo: ", SEQ2.upper()) # maiusculo

novaSeq = seq3.strip() # remove caracteres especiais e espaço
novaSeq1 = seq3.split() # converte variavel em lista 

busca = seq3.find(" ") # indice da posição que a palavra aparece na string
print (seq3[busca:]) # print apenas da palavra que busca na frase

mudar = seq3.replace("alves","francisco") # substitui uma palavra pela outra 

print (mudar)

print (novaSeq1)
print (novaSeq)
