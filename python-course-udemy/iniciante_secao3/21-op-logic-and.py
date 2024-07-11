# operadores lógicos
# and (e) or (ou) not (não)

# and - todas as condições precisam ser verdadeiras
# se qualquer valor for falso, a expressão inteira será avaliada naquele valor
# são considerados falsy 0 0.0 '' False
# também existe o tipo None que é usado para representar um não valor 

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ' )

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_digitada:
    print('Entrar')
else:
    print('Sair')


print(True and False and True)
print(bool(''))

if 0 and 1:
    print(True and 1)
