while True:
    try:
        entrada = input("Digite seu nome, idade e cidade (separados por espaço): ").split()
        
        if len(entrada) != 3:
            raise ValueError("Quantidade errada de informações")
            
        nome, idade, cidade = entrada
        
        print(f"\nSucesso! Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
        break 
        
    except ValueError:
        print("⚠️ Erro: Provavelmente falta informaçoes, tente novamente.\n")
