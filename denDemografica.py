def populacao_relativa(populacao, area):
    if area <= 0:
        raise ValueError("A área deve ser maior que zero.")
    if populacao < 0:
        raise ValueError("A população não pode ser negativa.")
    
    return populacao / area

habBra = 211700000
areBra = 8500000

habGoi = 7056495
areGoi = 340203

habJat = 105729
areJat = 7174

resultado1 = populacao_relativa(habBra, areBra)
resultado2 = populacao_relativa(habGoi, areGoi)
resultado3 = populacao_relativa(habJat, areJat)

print(f"Brasil: {resultado1:.2f} hab/km²")
print(f"Goiás:  {resultado2:.2f} hab/km²")
print(f"Jataí:  {resultado3:.2f} hab/km²")