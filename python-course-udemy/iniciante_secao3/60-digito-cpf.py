"""
Cálculo do primeiro DÍGITO do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

Ex.: 746.824.890-70
    10   9   8   7   6   5   4   3   2
*   7    4   6   8   2   4   8   9   0
    ___________________________________
    70   36  48  56  12  20  32  27  0

Somas todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 = 301

Multiplicar o resultado anterios por 10:
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 == 7

Se o resultado anterior for maior que 9:
    resultado = 0

"""
# começa pegando o CPF do usuário

cpf = '51882118073'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito = (resultado * 10) % 11
digito = digito if digito <= 9 else 0
print(digito)

