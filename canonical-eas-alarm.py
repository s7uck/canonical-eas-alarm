import os
import math
import re
import time
import signal
import mpv
import rich
from rich import print

color = 'red'
terminal_width = os.get_terminal_size().columns
terminal_height = os.get_terminal_size().lines

lines = [
'[blink]!!![/blink] ATTACCO NUCLEARE IN CORSO [blink]!!![/blink]',
'',
'CERCARE IMMEDIATAMENTE UN RIPARO',
'',
'ESEGUIRE SUBITO :',
'',
'1. git commit',
'2. git push',
'',
'EVACUARE IMMEDIATAMENTE LA SALA SERVER',
'E\' fortemente consigliato munirsi di una RADIO',
'A BATTERIA per rimanere in contatto con le Forze dell\'Ordine',
'',
'',
'PROTEZIONE CIVILE   \t   : \t 488 MHz',
'',
'',
'[italic]Messaggio di Allerta a Reti Unificate[/italic]',
'',
'[italic]Sender  : [yellow]IT-Alert Lombardia[/yellow] message validated in UNATTENDED MODE',
'[italic]see man canonical-eas-alarm[/italic]'
]

player = mpv.MPV()
alarm_sound = '/home/user/Scaricati/Tesla Low Battery Sound [Free Download].mp3'
player.loop = 'yes'

number_of_lines = len(lines)
number_of_rows = math.floor(terminal_height / 2)
number_of_newlines = number_of_rows - math.floor(len(lines) / 2)
newlines = '\n' * number_of_newlines

os.system('clear')

player.play(alarm_sound)

print(newlines)

for line in lines:
    number_of_columns = math.floor(terminal_width / 2)
    line_length = len(re.sub("[\(\[].*?[\)\]]", "", line))
    number_of_spaces = number_of_columns - math.floor(line_length / 2)
    spaces = ' ' * number_of_spaces

    print(f"{spaces}[{color}]{line}[/{color}]")

print(newlines)

signal.pause()
