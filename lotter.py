import configparser  # для работы с INI-файлом
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

import logging  # для ведения LOG-файла процесса работы скрипта
logging.basicConfig(level=logging.INFO,
                    filename='lotter.log',
                    filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')
logging.info('Инициализирован лог-файл "lotter.log"')

# Структуры, которые будут использоваться
list_49_of_0 = [ 0 for i in range(49) ]  # список '49 нулей'
list_1_to_49 = [ i for i in range(1, 50) ]  # список 'номера от 1 до 49'
dict_49_of_0 = dict.fromkeys(list_1_to_49, 0)  # словарь '49 нулей' формируется из списка

# Чтение параметров из lotter.ini
config = configparser.ConfigParser()  # создание объекта парсера
config.read("lotter.ini")
MIN = int(config["Lottery"]["MIN"])  # 6
MAX = int(config["Lottery"]["MAX"])  # 49
LEGEND = int(config["Lottery"]["LEGEND"])  # 1 или 0
DF_STATISTIC_CLASSIC = int(config["Analyze"]["DF_STATISTIC_CLASSIC"])  # 1 или 0
BUILD_GRAPH = int(config["Analyze"]["BUILD_GRAPH"])  # 1 или 0
DF_STATISTIC_ANOMALIC = int(config["Analyze"]["DF_STATISTIC_ANOMALIC"])  # 1 или 0
COUNTER_ANOMALIC_DRAWS = int(config["Analyze"]["COUNTER_ANOMALIC_DRAWS"])  # 3
COUNTER_USER_ANALYZE = int(config["Prediction"]["COUNTER_USER_ANALYZE"])  # 18

# Проверка наличия доступного архива тиражей
fn.check_lotter_results_xlsx()
logging.info('Доступен файл "lotter_results.xlsx" с базой тиражей')

# Проверка констант из файла 'lotter.ini'
fn.check_lotter_ini_const(MIN, MAX, LEGEND,
                          DF_STATISTIC_CLASSIC, BUILD_GRAPH,
                          DF_STATISTIC_ANOMALIC, COUNTER_ANOMALIC_DRAWS,
                          COUNTER_USER_ANALYZE)
logging.info('Успешно проверены константы из файла "lotter.ini"')

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

if LEGEND == 1:
    print("""Используемые сокращения:
    \tAGO - сколько дней назад выпадал данный конкретный номер;
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
    \tFREQ - частота выпадения данного конкретного номера;
    \tFR1...FR6 - частота выпадения номера 1...6;
    \tJACK - джек-пот, BYN;
    \tLSTDAT - дата выпадения данного конкретного номера;
    \tLSTDRW - номер тиража, в котором выпадал данный конкретный номер;
    \tN1...N6 - выигрышные номера;
    \tNUM - дата выпадения данного конкретного номера;
    \tODD - количество нечётных номеров в тираже;
    \tRPT - количество повторившихся номеров из предыдущего тиража;
    \tSUM - сумма всех номеров в тираже;
    \tWIN3 - количество игроков, угадавших 3 номера;
    \tWIN4 - количество игроков, угадавших 4 номера;
    \tWIN5 - количество игроков, угадавших 5 номеров;
    \tWIN6 - количество игроков, угадавших 6 номеров.
    \tВ секции JSON с названием 'DRW':
    \t\tDRW - подразумевается 'тираж';
    \t\tNUM - номер отдельного конкретного тиража;
    \t\tDAT - дата проведения отдельного конкретного тиража;
    \t\tRES - результаты отдельного конкретного тиража;
    \t\tODD - количество нечётных номеров в отдельном конкретном тираже;
    \t\tEVN - количество чётных номеров в отдельном конкретном тираже;
    \t\tRPT - количество повторившихся номеров (с прошлого тиража);
    \tВ секции JSON с названием 'NUMS':
    \t\t - ;
    \t\t - ;
    \t\t - ;
    \t\t - .""", '\n')  # , file = f

# Настройки для вывода Pandas в консоль:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Формирование датафрейма:
excel_data = pd.read_excel('lotter_results.xlsx', sheet_name='results', usecols=[x for x in range(18)])
logging.info('Считаны данные из файла "lotter_results.xlsx" в датафрейм')
columns_new_names = ['DRAW', 'DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'WIN6', 'BYN6', 'WIN5', 'BYN5', 'WIN4', 'BYN4', 'WIN3', 'BYN3', 'JACK', 'FOND']
excel_data.to_csv('lotter_results.csv', header=columns_new_names, index=False, sep=';', lineterminator=';\n', encoding='utf8')
df = pd.read_csv('lotter_results.csv', delimiter=';', index_col='DRAW', usecols=columns_new_names)

# Оптимизация датафрейма:
# - перевод текстовой даты '31.12.2023' в тип datetime '2023-12-31'
df['DATE'] = pd.to_datetime(df['DATE'], format='%d.%m.%Y')
# - сортировка номеров тиража по порядку (пока они в том порядке, в котором выпадали)
df[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']] = df[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']].apply(lambda x: np.sort(x), axis=1, raw=True)
logging.info('Датафрейм оптимизирован, номера в тиражах отсортированы')
# Сохранение датафрейма:
df.to_csv('lotter_results.csv', encoding='utf-8')  # delimiter=';'
logging.info('Датафрейм сохранён в файл "lotter_results.csv"')


if DF_STATISTIC_CLASSIC == 1:
    # Общая (классическая Pandas) статистика по датафрейму:
    fn.df_statistic_classic(MIN, MAX, df)
    logging.info('Сформирована классическая статистика датафрейма')

# Распределение 'горячих' и 'холодных' номеров по каналам
fn.df_hot_cold_numbers(df)

if DF_STATISTIC_CLASSIC == 1:
    print("- распределение 'горячих' / 'холодных' номеров по 'каналам':")
    columns_6_channels_names = ['N1', 'FR1', 'N2', 'FR2', 'N3', 'FR3', 'N4', 'FR4', 'N5', 'FR5', 'N6', 'FR6']
    df_freq_all_chanels = pd.read_csv('lotter_results.tmp', index_col='N1', usecols=columns_6_channels_names)
    # нет сиысла выводить датафрейм с 6-ю каналами полностью т.к. примерно после
    # 13-й строки номера начинают повторяются в соседних канаалах; чтобы избежать
    # 'магического числа': нужно узнать когда в певом канале 'FR1' появится частота
    # равная '0', например, 'zero_freq' - после этого вывод строк в консоль прервать
    zero_freq = list(df_freq_all_chanels['FR1']).index(0)  # индекс 'нуля'
    # здесь head ограничмвается параметром 'zero_freq'
    print(df_freq_all_chanels.head(zero_freq), '\n')  # даже более 13-ти строк выводить нет смысла - появляются повторы в соседних каналах



# СДЕЛАТЬ ФУНКЦИЮ (DRY!)
# количество анализируемых тиражей в датафрейме
amount_of_draws = len(df)

# Формирование словаря для накапливания статистики Hot/Cold и, возможно, перевода в JSON
drawing_data = dict()
# секция "DRW"
list_draw_result = [ 0 for i in range(MIN) ]  # сделать range(MIN)
drawing_data["DRW"] = {'NUM': 0, 'DAT': '0000-00-00', 'RST': list_draw_result,
                        'ODD': 0, 'EVN': 0, 'RPT': 0}
# секция "NUMS"
temp_dict = dict()
for i in range(1, MAX+1):  # сделать range(1, MAX+1, 1)
    temp_dict['No' + str(i)] = {'NUM': i, 'FREQ': 0, 'LSTDRW': 0,
                                'LSTDAT': '0000-00-00', 'AGO': 0, 'RPT': 0}
drawing_data["NUMS"] = temp_dict
del(temp_dict)
# секция "HOT"
temp_dict = dict()
for i in range(1, MAX+1):
    temp_dict[str(i)] = 0
drawing_data["HOT"] = temp_dict
del(temp_dict)

with open('lotter_results.csv', 'r', encoding='utf-8') as donor:
    with open('lotter_results.tm1', 'w', encoding='utf-8') as recepient:
        for line in donor:
            data = line.rstrip('\n').split(',')
            if data[0] == 'DRAW':
                # recepient.write(line)  # названия столбцов не записывать
                continue
            drawing_data["DRW"]['NUM'] = data[0]
            drawing_data["DRW"]['DAT'] = data[1]
            drawing_data["DRW"]['RST'] = [int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7])]

            # подсчёт количества нечётных и чётных номеров
            amount_odd = 0
            amount_even = 0
            for i in range(2, 8):
                if (int(data[i])) % 2 == 1:
                    amount_odd += 1
                else:
                    amount_even += 1
            drawing_data["DRW"]['ODD'] = amount_odd
            drawing_data["DRW"]['EVN'] = amount_even

            for i in range(2, 8):
                NoName = "No" + data[i]
                drawing_data['NUMS'][NoName]['FREQ'] += 1
                drawing_data['HOT'][str(NoName)[2:]] += 1
                drawing_data['NUMS'][NoName]['LSTDRW'] = data[0]
                drawing_data['NUMS'][NoName]['LSTDAT'] = data[1]
                delta_days = (parse(now_date) - parse(data[1])).days
                drawing_data['NUMS'][NoName]['AGO'] = delta_days
                # sum_1_6 = summ(int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7]))
                # сортировка nums, собранных в dict, в порядке hot -> cold (по уменьшению частотности):
                dict_hot_cold = dict(drawing_data['HOT'])
                drawing_data['HOT'] = dict(sorted(dict_hot_cold.items(), key=lambda x: x[1], reverse=True))

            # print(drawing_data)
            json_data = json.dumps(drawing_data)

            # progress bar
            if int(data[0]) % 100 == 0:  # '% 1' красивее, но медленно
                print(data[0] + '... ', sep=' ', end=('\b'*(len(data[0]) + 4)))

            recepient.write(json_data + '\n')  # в файл записывается JSON с текущими значениями hot/cold
            # recepient.write(line)   # в файл ранее записывалась исходная строка

        dict_hot_cold = dict(drawing_data['HOT'])
        # output json_data with result to console
        # json_data = json.dumps(drawing_data, indent=2)
        # print('\n', json_data)     # str
        # print('\n', drawing_data)     # str


# HOT/COLD номера для количества тиражей, находящихся в df
print('HOT/COLD НОМЕРА ДЛЯ', amount_of_draws, 'ПОСЛЕДНИХ ТИРАЖЕЙ')
print('=' * (20 + len(str(amount_of_draws)) + 18))
list_hot_cold = list(dict_hot_cold.keys())  # в list_hot_cold пока str
list_hot_cold = [ int(i) for i in list_hot_cold ]  # в list_hot_cold уже int
print('Ряд номеров от самых "горячих" к самым "холодным":')
print(*dict_hot_cold, '\n')
print('''Подробные сведения сведены в таблицу, где: Num - номер,
FR - количество выпадений номера за выбранный период,
LST - дата, когда последний раз выпадал данный номер,
DRW - номер тиража, когда номер выпадал в последний раз,
AGO - сколько дней назад последний раз выпадал номер\n''')
print('NUM', '\t', 'FR', '\t', 'LST', '\t\t', "DRW", '\t', 'AGO')
for i in range(0, 49):
    # print(list_hot_cold[i], sep=' ', end=' ')
    print(
        list_hot_cold[i], '\t',
        drawing_data['NUMS']['No' + str(list_hot_cold[i])]['FREQ'], '\t',
        drawing_data['NUMS']['No' + str(list_hot_cold[i])]['LSTDAT'], '\t',
        drawing_data['NUMS']['No' + str(list_hot_cold[i])]['LSTDRW'], '\t',
        drawing_data['NUMS']['No' + str(list_hot_cold[i])]['AGO'], '\t',
        sep=' ', end='\n')
# print('Hot -> Cold sorted:\n', dict(sorted(dict_hot_cold.items(), key=lambda x: x[1], reverse=True)))
print()












# Результаты последнего тиража:
fn.last_drawing_statistic(df)
# Результаты X последних тиражей:
# (сейчас отключено т.к. ниже показываются в более интересном варианте)
# fn.results_of_x_last_drawing(COUNTER_USER_ANALYZE, df, 'N6')
logging.info('Выдана статистика по самому последнему тиражу')

# Упрощение датафрейма (ненужные для расчётов столбцы исключаются):
df = pd.read_csv('lotter_results.csv', index_col='DRAW', usecols=['DRAW', 'DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6'])
# В датафрейм (после расчёта) добавляются дополнительные столбцы:
fn.add_columns_to_database(df)

# Вывод аномальных распределений номеров результатов тиражей:
if DF_STATISTIC_ANOMALIC == 1:
    fn.anomal_results_drawing(COUNTER_ANOMALIC_DRAWS, df)
    logging.info('Сформирована статистика датафрейма по аномальным результатам')


# Построение графиков распределения номеров по 6 каналам и распределений
# значений словарей, созданных из дополнительных столбцов датафрейма:
if BUILD_GRAPH == 1:  # DF_STATISTIC_CLASSIC == 1 and
    logging.info('Построение графиков со статистикой')
    print('ПОСТРОЕНИЕ ГРАФИКОВ СО СТАТИСТИКОЙ')
    print('=' * 34)
    # График 'распределение номеров по 6 каналам':
    df_freq_all_chanels = pd.read_csv("lotter_results.tmp")  # index_col=False менее наглядно
    fn.graph_df_all_channels(df_freq_all_chanels)
    logging.info('- построен график "распределение номеров по 6 каналам"')
    del(df_freq_all_chanels)
    # График 'DEC': распределение номеров по декадам
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
    logging.info('- построен график DEC "распределение номеров по декадам"')
    # График 'ODD': количество нечётных номеров в тираже
    fn.graph_from_dict(
        df,
        df_column='ODD',
        graph_title='распределение нечётных номеров по тиражам',
        graph_x ='количество нечётных номеров в одном тираже',
        graph_y ='количество тиражей',
        graph_color = 'b',
        graph_legend='количество\nнечётных\nномеров',
        graph_file_name='lotter_graph_odd_numbers.png'
        )
    logging.info('- построен график ODD "распределение нечётных номеров по тиражам"')
    # График 'EVN': количество чётных номеров в тираже
    fn.graph_from_dict(
        df,
        df_column='EVN',
        graph_title='распределение чётных номеров по тиражам',
        graph_x ='количество чётных номеров в одном тираже',
        graph_y ='количество тиражей',
        graph_color = 'g',
        graph_legend='количество\nчётных\nномеров',
        graph_file_name='lotter_graph_evn_numbers.png'
        )
    logging.info('- построен график EVN "распределение чётных номеров по тиражам"')
    # График 'RPT': количество повторов номеров из предыдущего тиража
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
    logging.info('- построен график RPT "количество повторов номеров из предыдущего тиража"')
    # График 'DIF': разность между номерами N6 и N1
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
    logging.info('- построен график DIF "распределение разностей между самым большим и самым маленьким номерами"')
    # График 'SUM': сумма выпавших в тираже номеров
    fn.graph_from_dict(
        df,
        df_column='SUM',
        graph_title='сумма всех номеров, выпавших в тираже',
        graph_x ='сумма выпавших в тираже номеров',
        graph_y ='количество тиражей',
        graph_color = 'b',
        graph_legend='величина\nсуммы\nномеров',
        graph_file_name='lotter_graph_summ_numbers.png'
        )
    logging.info('- построен график SUM "распределение сумм номеров, выпавших в одном тираже"')
    print()

# Полная статистика архива тиражей в словарях
# fn.dict_with_full_statistic(df)

# Результаты X последних тиражей с дополнительными столбцами:
fn.results_of_x_last_drawing(COUNTER_USER_ANALYZE, df, 'SUM')
logging.info('Выдан отчёт по заданному в "lotter.ini" количеству последних тиражей')

print(COUNTER_USER_ANALYZE)




logging.info('Работа программы успешно завершена, ожидается нажатие "ENTER"')
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
