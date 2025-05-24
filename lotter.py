import configparser
import datetime  # для расчёта 'текущей даты'
from time import sleep  # для засыпания перед нештатным exit()
import pandas as pd
import numpy as np  # для сортировки
import math
import matplotlib.pyplot as plt
from dateutil.parser import parse  # для расчётов 'сколько дней назад выпадал номер'
import json
import os
import platform  # для открытия файла отчёта в доступном текстовом редакторе

# import secrets
import sys  # перенаправления stdout с консоли в файл

import lotter_func as fn  # основные функции проекта вынесены в lotter_func.py


# Структуры, которые будут использоваться
list_49_of_0 = [ 0 for i in range(49) ]  # список '49 нулей'
list_1_to_49 = [ i for i in range(1, 50) ]  # список 'номера от 1 до 49'
dict_49_of_0 = dict.fromkeys(list_1_to_49, 0)  # словарь '49 нулей' формируется из списка
# Словарь для накапливания статистики последних AMOUNT_OF_DRAWING тиражей:
drawing_data = {
    "Draw": {
        'DrawNum': 0,
        'DrawDate': '0000-00-00',
        'DrawResult': [0, 0, 0, 0, 0, 0],
        'NumsOdd': 0,
        'NumsEven': 0,
        'RepeatNums': 0
    },
    'Nums': {
        'No1': {
            'Num': 1,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No2': {
            'Num': 2,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No3': {
            'Num': 3,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No4': {
            'Num': 4,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No5': {
            'Num': 5,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No6': {
            'Num': 6,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No7': {
            'Num': 7,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No8': {
            'Num': 8,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No9': {
            'Num': 9,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No10': {
            'Num': 10,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No11': {
            'Num': 11,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No12': {
            'Num': 12,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No13': {
            'Num': 13,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No14': {
            'Num': 14,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No15': {
            'Num': 15,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No16': {
            'Num': 16,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No17': {
            'Num': 17,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No18': {
            'Num': 18,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No19': {
            'Num': 19,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No20': {
            'Num': 20,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No21': {
            'Num': 21,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No22': {
            'Num': 22,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No23': {
            'Num': 23,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No24': {
            'Num': 24,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No25': {
            'Num': 25,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No26': {
            'Num': 26,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No27': {
            'Num': 27,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No28': {
            'Num': 28,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No29': {
            'Num': 29,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No30': {
            'Num': 30,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No31': {
            'Num': 31,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No32': {
            'Num': 32,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No33': {
            'Num': 33,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No34': {
            'Num': 34,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No35': {
            'Num': 35,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No36': {
            'Num': 36,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No37': {
            'Num': 37,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No38': {
            'Num': 38,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No39': {
            'Num': 39,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No40': {
            'Num': 40,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No41': {
            'Num': 41,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No42': {
            'Num': 42,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No43': {
            'Num': 43,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No44': {
            'Num': 44,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No45': {
            'Num': 45,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No46': {
            'Num': 46,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No47': {
            'Num': 47,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No48': {
            'Num': 48,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            },
        'No49': {
            'Num': 49,
            'Frequency': 0,
            'LastDraw': 0,
            'LastDate': '0000-00-00',
            'DayAgo': 0,
            'Repeat': 0
            }
        },
    'Advices': {
        'Hot/Cold': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0, '31': 0, '32': 0, '33': 0, '34': 0, '35': 0, '36': 0, '37': 0, '38': 0, '39': 0, '40': 0, '41': 0, '42': 0, '43': 0, '44': 0, '45': 0, '46': 0, '47': 0, '48': 0, '49': 0},
        # 'Ognev': []
        }
    }


# Чтение параметров из lotter.ini
config = configparser.ConfigParser()  # создание объекта парсера
config.read("lotter.ini")
MIN = int(config["Lottery"]["MIN"])
MAX = int(config["Lottery"]["MAX"])
ANALYZE_THIS = int(config["Analyze"]["ANALYZE_THIS"])
GRAPH_STAT = int(config["Analyze"]["GRAPH_STAT"])
USER_AMOUNT_DRAWING = int(config["Analyze"]["USER_AMOUNT_DRAWING"])
ANOMAL_DRAWING = int(config["Analyze"]["ANOMAL_DRAWING"])
if MIN != 6 or MAX != 49:
    print('В файле \'lotter.ini\' установлены некорректные настройки!\nПроверьте параметры MIN и MAX!')
    sleep(5)
    exit()


# Проверка наличия доступного архива тиражей
fn.check_lotter_results_xlsx()

# Получение текущей даты
now_date = datetime.date.today().isoformat()

"""
# Для вывода отчёта в файл, часть 1 из 2:
print('\nLOTTER', '*' * 25, MIN, 'из', MAX,  '*' * 25, now_date, '\n')
print('Ожидайте, формируется отчёт...')
# перенаправление stdout для записи консольного вывода в файл
sys.stdout = open('lotter_console.txt', 'w')
"""

print('\nLOTTER', '*' * 25, MIN, 'из', MAX,  '*' * 25, now_date, '\n')
print("""Используемые сокращения:
\tBYN3 - вознаграждение за 3 угаданных номера, BYN;
\tBYN4 - вознаграждение за 4 угаданных номера, BYN;
\tBYN5 - вознаграждение за 5 угаданных номеров, BYN;
\tBYN6 - вознаграждение за 6 угаданных номеров, BYN;
\tDATE - дата проведения тиража;
\tDEC - 'декады' - например, DEC=012234 для 5,10,25,27,35,40;
\tDIF - разность между самым маленьким и самым большим номером;
\tDRAW - номер тиража;
\tEVN - количество чётных номеров в тираже;
\tFOND - призовой фонд, BYN;
\tFR1...FR6 - частота выпадения номера;
\tJACK - джек-пот, BYN;
\tN1...N6 - выигрышные номера;
\tODD - количество нечётных номеров в тираже;
\tRPT - количество повторившихся номеров из предыдущего тиража;
\tSUM - сумма всех номеров в тираже;
\tWIN3 - количество игроков, угадавших 3 номера;
\tWIN4 - количество игроков, угадавших 4 номера;
\tWIN5 - количество игроков, угадавших 5 номеров;
\tWIN6 - количество игроков, угадавших 6 номеров.""", '\n')  # , file = f

# Настройки для вывода Pandas в консоль:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Формирование датафрейма:
excel_data = pd.read_excel('lotter_results.xlsx', sheet_name='results', usecols=[x for x in range(18)])
columns_new_names = ['DRAW', 'DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'WIN6', 'BYN6', 'WIN5', 'BYN5', 'WIN4', 'BYN4', 'WIN3', 'BYN3', 'JACK', 'FOND']
excel_data.to_csv('lotter_results.csv', header=columns_new_names, index=False, sep=';', lineterminator=';\n', encoding='utf8')
df = pd.read_csv('lotter_results.csv', delimiter=';', index_col='DRAW', usecols=columns_new_names)

# Оптимизация датафрейма:
# - перевод текстовой даты '31.12.2023' в тип datetime '2023-12-31'
df['DATE'] = pd.to_datetime(df['DATE'], format='%d.%m.%Y')
# - сортировка номеров тиража по порядку (пока они в том порядке, в котором выпадали)
df[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']] = df[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']].apply(lambda x: np.sort(x), axis=1, raw=True)
# Сохранение датафрейма:
df.to_csv('lotter_results.csv', encoding='utf-8')  # delimiter=';'

amount_of_draws = len(df)

# Общая статистика полной базы тиражей:
fn.full_database_statistic(MIN, MAX, df)
# Распределение 'горячих' и 'холодных' номеров по каналам
fn.hot_cold_full_database(df)

if GRAPH_STAT > 0:
    # Построение графика 'Распределение номеров по каналам'
    df_freq_all_chanels = pd.read_csv("lotter_results.tmp")  # index_col=False менее наглядно
    fn.graph_channels_full_database(df_freq_all_chanels)
    del df_freq_all_chanels

# Результаты последнего тиража:
fn.last_drawing_statistic(amount_of_draws, df)
# Результаты X последних тиражей:
# (сейчас отключено т.к. ниже показываются в более интересном варианте)
# fn.results_of_x_last_drawing(USER_AMOUNT_DRAWING, df, 'N6')

# Упрощение датафрейма (ненужные для расчётов столбцы исключаются):
df = pd.read_csv('lotter_results.csv', index_col='DRAW', usecols=['DRAW', 'DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6'])
# В датафрейм (после расчёта) добавляются дополнительные столбцы:
fn.add_columns_to_database(df)

# Вывод самых необычных результатов тиражей
if ANALYZE_THIS > 0:
    fn.anomal_results_drawing(ANOMAL_DRAWING, df)

# Построение графика по словарям значений из столбцов датафрейма:
if GRAPH_STAT > 0:
    # 'DEC': распределение номеров по декадам
    fn.graph_from_dict(
        df,
        df_column='DEC',
        graph_title='распределение номеров по декадам',
        graph_x ='декада',
        graph_y ='количество тиражей',
        graph_color = 'r',
        graph_legend='распределение\nпо декадам',
        graph_file_name='lotter_graph_decades.png'
        )
    # 'ODD': количество нечётных номеров в тираже
    fn.graph_from_dict(
        df,
        df_column='ODD',
        graph_title='распределение нечётных номеров в тиражах',
        graph_x ='количество нечётных номеров в одном тираже',
        graph_y ='количество тиражей',
        graph_color = 'b',
        graph_legend='количество\nнечётных\nномеров',
        graph_file_name='lotter_graph_odd_numbers.png'
        )
    # 'EVN': количество чётных номеров в тираже
    fn.graph_from_dict(
        df,
        df_column='EVN',
        graph_title='распределение чётных номеров в тиражах',
        graph_x ='количество чётных номеров в одном тираже',
        graph_y ='количество тиражей',
        graph_color = 'g',
        graph_legend='количество\nчётных\nномеров',
        graph_file_name='lotter_graph_evn_numbers.png'
        )
    # 'RPT': количество повторов номеров из предыдущего тиража
    fn.graph_from_dict(
        df,
        df_column='RPT',
        graph_title='количество повторов номеров из предыдущего тиража',
        graph_x ='количество повторов номеров',
        graph_y ='количество тиражей',
        graph_color = 'r',
        graph_legend='количество\nповторов\nномеров',
        graph_file_name='lotter_graph_repeat_numbers.png'
        )
    # 'DIF': разность между номерами N6 и N1
    fn.graph_from_dict(
        df,
        df_column='DIF',
        graph_title='разность между номерами N6 и N1',
        graph_x ='разность номеров N6 минус N1',
        graph_y ='количество тиражей',
        graph_color = 'g',
        graph_legend='величина\nразности\nномеров',
        graph_file_name='lotter_graph_difference_numbers.png'
        )
    # 'SUM': сумма выпавших в тираже номеров
    fn.graph_from_dict(
        df,
        df_column='SUM',
        graph_title='сумма выпавших в тираже номеров N1 ... N6',
        graph_x ='сумма выпавших в тираже номеров',
        graph_y ='количество тиражей',
        graph_color = 'b',
        graph_legend='величина\nсуммы\nномеров',
        graph_file_name='lotter_graph_summ_numbers.png'
        )

# Полная статистика архива тиражей в словарях
# fn.dict_with_full_statistic(df)


# Результаты X последних тиражей с дополнительными столбцами:
fn.results_of_x_last_drawing(USER_AMOUNT_DRAWING, df, 'SUM')

input('Для завершения нажмите ENTER...')

"""
# для вывода отчёта в файл, часть 2 из 2
# восстановление стандартного stdout
sys.stdout = sys.__stdout__
print("Завершено, отчёт записан в файл 'lotter_console.txt'")

# открыть lotter_console.txt в доступном текстовом редакторе
if platform.system() == "Windows" or platform.system() == "win32":
    os.system('notepad.exe lotter_console.txt')
if platform.system() == "Linux":
    os.system('nano lotter_console.txt')
"""
