import csv, time
from prettytable import PrettyTable

def main():
    print("Baseado no capítulo 1 do livro Matemática para Vencer por Laercio Vasconcelos")
    print('Tente resolver os problemas de adição dentro de 1 minuto. Digite "sair" para encerrar\n')
    with open('adicao.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        time_start = time.time()
        for row in reader:
            exit = False
            for count, value in enumerate(row):
                if '+' in value:                
                    if exit: break;
                    while (True):
                        result = input(f"{value} = ")
                        if result == 'sair':
                            print("\nSaindo do programa\n")
                            exit = True
                            break
                        elif result == row[count + 1]:
                            print("Muito bem!")
                            break
                        else:
                            print("Resposta errada")

        
        time_end = time.time()
        tempo = (time_end - time_start) / 60
        print("Você terminou a tabela em {:4.2f} minutos".format(tempo))
        
        
    table = PrettyTable(["Tempo", "Classificação"])
    tabela_adicao = [["Menos de 1 minuto", "Ótimo"], ["De 1 a 2 minutos", "Bom"], ["De 2 a 3 minutos", "Mais ou menos"],  ["De 3 a 4 minutos", "Fraco"],  ["Acima de 4 minutos", "Tá frito"]]
    for i in tabela_adicao:
        table.add_row(i)

    print(table)

    input("\nPressione qualquer tecla para continuar...")

if __name__ == '__main__':
    main()