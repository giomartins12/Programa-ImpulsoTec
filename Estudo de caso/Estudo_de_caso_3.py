# Estudo de caso 3 - Calcular o tempo de duração de um jogo

import datetime
from datetime import timedelta, time

hora_inc = time(hour=int(input("\tDigite a hora de inicio da partida(hh): ")),
                minute=int(input("\tDigite os minutos de inicio da partida(mm): ")),
                second=int(input("\tDigite os segundos de inicio da partida(ss): ")))

hora_fim = time(hour=int(input("\tDigite a hora de final da partida(hh): ")),
                minute=int(input("\tDigite os minutos finais da partida(mm): ")),
                second=int(input("\tDigite os segundos de finais da partida(ss): ")))

hi = datetime.timedelta(hours=hora_inc.hour, minutes=hora_inc.minute, seconds=hora_inc.second)
hf = datetime.timedelta(hours=hora_fim.hour, minutes=hora_fim.minute, seconds=hora_fim.second)

duracao = (hf - hi)

if (hi > hf):
    print("\t Inicio da partida: ", hora_inc)
    print("\t Termino da partida: ", hora_fim)
    print("\t A partida se extendeu para o outro dia!")
    print("\t Duração da partida: ", duracao)
else:
    print("\t Inicio da partida: ", hora_inc)
    print("\t Termino da partida: ", hora_fim)
    print("\t Duração da partida: ", duracao)







