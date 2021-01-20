"""
    BOT MHI v1
    - Analise em 1 minuto
    - Entradas para 1 minuto
    - Calcular as cores das velas de cada quadrado, ultimas 3 velas, minutos: 2, 3 e 4 / 7, 8 e 9
    - Entrar contra a maioria


"""
# -*- coding utf-8 -*-

from getpass import getpass

import locale
locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')
brl = locale.currency
# print(brl)

from multiprocessing import freeze_support
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time
import sys
from sys import stdout
# import os
import ctypes

freeze_support()

global saldohoje,novo_saldo,meta_perda,percenloss,meta_ganho,percengain,desligameta,ver,bamode,lucro,sensibilidade


def stop(lucro, gain, loss):
    if lucro <= float('-' + str(abs(loss))):
        print('Stop Loss batido!')
        sys.exit()

    if lucro >= float(abs(gain)):
        print('Stop Gain Batido!')
        sys.exit()


def entradas(par, valor_entrada, dir, timeframe):
    status, id = API.buy_digital_spot(par, valor_entrada, dir, timeframe)

    if status:
        while True:
            status, lucro = API.check_win_digital_v2(id)

            if status:
                if lucro > 0:
                    return 'win', round(lucro, 2)
                else:
                    return 'loss', 0
                # break


def entradas(par, entrada, direcao, timeframe):
    status, id = API.buy_digital_spot(par, entrada, direcao, timeframe)

    if status:
        while True:
            status, lucro = API.check_win_digital_v2(id)

            if status:
                if lucro > 0:
                    return 'win', round(lucro, 2)
                else:
                    return 'loss', 0
                # break


def sorosgale(perca):
    lucro_total = 0
    nivel = 2
    mao = 1
    lucro = 0
    print('\n Perca total:', perca, ' - entrada inicial:', (perca / 2))

    while True:

        resultado, lucro = entradas(par, (perca / 2) + lucro, direcao, 1)

        if resultado == 'win':
            lucro_total += lucro
            print('\n', nivel, '-', mao, '| ', resultado, '- lucro:', lucro, '- perca:', perca)
            mao += 1
        else:
            lucro_total = 0
            mao = 1
            perca += perca / 2
            print('\n', nivel, '-', mao, '| ', resultado, '- lucro:', lucro, '- perca:', perca)
            nivel += 1

        if lucro_total >= perca:
            print('FIM\n', nivel, '-', mao, '|', perca, ' -> ', lucro_total)
            break
        else:
            print('perca atual:', perca, 'lucro:', lucro)
            entradas(par, entrada, direcao, timeframe)

def Martingale(valor, payout):
    lucro_esperado = valor * payout
    perca = float(valor)

    while True:
        if round(valor * payout, 2) > round(abs(perca) + lucro_esperado, 2):
            return round(valor, 2)
            # break
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


dirdoji = int(0)
red = int(0)
green = int(0)
tdir = ''
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')


def buscadoji(dirdoji,green,red,tdir):
    velas1 = API.get_candles(par, 60, 20, time.time())

    velas1[0] = 'g' if velas1[0]['open'] < velas1[0]['close'] else 'r' if velas1[0]['open'] > velas1[0]['close'] else 'd'
    velas1[1] = 'g' if velas1[1]['open'] < velas1[1]['close'] else 'r' if velas1[1]['open'] > velas1[1]['close'] else 'd'
    velas1[2] = 'g' if velas1[2]['open'] < velas1[2]['close'] else 'r' if velas1[2]['open'] > velas1[2]['close'] else 'd'
    velas1[3] = 'g' if velas1[3]['open'] < velas1[3]['close'] else 'r' if velas1[3]['open'] > velas1[3]['close'] else 'd'
    velas1[4] = 'g' if velas1[4]['open'] < velas1[4]['close'] else 'r' if velas1[4]['open'] > velas1[4]['close'] else 'd'
    velas1[5] = 'g' if velas1[5]['open'] < velas1[5]['close'] else 'r' if velas1[5]['open'] > velas1[5]['close'] else 'd'
    velas1[6] = 'g' if velas1[6]['open'] < velas1[6]['close'] else 'r' if velas1[6]['open'] > velas1[6]['close'] else 'd'
    velas1[7] = 'g' if velas1[7]['open'] < velas1[7]['close'] else 'r' if velas1[7]['open'] > velas1[7]['close'] else 'd'
    velas1[8] = 'g' if velas1[8]['open'] < velas1[8]['close'] else 'r' if velas1[8]['open'] > velas1[8]['close'] else 'd'
    velas1[9] = 'g' if velas1[9]['open'] < velas1[9]['close'] else 'r' if velas1[9]['open'] > velas1[9]['close'] else 'd'
    velas1[10] ='g' if velas1[10]['open'] < velas1[10]['close'] else 'r' if velas1[10]['open'] > velas1[10]['close'] else 'd'
    velas1[11] ='g' if velas1[11]['open'] < velas1[11]['close'] else 'r' if velas1[11]['open'] > velas1[11]['close'] else 'd'
    velas1[12] ='g' if velas1[12]['open'] < velas1[12]['close'] else 'r' if velas1[12]['open'] > velas1[12]['close'] else 'd'
    velas1[13] ='g' if velas1[13]['open'] < velas1[13]['close'] else 'r' if velas1[13]['open'] > velas1[13]['close'] else 'd'
    velas1[14] ='g' if velas1[14]['open'] < velas1[14]['close'] else 'r' if velas1[14]['open'] > velas1[14]['close'] else 'd'
    velas1[15] ='g' if velas1[15]['open'] < velas1[15]['close'] else 'r' if velas1[15]['open'] > velas1[15]['close'] else 'd'
    velas1[16] ='g' if velas1[16]['open'] < velas1[16]['close'] else 'r' if velas1[16]['open'] > velas1[16]['close'] else 'd'
    velas1[17] ='g' if velas1[17]['open'] < velas1[17]['close'] else 'r' if velas1[17]['open'] > velas1[17]['close'] else 'd'
    velas1[18] ='g' if velas1[18]['open'] < velas1[18]['close'] else 'r' if velas1[18]['open'] > velas1[18]['close'] else 'd'
    velas1[19] ='g' if velas1[19]['open'] < velas1[19]['close'] else 'r' if velas1[19]['open'] > velas1[19]['close'] else 'd'

    # coresdoji = velas1[0] + ' ' + velas1[1] + ' ' + velas1[2] + ' ' + velas1[3] + ' ' + velas1[4] + ' ' + velas1[5] + ' ' + velas1[6] + ' ' + velas1[7] + ' ' + velas1[8] + ' ' + velas1[9] + ' ' + velas1[10] + ' ' + velas1[11] + ' ' + velas1[12] + ' ' + velas1[13] + ' ' + velas1[14] + ' ' + velas1[15] + ' ' + velas1[16] + ' ' + velas1[17] + ' ' + velas1[18] + ' ' + velas1[19]


    velas_array = []
    for i in velas1:
        velas_array.append(i)

    top0005 = velas_array[0:5]
    rtop0005 = top0005.count('r')
    gtop0005 = top0005.count('g')

    top0510 = velas_array[5:10]
    rtop0510 = top0510.count('r')
    gtop0510 = top0510.count('g')

    top1015 = velas_array[10:15]
    rtop1015 = top1015.count('r')
    gtop1015 = top1015.count('g')

    top1520 = velas_array[15:20]
    rtop1520 = top1520.count('r')
    gtop1520 = top1520.count('g')


    ############################################

    gtop0010 = gtop0005 + gtop0510
    rtop0010 = rtop0005 + rtop0510

    gtop1020 = gtop1015 + gtop1520
    rtop1020 = rtop1015 + rtop1520

    dtop1020 = velas_array[10:20]
    dtop1020 = dtop1020.count('d')
    dirdoji = dtop1020

    g = int(gtop0010+gtop1020)
    r = int(rtop0010+rtop1020)
    time.sleep(0.2)
    print('\nGreen:', g, 'Red:', r, 'Doji:', dirdoji)

    red = r
    green = g

    # v20 = velas_array[19:20]
    # v19 = velas_array[18:19]
    # v18 = velas_array[17:18]

    if sensibilidade == int(2):
        if (rtop0010 >= int(6) and rtop0010 <= int(10)) and (gtop1020 >= int(6) and gtop1020 <= int(10)):
            print('\n\nTendencia de Baixa ˅')
            tdir = 'put'
        elif (gtop0010 >= int(6) and gtop0010 <= int(10)) and (rtop1020 >= int(6) and rtop1020 <= int(10)):
            print('\n\nTendencia de Alta ˄')
            tdir = 'call'
        else:
            tdir = 'notrend'
            print('\nTendencia indefinida')
        time.sleep(1)
    if sensibilidade == int(1):
        if (rtop0010 >= int(7) and rtop0010 <= int(10)) and (gtop1020 >= int(7) and gtop1020 <= int(10)):
            print('\n\nTendencia de Baixa ˅')
            tdir = 'put'
        elif (gtop0010 >= int(7) and gtop0010 <= int(10)) and (rtop1020 >= int(7) and rtop1020 <= int(10)):
            print('\n\nTendencia de Alta ˄')
            tdir = 'call'
        else:
            tdir = 'notrend'
            print('\nTendencia indefinida')
        time.sleep(1)
    return (dirdoji,green,red,tdir)






print('''
             MHI BOT
 ------------------------------------
''')
def fmetaperda(percenloss):
    while percenloss >0:

        for i in range(percenloss, 0, -1):
            i -=5
            percenloss = i
            break
        return percenloss

def fmperda(lucro,percenloss):
    if lucro >= 0:
        mperda = round(lucro / 100 * percenloss,2)
        meta_perda = round(lucro - mperda,2)

    # else:
    #     mperda = round(saldohoje / 100 * percenloss,2)
    #     meta_perda = round(saldohoje - mperda,2)
        return meta_perda

def fmganho(saldohoje,percengain):
    mganho = round(saldohoje / 100 * percengain,2)
    meta_ganho = round(saldohoje + mganho,2)
    return meta_ganho



def alcance_meta(lucro,meta_perda,meta_ganho,desligameta):
    # continuar = ''
    while True:

        if lucro >= meta_perda and lucro <= meta_ganho:
            desligameta = 'NAO'
            return desligameta
            # break
        else:
            if lucro < meta_perda and desligameta == 'NAO':
                desligameta = str(input('\nTolerancia de perda batida, recomenda-se parar operação'
                                      ' e tentar em outro PAR'
                                      '\nDeseja continar?\nSIM\nNÃO\n')).upper()
            if lucro > meta_ganho and desligameta == 'NAO':
                desligameta = str(input('\nMeta de ganho batida, recomenda-se parar operação'
                                      ' e tentar em outro PAR'
                                      '\nDeseja continar?\nSIM\nNÃO\n')).upper()
                if desligameta == str('SIM') or desligameta == str('S'):
                    print('Continuando desligando meta perda')
                    desligameta = str('SIM')
                if desligameta != str('SIM') and desligameta != str('S'):
                    print('Fechando BOT')
                    sys.exit()
            return desligameta



# email = str(input('digite email'))
# senha = getpass()
# API = IQ_Option('tgll2002@yahoo.com.br', senha)
API = IQ_Option('genesiopmn@gmail.com', 'gpmneto210981')
# API = IQ_Option(email, senha)

API.connect()

if API.check_connect():
    print(' Conectado com sucesso!')
else:
    print(' Erro ao conectar')
    input('\n\n Aperte enter para sair')
    sys.exit()

bamode = str('PRACTICE')#str(input(' Indique o modo REAL ou PRACTICE: ')).upper()
API.change_balance(bamode)
novo_saldo = API.get_balance()
par = str('GBPJPY')#input(' Indique uma paridade para operar: ').upper()
valor_entrada = float(100)#float(input(' Indique um valor para entrar: '))
valor_entrada_b = float(valor_entrada)
ver = int(1)#int(input("Indique a versão:\n | 1=MHI1\n | 2=MHI2\n | 3=MHI3\n "))
martingale = int(0) # = int(input(' Indique a quantidade de martingales: '))
martingale += 1
stop_loss = float(1000)#float(input(' Indique o valor de Stop Loss: '))
stop_gain = float(1000)#float(input(' Indique o valor de Stop Gain: '))
percengain = int(30)#int(input(' Indique a meta diaria de ganho percentual: '))
percenloss = int(100)#int(input(' Indique a percentual de perda tolerado:'))
sensibilidade = int(2)#int(input("Escolha a sensibilidade da regra: \n1=MAIS - MAIS PRECISAO\n2=MENOS - MENOS PRECISAO \n"))
desligameta = str('NAO')


saldo = API.get_balance()
data = datetime.today()
hoje = data.strftime('%d-%m-%Y')
saldohoje = str(saldo)
li = []
#li.append(str(hoje+'\n'))
li.append(str(saldohoje+'\n'))
if bamode == 'REAL':
    file = open(f'{hoje}_real.txt', 'a+'.format(hoje=hoje))
else:
    file = open(f'{hoje}_practice.txt', 'a+'.format(hoje=hoje))
for l in li:
    file.write(l)
file.close()


if bamode == 'PRACTICE':
    arquivo = open(f'{hoje}_practice.txt', 'r'.format(hoje=hoje))
else:
    arquivo = open(f'{hoje}_real.txt', 'r'.format(hoje=hoje))
arquivo_array = []
linhas = arquivo.readlines()
for linha in linhas:
    arquivo_array.append(linha)
arquivo.close()

for arquivo in arquivo_array:
    #datahoje = arquivo_array[0].replace("\n","")
    saldohoje = float(arquivo_array[0])


meta_perda = float(0)
meta_ganho = fmganho(saldohoje,percengain)

def informe(desligameta):
    novo_saldo = API.get_balance()
    if lucro ==0: #meta_perda and lucro <= meta_ganho and desligameta == 'NAO':
        alcance_meta(lucro, meta_perda, meta_ganho, desligameta)
    balanco = novo_saldo - saldohoje
    print('Saldo do dia:', brl(saldohoje), ("| Balanço:"), brl(balanco) if novo_saldo > saldohoje or novo_saldo < saldohoje else '-')
    # print('Saldo Atual:', round(novo_saldo, 2))
    if desligameta == 'NAO' and novo_saldo > meta_perda:
        print('Limite perda:', brl(meta_perda),("- {percenloss}{perc}".format(percenloss=percenloss, perc='%')))
    elif desligameta == 'NAO' and novo_saldo < meta_perda:
        print('Limite perda:', brl(meta_perda),("- {percenloss}{perc}".format(percenloss=percenloss, perc='%')),'ALCANÇADO!!')
    else:
        print('Limite de perda: DESATIVADO')
    if desligameta == 'NAO' and novo_saldo < meta_ganho:
        print('Limite ganho:', brl(meta_ganho),("- {percengain}{perc}".format(percengain=percengain, perc='%')))
    elif desligameta == 'NAO' and novo_saldo > meta_ganho:
        print('Limite ganho:', brl(meta_ganho),("- {percengain}{perc}".format(percengain=percengain, perc='%')),'ALCANÇADO!!')
    else:
        print('Limite ganho: DESATIVADO')

    print('Acima da Meta WIN:', brl(novo_saldo - meta_ganho)) if novo_saldo >= meta_ganho and desligameta == 'NAO' else ''
    print('Abaixo da Meta LOSS:', brl(novo_saldo - meta_perda)) if novo_saldo < meta_perda and desligameta == 'NAO' else ''
    print("Payout: {pay}% ({paridade})".format(paridade=par, pay=(int(payout*100))))
    print("Acumulado: ",brl(lucro))

lucro = 0
versao = ver
operacao_tipo = get_bamode()
payout = Payout(par)
mperda = 0
novo_saldo = API.get_balance()
balanco = round(novo_saldo - saldohoje,2)

informe(desligameta)
ctypes.windll.kernel32.SetConsoleTitleW("WAVE20-BOT - "+str(par)+" - "+str(payout)+"%"+
                                        " - "+str(operacao_tipo)+" - "+"MHI-"+str(ver)+" - "+"MG"+str(martingale)
                                        +" - "+"Inicial"+str(' R$'+str(saldohoje))+" - "+"˅"+str(' R$'+str(meta_perda))+" - "+"˄"+str(' R$'+str(meta_ganho)))

while True:
    minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
    seconds = int(((datetime.now()).strftime('%S'))[:59])
    # if minutos >= 4.50 and minutos <= 4.50 or minutos >= 9.50 and minutos <= 9.50:
    if seconds >= 50 and seconds <= 51:
        instaveis = buscadoji(dirdoji,green,red,tdir)
        dirdoji = instaveis[0]
        green = instaveis[1]
        red = instaveis[2]
        tdir = instaveis[3]

    entrar = True if (seconds >= 58 and seconds <= 59) else False

    stdout.write(" \r{minutes} Hora de entrar? | {texto}{saldo}".format(minutes=minutos,texto='Saldo Atual: ',saldo=brl(API.get_balance())))
    stdout.flush()


    if entrar:
        novo_saldo = API.get_balance()
        # if lucro < meta_perda and desligameta == 'NAO':
        #     desligameta = alcance_meta(lucro,meta_perda,meta_ganho,desligameta)
        # if lucro > meta_ganho and desligameta == 'NAO':
        #     desligameta = alcance_meta(lucro,meta_perda,meta_ganho,desligameta)


        print('\n\nIniciando operação!')
        if ver == int(1):
            print('imediatamente')
        if ver == int(2):
            print('em 1 minuto')
        if ver == int(3):
            print('em 2 minutos')

        dir = False
        print('Verificando cores..', end='')

        if tdir == 'call':
            dir = 'call'
            time.sleep(1)
        elif tdir == 'put':
            dir = 'put'
            time.sleep(1)
        else:
            dir = 'notrend'
        if dirdoji > int(1):
            time.sleep(1)
            print("\nMERCADO INSTÁVEL DOJI(S):{dirdoji} À 10Mn:\n".format(dirdoji=dirdoji))
            informe(desligameta)
        else:
            # if dir != 'doji':
            if dir != 'notrend':
                valor_entrada = valor_entrada_b
                print('Direção:', dir)
                print("Payout: {pay}% Par:({paridade})".format(paridade=par, pay=(int(payout * 100))))
                print(data_e_hora_em_texto)

                if novo_saldo < valor_entrada:
                    print('Saldo Insuficiênte')
                if payout <= float(0.7):
                    print('Não faremos apostas, retorno invivável:',payout,'%')
                else:
                    if ver == int(1):
                        time.sleep(0)
                        print('imediatamente')
                    if ver == int(2):
                        time.sleep(58)
                        print('em 1 minuto')
                    if ver == int(3):
                        time.sleep(118)
                        print('em 2 minutos')

                    for i in range(martingale):
                        status, id = API.buy_digital_spot(par, valor_entrada, dir, 1)
                        if status:
                            while True:
                                status, valor = API.check_win_digital_v2(id)
                                if status:
                                    valor = valor if valor > 0 else float('-' + str(abs(valor_entrada)))
                                    lucro += round(valor,2)
                                    if valor > 0:
                                        print('Resultado operação: ', end='')
                                        print('WIN /', 'Rodada: ', brl(valor), '/','Acumulado: ', round(lucro,2))
                                        print('/ ' + str(i) + ' GALE' if i > 0 else '')
                                        print('\n\nPausaremos por (1) minuto, antes de uma nova checagem \n\n')
                                        time.sleep(60)
                                        print('RECOMEÇANDO...')
                                        # novo_saldo = lucro
                                        if lucro > 0 and lucro > valor_entrada_b:
                                            percenloss = fmetaperda(percenloss)
                                            mperda = (lucro - (lucro / 100 * percenloss))
                                            meta_perda = (lucro - mperda)
                                            # valor_entrada = mperda
                                        # else:
                                        #     mperda = (saldohoje / 100 * percenloss)
                                        #     meta_perda = (saldohoje - mperda)
                                    else:
                                        print('Resultado operação: ', end='')
                                        print('LOSS /', 'Rodada: ', brl(valor), '/',
                                          'Acumulado: ', brl(lucro))

                                        print('/ ' + str(i) + ' GALE' if i > 0 else '')
                                        # entradas(par, valor_entrada, dir, timeframe=60)
                                        # if entradas == 'loss':
                                        entrada = valor_entrada
                                        direcao = dir
                                        timeframe = 1
                                        resultado = entradas(par, entrada, direcao, timeframe)
                                        if resultado == 'win':
                                            print(resultado)
                                        else:
                                            perca = entrada
                                            sorosgale(perca)
                                        stop(lucro, stop_gain, stop_loss)
                                        # if lucro >= 0 and lucro < meta_perda and desligameta == 'NAO':
                                        #     desligameta = alcance_meta(lucro, meta_perda, meta_ganho,desligameta)
                                        # novo_saldo = API.get_balance()

                                    break
                            if valor > 0:
                                informe(desligameta)
                                dirdoji = int(0)
                                red = int(0)
                                green = int(0)
                                break
                        else:
                            time.sleep(2)
                            print('\nERRO!! NÃO FAREMOS ENTRADAS')
                            informe(desligameta)
            else:
                time.sleep(2)
                print('\nAbortar entrada! Checagem da tendência aponta inconsistência!!')
                informe(desligameta)

            # else:
            #     time.sleep(2)
            #     print('\n DOJI ENCONTRADO! SEM OPERAÇÕES')
            #     informe(desligameta)

    time.sleep(0.5)
