import pandas as pd
from datetime import datetime
import pytz
import os

fuso_horario = pytz.timezone('America/Sao_Paulo')
data_hora = datetime.now(fuso_horario).strftime('%d-%m-%Y %H:%M')
if not os.path.exists('dados'):
    os.makedirs('dados')

tabela_path = os.path.join('dados', 'tabela.csv')
if os.path.exists(tabela_path):
    tabela = pd.read_csv(tabela_path)
else:
    tabela = pd.DataFrame(columns=['Nome', 'Idade', 'Obs', 'OD', 'OE', 'AD'])
    tabela.to_csv(tabela_path, index=False)

continuar = True

menu = input('\nO que deseja fazer?\n(a) Adicionar outra linha à tabela\n(b) Editar uma linha existente\n(c) Remover uma linha existente\n(s) Sair\n')
def editar_linha():
    index = input('Digite o índice da linha a ser editada: ')
    while not index.isdigit():
        print('Entrada inválida. É do 0 para cima!')
        index = input('Digite o índice da linha a ser editada: ')
    index = int(index)
    linha = tabela.iloc[index]
    nome = input(f'Digite o novo nome do paciente ({linha["Nome"]}): ') or linha['Nome']
    idade = input(f'Digite a nova idade do paciente ({linha["Idade"]}): ') or linha['Idade']
    obs = input(f'Digite as novas observações ({linha["Obs"]}): ') or linha['Obs']
    od = input(f'Digite a nova medida do olho direito ({linha["OD"]}): ') or linha['OD']
    oe = input(f'Digite a nova medida do olho esquerdo ({linha["OE"]}): ') or linha['OE']
    ad = input(f'Digite a nova adição ({linha["AD"]}): ') or linha['AD']
    tabela.iloc[index] = [nome, idade, obs, od, oe, ad]
    print('\nTabela atual:')
    print(tabela)
    menu()

def adicionar_linha():
    global tabela  
    nome = input('Digite o nome do paciente: ')
    idade = input('Digite a idade do paciente: ')
    obs = input('Digite as observações: ')
    od = input('Digite a medida do olho direito: ')
    oe = input('Digite a medida do olho esquerdo: ')
    ad = input('Digite a adição: ')
    
    nova_linha = {'Nome': nome, 'Idade': idade, 'Obs': obs, 'OD': od, 'OE': oe, 'AD': ad}
    nova_linha_df = pd.DataFrame([nova_linha], columns=tabela.columns)
    tabela = pd.concat([tabela, nova_linha_df], ignore_index=True)
    print('\nTabela atual:')
    print(tabela)
    print(menu)
    return
    
def remover_linha():
    global tabela
    index = int(input('Digite o índice da linha a ser removida: '))
    while not index.int():
        print('Entrada inválida. É do 0 para cima!')
        index = input('Digite o índice da linha a ser editada: ')
    tabela.drop(index, inplace=True)
    print('\nTabela atual:')
    print(tabela)
    return
    
    if menu.lower() == 'a':
        adicionar_linha()
    elif menu.lower() == 'b':
        editar_linha()
    elif menu.lower() == 'c':
        remover_linha()
    elif menu.lower() == 's':
        return

while continuar:
    nome = input('Digite o nome do paciente: ')
    idade = input('Digite a idade do paciente: ')
    obs = input('Digite as observações: ')
    od = input('Digite a medida do olho direito: ')
    oe = input('Digite a medida do olho esquerdo: ')
    ad = input('Digite a adição: ')
    data_hora = datetime.now(fuso_horario).strftime('%d-%m-%Y %H:%M')
    nova_linha = {'Nome': nome, 'Idade': idade, 'Obs': obs, 'OD': od, 'OE': oe, 'AD': ad}
    nova_linha_df = pd.DataFrame([nova_linha], columns=tabela.columns)
    tabela = pd.concat([tabela, nova_linha_df], ignore_index=True)
    print('\nTabela atual:')
    print(tabela)
    print(menu)

while continuar:
    if menu.lower() == 'a':
      continuar = True
    elif menu.lower() == 'b':
        editar_linha()
    elif menu.lower() == 'c':
        remover_linha()
    elif menu.lower() == 's':
        continuar = False

with open(f"tabela_{data_hora}.txt", 'w') as arquivo:
  for index, linha in tabela.iterrows():
    str_linha = f"Data/Hora: {data_hora}\n" \
                f"Nome: {linha['Nome']}\n" \
                f"Idade: {linha['Idade']}\n" \
                f"Obs: {linha['Obs']}\n" \
                f"OD: {str(linha['OD']).ljust(15)}" \
                f"OE: {str(linha['OE']).ljust(15)}" \
                f"AD: {str(linha['AD']).ljust(15)}\n\n"
    arquivo.write(str_linha)
print('Programa encerrado.')


# dando erro, nem me pergunte o erro porque eu já tinha ido logo para outro teste :D
# este aqui no caso seria de salvamento em csv e txt, porém sem finalização.