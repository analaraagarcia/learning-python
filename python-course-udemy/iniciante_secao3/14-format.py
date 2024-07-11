# formatação de strings com o método format

a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)

print(formato)