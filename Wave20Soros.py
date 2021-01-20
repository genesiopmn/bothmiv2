###############################################################
# SOROS GALE
# -*- coding utf-8 -*-
# from multiprocessing import freeze_support
# from iqoptionapi.stable_api import IQ_Option
# from datetime import datetime
# import time
import locale
locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')
brl = locale.currency

from sys import stdout
# import os
# import ctypes
from datetime import datetime
import time
# from random import randint
from iqoptionapi.stable_api import IQ_Option
import sys

API=IQ_Option("genesiopmn@gmail.com","gpmneto210981")
API.connect()#connect to iqoption

bamode = str('PRACTICE')#str(input(' Indique o modo REAL ou PRACTICE: ')).upper()
API.change_balance(bamode)
novo_saldo = API.get_balance()
par = str('GBPJPY')#input(' Indique uma paridade para operar: ').upper()
valor_entrada = float(4)#float(input(' Indique um valor para entrar: '))
stop_loss = float(2000)#float(input(' Indique o valor de Stop Loss: '))
stop_gain = float(2000)#float(input(' Indique o valor de Stop Gain: '))
entrada = 100
direcao = ''
timeframe = 1
lucro = 0
acumulado = 0
num = 0
sensibilidade = int(1)

dirdoji = int(0)
red = int(0)
green = int(0)
tdir = ''
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')



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

# novo_saldo = API.get_balance()
# balanco = round(novo_saldo - saldohoje,2)
# operacao_tipo = get_bamode()
payout = Payout(par)
# mperda = 0
# novo_saldo = 0

def buscadoji(dirdoji,tdir):
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

    # red = r
    # green = g

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
        if (rtop0010 >= int(5) and rtop0010 <= int(10)) and (gtop1020 >= int(5) and gtop1020 <= int(10)):
            print('\n\nTendencia de Baixa ˅')
            tdir = 'put'
        elif (gtop0010 >= int(5) and gtop0010 <= int(10)) and (rtop1020 >= int(5) and rtop1020 <= int(10)):
            print('\n\nTendencia de Alta ˄')
            tdir = 'call'
        else:
            tdir = 'notrend'
            print('\nTendencia indefinida')
        time.sleep(1)
    return (dirdoji,tdir)


def stop(slucro, sperca):
    # if lucro <= float('-' + str(abs(loss))):
    if sperca >= float(stop_loss):
        print('Stop Loss batido!')
        sys.exit()

    if slucro >= float(stop_gain):
        print('Stop Gain Batido!')
        sys.exit()


def mudadir(direcao,num):
    while True:
        for i in range(num,100,1):
            i +=1
            num =i
            if num % 2 ==0:
                direcao = 'put'
            else:
                direcao = 'call'
            break
        return direcao,num

def entradas(par, entrada, direcao, timeframe):
    lucro = 0
    status, id = API.buy_digital_spot(par, entrada, direcao, timeframe)
    if status:
        while True:
            status, valor = API.check_win_digital_v2(id)
            if status:

                valor = valor if valor > 0 else float('-' + str(abs(entrada)))
                lucro += round(valor, 2)
                if lucro > 0:
                    return 'win', round(lucro)
                else:
                    return 'loss', float(abs(lucro))

def sorosgale(perca,acumulado):
    lucro_total = 0
    perca_total = perca
    loss = 0
    win = 0
    gain = 0
    nogain = 0
    retorno = 0
    num = 0
    direcao = ''


    print('\n Perda total:', brl(perca), ' - entrada inicial:', brl(perca / 2))
    while True:
        direcao, num = mudadir(direcao, num)
        stop(slucro=lucro_total, sperca=perca_total)
        resultado, retorno = entradas(par, (perca / 2) + retorno, direcao, timeframe)

        if resultado == 'win':
            # perca_total -= retorno
            lucro_total += retorno
            # if perca_total < float(0):
            #     perca_total = float(0)
            win += 1
            gain = retorno
            nogain = 0
            print('\nWIN', win, '-', 'LOSS',loss, '| ', resultado, '- lucro atual:', brl(gain), '- Perda atual:', brl(nogain))
            print('Perda Total:', brl(perca_total), 'lucro Total:', brl(lucro_total))
            if lucro_total >= perca_total:
                saldo = lucro_total - perca_total
                acumulado += saldo
                print('FIM', 'WIN', win, '-', 'LOSS', loss, '|', 'Lucro Total', brl(lucro_total), ' -> ','Perda Total', brl(perca_total), 'Saldo:', brl(saldo))
                return perca, acumulado

        else:
            loss += 1
            retorno - (retorno/payout*100)
            perca_total += retorno
            # lucro_total -= retorno
            # if lucro_total < float(0):
            #     lucro_total = float(0)
            perca += retorno / 2
            gain = 0
            nogain = retorno
            # retorno = 0
            print('\nWIN', win, '-', 'LOSS',loss, '| ', resultado, '- lucro atual:', brl(gain), '- Perda atual:', brl(nogain))
            print('Perda Total:', brl(perca_total), 'lucro Total:', brl(lucro_total))
        if lucro_total >= perca_total:
            saldo = lucro_total - perca_total
            acumulado += saldo
            print('FIM', 'WIN', win, '-', 'LOSS', loss, '|', 'Lucro Total', brl(lucro_total), ' -> ',
                  'Perda Total', brl(perca_total), 'Saldo:', brl(saldo))
            return perca, acumulado

        else:
            direcao, num = mudadir(direcao, num)
            stop(slucro=lucro_total, sperca=perca_total)
            resultado, retorno = entradas(par, perca, direcao, timeframe)
            if resultado == 'win':
                win += 1
                # perca_total -= retorno
                lucro_total += retorno
                # if perca_total < float(0):
                #     perca_total = float(0)
                gain = retorno
                nogain = 0
                print('\nWIN', win, '-', 'LOSS', loss, '| ', resultado, '- lucro atual:', brl(gain),'- Perda atual:', brl(nogain))
                print('Perda Total:', brl(perca_total), 'lucro Total:', brl(lucro_total))
            else:
                perca_total += retorno
                # lucro_total -= retorno
                # if lucro_total < float(0):
                #     lucro_total = float(0)
                loss += 1
                gain = 0
                nogain = retorno
                print('\nWIN', win, '-', 'LOSS', loss, '| ', resultado, '- lucro atual:', brl(gain),'- Perda atual:', brl(nogain))
                print('Perda total:', brl(perca_total), 'lucro total:', brl(lucro_total))



while True:
    minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
    seconds = int(((datetime.now()).strftime('%S'))[:59])
    # if minutos >= 4.50 and minutos <= 4.50 or minutos >= 9.50 and minutos <= 9.50:
    if seconds >= 50 and seconds <= 51:
        dirdoji, tdir = buscadoji(dirdoji,tdir)


    entrar = True if (seconds >= 58 and seconds <= 59) else False
    stdout.write(" \r{minutes} Hora de entrar? | {texto}{saldo}".format(minutes=minutos, texto='Saldo Atual: ',saldo=brl(API.get_balance())))
    stdout.flush()

    if entrar:
        dir = False
        print('\nVerificando cores..\n')

        if tdir == 'call':
            dir = 'call'
            time.sleep(1)
        elif tdir == 'put':
            dir = 'put'
            time.sleep(1)
        else:
            dir = 'notrend'
        if dirdoji > int(0):
            time.sleep(1)
            print("\nMERCADO INSTÁVEL DOJI(S):{dirdoji} À 10Mn:\n".format(dirdoji=dirdoji))
            # informe(desligameta)
        else:
            # if dir != 'doji':
            if dir != 'notrend':
                # valor_entrada = valor_entrada_b
                print('Direção:', dir)
                print("Payout: {pay}% ({paridade})".format(paridade=par, pay=(int(payout*100))))
                print(data_e_hora_em_texto)

                if novo_saldo < valor_entrada:
                    print('Saldo Insuficiênte')
                if payout <= float(0.7):
                    print('Não faremos apostas, retorno invivável:', payout, '%')
                else:
                    # direcao, num = mudadir(direcao, num)
                    direcao = dir
                    print('Inserindo aposta direção:',direcao,'Valor:',brl(entrada))
                    resultado, retorno = entradas(par, entrada, direcao, timeframe)

                    if resultado == str('win'):
                        print(resultado, brl(retorno))
                        acumulado += float(retorno)
                    else:
                        print(resultado, brl(retorno))
                        perca = float(retorno)
                        perca, acumulado = sorosgale(perca, acumulado)
                    print('Iniciando nos proximos 60s')
                    print('Acumulado:',brl(acumulado))
                    if acumulado >= float(2000):
                        print('Stop Gain batido')
                        sys.exit()

            else:
                time.sleep(2)
                print('\nAbortar entrada! Checagem da tendência aponta inconsistência!!')
                # informe(desligameta)


    time.sleep(0.5)
