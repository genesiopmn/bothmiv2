from multiprocessing import freeze_support
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time
import sys
from sys import stdout
# import os
import ctypes

freeze_support()



import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [  [sg.Text('Selecione o modo REAL ou PRACTICE:'), sg.Text(size=(15,1), key='-OUTPUT1-')],
            [sg.Input(key='smode')],
            [sg.Text('Indique o PAR:'), sg.Text(size=(15,1), key='-OUTPUT2-')],
            [sg.Input(key='spar')],
            [sg.Text('Indique o valor da entrada:'), sg.Text(size=(15,1), key='-OUTPUT3-')],
            [sg.Input(key='svalor_entrada')],
            [sg.Button('Enviar'), sg.Button('Sair')]]

window = sg.Window('BotMHI  ', layout)

while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Enviar':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT1-'].update(values['smode'])
        bamode = str(values['smode'])
        window['-OUTPUT2-'].update(values['spar'])
        par = str(values['spar'])
        window['-OUTPUT3-'].update(values['svalor_entrada'])
        valor_entrada = float(values['svalor_entrada'])


window.close()

# Very basic form.  Return values as a list
#form = sg.FlexForm('Bot HMI')  # begin with a blank form
# class TelaPython:
#     def __init__(self):
#         layout = [
#         [sg.Text('Selecione o Modo',size=(5,0)),sg.Input(size=(15,0),key=str('smodo'))],
#         [sg.Text('Insira o PAR',size=(5,0)),sg.Input(size=(15,0),key='spar')],
#         [sg.Text('Insira o Valor da entrada', size=(5, 0)), sg.Input(size=(15, 0), key='svalor')],
#         [sg.Submit('Enviar Dados'), sg.Cancel('Cancelar')]
#          ]
#
#         janela = sg.Window('Dados do usuário').layout(layout)
#         self.button, self.values = janela.Read()



def stop(lucro, gain, loss):
    if lucro <= float('-' + str(abs(loss))):
        print('Stop Loss batido!')
        sys.exit()

    if lucro >= float(abs(gain)):
        print('Stop Gain Batido!')
        sys.exit()


def Martingale(valor, payout):
    lucro_esperado = valor * payout
    perca = float(valor)

    while True:
        if round(valor * payout, 2) > round(abs(perca) + lucro_esperado, 2):
            return round(valor, 2)
            break
        valor += 0.01


def Payout(par):
    API.subscribe_strike_list(par, 1)
    while True:
        d = API.get_digital_current_profit(par, 1)
        if d != False:
            d = round(int(d) / 100, 2)
            break
        time.sleep(1)
    API.unsubscribe_strike_list(par, 1)

    return d


# def banca():
#     return API.get_balance()

def get_bamode():
    return API.get_balance_mode()


def fversao(ver):
    ver = int(ver)
    if ver == int(1):
        ver = int(1)
    if ver == int(2):
        ver = int(2)
    if ver == int(3):
        ver = int(3)
    return ver


print('''
             MHI BOT
 ------------------------------------
''')


def fmperda(novo_saldo, percenloss):
    if novo_saldo > saldohoje:
        mperda = float(novo_saldo / 100 * percenloss)
        meta_perda = float(novo_saldo - mperda)

    else:
        mperda = float(saldohoje / 100 * percenloss)
        meta_perda = float(saldohoje - mperda)
    return meta_perda


def fmganho(saldohoje, percengain):
    mganho = (saldohoje / 100 * percengain)
    meta_ganho = float(saldohoje + mganho)
    return meta_ganho


def alcance_meta(novo_saldo, meta_perda):  # ,meta_ganho):
    while True:
        if novo_saldo >= meta_perda:  # and novo_saldo <= meta_ganho:
            break
        else:
            if novo_saldo < meta_perda:  # novo_saldo > meta_ganho:
                continuar = str(input('Tolerancia de perda batida, recomenda-se parar operação'
                                      ' e tentar em outro PAR'
                                      '\nDeseja continar?\nSIM\nNÃO\n')).upper()

                # time.sleep(5)
                if continuar == '' or continuar is None:
                    continuar = 'NAO'

                if continuar == str('SIM') or continuar == str('S'):
                    print('Continuando')
                    break
                else:
                    print('Fechando BOT')
                    sys.exit()


# senha = input('Insira sua senha: ')
API = IQ_Option('genesiopmn@gmail.com', 'gpmneto210981')
API.connect()

if API.check_connect():
    print(' Conectado com sucesso!')
else:
    print(' Erro ao conectar')
    input('\n\n Aperte enter para sair')
    sys.exit()



# bamode = input(' Indique o modo REAL ou PRACTICE: ').upper()
API.change_balance(bamode)
# par = input(' Indique uma paridade para operar: ').upper()
# valor_entrada = float(input(' Indique um valor para entrar: '))
valor_entrada_b = float(valor_entrada)
ver = int(input("Indique a versão:\n | 1=MHI1\n | 2=MHI2\n | 3=MHI3\n "))
martingale = int(input(' Indique a quantidade de martingales: '))
martingale += 1


stop_loss = float(input(' Indique o valor de Stop Loss: '))
stop_gain = float(input(' Indique o valor de Stop Gain: '))
percengain = float(input(' Indique a meta diaria de ganho percentual: '))
percenloss = float(input(' Indique a percentual de perda tolerado: '))


lucro = 0
versao = ver
operacao_tipo = get_bamode()
payout = Payout(par)
mperda = 0
novo_saldo = API.get_balance()



saldo = novo_saldo
data = datetime.today()
hoje = data.strftime('%d-%m-%Y')
saldohoje = str(saldo)
li = []
# li.append(str(hoje+'\n'))
li.append(str(saldohoje + '\n'))
file = open(f'{hoje}.txt', 'a+'.format(hoje=hoje))
for l in li:
    file.write(l)
file.close()

arquivo = open(f'{hoje}.txt', 'r'.format(hoje=hoje))
arquivo_array = []
linhas = arquivo.readlines()
for linha in linhas:
    arquivo_array.append(linha)
arquivo.close()

for arquivo in arquivo_array:
    # datahoje = arquivo_array[0].replace("\n","")
    saldohoje = float(arquivo_array[0])

meta_perda = fmperda(novo_saldo, percenloss)
meta_ganho = fmganho(saldohoje, percengain)
print('Saldo do dia:', round(saldohoje, 2),
      round(novo_saldo - saldohoje, 2) if novo_saldo > saldohoje or novo_saldo < saldohoje else round(
          saldohoje - novo_saldo, 2))
print('Saldo atual', round(novo_saldo, 2))
print('Limite de Perda:', round(meta_perda, 2), 'ALCANÇADO!!' if novo_saldo < meta_perda else '')
print('Meta Ganho:', round(meta_ganho, 2), 'ALCANÇADO!!' if novo_saldo >= meta_ganho else '')
print('Acima da Meta WIN:', round(novo_saldo - meta_ganho, 2)) if novo_saldo >= meta_ganho else ''
print('Abaixo da Meta LOSS:', round(novo_saldo - meta_perda, 2)) if novo_saldo < meta_perda else ''

ctypes.windll.kernel32.SetConsoleTitleW("MHI-BOT - " + str(par) + " - " + str(payout) + "%" +
                                        " - " + str(operacao_tipo) + " - " + "MHI-" + str(ver) + " - " + "MG" + str(martingale)
                                        + " - " + "Inicial" + str(' R$' + str(saldohoje)) + " - " + "˅" + str(' R$' + str(meta_perda)) + " - " + "˄" + str(' R$' + str(meta_ganho)))
while True:
    minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
    entrar = True if (minutos >= 4.58 and minutos <= 5) or minutos >= 9.58 else False
    # print('Hora de entrar?',entrar,'/ Minutos:',minutos)

    stdout.write(" \r{minutes} Hora de entrar? ".format(minutes=minutos))
    stdout.flush()

    if entrar:

        print('\n\nIniciando operação!')
        if versao == int(1):
            print('imediatamente')
        if ver == int(2):
            print('em 1 minuto')
        if ver == int(3):
            print('em 2 minutos')

        dir = False
        print('Verificando cores..', end='')
        velas = API.get_candles(par, 60, 3, time.time())

        velas[0] = 'g' if velas[0]['open'] < velas[0]['close'] else 'r' if velas[0]['open'] > velas[0]['close'] else 'd'
        velas[1] = 'g' if velas[1]['open'] < velas[1]['close'] else 'r' if velas[1]['open'] > velas[1]['close'] else 'd'
        velas[2] = 'g' if velas[2]['open'] < velas[2]['close'] else 'r' if velas[2]['open'] > velas[2]['close'] else 'd'
        # velas[3] = 'g' if velas[3]['open'] < velas[3]['close'] else 'r' if velas[3]['open'] > velas[3]['close'] else 'd'
        # velas[4] = 'g' if velas[4]['open'] < velas[4]['close'] else 'r' if velas[4]['open'] > velas[4]['close'] else 'd'

        cores = velas[0] + ' ' + velas[1] + ' ' + velas[2]  # + ' ' + velas[3] + ' ' + velas[4]
        print(cores)

        if cores.count('g') > cores.count('r'):
            dir = 'put'
            # if cores.count('g') >= 4:
            #     dir = 'call'
        if cores.count('r') > cores.count('g'):
            dir = 'call'
            # if cores.count('r') >= 4:
            #     dir = 'put'
        if cores.count('d') > 0:
            dir = 'doji'

        if payout < float(0.7):
            print('Retorno baixo: operação inviável', payout)
        else:
            if dir != 'bad_humor':
                if dir != 'doji':
                    valor_entrada = valor_entrada_b
                    print('Direção:', dir)
                    # print('Humor', humor)
                    print('Par:', par)
                    print('Payout', payout, '%', '\n')

                    if novo_saldo < valor_entrada:
                        print('Saldo Insuficiênte')
                    else:
                        if versao == int(1):
                            time.sleep(0)
                        if versao == int(2):
                            time.sleep(58)
                        if versao == int(3):
                            time.sleep(118)

                        for i in range(martingale):
                            status, id = API.buy_digital_spot(par, valor_entrada, dir, 1)
                            if status != 'closed':
                                if status:

                                    while True:
                                        status, valor = API.check_win_digital_v2(id)
                                        if status:
                                            valor = valor if valor > 0 else float('-' + str(abs(valor_entrada)))
                                            lucro += round(valor, 2)

                                            if valor > 0:
                                                print('Resultado operação: ', end='')
                                                print('WIN /', 'Rodada: ', brl(valor), '/',
                                                      'Acumulado: ', brl(lucro))
                                                novo_saldo = API.get_balance()

                                                print('/ ' + str(i) + ' GALE' if i > 0 else '')
                                                # break
                                                meta_perda = fmperda(novo_saldo, percenloss)


                                            else:
                                                print('Resultado operação: ', end='')
                                                print('LOSS /', 'Rodada: ', round(valor, 2), '/',
                                                      'Acumulado: ', round(lucro, 2))
                                                novo_saldo = API.get_balance()
                                                print('/ ' + str(i) + ' GALE' if i > 0 else '')
                                                # status = ''
                                                # break
                                                alcance_meta(novo_saldo, meta_perda)

                                            valor_entrada = Martingale(valor_entrada, payout)
                                            stop(lucro, stop_gain, stop_loss)

                                            print('Saldo do dia:', round(saldohoje, 2), round(novo_saldo - saldohoje,
                                                                                              2) if novo_saldo > saldohoje or novo_saldo < saldohoje else round(
                                                saldohoje - novo_saldo, 2))
                                            print('Saldo atual', round(novo_saldo, 2))
                                            print('Limite Perda:', round(meta_perda, 2),
                                                  'ALCANÇADO!!' if novo_saldo < meta_perda else '')
                                            print('Meta Ganho:', round(meta_ganho, 2),
                                                  'ALCANÇADO!!' if novo_saldo >= meta_ganho else '')
                                            print('Além da Meta:',
                                                  round(novo_saldo - meta_ganho, 2)) if novo_saldo >= meta_ganho else ''
                                            print('Abaixo da Meta:',
                                                  round(novo_saldo - meta_perda, 2)) if novo_saldo < meta_perda else ''

                                            break

                                    if valor > 0:
                                        break
                                else:
                                    print('\n ERRO!! NÃO FAREMOS ENTRADAS\n\n')
                            else:
                                print('\n PAR FECHADO PARA OPERAÇÕES\n\n')

                else:
                    print('\n DOJI ENCONTRADO! SEM OPERAÇÕES\n\n')
            else:
                print('\n HUMOR NÃO COMPATÍVEL\n\n')

    time.sleep(0.5)
# else:
#     sys.exit()

