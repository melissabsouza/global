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