""" 
Gerando cpf a partir do código passado
"""
#Importar o random para gerar números aleatórios
import random 

#Deixo a variável vazia para jogar no for
nove_digitos = ''
#no for eu coloco um range para gerar apenas 9 números
for i in range(9):
    nove_digitos += str(random.randint(0, 9)) #transformo em str e gero

cont_regressivo_1 = 10
resultado1 = 0

for digito in nove_digitos:
    resultado1 += int(digito) * cont_regressivo_1
    cont_regressivo_1 -= 1

digito_um = (resultado1 * 10) % 11
digito_um = digito_um if digito_um <= 9 else 0
#----------------------------------------------------
dez_digitos = nove_digitos + str(digito_um)
resultado2 = 0
cont_regressivo2 = 11

for digito in dez_digitos:
    resultado2 += int(digito) * cont_regressivo2
    cont_regressivo2 -= 1
digito_dois = resultado2 * 10 % 11
digito_dois = digito_dois if digito_dois <= 9 else 0 

cpf_gerado = f'{nove_digitos}{digito_um}{digito_dois}'

print(cpf_gerado)
