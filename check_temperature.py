def sensacao_termica(temperatura):
    if temperatura < 7:
        return 'Congelando!'
    elif temperatura < 10:
        return 'Frio'
    elif temperatura < 26:
        return 'Ótimo'
    else:
        return 'Muito quente!'
    
temperatura_atual = float(input('Qual a temperatura atual? '))

print('Sensação térmica atual está:',sensacao_termica(temperatura_atual))