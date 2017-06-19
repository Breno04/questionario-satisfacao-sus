total1 = 0
total2 = 0

for i in range(1, 11):
    # resposta: opção marcada pelo usuário
    resposta = int(input('Q{}: '.format(i)))

    if i % 2 == 0:
        # Para os itens 2,4,6,8 e 10, a pontuação será 5 menos a opção marcada na escala
        pontuacao1 = 5 - resposta
        total1 = total1 + pontuacao1
    else:
        # Para os itens 1,3,5,7 e 9, a pontuação será a opção marcada na escala menos 1
        pontuacao2 = resposta - 1
        total2 = total2 + pontuacao2

satisfacao = (total1 + total2) * 2.5
print('Satisfação de {} %'.format(satisfacao))