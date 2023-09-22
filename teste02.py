import pandas as pd

try:
    tabela = pd.read_csv('tabela.csv')
except FileNotFoundError:
    tabela = pd.DataFrame(columns=['Nome', 'Idade', 'Obs', 'OD', 'OE', 'AD'])

continuar = True
while continuar:
    nome = input('Digite o nome do paciente: ')
    idade = input('Digite a idade do paciente: ')
    obs = input('Digite as observações: ')
    od = input('Digite a medida do olho direito: ')
    oe = input('Digite a medida do olho esquerdo: ')
    ad = input('Digite a adição: ')

    nova_linha = [pd.Series({'Nome': nome, 'Idade': idade, 'Obs': obs, 'OD': od, 'OE': oe, 'AD': ad})]
    tabela = pd.concat([tabela, pd.DataFrame(nova_linha)], ignore_index=True)

    print('\nTabela atual:')
    print(tabela)

    opcao = input('\nDeseja adicionar outra linha à tabela? (s/n) ')

    if opcao.lower() == 'n':
        continuar = False

tabela.to_csv('tabela.csv', index=False, sep=',')

print('Programa encerrado.')


# salvamento da tabela em csv