###############################################################
# SOROS GALE
# -*- coding utf-8 -*-
# from multiprocessing import freeze_support
# from iqoptionapi.stable_api import IQ_Option
# from datetime import datetime
import time
# import sys
# from sys import stdout
# import os
# import ctypes
# from datetime import datetime
# import time
from iqoptionapi.stable_api import IQ_Option
# import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
API=IQ_Option("genesiopmn@gmail.com","gpmneto210981")
API.connect()#connect to iqoption

bamode = str('PRACTICE')#str(input(' Indique o modo REAL ou PRACTICE: ')).upper()
API.change_balance(bamode)
novo_saldo = API.get_balance()
par = str('AUDJPY')#input(' Indique uma paridade para operar: ').upper()
valor_entrada = float(100)#float(input(' Indique um valor para entrar: '))
entrada = 100
direcao = 'call'
timeframe = 1
lucro = 0
# perca = 0



def CheckActive():
    ATIVOS = API.get_all_open_time()
    # #check if open or not
    # print(ALL_Asset["digital"]["EURUSD-OTC"]["open"])
    # Checando se está aberto ou não
    aberto = (ATIVOS["digital"][par]["open"])
    if aberto == True:
        print(par,': Aberto')
        return True
    else:
        print(par,': Fechado')
        return False

while True:
    chechagem = CheckActive()
    print(chechagem)
    time.sleep(2)
#
#
# # num=int(1)
# def mudadir(direcao,num):
#     while True:
#         for i in range(num,20,1):
#             i +=1
#             num =i
#             if num % 2 ==0:
#                 direcao = 'put'
#             else:
#                 direcao = 'call'
#             break
#         return direcao,num
#
# def entradas(par, entrada, direcao, timeframe):
#     status, id = API.buy_digital_spot(par, entrada, direcao, timeframe)
#
#     if status:
#         while True:
#             status, lucro = API.check_win_digital_v2(id)
#
#             if status:
#                 if lucro > 0:
#                     return 'win', round(lucro, 2)
#                 else:
#                     return 'loss', float(abs(lucro))
#                 # break
#
#
# def sorosgale(perca,acumulado):
#     lucro_total = 0
#     perca_total = perca
#     nivel = 1
#     mao = 1
#     retorno = 0
#     num = 1
#     direcao = ''
#     direcao, num = mudadir(direcao, num)
#     # direcao = mdir[0]
#     # num = mdir[1]
#     print('\n Perca total:', round(perca,2), ' - entrada inicial:', round(perca,2) / 2)
#
#     while True:
#
#         resultado, retorno = entradas(par, (perca / 2) + retorno, direcao, 1)
#
#         if resultado == 'win':
#             lucro_total += retorno
#             print('\nRodada', mao, '-', 'Nivel',nivel, '| ', resultado, '- lucro atual:', round(retorno,2), '- perca atual:', round(perca,2))
#             mao += 1
#         elif resultado == 'loss':
#             mao = 1
#             perca_total += retorno
#             perca += retorno / 2
#             # retorno = 0
#             print('\nRodada', mao, '-', 'Nivel',nivel, '| ', resultado, '- lucro atual:', round(retorno,2), '- perca atual:', round(perca,2))
#             nivel += 1
#
#         if lucro_total >= perca_total:
#             lucro_total = lucro_total - perca_total
#             acumulado += lucro_total
#             print('FIM\n', nivel, '-', mao, '|', 'Perca Total',round(perca_total,2), ' -> ','Lucro Total', round(lucro_total,2))
#
#             break
#
#         else:
#             print('perca Total:', round(perca_total,2), 'lucro Total:', round(lucro_total,2))
#             direcao,num = mudadir(direcao, num)
#             resultado, retorno = entradas(par, perca+entrada, direcao, timeframe)
#
#             if resultado == 'win':
#                 lucro_total += retorno
#             else:
#                 perca_total += retorno
#             print('perca total:', round(perca_total, 2), 'lucro total:', round(lucro_total, 2))
#
#
# acumulado = 0
# num = 1
# while True:
#     print('Inserindo aposta direção:',direcao,'Valor:',entrada)
#     resultado,retorno = entradas(par, entrada, direcao, timeframe)
#
#     if resultado == str('win'):
#         print(resultado,retorno)
#         acumulado += float(retorno)
#     else:
#         print(resultado,retorno)
#         perca = float(retorno)
#         sorosgale(perca,acumulado)
#         acumulado += float(acumulado)
#     print('Iniciando nos proximos 60s')
#     print('Acumulado:',round(acumulado,2))
#     time.sleep(60)
#     direcao, num = mudadir(direcao, num)
#
#
#
#
#
#
#
# ####################################################
# # rtop0010 = 3
# # grtop0010 = 7
# # gtop1020 = 3
# # rtop1020 = 7
# # if (rtop0010 >= int(7) and rtop0010 <= int(10)) and (gtop1020 >= int(7) and gtop1020 <= int(10)):
# #     print('V',True)
# # elif (grtop0010 >= int(7) and grtop0010 <= int(10)) and (rtop1020 >= int(7) and rtop1020 <= int(10)):
# #     print("Λ",True)
# # else:
# #     print(False)
#
# ###############################################################
# # -*- coding utf-8 -*-
# # from multiprocessing import freeze_support
# # from iqoptionapi.stable_api import IQ_Option
# # from datetime import datetime
# # import time
# # import sys
# # from sys import stdout
# # import os
# # import ctypes
# # from datetime import datetime
# # import time
# # from iqoptionapi.stable_api import IQ_Option
# # # import logging
# # # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
# # API=IQ_Option("genesiopmn@gmail.com","gpmneto210981")
# # API.connect()#connect to iqoption
# #
# # par = 'GBPUSD-OTC'
# # pumpdump = ''
# # dirdoji = ''
# # tdir = ''
# #
# # def buscadoji(pumpdump,dirdoji,tdir):
# #     instaveis = []
# #     velas = API.get_candles(par, 60, 40, time.time())
# #     velas[-19] = 'g' if velas[-19]['open'] < velas[-19]['close'] else 'r' if velas[-19]['open'] > velas[-19]['close'] else 'd'
# #     print(float(((datetime.now()).strftime('%M.%S'))[1:]))
# #     velas[0] = 'g' if velas[0]['open'] < velas[0]['close'] else 'r' if velas[0]['open'] > velas[0]['close'] else 'd'
# #     velas[1] = 'g' if velas[1]['open'] < velas[1]['close'] else 'r' if velas[1]['open'] > velas[1]['close'] else 'd'
# #     velas[2] = 'g' if velas[2]['open'] < velas[2]['close'] else 'r' if velas[2]['open'] > velas[2]['close'] else 'd'
# #     velas[3] = 'g' if velas[3]['open'] < velas[3]['close'] else 'r' if velas[3]['open'] > velas[3]['close'] else 'd'
# #     velas[4] = 'g' if velas[4]['open'] < velas[4]['close'] else 'r' if velas[4]['open'] > velas[4]['close'] else 'd'
# #     velas[5] = 'g' if velas[5]['open'] < velas[5]['close'] else 'r' if velas[5]['open'] > velas[5]['close'] else 'd'
# #     velas[6] = 'g' if velas[6]['open'] < velas[6]['close'] else 'r' if velas[6]['open'] > velas[6]['close'] else 'd'
# #     velas[7] = 'g' if velas[7]['open'] < velas[7]['close'] else 'r' if velas[7]['open'] > velas[7]['close'] else 'd'
# #     velas[8] = 'g' if velas[8]['open'] < velas[8]['close'] else 'r' if velas[8]['open'] > velas[8]['close'] else 'd'
# #     velas[9] = 'g' if velas[9]['open'] < velas[9]['close'] else 'r' if velas[9]['open'] > velas[9]['close'] else 'd'
# #     velas[10] ='g' if velas[10]['open'] < velas[10]['close'] else 'r' if velas[10]['open'] > velas[10]['close'] else 'd'
# #     velas[11] ='g' if velas[11]['open'] < velas[11]['close'] else 'r' if velas[11]['open'] > velas[11]['close'] else 'd'
# #     velas[12] ='g' if velas[12]['open'] < velas[12]['close'] else 'r' if velas[12]['open'] > velas[12]['close'] else 'd'
# #     velas[13] ='g' if velas[13]['open'] < velas[13]['close'] else 'r' if velas[13]['open'] > velas[13]['close'] else 'd'
# #     velas[14] ='g' if velas[14]['open'] < velas[14]['close'] else 'r' if velas[14]['open'] > velas[14]['close'] else 'd'
# #     velas[15] ='g' if velas[15]['open'] < velas[15]['close'] else 'r' if velas[15]['open'] > velas[15]['close'] else 'd'
# #     velas[16] ='g' if velas[16]['open'] < velas[16]['close'] else 'r' if velas[16]['open'] > velas[16]['close'] else 'd'
# #     velas[17] ='g' if velas[17]['open'] < velas[17]['close'] else 'r' if velas[17]['open'] > velas[17]['close'] else 'd'
# #     velas[18] ='g' if velas[18]['open'] < velas[18]['close'] else 'r' if velas[18]['open'] > velas[18]['close'] else 'd'
# #     velas[19] ='g' if velas[19]['open'] < velas[19]['close'] else 'r' if velas[19]['open'] > velas[19]['close'] else 'd'
# #
# #     coresdoji = velas[0] + ' ' + velas[1] + ' ' + velas[2] + ' ' + velas[3] + ' ' + velas[4] + ' ' + velas[5] + ' ' + velas[6] + ' ' + velas[7] + ' ' + velas[8] + ' ' + velas[9] + ' ' + velas[10] + ' ' + velas[11] + ' ' + velas[12] + ' ' + velas[13] + ' ' + velas[14] + ' ' + velas[15] + ' ' + velas[16] + ' ' + velas[17] + ' ' + velas[18] + ' ' + velas[19]
# #
# #     velas_array = []
# #     for i in velas:
# #         velas_array.append(i)
# #
# #     top0005 = velas_array[0:5]
# #     rtop0005 = top0005.count('r')
# #     gtop0005 = top0005.count('g')
# #
# #     top0510 = velas_array[5:10]
# #     rtop0510 = top0510.count('r')
# #     gtop0510 = top0510.count('g')
# #
# #     top1015 = velas_array[10:15]
# #     rtop1015 = top1015.count('r')
# #     gtop1015 = top1015.count('g')
# #
# #     top1520 = velas_array[15:20]
# #     rtop1520 = top1520.count('r')
# #     gtop1520 = top1520.count('g')
# #
# #
# #     gtop0010 = gtop0005 + gtop0510
# #     rtop0010 = rtop0005 + rtop0510
# #
# #     gtop1020 = gtop1015 + gtop1520
# #     rtop1020 = rtop1015 + rtop1520
# #
# #     v20 = velas_array[19:20]
# #     v19 = velas_array[18:19]
# #     v18 = velas_array[17:18]
# #
# #     if rtop0010 >= int(7) and rtop0010 <= int(10) and gtop1020 >= int(7) and gtop1020 <= int(10):
# #         print('\n\nTendencia de baixa ˅')
# #         tdir = 'put'
# #     elif gtop0010 >= int(7) and gtop0010 <= int(10) and rtop1020 >= int(7) and rtop1020 <= int(10):
# #         print('\n\nTendencia de Alta ˄')
# #         tdir = 'call'
# #
# #     elif ((rtop0010) >= int(8)) and ((gtop0010) >= int(8)):
# #         print('\n\nTendencia de baixa Ɐ')
# #         tdir = 'put'
# #     elif ((gtop0010) >= int(8)) and ((rtop0010) >= int(8)):
# #         print('\n\nTendencia de Alta A')
# #         tdir = 'call'
# #
# #     elif rtop0005 > gtop0005 and gtop0510 > rtop0510 and rtop1015 > gtop1015 and gtop1520 > rtop1520:
# #         print('\n\nTendencia de baixa W\n')
# #         tdir = 'put'
# #     elif gtop0005 > rtop0005 and rtop0510 > gtop0510 and gtop1015 > rtop1015 and rtop1520 > gtop1520:
# #         print('\n\nTendencia de alta M\n')
# #         tdir = 'call'
# #     elif rtop0005 >= int(4) and gtop0510 >= int(2) and gtop0510 <= int(3) and rtop1015 >= int(3) and rtop1015 <= int(4) and rtop1520 >= int(3) and rtop1520 <= int(5):
# #         print('\n\nTendencia de alta m\n')
# #         tdir = 'call'
# #     elif gtop0005 >= int(4) and rtop0510 >= int(3) and rtop0510 <= int(4) and gtop1015 >= int(3) and gtop1015 <= int(4) and gtop1520 >= int(3) and gtop1520 <= int(5):
# #         print('\n\nTendencia de baixa w\n')
# #         tdir = 'put'
# #     else:
# #         tdir = 'notrend'
# #
# #
# #
# #     d = coresdoji.count('d')
# #     g = coresdoji.count('g')
# #     r = coresdoji.count('r')
# #     print('\n\nDoji {doji} Red {red} Green {green}'.format(doji=d,red=r,green=g))
# #     print(par)
# #     return (pumpdump, dirdoji, tdir)
# #
# # valor_entrada = float(100)
# # while True:
# #     minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
# #     seconds = int(((datetime.now()).strftime('%S'))[:59])
# #     stdout.write(" \r{minutes} Hora de entrar?".format(minutes=minutos))
# #     stdout.flush()
# #
# #     checar = True if (seconds >= 30 and seconds <= 31) else False
# #     if checar == True:
# #         teste = buscadoji(pumpdump, dirdoji, tdir)
# #         tdir = teste[2]
# #         time.sleep(2)
# #     data_e_hora_atuais = datetime.now()
# #     data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
# #
# #     entrar = True if (seconds >= 57 and seconds <= 59) else False
# #     if entrar:
# #         if tdir == 'put':
# #             time.sleep(1)
# #             dir = 'put'
# #             print('\n\nDireção: put')
# #             print(data_e_hora_em_texto)
# #         elif tdir == 'call':
# #             time.sleep(1)
# #             dir = 'call'
# #             print('\n\nDireção: = call')
# #             print(data_e_hora_em_texto)
# #             if status == True:
# #                 status, id = API.buy_digital_spot(par, valor_entrada, dir, 1)
# #                 while True:
# #                     status, valor = API.check_win_digital_v2(id)
# #                     if status:
# #                         novo_saldo = API.get_balance()
# #                         valor = valor if valor > 0 else float('-' + str(abs(valor_entrada)))
# #                         lucro = valor - valor_entrada
# #                         lucro += round(valor, 2)
# #                         if valor > 0:
# #                             print('Resultado operação: ', end='')
# #                             print('WIN /', 'Rodada: ', round(valor, 2), '/','Acumulado: ', round(lucro, 2))
# #                             print(novo_saldo)
# #                             # print('/ ' + str(i) + ' GALE' if i > 0 else '')
# #
# #
# #                         else:
# #                             print('Resultado operação: ', end='')
# #                             print('LOSS /', 'Rodada: ', round(valor, 2), '/','Acumulado: ', round(lucro, 2))
# #                             novo_saldo = API.get_balance()
# #                             print(novo_saldo)
# #                     break
# #
# #         else:
# #             time.sleep(3)
# #             print('\n\nTendencia indefinida\n')
# #             print(data_e_hora_em_texto)
# #     time.sleep(0.5)
#
# ###############################################################
#
# #
# # from iqoptionapi.stable_api import IQ_Option
# # import time
# # Iq=IQ_Option("genesiopmn@gmail.com","gpmneto210981")
# # Iq.connect()#connect to iqoption
# #
# # Money = 100
# # ACTIVES = "EURUSD-OTC"
# # ACTION = "put"
# # duration = 1
# # expirations_mode=1
# #
# # # id = Iq.buy_digital_spot(Money, ACTIVES, ACTION, expirations_mode)
# #
# # id=Iq.buy(Money, ACTIVES, ACTION, expirations_mode)
# # id2=Iq.buy(Money, ACTIVES, ACTION, expirations_mode)
# #
# # time.sleep(5)
# # sell_all = []
# # sell_all.append(id)
# # sell_all.append(id2)
# # print(Iq.sell_option(sell_all))
# #
# #
# #
# #
# #
# ###############################################################
# #
# # global saldohoje,novo_saldo,desligameta,meta_perda,percenloss,meta_ganho,percengain
# # saldohoje = float(1000)
# # novo_saldo = float(1100)
# # desligameta = 'NAO'
# # meta_ganho = int(10)
# # meta_perda = int(10)
# # percengain = int(10)
# # percenloss = int(12)
# # def informe():
# #     print('Resultado operação: ', end='')
# #     print('Saldo do dia:', round(saldohoje, 2), ("| Balanço:"),
# #           round(novo_saldo - saldohoje,
# #                 2) if novo_saldo > saldohoje or novo_saldo < saldohoje else '-')
# #     print('Saldo atual', round(novo_saldo, 2))
# #     if desligameta == 'NAO' and novo_saldo > meta_perda:
# #         print('Limite Perda:', round(meta_perda, 2),
# #               ("- {percenloss}{perc}".format(percenloss=percenloss, perc='%')))
# #     elif desligameta == 'NAO' and novo_saldo < meta_perda:
# #         print('Limite Perda:', round(meta_perda, 2),
# #               ("- {percenloss}{perc}".format(percenloss=percenloss, perc='%')),
# #               'ALCANÇADO!!')
# #     else:
# #         print('Limite de perda: DESATIVADO')
# #
# #     if desligameta == 'NAO' and novo_saldo < meta_ganho:
# #         print('Limite ganho:', round(meta_ganho, 2),
# #               ("- {percengain}{perc}".format(percengain=percengain, perc='%')))
# #     elif desligameta == 'NAO' and novo_saldo > meta_ganho:
# #         print('Limite ganho:', round(meta_ganho, 2),
# #               ("- {percengain}{perc}".format(percengain=percengain, perc='%')),
# #               'ALCANÇADO!!')
# #     else:
# #         print('Limite ganho: DESATIVADO')
# #     # print('Meta Ganho:', round(meta_ganho, 2),
# #     #       ("- {percengain}{perc}".format(percengain=percengain, perc='%')),
# #     #       'ALCANÇADO!!' if novo_saldo >= meta_ganho else '')
# #     print('Acima da Meta WIN:', round(novo_saldo - meta_ganho,
# #                                       2)) if novo_saldo >= meta_ganho and desligameta == 'NAO' else ''
# #     print('Abaixo da Meta LOSS:', round(novo_saldo - meta_perda,
# #                                         2)) if novo_saldo < meta_perda and desligameta == 'NAO' else ''
# #
# # informe()
#
# ###############################################################
#
# # valor_entrada = float(110)
# # lucro = float(15)
# # i = 2
# # while True:
# #     status = True
# #     valor = float(0)
# #     if status:
# #         valor = valor if valor > 0 else float('-' + str(abs(valor_entrada)))
# #         lucro += round(valor, 2)
# #         if valor > 0:
# #             print('Resultado operação: ', end='')
# #             print('WIN /', 'Rodada: ', round(valor, 2), '/',
# #                   'Acumulado: ', round(lucro, 2))
# #             print('/ ' + str(i) + ' GALE' if i > 0 else '')
# #
# #             if novo_saldo > saldohoje:
# #                 percenloss = int(10)
# #                 mperda = int(novo_saldo / 100 * percenloss)
# #                 meta_perda = int(novo_saldo - mperda)
# #             else:
# #                 mperda = int(saldohoje / 100 * percenloss)
# #                 meta_perda = int(saldohoje - mperda)
# #         else:
# #             print('Resultado operação: ', end='')
# #             print('LOSS /', 'Rodada: ', round(valor, 2), '/',
# #                   'Acumulado: ', round(lucro, 2))
# #
# #             print('/ ' + str(i) + ' GALE' if i > 0 else '')
# #             if 1 + 2 == 3:
# #                 print('ok')
# #
# #             valor_entrada = valor_entrada + valor
# #             print(valor_entrada)
# #
# #         break
# ###############################################################
# # import sys
#
# # novo_saldo = int(80)
# # meta_perda = int(90)
# # meta_ganho = int(110)
# # global desligameta
# # desligameta = 'NAO'
# #
# # def alcance_meta(novo_saldo,meta_perda,meta_ganho,desligameta):
# #     continuar = ''
# #     while True:
# #         if novo_saldo >= meta_perda and novo_saldo <= meta_ganho:
# #             desligameta = 'NAO'
# #             return desligameta
# #             # break
# #         else:
# #             if novo_saldo < meta_perda and desligameta == 'NAO':
# #                 continuar = str(input('\nTolerancia de perda batida, recomenda-se parar operação'
# #                                       ' e tentar em outro PAR'
# #                                       '\nDeseja continar?\nSIM\nNÃO\n')).upper()
# #             if novo_saldo > meta_ganho and desligameta == 'NAO':
# #                 continuar = str(input('\nMeta de ganho batida, recomenda-se parar operação'
# #                                       ' e tentar em outro PAR'
# #                                       '\nDeseja continar?\nSIM\nNÃO\n')).upper()
# #             if continuar == str('SIM') or continuar == str('S'):
# #                 print('Continuando desligando meta perda')
# #                 desligameta = str('SIM')
# #             if continuar != str('SIM') and continuar != str('S'):
# #                 print('Fechando BOT')
# #                 desligameta = str('NAO')
# #         return desligameta
# #
# #
# # while True:
# #     if desligameta == 'NAO':
# #         desligameta = alcance_meta(novo_saldo,meta_perda,meta_ganho,desligameta)
# #         print('META LIGADA?: SIM')
# #     else:
# #         print('META DESLIGADA?: SIM')
#
# ###############################################################
# # generate random integer values
# # from random import seed
# # from random import randint
# # # seed random number generato
# # import locale
# # locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')
# # brl = locale.currency
# # import sys
# # def Sorosgale(perca):
# #     lucro_total = 0
# #     nivel = 1
# #     mao = 1
# #     lucro = 0
# #     print('\n Perca total:', perca, ' - entrada inicial:', (perca / 2))
# #
# #     while True:
# #
# #         resultado, lucro = aumentalucro((perca / 2) + lucro, 'put')
# #
# #         if resultado == 'win':
# #             lucro_total += lucro
# #             print('\n', nivel, '-', mao, '| ', resultado, '- lucro:', lucro, '- perca:', perca)
# #             mao += 1
# #         else:
# #             lucro_total = 0
# #             mao = 1
# #             perca += perca / 2
# #             print('\n', nivel, '-', mao, '| ', resultado, '- lucro:', lucro, '- perca:', perca)
# #             nivel += 1
# #
# #         if lucro_total >= perca:
# #             print('FIM\n', nivel, '-', mao, '|', perca, ' -> ', lucro_total)
# #             break
# #         else:
# #             print('perca atual:', perca, 'lucro:', lucro)
# #
# # def aumentalucro(luc,lucro):
# #     while luc > 0:
# #         for i in range(luc):
# #             for value in range(6):
# #                 value = randint(0,5)
# #                 if value == 0:
# #                     i -= 10
# #                 elif value == 1:
# #                     i += 20
# #                 elif value == 2:
# #                     i += 10
# #                 elif value == 3:
# #                     i -= 20
# #                 elif value == 4:
# #                     i += 30
# #                 elif value == 5:
# #                     i -= 30
# #                 break
# #             lucro = lucro + i
# #
# #             break
# #         return float(lucro)
# #
# # def fmetaperda(percenloss):
# #     while percenloss >0:
# #
# #         for i in range(percenloss, 0, -1):
# #             i -=5
# #             percenloss = i
# #             break
# #         return percenloss
# #
# # def fmperda(novo_saldo,percenloss):
# #     if novo_saldo >= 0:
# #         fsalvo = round(novo_saldo / 100 * percenloss,2)
# #         meta_perda = round(novo_saldo - fsalvo,2)
# #
# #     # else:
# #     #     fsalvo = round(saldohoje / 100 * percenloss,2)
# #     #     meta_perda = round(saldohoje - fsalvo,2)
# #         return meta_perda
# #
# # def fmganho(saldohoje,percengain):
# #     mganho = round(saldohoje / 100 * percengain,2)
# #     meta_ganho = round(saldohoje + mganho,2)
# #     return meta_ganho
# #
# #
# #
# # def alcance_meta(novo_saldo,meta_perda,meta_ganho,desligameta):
# #     continuar = ''
# #     while True:
# #
# #         if novo_saldo >= meta_perda and novo_saldo <= meta_ganho:
# #             desligameta = 'NAO'
# #             return desligameta
# #             # break
# #         else:
# #             if novo_saldo < meta_perda and desligameta == 'NAO':
# #                 continuar = str(input('\nTolerancia de perda batida, recomenda-se parar operação'
# #                                       ' e tentar em outro PAR'
# #                                       '\nDeseja continar?\nSIM\nNÃO\n')).upper()
# #             if novo_saldo > meta_ganho and desligameta == 'NAO':
# #                 continuar = str(input('\nMeta de ganho batida, recomenda-se parar operação'
# #                                       ' e tentar em outro PAR'
# #                                       '\nDeseja continar?\nSIM\nNÃO\n')).upper()
# #             if continuar == str('SIM') or continuar == str('S'):
# #                 print('Continuando desligando meta perda')
# #                 desligameta = str('SIM')
# #             if continuar != str('SIM') and continuar != str('S'):
# #                 print('Fechando BOT')
# #                 sys.exit()
# #             return desligameta
# # saldohoje = float(150)
# # novo_saldo = float(20)
# # percenloss = int(100) #Precisa ser inteiro
# # percengain = int(20)
# # desligameta = 'NAO'
# # lucro = float(20)
# # luc = int(1)
# #
# #
# # meta_perda = round(fmperda(novo_saldo,percenloss),2)
# # meta_ganho = round(fmganho(saldohoje,percengain),2)
# # while(desligameta!=''):
# #
# #     lucro = aumentalucro(luc,lucro)
# #     novo_saldo += lucro
# #
# #     if round(novo_saldo < meta_perda,2) and desligameta == 'NAO':
# #         desligameta = alcance_meta(novo_saldo, meta_perda, meta_ganho, desligameta)
# #     if round(novo_saldo > meta_ganho,2) and desligameta == 'NAO':
# #         desligameta = alcance_meta(novo_saldo, meta_perda, meta_ganho, desligameta)
# #
# #     if novo_saldo > meta_perda:
# #         percenloss = fmetaperda(percenloss)
# #         fsalvo = (novo_saldo - (novo_saldo / 100 * percenloss))
# #         meta_perda = (novo_saldo - fsalvo)
# #     if lucro <0:
# #         perca = lucro
# #         Sorosgale(perca)
# #
# #     # else:
# #     #     fsalvo = float(0)
# #     #     fsalvo = (saldohoje / 100 * percenloss)
# #     #     meta_perda = (saldohoje - fsalvo)
# #
# #
# #     print("##############################\n")
# #     print('Saldo do dia:', brl(saldohoje))
# #     print('Limite de perda:',brl(meta_perda))
# #     print('Limite de gamho:', brl(meta_ganho))
# #     print('Novo saldo:', brl(novo_saldo+lucro))
# #     print('Salvo:',brl(fsalvo))
# #     print('Percentual:',("{pl}{perc}".format(perc='%',pl=percenloss)))
# #
# #
# #
# #
#
#
# #
# #
# # def fmperda(novo_saldo,percenloss):
# #     percenloss = fmetaperda(percenloss)
# #     if novo_saldo > saldohoje:
# #         mperda = round(saldohoje / 100 * percenloss,2)
# #         meta_perda = round(novo_saldo - mperda,2)
# #
# #     else:
# #         mperda = float(saldohoje / 100 * percenloss)
# #         meta_perda = float(saldohoje - mperda)
# #     return meta_perda, percenloss
# #
# #
# #
# # while True:
# #     meta_perda = fmperda(novo_saldo,percenloss)
# #     metaperda = meta_perda
# #     print(meta_perda)
#
# # def fun():
# #     d = dict();
# #     d['str'] = "GeeksforGeeks"
# #     d['x'] = 20
# #     return d
# #
# #
# # # Driver code to test above method
# # s = fun()
# # print(s)
#
#
#
#
#
# # goal="USDCHF"
# # size=1 #size=[1,5,10,15,30,60,120,300,600,900,1800,3600,7200,14400,28800,43200,86400,604800,2592000,"all"]
# # maxdict=20
# # print("start stream...")
# # I_want_money.start_candles_stream(goal,size,maxdict)
# # #DO something
# # print("Do something...")
# # time.sleep(10)
# #
# # print("print candles")
# # cc=I_want_money.get_realtime_candles(goal,size)
# # for k in cc:
# #     print(goal,"size",k,cc[k])
# # print("stop candle")
# # I_want_money.stop_candles_stream(goal,size)
#
# # # ALL_Asset = I_want_money.get_all_open_time()
# # # #check if open or not
# # # print(ALL_Asset["digital"]["EURUSD-OTC"]["open"])
# #
# # ATIVOS = I_want_money.get_all_open_time()
# #
# # #Checando se está aberto ou não
# # EURUSD = (ATIVOS["digital"]["EURUSD"]["open"])
# # EURUSD_OTC = (ATIVOS["digital"]["EURUSD-OTC"]["open"])
# # AUDCAD = (ATIVOS["digital"]["AUDCAD"]["open"])
# # if EURUSD == True:
# #     print('EURUSD: Aberto')
# # else:
# #     print('EURUSD: Fechado')
# # if EURUSD_OTC == True:
# #     print('EURUSD-OTC: Aberto')
# # else:
# #     print('EURUSD-OTC: Fechado')
# # if AUDCAD == True:
# #     print('AUDCAD: Aberto')
# # else:
# #     print('AUDCAD: Fechado')
#
#################################################
# PEGANDO PARIDADES ABERTAS E PAYOUT
# def payout(par, tipo, timeframe=1):
#     if tipo == 'turbo':
#         a = API.get_all_profit()
#         return int(100 * a[par]['turbo'])
#
#     elif tipo == 'digital':
#
#         API.subscribe_strike_list(par, timeframe)
#         while True:
#             d = API.get_digital_current_profit(par, timeframe)
#             if d != False:
#                 d = int(d)
#                 break
#             time.sleep(1)
#         API.unsubscribe_strike_list(par, timeframe)
#         return d
#
#
# par = API.get_all_open_time()
#
# for paridade in par['turbo']:
#     if par['turbo'][paridade]['open'] == True:
#         print('[ TURBO ]: ' + paridade + ' | Payout: ' + str(payout(paridade, 'turbo')))
#
# print('\n')
#
# for paridade in par['digital']:
#     if par['digital'][paridade]['open'] == True:
#         print('[ DIGITAL ]: ' + paridade + ' | Payout: ' + str(payout(paridade, 'digital')))