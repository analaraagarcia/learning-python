# operadores lógicos
# and (e) or (ou) not (não)

# or - qualquer condição verdadeira avalia toda a expressão como verdadeira
# se qualquer valor for verdadeiro, a expressão inteira será avaliada naquele valor
# são considerados falsy 0 0.0 '' False
# também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ' )

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_digitada:
    print('Entrar')
else:
    print('Sair')

# avaliação de curto circuito

print(True or False)
print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)
