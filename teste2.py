import sys
# import time
import locale
import enum
from sys import stdout
# import os
# import ctypes
from datetime import datetime
import time
locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')
brl = locale.currency
from random import randint
from iqoptionapi.stable_api import IQ_Option
# import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
API=IQ_Option("genesiopmn@gmail.com","gpmneto210981")
API.connect()#connect to iqoption

bamode = str('PRACTICE')#str(input(' Indique o modo REAL ou PRACTICE: ')).upper()
API.change_balance(bamode)
novo_saldo = API.get_balance()
par = str('AUDCAD')#input(' Indique uma paridade para operar: ').upper()
valor_entrada = float(100)#float(input(' Indique um valor para entrar: '))
stop_loss = float(1000)
stop_gain = float(1000)
sensibilidade = int(1)
entrada = 100
direcao = ''
timeframe = 1
lucro = float(0)
perda = float(0)
num = 0
dirdoji = int(0)
red = int(0)
green = int(0)
tdir = ''
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
acumulado = float(0)
ATIVO = API.get_all_open_time()
paridade = ''

class SaldoInicial(enum.Enum):
    banca = API.get_balance()
bancainicial = SaldoInicial.banca.value

def stop(stop_gain,stop_loss):
    perda = 0
    lucro = 0
    valor = (API.get_balance() - bancainicial)
    if valor > 0:
        lucro = valor
    else:
        perda = abs(valor)
    if lucro >= stop_gain:
        print('Stop Gain batido')
        sys.exit()
    if perda >= stop_loss:
        print('Stop Loss batido')
        sys.exit()
    return lucro

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

payout = Payout(par)
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

# def CheckActive():
#     ATIVOS = API.get_all_open_time()
#     # Checando se está aberto ou não
#     aberto = (ATIVOS["digital"][par]["open"])
#     if aberto == True:
#         # print(par,': Aberto')
#         return True
#     else:
#         # print(par,': Fechado')
#         return False

def entradas(par, entrada, direcao, timeframe):
    status, id = API.buy_digital_spot(par, entrada, direcao, timeframe)
    if status:
        while True:
            status, valor = API.check_win_digital_v2(id)
            if status:
                # valor = valor if valor > 0 else float('-' + str(abs(valor)))
                if valor > 0:
                    return 'win', float(valor)
                else:
                    return 'loss', float(abs(valor))



# def mudadir(direcao,num):
#     while True:
#         for i in range(num,100,1):
#             i +=1
#             num =i
#             if num % 2 ==0:
#                 direcao = 'put'
#             else:
#                 direcao = 'call'
#             break
#         return direcao,num

def mudadir(direcao):
    while True:
        for i in range(11):
            value = randint(0, 10)
            i = value
            if i % 2 == 0:
                direcao = 'put'
            else:
                direcao = 'call'
            break
        return direcao


def sorosgale(perda):
    lucro_total = float(0)
    perda_total = perda
    win = 0
    loss = 1
    num = 0
    retorno = 0
    gain = 0
    nogain = 0
    direcao=''

    # lucro = 0
    print('\n perda total:', brl(perda), ' - Entrada inicial:', brl(perda / 2))

    while True:
        if paridade != 'fechado':
            direcao = mudadir(direcao)  # direcao, num = mudadir(direcao, num)
            stop(stop_gain, stop_loss)
            resultado, retorno = entradas(par, (perda / 2 + retorno), direcao, timeframe)
            stop(stop_gain, stop_loss)
            if resultado == 'win':
                lucro_total += retorno
                win += 1
                gain += retorno
                print('\n', win, '-', loss, '| ', resultado, '- perda total:', brl(perda_total), '- lucro total:', brl(lucro_total))
                stop(stop_gain, stop_loss)

            else:
                perda_total += retorno
                perda += retorno / 2
                loss += 1
                nogain += retorno
                print('\n', win, '-', loss, '| ', resultado, '- perda total:', brl(perda_total), '- lucro total:', brl(lucro_total))


            if lucro_total >= perda_total:
                print('FIM\n', win, '-', loss, '|', '- perda total:', brl(perda_total), ' -> ','- lucro total:', brl(lucro_total),'| - Saldo:', brl(lucro_total-perda_total))

                break
            else:
                print('perda atual:', brl(nogain), 'lucro atual:', brl(gain))
        else:
            print("\nPar: {paridade} Fechado para operações".format(paridade=par))




while True:
    minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
    seconds = int(((datetime.now()).strftime('%S'))[:59])
    if seconds >= 30 and seconds <= 33:
        aberto = (ATIVO["digital"][par]["open"])
        if aberto == True:
            paridade = 'aberto'
        else:
            paridade = 'fechado'
    if seconds >= 50 and seconds <= 51:
        dirdoji, tdir = buscadoji(dirdoji,tdir)
    entrar = True if (seconds >= 58 and seconds <= 59) else False
    stdout.write(" \r{minutes} Hora de entrar? | {texto}{saldo} | {texto1} {saldo1} | {acum} {luc}".format(minutes=minutos, texto='Saldo Atual: ',saldo=brl(API.get_balance()),texto1='Banca Inicial',saldo1=brl(bancainicial),acum='Acumulado:', luc=brl(lucro)))
    stdout.flush()

    if entrar:
        if paridade == 'fechado' or paridade == '':
            time.sleep(2)
            print("\n\nPar: {paridade} Fechado para operações\n".format(paridade=par))
        else:
            print('\nVerificando cores...')
            if tdir == 'call':
                direcao = 'call'
                time.sleep(1)
            elif tdir == 'put':
                direcao = 'put'
                time.sleep(1)
            else:
                direcao = 'notrend'
            if dirdoji > int(0):
                time.sleep(1)
                print("\nMERCADO INSTÁVEL DOJI(S):{dirdoji} À 10Mn:\n".format(dirdoji=dirdoji))
                # informe(desligameta)
            else:
                if direcao != 'notrend':
                    print('Direção:', direcao)
                    print("Payout: {pay}% ({paridade})".format(paridade=par, pay=(int(payout*100))))
                    print(data_e_hora_em_texto)

                    if novo_saldo < valor_entrada:
                        print('Saldo Insuficiênte')
                    if payout <= float(0.7):
                        print("Não faremos entrada, retorno inviável: Payout: {pay}% ({paridade})".format(paridade=par, pay=(int(payout*100))))
                    else:
                        # direcao = direcao
                        print("Inserindo aposta Direção: {direcao} - Entrada: {entrada} - Par: ({par}) - Payout: {pay}%".format(direcao=direcao,entrada=brl(entrada),par=par,pay=(int(payout*100))))
                        resultado, retorno = entradas(par, entrada, direcao, timeframe)
                        if resultado == str('win'):
                            print(resultado, brl(retorno))
                            lucro = stop(stop_gain, stop_loss)
                        else:
                            print(resultado, brl(retorno))
                            perda = float(retorno)
                            perda = sorosgale(perda)
                            lucro = stop(stop_gain, stop_loss)
                        print('Acumulado:', brl(lucro))
                        print('Banca Inicial:', brl(bancainicial))
                        print('Novo Saldo:', brl(API.get_balance()))
                else:
                    time.sleep(2)
                    print('\nAbortar entrada! Checagem da tendência aponta inconsistência!!')
                    # informe(desligameta)
    time.sleep(0.5)





    # print("Inserindo aposta Direção: {direcao} - Entrada: {entrada} - Par: ({par}) - Payout: {pay}%".format(direcao=direcao,entrada=brl(entrada),par=par,pay=(int(payout*100))))
    # direcao = mudadir(direcao)
    # resultado, retorno = entradas(par, entrada, direcao, timeframe)
    #
    # if resultado == str('win'):
    #     print(resultado,brl(retorno))
    # else:
    #     print(resultado,brl(retorno))
    #     perda = float(retorno)
    #     stop(stop_gain, stop_loss)
    #     perda = sorosgale(perda)
    #
    # print('Iniciando nos proximos 60s')
    # lucro = stop(stop_gain, stop_loss)
    # print('Acumulado:', brl(lucro))
    # print('Banca Inicial:', brl(bancainicial))
    # print('Novo Saldo:', brl(API.get_balance()))
    # time.sleep(60)

