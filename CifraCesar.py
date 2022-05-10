texto = input("Digite o texto que deseja criptar ou desincriptar: ")
chave = int(input("Digite a chave: "))
modo = input("Escolha E para criptografar e D para desincriptografar:  ")
convertido = ' '
CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

texto =  texto.upper()

for caracter in texto:
    if caracter in CARACTERES:

        num = CARACTERES.find(caracter) # obter o numero criptografado ou descriptado do caracter

        if modo.upper() == 'E':
            num += chave
        elif modo.upper() == 'D':
            num -= chave


        convertido += CARACTERES[num]
    else:
         convertido  += caracter

if modo.upper() == 'E':
    print("O texto criptografado é {}".format(convertido))

if modo.upper() == 'D':
    print("O texto descriptografado é {}".format(convertido))
