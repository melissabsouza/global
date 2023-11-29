def atividade_fisica():
    atividade_fisica = input("Você faz atividade Fisica?\n 1 - Sim \n 2 - Não\n"
                             + "Resposta: ")
    print("\n")

    if atividade_fisica == '1':
        modo = input("A -Pouco ativo – exercício/esporte leve 1-3 dias/semana\n"
                     + "B - Moderadamente ativo – exercício/esporte moderado 3-5 dias/semana\n"
                     + "C - Muito ativo – exercício/esporte pesado 6-7 dias/semana\n"
                     + "D - Extremamente ativo – exercício/esporte muito pesado e trabalho físico intenso diariamente ou treino de 2x ao dia\n"
                     + " "
                     + "Digite a letra correspondente: ")
        print("\n")
        modo = modo.upper()

        match modo:
            case 'A':
                if sexo == '1':
                    pouco_ativo = tmb_fem * 1.375
                if sexo == '2':
                    pouco_ativo = tmb_masc * 1.375
                print(f"Você deve ingerir {pouco_ativo} para manter o peso!")
                

                return pouco_ativo
            case 'B':
                if sexo == '1':
                    moderadamente_ativo = tmb_fem * 1.55
                
                if sexo == '2':
                    moderadamente_ativo = tmb_masc * 1.55

                print(f"Você deve ingerir {moderadamente_ativo:.2f} para manter o peso!")
                
                return moderadamente_ativo
            case 'C':
                if sexo == '1':
                    muito_ativo = tmb_fem * 1.725
                if sexo == '2':
                    muito_ativo = tmb_masc * 1.72

                print(f"Você deve ingerir {muito_ativo:.2f} para manter o peso!")
                

                return muito_ativo
            case 'D':
                if sexo == '1':
                    extremamente_ativo = tmb_fem * 1.9
                if sexo == '2':
                    extremamente_ativo = tmb_masc * 1.9

                print(f"Você deve ingerir {extremamente_ativo:.2f} para manter o peso!")
                

                return extremamente_ativo
            
    elif atividade_fisica == '2':
        if sexo == '1':
            sedentario = tmb_fem * 1.2

        if sexo == '2':
            sedentario = tmb_masc * 1.2
        
        print(f"Você deve ingerir {sedentario:.2f} para manter o peso!")
        return sedentario
    else:
        print('Opção invalida')
        


while True:
    print("============= Veja sua estimativa de gasto médio de calorias e estimar suas necessidades para o funcionamento do seu corpo! =============")
    print("\n")

    idade = int(input("Qual sua idade? "))
    peso = float(input("Qual seu peso? Digite em Quilogramas. "))
    altura = int(input("Qual sua altura? Digite em Centimetros. "))
    print("\n")
    sexo = input("Digite a opção correspondente a seu sexo\n 1 - Feminino \n 2 - Masculino\n"
                 + "Resposta: ")
    print("\n")
    tmb_fem = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    tmb_masc = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    match sexo:
        case '1':
            atividade_fisica()
            print("\n")
        case '2':
            atividade_fisica()
            print("\n")
        case _:
            print("Inválido")
            print("\n")

    print("Se quiser saber mais, agende uma consulta!")
    sair = input("Você deseja sair?\n 1 - Sim\n 2 - Não\n"
                 + "Resposta: ")
    
    if sair == '1':
        print("Tchau!")
        break
        
    elif sair == '2':
        continue
    else:
        print("Opção inválida")
