"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O global é onde todo o código é acançável.
O local é onde apenas nomes do mesmo local podem ser alcançados.
Não temos acessso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.
"""
x = 1

def escopo():
    global x 
    x = 10 # alterou o valor de x 

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)