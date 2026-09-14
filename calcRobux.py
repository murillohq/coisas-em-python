TAXA = 0.07375

print("Calculadora de Robux \nOpções: 'rbx', 'r', 'sair' (ou a senha)")

respostas = {
    "123": "Você descobriu a senha! Opções secretas: (sla/oi/pq vc fez uma calculadora de robux?)",
    "pq vc fez uma calculadora de robux?": "As calculadoras da internet são limitadas; fiz para treinar e ajudar.",
    "sla": "entao decida e volte depois",
    "oi": "tchau"
}

while True:
    op = input("\nEscolha uma opção: ").lower().strip()

    if op == "sair" or op in ["sla", "oi"]:
        print(respostas.get(op, "👋 Encerrando."))
        break
    
    if op == "rbx":
        qtd = float(input("Quantos Robux? "))
        print(f"💰 Custo: R${qtd * TAXA:.2f}")
    
    elif op == "r":
        reais = float(input("Quantos reais? "))
        print(f"🎮 Você recebe: {reais / TAXA:.0f} Robux")
    
    elif op in respostas:
        print(respostas[op])
    
    else:
        print("⚠️ Opção inválida!")
