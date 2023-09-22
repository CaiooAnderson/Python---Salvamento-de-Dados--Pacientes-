import pandas as pd
from datetime import datetime
import pytz
import os

fuso_horario = pytz.timezone('America/Sao_Paulo')
data = datetime.now(fuso_horario).strftime('%d-%m-%Y')
agora = datetime.now(fuso_horario).strftime('%H:%M')
if not os.path.exists('dados'):
  os.makedirs('dados')

tabela_path = os.path.join('dados', 'pacientes.csv')
if os.path.exists(tabela_path):
  tabela = pd.read_csv(tabela_path)
else:
  tabela = pd.DataFrame(columns=['Nome', 'Idade', 'Obs', 'OD', 'OE', 'AD'])
  tabela.to_csv(tabela_path, index=False)

fuso = pytz.timezone('America/Sao_Paulo')
def bom_dia():
  agora = datetime.now(fuso).time()  
  if agora >= datetime.strptime('05:00', '%H:%M').time() and agora < datetime.strptime('12:00', '%H:%M').time():
    print("\nBom dia!")
  elif agora >= datetime.strptime('12:00', '%H:%M').time() and agora < datetime.strptime('18:00', '%H:%M').time():
    print("\nBoa tarde!")
  else:
    print("\nBoa noite!")


continuar = True
while True:
    bom_dia()
    nome = input("\nCom quem eu irei trabalhar hoje? (Caio/Kylo)\n ").lower()
    if nome == 'caio':
        print("\n\nCaio! Que bom estar com você novamente!\n")
        print("Vamos ao trabalho?")
        break
    elif nome == 'kylo':
        print("\n\nQue bom revê-lo, mestre. O império estava a espera de suas ordens!")
        break
    else:
        print("\nDesculpe, não reconheci o seu nome! Tente novamente.\n\n")
    
    

continuar = True
while continuar:
  menu = input(
    '\nO que deseja fazer?\n\n(1) Adicionar um novo paciente à tabela\n\n')
  if menu == '1':
    continuar = True
    break
  else:
    print('\nOpção inválida. Tente novamente!')


def editar_linha():
  global tabela
  if len(tabela) == 0:
    print('\nNão há linhas na tabela para editar!')
    main_menu()

  index = input('\nDigite o índice da linha a ser editada: ')
  while not index.isdigit() or int(index) >= len(tabela):
    print(
      f'\nEntrada inválida. O índice deve estar entre 0 e {len(tabela)-1}.\n')
    index = input('Digite o índice da linha a ser editada: ')
  index = int(index)
  linha = tabela.iloc[index]
  nome = input(
    f'\nDigite o novo nome do paciente ({linha["Nome"]}): ') or linha['Nome']
  idade = input(
    f'Digite a nova idade do paciente ({linha["Idade"]}): ') or linha['Idade']
  obs = input(
    f'Digite as novas observações ({linha["Obs"]}): ') or linha['Obs']
  od = input(
    f'Digite a nova medida do olho direito ({linha["OD"]}): ') or linha['OD']
  oe = input(
    f'Digite a nova medida do olho esquerdo ({linha["OE"]}): ') or linha['OE']
  ad = input(f'Digite a nova adição ({linha["AD"]}): ') or linha['AD']
  tabela.iloc[index] = [nome, idade, obs, od, oe, ad]
  print(f"\nO(a) paciente {nome} foi atualizado(a)!\n")
  print('\nTabela atual:')
  print(tabela)
  main_menu()


def adicionar_linha():
  global tabela
  nome = input('\nDigite o nome do paciente: ')
  idade = input('Digite a idade do paciente: ')
  obs = input('Digite as observações do paciente: ')
  od = input('Digite a medida do olho direito: ')
  oe = input('Digite a medida do olho esquerdo: ')
  ad = input('Digite a adição: ')

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
  main_menu()


continuar = True
def remover_linha():
  if len(tabela) == 0:
    print('\nNão há pacientes nesta tabela para remover!')
    main_menu()
    print(tabela)
 
  index = input('\nDigite o índice da linha a ser removida: ')
  while not index.isdigit() or int(index) >= len(tabela):
    print(
      f'\nEntrada inválida. O índice deve estar entre 0 e {len(tabela)-1}.\n')
    index = input('Digite o índice da linha para ser removida: ')
  index = int(index)
  indice_maximo = len(tabela) - 1
  for i in range(index, indice_maximo):
    tabela.iloc[i] = tabela.iloc[i + 1]
  nome = tabela.iloc[index] = ['Nome']
  tabela.drop(indice_maximo, inplace=True)
  print(f"\nO(a) paciente {nome} foi removido(a) da tabela!\n")
  if tabela.empty:
    print("A tabela está vazia!")
    main_menu()
  else:
    print("Tabela atual:")
    print(tabela)

  while continuar:
    escolha = input('\nDeseja remover outro paciente? (s/n)\n')
    if escolha.lower() == 's':
      remover_linha()
      return
    elif escolha.lower() == 'n':
      print(tabela)
      main_menu()
    else:
      print('Opção inválida! Por favor, digite s para sim ou n para não.')


def main_menu():
  while continuar:
    menu = input(
      '\nO que deseja fazer?\n(1) Adicionar outro paciente à tabela\n(2) Editar informações de um paciente existente\n(3) Remover um paciente existente\n(4) Sair\n\n'
    )
    if menu.lower() == '1':
      adicionar_linha()
    elif menu.lower() == '2':
      if tabela.empty:
        print("\nNão há linhas na tabela para editar!")
        main_menu()
      else:
        print("\nTabela atual:")
        print(tabela)
        editar_linha()
    elif menu.lower() == '3':
      if tabela.empty:
        print("\nNão há pacientes nesta tabela para remover!")
        main_menu()
      else:
        print("\nTabela atual:")
        print(tabela)
        remover_linha()
    elif menu.lower() == '4':
      print("\nSalvando...")
      break
    else:
      print("\nOpção inválida, tente novamente!")
      main_menu()
continuar = True
while continuar:
  nome = input('\nDigite o nome do paciente: ')
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
  main_menu()
continuar = True
while continuar:
  menu = input("Digite a opção desejada: ")
  if menu.lower() == '4':
    print("Salvando...")
    continuar = False
  elif menu.lower() == '2':
    editar_linha()
  elif menu.lower() == '3':
    remover_linha()
  elif menu.lower() == '1':
    adicionar_linha()

caminho_arquivo = os.path.join(os.getcwd(), "documentos",
                               f"tabela_{data}.txt")

with open(caminho_arquivo, 'w') as arquivo:
  for index, linha in tabela.iterrows():
    str_linha = f"Data: {data}\n" \
                f"Nome: {linha['Nome']}\n" \
                f"Idade: {linha['Idade']}\n" \
                f"Obs: {linha['Obs']}\n" \
                f"OD: {str(linha['OD']).ljust(15)}" \
                f"OE: {str(linha['OE']).ljust(15)}" \
                f"AD: {str(linha['AD']).ljust(15)}\n\n"
    arquivo.write(str_linha)
  continuar = input("Deseja continuar? (s/n): ").lower() == "s"
print('Programa encerrado.')




# PROBLEMAS:
# ao tentar sair ele faz a pergunta de saída se eu desejo remover outro.
# salvamento em csv e txt