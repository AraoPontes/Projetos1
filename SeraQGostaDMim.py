nome = input('Olá! É um prazer ter você aqui. Imagino que você queira saber se ele ou ela gosta de você, não é? Então vamos começar! Me diga seu nome ')
print(f'Legal, {nome}, agora vamos responder algumas perguntas para nossa inteligência artificial calcular e te dizer se ele ou ela gosta de você!')
resp = eval(input('Para todas as perguntas escreva 1 para respostas NEGATIVAS e 2 para respostas POSITIVAS, ok? (1 para NÃO e 2 para SIM) '))
if resp == 2:
    print(f'Então vamos começar, {nome}')
elif resp == 1:
    print(f'Tem algo que você não entendeu, {nome}? ')
print('Como você se sente agora? ')
resp = eval(input('Responda 2 para Bem e 1 para Mal '))
print('Como você se sente hoje em relação a pessoa que você gosta? ')
resp2 = eval(input('Responda 2 para Com Saudade e 1 Não estou com Saudade '))
resp2 = resp2 + resp
print('Ele te mandou mensagem no WhatsApp hoje? ')
resp3 = eval(input('2 para SIM e 1 para NÃO :( '))
if resp3 == 1:
    print(f'Ele não tem mandou mensagem hoje? Que tal você mandar, {nome}? Mas antes vamos continuar o seu teste! ')
resp3 = resp3 + resp2
print(f'Essa pergunta é bem importante, ein, {nome}!')
print(f'{nome}, há quanto tempo você não vê a pessoa que você gosta? ')
resp4 = eval(input('Responda 2 para menos de 3 dias e 1 para mais de 3 dias '))
if resp4 == 2:
    resp4 = resp3 + 3
    print(f'Parece pouco tempo. Isso aí, {nome}')
elif resp4 == 1:
    resp = resp3 - 3
    print(f'Poxa, já faz algum tempo que vocês não se falam, não acha {nome}? ')
resp4 = resp4 + resp3
print(f'Agora, {nome}, você tem que responder com sinceridade, ta bom?')
print('Você pensa em outras pessoas as vezes?')
resp5 = eval(input('Responda 2 para SIM e 1 para NÃO '))
if resp5 == 1:
    print(f'A fidelidade é tudo, {nome}! Continue assim! ')
if resp5 == 2:
    print(f'As vezes não dá pra segurar, né {nome}? ')
resp5 = resp5 + resp4
print('A proxima pergunta é decisiva, ein?: ')
print('Numa escala de 0 a 5, quanto você pensa na pessoa que gosta? ')
resp6 = eval(input('Digite um número de 0 a 5'))
resp6 = resp6 + resp5
if resp6 < 3:
    print(f'Talvez seja cedo demais pra você pensar em algo com essa pessoa. Experimente perguntar o nome dela')
elif resp6 <= 4:
    print(f'{nome}, Talvez você ainda precise saber se vale a pena pensar tanto nessa pessoa. Deixe a corrente te levar" ')
elif resp6 <= 9:
    print(f'Você e a pessoa que você gosta ainda precisam se conhecer mais, para que você possa ter mais pistas do que ele ou ela sente. Vocês ainda não estão conectados ')
elif resp6 <= 14:
    print(f'{nome}, você e a pessoa que se gostam ainda tem um caminho pela frente no que diz respeito ao sentimento mais profundo, mas não desista e tenha paciência ')
elif resp6 <= 18:
    print(f'{nome}, vocês estão numa fase boa de se conhecer, continue investindo nesse sentimento! ')
elif resp6 <= 21:
    print(f'Uau! Vocês tem uma forte conexão e não podem ficar sem se falar por muito tempo. Isso é sinal de namoro, ein, {nome}? ')

