nome = input('Qual é o seu Nome? ')
print(f'Olá, {nome}, vamos descobrir o seu IMC? ')

altura = eval(input('Informe a sua Altura (por favor utilize pontos e não vírgulas) '))
print(f'Sua altura é {altura}')

peso = eval(input('Informe o seu peso '))
print(f'Seu peso é {peso}')

imc = peso/(altura**2)
print('Seu Índice de Massa Corporal é  %.1f'% imc)


if imc < 17:
    print('Você está com o peso baixo, convém procurar um Nutricionista ')
elif imc < 24:
    print('Você está no peso ideal, segundo especialistas ')
elif imc < 29:
    print('Segundo especialista, você está em sobrepeso ')
elif imc < 34:
    print('Segundo especialista, você está em obesidade moderada ')
elif imc > 39:
    print('Você está com obesidade mórbida, procure imediatamente um médico ')

print('Gostaria de dicas de alimentação saudável? ')
dicas = eval(input('Responda 1 para Sim e 2 para Não '))

if dicas == 1:
    print('Veja estas dicas incríveis de Alimentação Saudável dos especialistas do Hospital Albert Eistein: https://vidasaudavel.einstein.br/alimentacao-equilibrada/')
if dicas == 2:
    print(f'Ah, que pena. Mas você pode enviar o link deste site para o seu amigx ou parente. Que tal {nome}? ')





