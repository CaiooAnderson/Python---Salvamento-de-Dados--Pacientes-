import pandas as pd
from datetime import datetime
import pytz

fuso_horario = pytz.timezone('America/Sao_Paulo')

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

  data_hora = datetime.now(fuso_horario).strftime('%d-%m-%Y %H:%M')

  nova_linha = {
    'Nome': nome,
    'Idade': idade,
    'Obs': obs,
    'OD': od,
    'OE': oe,
    'AD': ad
  }
  nova_linha_df = pd.DataFrame([nova_linha], columns=tabela.columns)
  tabela = pd.concat([tabela, nova_linha_df], ignore_index=True)
  print('\nTabela atual:')
  print(tabela)

  opcao = input('\nDeseja adicionar outra linha à tabela? (s/n) ')

  if opcao.lower() == 'n':
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

# salvamento da tabela em txt