# -*- coding: utf-8 -*-
"""
"Спортлото 6/49" – электронная интерактивная игра, аналог советского "Спортлото 6/49".
В ходе розыгрыша из лототрона, в котором находится 49 шаров с номерами от 1 до 49, случайным образом выпадают 6 шаров, образующих призовую комбинацию. Цель игры - угадать как можно больше выпавших в лототроне чисел. Участник, угадавший все 6 выпавших шаров, становится обладателем джекпота!
Сделать ставку просто: Выберите 6 чисел из 49, отметив соответствующие значения в игровом поле. Вы можете заполнить несколько игровых полей и/или выбрать несколько розыгрышей, в которых ваша комбинация (комбинации) будет принимать участие. Стоимость участия в игре определяется путем умножения стоимости одной комбинации (4 рубля) на выбранное количество комбинаций и количество розыгрышей.
В ходе розыгрыша из лототрона, в котором находится 49 шаров с номерами от 1 до 49, случайным образом выпадают 6 шаров, образующих призовую комбинацию. Процесс происходит автоматически без участия человека и без возможности повлиять на результаты розыгрыша. Розыгрыши проводятся в присутствии тиражной комиссии, которая фиксирует порядок выпадения шаров в протоколе.
Розыгрыши "Спортлото 6 из 49" проходят 4 раза в неделю в эфире телеканала "Беларусь 2", а также на YouTube-канале компании.
		Понедельник - 21:10
		Вторник - 21:10
		Четверг - 21:10
		Суббота - 21:10
	Время проведения розыгрышей может смещаться по эфирной сетке из-за трансляций спортивных мероприятий.
	В день проведения розыгрыша прием ставок прекращается в 20:50.

Минимальный выигрыш - 3 угаданных числа. Выигрыш 3 из 6 является фиксированным и на данный момент составляет 20 рублей. Выплаты за совпадение 4 и более чисел формируются в зависимости от общего количества ставок, сделанных участниками. Средства призового фонда распределяются следующим образом:
		совпадение 6 чисел (джекпот, 1 категория) – 35% выигрышного фонда тиража;
		совпадение 5 чисел (2 категория) – 50% от разницы выигрышного фонда тиража и выплат за первую и четвертую категории данного тиража;
		совпадение 4 чисел (3 категория) – 50% от разницы выигрышного фонда тиража и выплат за первую и четвертую категории данного тиража;
		совпадение 3 чисел (4 категория) – фиксированная выплата, установленная организатором.
Джекпот формируется за счёт средств доли категории 1, которые переходят из тиража в тираж до тех пор, пока в данной категории не появится хотя бы один победитель.
Результаты тиражей можно узнать на сайте и в мобильном приложении, в точках продаж ЗАО "Спорт-пари", а также по телефону Горячей линии 143.
	Результаты тиража становятся доступны на сайте и в мобильном приложении в течение 10-30 минут после прямого эфира.
Выплата выигрышей начинается не позднее 11:00 дня, следующего за днём проведения розыгрыша призового фонда тиража.
	Выигрыш за ставки, сделанные на сайте sportpari.by и в мобильном приложении, можно получить перечислением на банковскую карту (данная опция станет доступна в ближайшее время), которая была привязана к игровому аккаунту, либо зачислить на игровой счёт. Обратите внимание, что деньги, зачисленные на игровой счёт, не подлежат выплате и предназначены только для оплаты ставок. Также выигрыши в игре в зависимости от его размера можно получить наличными в фирменных точках продаж компании "Спорт-пари" и на некоторых дилерских точках продаж.
	Расположение ближайших точек продаж "Спорт-пари", где возможно получить выигрыш, можно узнать по телефону Горячей линии 143.
Чек-прогноз принимается к оплате в течение 6 месяцев, начиная со дня проведения розыгрыша призового фонда тиража.
"""
"""
мода — значение, которое встречается в выборке чаще всего;
медиана — «серединное» значение. Если построить все данные в ряд по возрастанию, медианное значение окажется ровно посреди ряда: одна половина значений меньше, а другая половина больше. Медиана отличается от среднего тем, что не так чувствительна к аномально высоким или низким значениям;
процентили, или перцентили — по смыслу похожи на медиану, но находятся не посередине. Например, 25 перцентиль означает, что 25% значений в выборке меньше него, а остальные больше;
среднее — имеется в виду среднее арифметическое, когда все значения складывают и делят на их количество. В отличие от медианы, не учитывает разброс;
минимум и максимум — самое маленькое и самое большое значения;
размах — разница между минимумом и максимумом;
дисперсия — уровень разброса значений относительно определенной точки. В качестве точки может выступать среднее, медиана, истинное или целевое значение — зависит от ситуации. Если все данные в выборке близки к этой точке — дисперсия низкая. Тогда говорят, что у данных высокая кучность. А если результаты «разбросаны» в большом диапазоне относительно точки, дисперсия высокая;
смещение — нежелательные связи между данными — то, насколько данные и выводы из них «смещены» относительно реальной ситуации;
выборка — определенный набор данных, который отражает реальную ситуацию. Выборка должна быть репрезентативной. Это значит, что в ней нужно передать реальную картину происходящего — в статистике говорят «свойства генеральной совокупности»;
семплирование или семплинг — набор методов, которые помогают сделать выборку релевантной. Семплирование помогает составить правила для отбора данных в выборку. У него две главных цели: репрезентативность (выборка отражает реальную ситуацию) и полнота (данных хватает для полноценного анализа);
мажоритарный класс данных — класс большего размера;
миноритарный класс данных — класс меньшего размера;
оверсемплинг — способ, когда данные в минориторном классе клонируют, чтобы их стало больше. Причем клонируют так, чтобы не нарушить изначальные соотношения значений и распределение.
андерсемплинг — способ, когда мажоритарный класс уменьшают. Проще всего убрать случайные значения, но чаще уменьшение опять же делается так, чтобы не нарушить соотношения.
снижение размерности — уменьшение количества переменных, отбрасывание лишнего. У снижения размерности есть два основных способа:
отбор признаков — с помощью формул и векторных преобразований специалисты решают, какие признаки связаны с результатом или целевым показателем, а какие нет. Незначительные признаки отбрасывают;
проекция признаков — показатели представляют на графике, а потом уменьшают размерность этого графика. Например, изначально он трехмерный — его делают двумерным. Некоторые точки трехмерного графика накладываются друг на друга и в двумерной версии выглядят как одна точка. Переменных становится меньше.
Равномерное распределение: когда есть конкретные диапазоны значений со статичной вероятностью. График распределения состоит из прямых, горизонтальных и вертикальных линий.
Нормальное распределение: встречается чаще всего. Распределение на графике выглядит как холм, который называют колоколом Гаусса или гауссианой. Колокол показывает: вероятность получить «среднее» значение больше всего. Чем больше отклонение от среднего, тем ниже вероятность. Для самых низких или высоких значений вероятность особенно низкая. Колокол может быть сдвинут влево или вправо относительно среднего — по медиане.
Распределение Пуассона: в некоторых случаях очень похоже на нормальное. Распределение используют для анализа количества тиражей за определенный промежуток времени. События должны быть не связаны друг с другом. У распределения Пуассона есть дополнительный показатель интенсивности, который влияет на форму графика: чем выше, тем больше похоже на гауссиану.
Корреляция — явление, когда изменение одного показателя похоже на изменение другого показателя. Например, один растет, другой растет. Или один растет, другой падает — обратная корреляция. Линейная корреляция — один показатель меняется, другой меняется пропорционально первому. Нелинейная корреляция — показатели меняются непропорционально друг другу, а, например, экспоненциально.
Байесианская вероятность  — теорема Байеса помогает подсчитать вероятность события с учетом каких-то гипотетических новых факторов. Классическая вероятность считается только с учетом так называемых априорных факторов: тех, что даны изначально. Если в процессе появится новое предположение или гипотеза, классическая вероятность это не учтет. А байесианская  — учтет.
"""

import loter_func

import pandas as pd
import numpy as np
import math

import datetime
from time import sleep   # только для засыпания перед нештатным exit()
from dateutil.parser import parse
import json
# import csv


import os
import secrets



"""РАЗНЫЕ ДАННЫЕ, СПИСКИ И СЛОВАРИ, КОТОРЫЕ БУДУТ ИСПОЛЬЗОВАТЬСЯ"""
# Число последних тиражей, которые будут анализироваться в секции рекомендаций
# (параметр может быть переназначен пользовательским вводом ниже по тексту)
count_of_draw_for_analyze = 18;

# Текущая дата для расчётов 'сколько дней назад выпадал номер'
now_date = datetime.date.today().isoformat()

# Структуры данных, которые будут использоваться:
list_49_of_0 = [ 0 for i in range(49) ]  # список "49 нулей"
list_from_1_to_49 = [ i for i in range(1, 50) ]  # список "номера от 1 до 49"
dict_49_of_0 = dict.fromkeys(list_from_1_to_49, 0)  # словарь "49 нулей" из списка

# генерация множества "номера от 1 до 49" с помощью range():
# range_1_49 = range(1, 50)
# set_1_49 = set(range_1_49)

"""ГОТОВО: ПУСТОЙ ДАТАФРЕЙМ ДЛЯ ЗАПИСИ В EXEL
# датафрейм df_red_num со столбцами: N1Freq, N1LastDraw, N1LastDate, N1DayAgo, ... N49Freq, N49LastDraw, N49LastDate, N49DayAgo
columns_for_df_red_num = ["Draw", "Date"]
for i in range(1, 50, 1):
    columns_for_df_red_num.append('N' + str(i) + 'Freq')
    columns_for_df_red_num.append('N' + str(i) + 'LastDraw')
    columns_for_df_red_num.append('N' + str(i) + 'LastDate')
    columns_for_df_red_num.append('N' + str(i) + 'DayAgo')
    columns_for_df_red_num.append('N' + str(i) + 'Repeat')
df_red_num = pd.DataFrame(columns=columns_for_df_red_num)
df_red_num.fillna(0)
"""

# задаём структуру словаря 'drawData' для будущей JSON-структуры
# эту JSON-структуру будем построчно записывать в 'loter_results.tmp' т.к. после каждого тиража статистика изменяется
drawData = {
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
# ниже закомментирован тест взаимной конвертации DICT в JSON и JSON в DICT:
# print(drawData)
# jsonData = json.dumps(drawData)   #, indent=2)
# print(drawData)       # тип dict
# print(jsonData)       # тип str
# jsonData = '{"Draw": {"DrawNum": 0, "DrawDate": "0000-00-00", "DrawResult": [0, 0, 0, 0, 0, 0]}, "Nums": {"Num1": {"Num": 1, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num2": {"Num": 2, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num3": {"Num": 3, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num4": {"Num": 4, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num5": {"Num": 5, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num6": {"Num": 6, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num7": {"Num": 7, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num8": {"Num": 8, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num9": {"Num": 9, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num10": {"Num": 10, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num11": {"Num": 11, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num12": {"Num": 12, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num13": {"Num": 13, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num14": {"Num": 14, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num15": {"Num": 15, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num16": {"Num": 16, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num17": {"Num": 17, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num18": {"Num": 18, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num19": {"Num": 19, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num20": {"Num": 20, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num21": {"Num": 21, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num22": {"Num": 22, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num23": {"Num": 23, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num24": {"Num": 24, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num25": {"Num": 25, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num26": {"Num": 26, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num27": {"Num": 27, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num28": {"Num": 28, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num29": {"Num": 29, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num30": {"Num": 30, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num31": {"Num": 31, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num32": {"Num": 32, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num33": {"Num": 33, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num34": {"Num": 34, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num35": {"Num": 35, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num36": {"Num": 36, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num37": {"Num": 37, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num38": {"Num": 38, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num39": {"Num": 39, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num40": {"Num": 40, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num41": {"Num": 41, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num42": {"Num": 42, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num43": {"Num": 43, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num44": {"Num": 44, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num45": {"Num": 45, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num46": {"Num": 46, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num47": {"Num": 47, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num48": {"Num": 48, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}, "Num49": {"Num": 49, "Frequency": 0, "LastDraw": 0, "LastDate": "0000-00-00", "DayAgo": 0}}}'
# dictData = json.loads(jsonData)
# print(jsonData)       # тип str
# print(dictData)       # тип dict



"""ГОТОВО: ПРОВЕРКА НАЛИЧИЯ ФАЙЛА С АРХИВОМ ТИРАЖЕЙ, ЕГО АКТУАЛИЗАЦИЯ"""

print('\nПредварительная проверка наличия и актуализация базы тиражей:')
print('- текущая рабочая директория', os.getcwd())
# Находится ли файл с архивом тиражей loter_results.xlsx в текущей директории:
list_of_dir = os.listdir()

other_xlsx_files = []  # для хранения имён типа 'game results 6-49 (06.10.2024 01_41_47).xlsx'
for i in range(0, len(list_of_dir)):
    if 'game results 6-49' in list_of_dir[i]:
        other_xlsx_files.append(list_of_dir[i])

if 'loter_results.xlsx' in list_of_dir:
    # есть ли в директории файл - архив тиражей с правильным именем:
    print('- файл с архивом тиражей находится в текущей директории')
    # дата модификации файла в формате количества секунд, прошедших с начала эпохи:
    time_loter_results = os.path.getmtime(r'loter_results.xlsx')
elif ('loter_results.xlsx' not in list_of_dir) and (len(other_xlsx_files) != 0):
    # если нет файла с правильным именем, но есть хоть один файл загруженный с сайта лотерей
    os.rename(other_xlsx_files[0], 'loter_results.xlsx')
    other_xlsx_files.remove(other_xlsx_files[0])
    time_loter_results = os.path.getmtime(r'loter_results.xlsx')
    print('- файл, загруженный с сайта лотерей, переименован для дальнейших тестов')
else:
    # если нет никаких файлов с архивами тиражей, завершаем работу
    print('- файл с архивом тиражей в текущей директории отсутствует\n\nЗавершение работы программы...')
    del(list_of_dir)
    sleep(5)
    exit()

# Если в директории есть файлы вида 'game results 6-49 (07.10.2024 21_28_50).xlsx'
if len(other_xlsx_files) != 0:
    print('- в директории имеются альтернативные файлы с архивами тиражей')
    while len(other_xlsx_files) != 0:
        for f in other_xlsx_files:
            # сравнение времени модификации файлов (в виде количества секунд, прошедших с начала эпохи)
            if time_loter_results < os.path.getmtime(f):
                # loter_results.xlsx более старый, чем f. Удаление старого loter_results.xlsx
                os.remove('loter_results.xlsx')
                os.rename(f, 'loter_results.xlsx')
                other_xlsx_files.remove(f)
                time_loter_results = os.path.getmtime(r'loter_results.xlsx')
            else:
                # loter_results.xlsx новее, чем f. Удаление файла f
                os.remove(f)
                other_xlsx_files.remove(f)
    print('- оставлен наиболее актуальный файл с архивом тиражей, старые файлы удалены')
else:
    print('- других (непереименованных) файлов с архивами тиражей нет')
del(list_of_dir)


print('\n**************************** LOTER 6.49', now_date, '****************************\n')
print('''При обработке результатов тиражей будут введены следующие сокращения:
    BLU: количество выпавших 'blue' ('cold', 'синих') номеров по состоянию на прошлый тираж
    DEC: декады - например, для тиража 5 10 25 27 35 40 параметр DEC=012234
    DIF: разность между самым маленьким и самым большим номером тиража
    EVN: количество чётных номеров в состоявшемся или прогнозируемом тираже
    ODD: количество нечётных номеров в состоявшемся или прогнозируемом тираже
    RED: количество выпавших 'red' ('red', 'красных') номеров по состоянию на прошлый тираж
    RPT: количество повторившихся номеров из предыдущего тиража
    SUM: сумма всех номеров состоявшегося или прогнозируемого тиража\n''')

# Импорт данных из *.XLSX в *.CSV - пока без этого
"""excel_data = pd.read_excel('loter_results.xlsx',
                            sheet_name='results',
                            usecols=['Тираж', 'Дата', 'Шар 1', 'Шар 2', 'Шар 3', 'Шар 4', 'Шар 5', 'Шар 6', '6 чисел угадали', 'Выигрыш', '5 чисел угадали', 'Выигрыш', '4 числа угадали', 'Выигрыш', '3 числа угадали', 'Выигрыш', 'Джек-пот', 'Призовой фонд'],
                            dtype={'Тираж': int, 'Дата': object, 'Шар 1': int, 'Шар 2': int, 'Шар 3': int, 'Шар 4': int, 'Шар 5': int, 'Шар 6': int,
                                   })
"""
excel_data = pd.read_excel('loter_results.xlsx', sheet_name='results', usecols=[x for x in range(18)])

columns_new_names = ['DRAW', 'DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6',
                    'WIN6', 'BNS6', 'WIN5', 'BNS5', 'WIN4', 'BNS4',
                    'WIN3', 'BNS3', 'JACK', 'FOND']
excel_data.to_csv('loter_results.csv', header=columns_new_names, index=False, sep=';', lineterminator=';\n', encoding='utf8')

# Настройка вывода Pandas в консоль:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
# Формирование датафрейма из Excel-файла ------------------------------------
# df_temp - временный датафрейм, содержащий все столбцы Excel-файла
df_temp = pd.read_excel("loter_results.xlsx",
                    sheet_name='results',
                    index_col='Тираж',  # нужно чтобы индексным столбцом был именно 'Тираж'
                    )
'''
Проблема:
Столбцы Excel-файла имеют следующие названия: 'Тираж', 'Дата', 'Шар 1',
'Шар 2', 'Шар 3', 'Шар 4', 'Шар 5', 'Шар 6', '6 чисел угадали', 'Выигрыш',
'5 чисел угадали', 'Выигрыш', '4 числа угадали', 'Выигрыш', '3 числа угадали',
'Выигрыш', 'Джек-пот', 'Призовой фонд'. Срели них есть 4 столбца с одинаковым
названием 'Выигрыш', что не даёт возможности сохранить структуру датафрейма
при их переименовании. Из четырёх этих столбцов по итогу остаётся только один.
Решение:
Читать данные из таких столбцов датафрейма по номеру столбца в списки
'''
listWIN6 = df_temp.iloc[:,7].tolist()
listBYN6 = df_temp.iloc[:,8].tolist()
listWIN5 = df_temp.iloc[:,9].tolist()
listBYN5 = df_temp.iloc[:,10].tolist()
listWIN4 = df_temp.iloc[:,11].tolist()
listBYN4 = df_temp.iloc[:,12].tolist()
listWIN3 = df_temp.iloc[:,13].tolist()
listBYN3 = df_temp.iloc[:,14].tolist()
listJACK = df_temp.iloc[:,15].tolist()
listFOND = df_temp.iloc[:,16].tolist()

'''print('listWIN6 = ', listWIN6)
print('listBYN6 = ', listBYN6)
print('listWIN5 = ', listWIN5)
print('listBYN5 = ', listBYN5)
print('listWIN4 = ', listWIN4)
print('listBYN4 = ', listBYN4)
print('listWIN3 = ', listWIN3)
print('listBYN3 = ', listBYN3)
print('listJACK = ', listJACK)
print('listFOND = ', listFOND)'''

df = pd.read_excel("loter_results.xlsx",
                    sheet_name='results',
                    index_col='Тираж',  # index_col='Тираж', указать если нужно чтобы индексным столбцом был именно 'Тираж'
                    usecols=['Тираж', 'Дата', 'Шар 1', 'Шар 2', 'Шар 3', 'Шар 4', 'Шар 5', 'Шар 6'])

# Переименование столбцов:
df.index.names = ["DRAW"]
df.rename(columns={'Дата': 'DATE', 'Шар 1': 'N1', 'Шар 2': 'N2', 'Шар 3': 'N3', 'Шар 4': 'N4', 'Шар 5': 'N5', 'Шар 6': 'N6'}, inplace=True)

# полученные ранее списки разворачивается в дополнительные столбцы датафрейма
df["WIN6"] = listWIN6
df["BYN6"] = listBYN6
df["WIN5"] = listWIN5
df["BYN5"] = listBYN5
df["WIN4"] = listWIN4
df["BYN4"] = listBYN4
df["WIN3"] = listWIN3
df["BYN3"] = listBYN3
df["JACK"] = listJACK
df["FOND"] = listFOND


print(df.tail())









'''old:
df = pd.read_excel("loter_results.xlsx",
                    sheet_name='results',
                    index_col='Тираж',  # index_col='Тираж', указать если нужно чтобы индексным столбцом был именно 'Тираж'
                    usecols=[
                        'Тираж', 'Дата', 'Шар 1', 'Шар 2', 'Шар 3', 'Шар 4', 'Шар 5', 'Шар 6',
                        '6 чисел угадали', 'Выигрыш', '5 чисел угадали', 'Выигрыш',
                        '4 числа угадали', 'Выигрыш', '3 числа угадали', 'Выигрыш',
                        'Джек-пот', 'Призовой фонд'
                        ])
'''









print(list(df.columns))


df.rename(columns={'Дата': 'DATE', 'Шар 1': 'N1', 'Шар 2': 'N2', 'Шар 3': 'N3', 'Шар 4': 'N4', 'Шар 5': 'N5', 'Шар 6': 'N6',
'6 чисел угадали': 'WIN6', 'Выигрыш': 'BYN6', '5 чисел угадали': 'WIN5', 'Выигрыш': 'BYN5',
'4 числа угадали': 'WIN4', 'Выигрыш': 'BYN4', '3 числа угадали': 'WIN3', 'Выигрыш': 'BYN3',
'Джек-пот': 'JACK', 'Призовой фонд': 'FOND'}, inplace=True)









# df.to_csv('loter_results.csv', encoding='utf-8')
# Перевод текстовой даты '31.12.2023' в настоящий тип datetime '2023-12-31'
df["DATE"] = pd.to_datetime(df["DATE"], format='%d.%m.%Y')


# Сортировка номеров тиража по порядку (изначально они в том порядке, в котором выпадали)
df[["N1", "N2", "N3", "N4", "N5", "N6"]] = df[["N1", "N2", "N3", "N4", "N5", "N6"]].apply(lambda x: np.sort(x), axis=1, raw=True)

# Добавление в датафрейм дополнительных столбцов:
# DEC - распределение выпавших номеров по десяткам
df["DEC"] = (df["N1"] // 10).astype(str) + (df["N2"] // 10).astype(str) + (df["N3"] // 10).astype(str) + (df["N4"] // 10).astype(str) + (df["N5"] // 10).astype(str) + (df["N6"] // 10).astype(str)
# ODD - количество нечётных номеров
df["ODD"] = df["N1"] % 2 + df["N2"] % 2 + df["N3"] % 2 + df["N4"] % 2 + df["N5"] % 2 + df["N6"] % 2
# EVN - количество чётных номеров: просто как число всех номеров минус количество чётных
df["EVN"] = 6 - df["ODD"]

# RPT - количество повторившихся номеров из прошлого тиража
repeat_nums_list = []  # список, в который соберём количество повторов
numbers_in_past_draw = [0, 0, 0, 0, 0, 0]  # список для хранения результата прошлого тиража
for i in range(0, len(df)):
    numbers_in_this_draw = [int(df.iloc[i, 1]), int(df.iloc[i, 2]), int(df.iloc[i, 3]), int(df.iloc[i, 4]), int(df.iloc[i, 5]), int(df.iloc[i, 6])]
    # количество совпадений = длине пересечения двух множеств-результатов прошлого и нынешнего тиражей:
    repeat_nums = len((set(numbers_in_past_draw)).intersection(set(numbers_in_this_draw)))
    # накопление количества совпадений в списке:
    repeat_nums_list.append(repeat_nums)
    numbers_in_past_draw = numbers_in_this_draw
    i += 1
# полученный список разворачивается в дополнительный столбец датафрейма
df["RPT"] = repeat_nums_list

# DIF - разница между номерами: самым большим (N6) и самым маленьким (N1)
df["DIF"] = df["N6"] - df["N1"]
# SUM - сумма номеров
df["SUM"] = df["N1"] + df["N2"] + df["N3"] + df["N4"] + df["N5"] + df["N6"]

# Печать фрагмента полученного датафрейма (для контроля)
# print('Последний тираж в базе данных:')
# print(df.loc[:, "DATE":"SUM"].tail(1).sort_values(by="DRAW", ascending=False), '\n')
df.to_csv('loter_results.csv', encoding='utf-8')
# print('Импорт данных из файла \'loter_results.xlsx\' в файл \'loter_results.csv\' и датафрейм завершён')
# копирование файла 'loter_results.csv' в 'loter_results.tmp' пока не используется
# shutil.copy('loter_results.csv', 'loter_results.tmp')



"""ГОТОВО: СТАТИСТИКА ПО ПОЛНОЙ БАЗЕ И САМЫЕ НЕОБЫЧНЫЕ РЕЗУЛЬТАТЫ"""
print('ОБЩАЯ СТАТИСТИКА ПО ПОЛНОЙ БАЗЕ ТИРАЖЕЙ:\n')
amount_of_draws = len(df)
print('- число тиражей в базе', amount_of_draws)
print('- последний', amount_of_draws, '\b-ой тираж состоялся', df["DATE"][amount_of_draws].date(), 'с результатами:', df['N1'][amount_of_draws], df['N2'][amount_of_draws], df['N3'][amount_of_draws], df['N4'][amount_of_draws], df['N5'][amount_of_draws], df['N6'][amount_of_draws], '\n')
print('- результаты 10 последних тиражей отсортированные по убыванию:')
print(df.loc[:, "DATE":"SUM"].tail(10).sort_values(by="DRAW", ascending=False), '\n')

C_5_48 = int(math.factorial(48) / (math.factorial(5) * math.factorial(48-5)))
C_6_49 = int(math.factorial(49) / (math.factorial(6) * math.factorial(49-6)))    # 13.983.816
print('- число возможных комбинаций 6 номеров из 49 =', C_6_49)
print('- число перестановок для 6 номеров =', math.factorial(6))  # 720
print('- вероятность выпадения в тираже одного номера =', round((C_5_48 / C_6_49), 5))  # 0.12245
print('- вероятность выпадения в тираже пары номеров =', round(((1 / 49) * (5 / 48)), 5))  # 0.00213
print('- вероятность выпадения в тираже тройки номеров =', round(((1 / 49) * (5 / 48) * (4 / 47)), 5), '\n')  # 0.00018
print('- основные статистические характеристики базы тиражей по pandas.df.describe():')  # статистика, выводимая с помощью df.describe()
'''
print(round(df.describe()), '\n')
print('"count" - число непропущенных значений датафрейма\n\
"std" - стандартн.отклонение, среднеквадратичный разброс относительно мат.ожидания\n\
"min" - минимальное значение в датафрейме\n\
"25%" - нижний процентиль, 25% значений в датафрейме меньше этого значения\n\
"50%" - 0.5 процентиль, среднее значение\n\
"mean" - медиана, одна половина значений меньше неё, а другая половина больше\n\
"75%" - верхний процентиль, 75% значений в датафрейме меньше этого значения\n\
"max" - максимальное значение в датафрейме', '\n')
'''
# Данные из df.describe() сперва собираем в соответствующие списки:
list_pandas_mean = [int((df.describe()['N1']['mean']).round(0)), int((df.describe()['N2']['mean']).round(0)), int((df.describe()['N3']['mean']).round(0)), int((df.describe()['N4']['mean']).round(0)), int((df.describe()['N5']['mean']).round(0)), int((df.describe()['N6']['mean']).round(0))]  #, int((df.describe()['SUM']['mean']).round(0)), int((df.describe()['DIF']['mean']).round(0))]
list_pandas_min = [int(df.describe()['N1']['min']), int(df.describe()['N2']['min']), int(df.describe()['N3']['min']), int(df.describe()['N4']['min']), int(df.describe()['N5']['min']), int(df.describe()['N6']['min'])]  #, int(df.describe()['SUM']['min']), int(df.describe()['DIF']['min'])]
list_pandas_25p = [int(df.describe()['N1']['25%']), int(df.describe()['N2']['25%']), int(df.describe()['N3']['25%']), int(df.describe()['N4']['25%']), int(df.describe()['N5']['25%']), int(df.describe()['N6']['25%'])]  #, int(df.describe()['SUM']['25%']), int(df.describe()['DIF']['25%'])]
list_pandas_50p = [int(df.describe()['N1']['50%']), int(df.describe()['N2']['50%']), int(df.describe()['N3']['50%']), int(df.describe()['N4']['50%']), int(df.describe()['N5']['50%']), int(df.describe()['N6']['50%'])]  #, int(df.describe()['SUM']['50%']), int(df.describe()['DIF']['50%'])]
list_pandas_75p = [int(df.describe()['N1']['75%']), int(df.describe()['N2']['75%']), int(df.describe()['N3']['75%']), int(df.describe()['N4']['75%']), int(df.describe()['N5']['75%']), int(df.describe()['N6']['75%'])]  #, int(df.describe()['SUM']['75%']), int(df.describe()['DIF']['75%'])]
list_pandas_max = [int(df.describe()['N1']['max']), int(df.describe()['N2']['max']), int(df.describe()['N3']['max']), int(df.describe()['N4']['max']), int(df.describe()['N5']['max']), int(df.describe()['N6']['max'])]  #, int(df.describe()['SUM']['max']), int(df.describe()['DIF']['max'])]
print('минимальные номера:\t', *list_pandas_min, '\b,', loter_func.search_in_dataframe(list_pandas_min, df))
print('25% номеров <= чем:\t', *list_pandas_25p, '\b,', loter_func.search_in_dataframe(list_pandas_25p, df))
print('50% номеров <= чем:\t', *list_pandas_50p, '\b,', loter_func.search_in_dataframe(list_pandas_50p, df))
print('медианное значение:\t', *list_pandas_mean, '\b,', loter_func.search_in_dataframe(list_pandas_mean, df))
print('75% номеров <= чем:\t', *list_pandas_75p, '\b,', loter_func.search_in_dataframe(list_pandas_75p, df))
print('максимальные номера:\t', *list_pandas_max, '\b,', loter_func.search_in_dataframe(list_pandas_max, df), '\n')


# HOT/COLD номера по 6 каналам для всех тиражей -------------------------------
print("- распределение горячих/холодных номеров по 6 каналам для", amount_of_draws, "тиражей:")
# с помощью value_counts() можно подсчитать частоту появления номеров по каждому из каналов
# и сформировать новый dataframe_freq_all_chanels с общим результатом по всем каналам
# т.к. при формировании датафрейма данные д.быть одного размера (а в каналах есть не все номера),
# функция 'add_0_to_not_full_dict()' добавит в словари недостающие keys с нулевыми values
dict_freq_chanel_1 = loter_func.add_0_to_not_full_dict(dict(df.N1.value_counts()))
dict_freq_chanel_2 = loter_func.add_0_to_not_full_dict(dict(df.N2.value_counts()))
dict_freq_chanel_3 = loter_func.add_0_to_not_full_dict(dict(df.N3.value_counts()))
dict_freq_chanel_4 = loter_func.add_0_to_not_full_dict(dict(df.N4.value_counts()))
dict_freq_chanel_5 = loter_func.add_0_to_not_full_dict(dict(df.N5.value_counts()))
dict_freq_chanel_6 = loter_func.add_0_to_not_full_dict(dict(df.N6.value_counts()))
# исходные данные для датафрейма - словарь списков. добавить "No": list_from_1_to_49, если понадобится
dict_freq_all_chanels = {
    "N1": list(dict_freq_chanel_1.keys()), "F1": list(dict_freq_chanel_1.values()),
    "N2": list(dict_freq_chanel_2.keys()), "F2": list(dict_freq_chanel_2.values()),
    "N3": list(dict_freq_chanel_3.keys()), "F3": list(dict_freq_chanel_3.values()),
    "N4": list(dict_freq_chanel_4.keys()), "F4": list(dict_freq_chanel_4.values()),
    "N5": list(dict_freq_chanel_5.keys()), "F5": list(dict_freq_chanel_5.values()),
    "N6": list(dict_freq_chanel_6.keys()), "F6": list(dict_freq_chanel_6.values())
    }
# создание датафрейма 'df_freq_all_chanels'
df_freq_all_chanels = pd.DataFrame(dict_freq_all_chanels)
# запись датафрейма во временный файл 'loter_results.tmp': во-первых - это backup,
# во-вторых - для того, чтобы избавиться от ненужного индексного столбца
# df_freq_all_chanels.to_csv('loter_results.tmp', header=True, index=False, sep=',', lineterminator=',\n', encoding='utf8')
# del(df_freq_all_chanels)
# читаем заново в чистый df_freq_all_chanels
# df_freq_all_chanels = pd.read_csv("loter_results.tmp", index_col=False, usecols=['N1', 'F1', 'N2', 'F2', 'N3', 'F3', 'N4', 'F4', 'N5', 'F5', 'N6', 'F6'])  # index_col=False менее наглядно
print(df_freq_all_chanels.head(13), '\n\n')  # более 13-ти строк выводить нет смысла - появляются повторы в соседних каналах



"""ГОТОВО: АНОМАЛЬНЫЕ РАСПРЕДЕЛЕНИЯ"""
print('САМЫЕ НЕОБЫЧНЫЕ (АНОМАЛЬНЫЕ) РЕЗУЛЬТАТЫ ТИРАЖЕЙ:\n')
n = 5  # количество строк датафрейма, выводимых на печать для примера
print("Встречаются ли среди тиражей такие, в которых выпало по 4, 5, 6 \nномеров из одного десятка и насколько много таких тиражей:\n")
# четыре номера из первого десятка
df_temp = df[(df["N1"] <= 9) & (df["N2"] <= 9) & (df["N3"] <= 9) & (df["N4"] <= 9)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже четыре номера из первого десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# четыре номера из второго десятка
df_temp = df[
    ((df["N1"] >= 10) & (df["N1"] <= 19) & (df["N2"] <= 19) & (df["N3"] <= 19) & (df["N4"] <= 19)) |
    ((df["N2"] >= 10) & (df["N2"] <= 19) & (df["N3"] <= 19) & (df["N4"] <= 19) & (df["N5"] <= 19)) |
    ((df["N3"] >= 10) & (df["N3"] <= 19) & (df["N4"] <= 19) & (df["N5"] <= 19) & (df["N6"] <= 19))
    ]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже четыре номера из второго десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# четыре номера из третьего десятка
df_temp = df[
    (df["N1"] >= 20) & (df["N1"] <= 29) & (df["N2"] <= 29) & (df["N3"] <= 29) & (df["N4"] <= 29) |
    (df["N2"] >= 20) & (df["N2"] <= 29) & (df["N3"] <= 29) & (df["N4"] <= 29) & (df["N5"] <= 29) |
    (df["N3"] >= 20) & (df["N3"] <= 29) & (df["N4"] <= 29) & (df["N5"] <= 29) & (df["N6"] <= 29)
    ]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже четыре номера из третьего десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# четыре номера из четвёртого десятка
df_temp = df[
    (df["N1"] >= 30) & (df["N1"] <= 39) & (df["N2"] <= 39) & (df["N3"] <= 39) & (df["N4"] <= 39) |
    (df["N2"] >= 30) & (df["N2"] <= 39) & (df["N3"] <= 39) & (df["N4"] <= 39) & (df["N5"] <= 39) |
    (df["N3"] >= 30) & (df["N3"] <= 39) & (df["N4"] <= 39) & (df["N5"] <= 39) & (df["N6"] <= 39)
    ]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже четыре номера из четвёртого десятка?")
    print(df_temp.tail(n))
print("таких тиражей", len_df_temp, "\n")
# четыре номера из пятого десятка
df_temp = df[(df["N3"] >= 40) & (df["N3"] <= 49) & (df["N4"] <= 49) & (df["N5"] <= 49) & (df["N6"] <= 49)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже четыре номера из пятого десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# пять номеров из первого десятка
df_temp = df[(df["N1"] <= 9) & (df["N2"] <= 9) & (df["N3"] <= 9) & (df["N4"] <= 9) & (df["N5"] <= 9)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже пять номеров из первого десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# пять номеров из второго десятка
df_temp = df[
    (df["N1"] >= 10) & (df["N1"] <= 19) & (df["N2"] <= 19) & (df["N3"] <= 19) & (df["N4"] <= 19) & (df["N5"] <= 19) |
    (df["N2"] >= 10) & (df["N2"] <= 19) & (df["N3"] <= 19) & (df["N4"] <= 19) & (df["N5"] <= 19) & (df["N6"] <= 19)
    ]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже пять номеров из второго десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# пять номеров из третьего десятка
df_temp = df[
    (df["N1"] >= 20) & (df["N1"] <= 29) & (df["N2"] <= 29) & (df["N3"] <= 29) & (df["N4"] <= 29) & (df["N5"] <= 29) |
    (df["N2"] >= 20) & (df["N2"] <= 29) & (df["N3"] <= 29) & (df["N4"] <= 29) & (df["N5"] <= 29) & (df["N6"] <= 29)
    ]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже пять номеров из третьего десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# пять номеров из четвёртого десятка
df_temp = df[
    (df["N1"] >= 30) & (df["N1"] <= 39) & (df["N2"] <= 39) & (df["N3"] <= 39) & (df["N4"] <= 39) & (df["N5"] <= 39) |
    (df["N2"] >= 30) & (df["N2"] <= 39) & (df["N3"] <= 39) & (df["N4"] <= 39) & (df["N5"] <= 39) & (df["N6"] <= 39)
    ]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже пять номеров из четвёртого десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# пять номеров из пятого десятка
df_temp = df[(df["N2"] >= 40) & (df["N2"] <= 49) & (df["N3"] <= 49) & (df["N4"] <= 49) & (df["N5"] <= 49) & (df["N6"] <= 49)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже пять номеров из пятого десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# шесть номеров из первого десятка
df_temp = df[(df["N1"] <= 9) & (df["N2"] <= 9) & (df["N3"] <= 9) & (df["N4"] <= 9) & (df["N5"] <= 9) & (df["N6"] <= 9)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже шесть номеров из первого десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# шесть номеров из второго десятка
df_temp = df[(df["N1"] >= 10) & (df["N1"] <= 19) & (df["N2"] <= 19) & (df["N3"] <= 19) & (df["N4"] <= 19) & (df["N5"] <= 19) & (df["N6"] <= 19)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже шесть номеров из второго десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# шесть номеров из третьего десятка
df_temp = df[(df["N1"] >= 20) & (df["N1"] <= 29) & (df["N2"] <= 29) & (df["N3"] <= 29) & (df["N4"] <= 29) & (df["N5"] <= 29) & (df["N6"] <= 29)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже шесть номеров из третьего десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# шесть номеров из четвёртого десятка
df_temp = df[(df["N1"] >= 30) & (df["N1"] <= 39) & (df["N2"] <= 39) & (df["N3"] <= 39) & (df["N4"] <= 39) & (df["N5"] <= 39) & (df["N6"] <= 39)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже шесть номеров из четвёртого десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# шесть номеров из пятого десятка
df_temp = df[(df["N1"] >= 40) & (df["N1"] <= 49) & (df["N2"] <= 49) & (df["N3"] <= 49) & (df["N4"] <= 49) & (df["N5"] <= 49) & (df["N6"] <= 49)]
len_df_temp = len(df_temp)
if len_df_temp:
    print("- есть ли в каком-либо тираже шесть номеров из пятого десятка?")
    print(df_temp.tail(n))
    print("таких тиражей", len_df_temp, "\n")
# все номера нечётные
print("Встречаются ли в базе тиражи только с нечётными номерами?")
print(df[df["ODD"] == 6].tail(n), "\n")
# все номера чётные
print("Встречаются ли в базе тиражи только с чётными номерами?")
print(df[df["EVN"] == 6].tail(n), "\n\n")




print('ПОДРОБНАЯ СТАТИСТИКА ПО ПОЛНОЙ БАЗЕ ТИРАЖЕЙ:\n')
print("- ODD: количество нечётных номеров в тираже / количество таких тиражей:")
print(dict(df.ODD.value_counts()), "\n")
print("- EVN: количество чётных номеров в тираже / количество таких тиражей:")
print(dict(df.EVN.value_counts()), "\n")
print("- RPT: количество повторов номеров из прошлого тиража / количество тиражей с повторами:")
print(dict(df.RPT.value_counts()), "\n")
print("- DIF: разность N6 минус N1 в тираже / количество тиражей с такими разностями:")
print(dict(df.DIF.value_counts()), "\n")
print("- SUM: сумма номеров с N1 по N6 в тираже / количество тиражей с такими суммами:")
print(dict(df.SUM.value_counts()), "\n")
print("- DEC: распределение номеров тиража по десяткам / количество тиражей с таким распределением:")
print(dict(df.DEC.value_counts()), "\n\n")



"""ГОТОВО: ГРАФИК распределение номеров по каналам
# построение графика "распределение номеров по каналам" -----------------------
fig, ax = plt.subplots()
df_freq_all_chanels.groupby('N1')['F1'].mean().plot(label=r'$канал\ N1$')
df_freq_all_chanels.groupby('N2')['F2'].mean().plot(label=r'$канал\ N2$')
df_freq_all_chanels.groupby('N3')['F3'].mean().plot(label=r'$канал\ N3$')
df_freq_all_chanels.groupby('N4')['F4'].mean().plot(label=r'$канал\ N4$')
df_freq_all_chanels.groupby('N5')['F5'].mean().plot(label=r'$канал\ N5$')
df_freq_all_chanels.groupby('N6')['F6'].mean().plot(label=r'$канал\ N6$')
plt.xlabel(r'$номера$')
plt.xticks(rotation=0)
plt.ylabel(r'$частота$')
plt.title(r'распределение номеров по каналам N1, N2, N3, N4, N5, N6')
plt.grid(True)
plt.legend(loc='best', fontsize=10)
fig.savefig("results_channels_A-F_from_all_draws.png", transparent=False, dpi=600)
# plt.show()
# /построение графика "распределение номеров по каналам" ----------------------
"""



# обработка данных, полученных от пользователя ================================
print('====== ОБРАБОТКА ДАННЫХ ЗА КОЛИЧЕСТВО ТИРАЖЕЙ, ОПРЕДЕЛЁННЫХ ПОЛЬЗОВАТЕЛЕМ =======\n')
print('Разыгрывают 4 тиража в неделю, 16-18 тиражей в месяц, 104 тиража за полгода.\n\
Каждые 17-19 тиражей имеется 5-7 номеров, которые не выпали за этот период.\n\
За период проведения 30 тиражей обычно выпадают все номера.\n\
Сколько тиражей нужно обработать (обычно считают от 50 до 100)?\t', end='')
# count_of_draw_for_analyze = input()
# ниже - фрагмент для отладки (чтобы постоянно не набирать).
print(count_of_draw_for_analyze)
print()
# проверка данных, полученных от пользователя
tmp_draw_count = int(len(df)) - int(count_of_draw_for_analyze) + 1
if tmp_draw_count <= 0:
    print('\nНеверное количество тиражей!')
    print('Введённое число не должно быть больше числа тиражей, хранящихся в базе!\n')
    exit()

print('результаты последних', count_of_draw_for_analyze, ' х 3 тиражей:')
print(df.tail(int(count_of_draw_for_analyze) * 3).sort_values(by="DRAW", ascending=False), '\n')

# счётчик для формирования датафрейма df_red_num
count_df_red_num = 0

# помещаем в 'loter_results.tmp' столько тиражей, сколько указал пользователь -------
space = 0  # для пропуска тиражей, которые не нужны пользователю
numbers_in_past_draw = [0, 0, 0, 0, 0, 0]  # результат 0-го тиража для начала подсчёта REP с 1-го
with open('loter_results.csv', 'r', encoding='utf-8') as donor:
    with open('loter_results.tmp', 'w', encoding='utf-8') as recepient:
        # useful data parsing:
        for line in donor:
            # line.rstrip('\n')
            data = line.rstrip('\n').split(',')
            if space < tmp_draw_count:
                # progress bar счётчик пропускаемых тиражей -------------------
                # print(str(space) + '... ', sep=' ', end=('\b'*(len(str(space)) + 4)))
                space += 1
                continue
            #print('\b'*(len(str(space)) + 4))
            drawData["Draw"]['DrawNum'] = data[0]
            drawData["Draw"]['DrawDate'] = data[1]
            drawData["Draw"]['DrawResult'] = [int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7])]

            # подсчёт количества нечётных и чётных номеров
            amount_odd = 0
            amount_even = 0
            for i in range(2, 8):
                if (int(data[i])) % 2 == 1:
                    amount_odd += 1
                else:
                    amount_even += 1
            drawData["Draw"]['NumsOdd'] = amount_odd
            drawData["Draw"]['NumsEven'] = amount_even

            # подсчёт сколько номеров из прошлого тиража выпало в этом
            '''
            numbers_in_this_draw = [int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7])]
            drawData["Draw"]["RepeatNums"] = len((set(numbers_in_past_draw)).intersection(set(numbers_in_this_draw)))
            numbers_in_past_draw = [int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7])]
            '''

            for i in range(2, 8):
                NoName = "No" + data[i]
                drawData['Nums'][NoName]['Frequency'] += 1
                drawData['Advices']['Hot/Cold'][str(NoName)[2:]] += 1
                drawData['Nums'][NoName]['LastDraw'] = data[0]
                drawData['Nums'][NoName]['LastDate'] = data[1]
                delta_days = (parse(now_date) - parse(data[1])).days
                drawData['Nums'][NoName]['DayAgo'] = delta_days
                # sum_1_6 = summ(int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7]))
                # сортировка nums, собранных в dict, в порядке hot -> cold (по уменьшению частотности):
                dict_hot_cold = dict(drawData['Advices']['Hot/Cold'])
                drawData['Advices']['Hot/Cold'] = dict(sorted(dict_hot_cold.items(), key=lambda x: x[1], reverse=True))
                # ognevs numbers:

            # print(drawData)
            jsonData = json.dumps(drawData)


            """ГОТОВО: НАПОЛНЕНИЕ ДАТАФРЕЙМА ДЛЯ EXEL
            # собираем датафрейм 'df_red_num' используя словарь 'drawData' ----
            df_red_num.at[count_df_red_num, "Draw"] = drawData["Draw"]['DrawNum']
            df_red_num.at[count_df_red_num, "Date"] = drawData["Draw"]['DrawDate']
            df_red_num.at[count_df_red_num, "Repeat"] = drawData["Draw"]['RepeatNums']
            for o in range(1, 50, 1):
                df_red_num.at[count_df_red_num, 'N' + str(o) + 'Freq'] = drawData['Nums']['No' + str(o)]['Frequency']
                df_red_num.at[count_df_red_num, 'N' + str(o) + 'LastDraw'] = drawData['Nums']['No' + str(o)]['LastDraw']
                df_red_num.at[count_df_red_num, 'N' + str(o) + 'LastDate'] = drawData['Nums']['No' + str(o)]['LastDate']
                df_red_num.at[count_df_red_num, 'N' + str(o) + 'DayAgo'] = drawData['Nums']['No' + str(o)]['DayAgo']
            count_df_red_num += 1  # count_df_red_num должен достигнуть count_of_draw_for_analyze
            # датафрейм 'df_red_num' будет записан в 'loter_red_num.xlsx' позднее
            """


            # progress bar ----------------------------------------------------
            if int(data[0]) % 1 == 0:
                print(data[0] + '... ', sep=' ', end=('\b'*(len(data[0]) + 4)))

            # recepient.write(jsonData + '\n')  # в файл ранее после каждого тиража записывалась структура JSON (hot / cold номера)
            recepient.write(line)

        # ognevs_numbers = list(drawData['Advices']['Ognev'])
        dict_hot_cold = dict(drawData['Advices']['Hot/Cold'])
        # output jsonData with result to console
        # jsonData = json.dumps(drawData, indent=2)
        # print('\n', jsonData)     # str
        # print('\n', drawData)     # str



"""НА БУДУЩЕЕ СНОВА СДЕЛАТЬ ГРАФИКИ
numDraw = count_of_draw_for_analyze
# умножаем на 6, т.к. в одном тираже 6 номеров
numDraw = (int(numDraw)-1) * 6
# срез от введённого тиража до самого недавнего
numXmini = numX[numDraw : len(numX)]
numYmini = numY[numDraw : len(numY)]

print(numXmini, numYmini)

# построение общего графика распределения всех номеров во всех тиражах:

fig, ax = plt.subplots()
# рисовать график точками
plt.scatter(numXmini, numYmini, color="#0000ee")
# подписи графика и осей
plt.title("спортлото 6 из 49")
plt.ylabel("номера")
plt.xlabel("тиражи")
# рисовать сетку по обоим осям
plt.grid()

# диапазон делений на осях
ax.set(xlim=((numDraw/6), count+1), ylim=(0, 50))
# шаг делений по осям: главные деления
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
# шаг делений по осям: вспомогательные деления
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

# метки к делениям по оси Y
Yax = ax.get_yaxis()
Ylabels = Yax.get_ticklabels()
for label in Ylabels:
    # цвет подписи деленений оси Y
    label.set_color('blue')
    # поворот подписей деленений оси Y
    label.set_rotation(0)
    # размер шрифта подписей делений оси Y
    label.set_fontsize(6)

# метки к делениям по оси X
Xax = ax.get_xaxis()
Xlabels = Xax.get_ticklabels()
for label in Xlabels:
    # цвет подписи деленений оси X
    label.set_color('blue')
    # поворот подписей деленений оси X
    label.set_rotation(60)
    # размер шрифта подписей делений оси X
    label.set_fontsize(6)

# можно сохранить в *.pdf или в *.png, но не актуально - если строить график с 1-го тиража, слишком много данных для отображения, всё сливается
# fig.savefig("loter_results6x49.png", transparent=True, dpi=1200)
# рисовать график с 1-го тиража смысла нет - очень плотно получается и ничего не разобрать
# нормальный вариант - если строить график для последних десятков - сотни
plt.show()
"""



"""ГОТОВО: HOT/COLD НОМЕРА ДЛЯ ХХХХ ПОСЛЕДНИХ ТИРАЖЕЙ"""
# HOT/COLD номера для количества тиражей, указанных пользователем =============
print('====== HOT/COLD НОМЕРА ДЛЯ', count_of_draw_for_analyze, 'ПОСЛЕДНИХ ТИРАЖЕЙ ==============================\n')
list_hot_cold = list(dict_hot_cold.keys())  # в list_hot_cold пока str
list_hot_cold = [ int(i) for i in list_hot_cold ]  # в list_hot_cold уже int
print("Ряд номеров от самых \"горячих\" к самым \"холодным\":")
print(*dict_hot_cold, '\n')
print('''Подробные сведения сведены в таблицу, где: Num - номер,
Freq - количество выпадений номера за выбранный период,
Last - дата, когда последний раз выпадал данный номер,
Draw - номер тиража, когда номер выпадал в последний раз,
Ago - сколько дней назад последний раз выпадал номер\n''')
print('Num', '\t', 'Freq', '\t', 'Last', '\t\t', "Draw", '\t', 'Ago')
for i in range(0, 49):
    # print(list_hot_cold[i], sep=' ', end=' ')
    print(
        list_hot_cold[i], '\t',
        drawData['Nums']['No' + str(list_hot_cold[i])]['Frequency'], '\t',
        drawData['Nums']['No' + str(list_hot_cold[i])]['LastDate'], '\t',
        drawData['Nums']['No' + str(list_hot_cold[i])]['LastDraw'], '\t',
        drawData['Nums']['No' + str(list_hot_cold[i])]['DayAgo'], '\t',
        sep=' ', end='\n')
# print('Hot -> Cold sorted:\n', dict(sorted(dict_hot_cold.items(), key=lambda x: x[1], reverse=True)))
# print('\n- числа Огнева для следующего draw:)', ognevs_numbers, '\n')
print()



"""ГОТОВО: ЗАПИСЬ ДАТАФРЕЙМА В ФАЙЛ EXEL
# запись датафрейма 'df_red_num' в файл 'loter_red_num.xlsx' ------------------
# предварительное преобразование типов в некоторых столбцах
df_red_num["Draw"] = df_red_num["Draw"]. astype(float)
for i in range(1, 50):
    df_red_num['N' + str(i) + 'LastDraw'] = df_red_num['N' + str(i) + 'LastDraw'].astype('int32')

df_red_num.to_excel('loter_red_num.xlsx', sheet_name='Hot and Cold Nums', index=False)
print('датафрейм со всеми данными записан в файл \'loter_red_num.xlsx\'\n')
"""



"""ГОТОВО: СЕКЦИЯ ПРОГНОЗОВ И ПОИСКА В БАЗЕ"""
# секция ADVICES ==============================================================
print('====== СЕКЦИЯ ПРОГНОЗОВ С УЧЁТОМ', count_of_draw_for_analyze, 'ПОСЛЕДНИХ ТИРАЖЕЙ ========================\n')
print('Идея: исключить из генерации нетипичные для тиражей последовательности номеров')
n_gen_items = 6  # количество случайных чисел в одной генерации
n_gen_samples = 50  # количество генераций
n_excluding_draws = int(49 / 6)  # количество исключаемых тиражей

# dict_of_odd = dict(df["ODD"].value_counts())
# print('Значения ODD за всю историю тиражей, упорядоченные от самых частых к самым редким:', *dict_of_odd)
# dict_of_evn = dict(df["EVN"].value_counts())
# print('Значения EVN за всю историю тиражей, упорядоченные от самых частых к самым редким:', *dict_of_evn)
# print('Генерироваться будут последовательности со значениями ODD и EVN, выпадавшими наиболее часто: не равными 0 и не равными 6.', '\n')

dict_of_dif = dict(df["DIF"].value_counts())
# print('Значения DIF за всю историю тиражей, упорядоченные от самых частых к самым редким:\n', *dict_of_dif)
for key, value in dict(dict_of_dif).items():
    # Отбросим редко появляющиеся DIF - те, что появились реже, чем в 0.5 % от количества тиражей.
    limit_of_DIF = int(len(df) * 1/(2*100))
    if value < limit_of_DIF:
        del dict_of_dif[key]
# print('Генерироваться будут последовательности со значениями DIF, выпадавшими наиболее часто: более', limit_of_DIF, 'раз за всю историю тиражей:\n', *dict_of_dif, '\n')

dict_of_sum = dict(df["SUM"].value_counts())
# print('Значения SUM за всю историю тиражей, упорядоченные от самых частых к самым редким:\n', *dict_of_sum)
for key, value in dict(dict_of_sum).items():
    # Отбросим редко появляющиеся SUM - те, что появились реже, чем в 0.25 % от количества тиражей.
    limit_of_SUM = int(len(df) * 1/(4*100))
    if value < limit_of_SUM:
        del dict_of_sum[key]
# print('Генерироваться будут последовательности со значениями SUM, выпадавшими наиболее часто: более', limit_of_SUM, 'раз за всю историю тиражей:\n', *dict_of_sum, '\n')

dict_of_decades = dict(df["DEC"].value_counts())
# print('Значения DEC за всю историю тиражей, упорядоченные от самых частых к самым редким:\n', *dict_of_decades)
for key, value in dict(dict_of_decades).items():
    # Отбросим редко появляющиеся DEC - те, что появились реже, чем в 0.25 % от количества тиражей.
    limit_of_DEC = int(len(df) * 1/(4*100))
    if value < limit_of_DEC:
        del dict_of_decades[key]
# print('Генерироваться будут последовательности со значениями DEC, выпадавшими наиболее часто: более', limit_of_DEC, 'раз за всю историю тиражей:\n', *dict_of_decades, '\n')

# Случайная генерация без исключения номеров:
print('Случайная генерация без исключения номеров:')
print('- номера:', *list_from_1_to_49.copy())
loter_func.random_generation(df, list_from_1_to_49.copy(), n_gen_items, n_gen_samples, dict_of_dif, dict_of_sum, dict_of_decades)
print()

# Генерация с исключением номеров, выпавших в последних int(49/6) тиражах:
loter_func.random_generation_with_cut_numbers(df, list_from_1_to_49.copy(), n_gen_items, n_gen_samples, n_excluding_draws, dict_of_dif, dict_of_sum, dict_of_decades)

# Генерация с исключением 6 самых редких BLUE номеров
print('Генерация с исключением 6 самых редких BLUE номеров:')
temp_list = list_hot_cold.copy()
print('- исключены номера:', *temp_list[43:49:1])
temp_list = temp_list[0:43:1]
print('- оставшиеся номера:', *temp_list)
loter_func.random_generation(df, temp_list, n_gen_items, n_gen_samples, dict_of_dif, dict_of_sum, dict_of_decades)

# Генерация с исключением 6 самых частых RED номеров
print('\nИсключение 6 самых частых RED номеров:')
temp_list = list_hot_cold.copy()
print('- исключены номера:', *temp_list[0:5:1])
temp_list = list_hot_cold.copy()[6:50:1]
print('- оставшиеся номера:', *temp_list)
loter_func.random_generation(df, temp_list, n_gen_items, n_gen_samples, dict_of_dif, dict_of_sum, dict_of_decades)
print()

# Генерация с исключением 6 самых частых и 6 самых редких номеров
print('Генерация с исключением 6 самых редких и 6 самых частых номеров:')
temp_list = list_hot_cold.copy()
print('- исключены номера:', *temp_list[43:49:1], *temp_list[0:5:1])
temp_list = list_hot_cold.copy()[6:43:1]
print('- оставшиеся номера:', *temp_list)
loter_func.random_generation(df, temp_list, n_gen_items, n_gen_samples, dict_of_dif, dict_of_sum, dict_of_decades)
print()

# поиск вводимого списка. while true. сперва сортировать, после - искать в датафрейме.
print('===== ПОИСК ПО БАЗЕ ДАННЫХ ===================================================')
print('Для поиска комбинации номеров базе введите 6 номеров разделяя их пробелами.')
print('Проверку корректности работы поиска можно выполнить введя 5 6 7 8 21 44 -')
print('результата тиража номер 1609, состоявшегося 12 октября 2023 года.\n')
while True:
    str_for_find = input('Введите 6 номеров или нажмите ENTER для завершения программы: ')

    # если нажата клавиша ENTER - сразу завершить выполнение:
    if str_for_find == '':
        print('Выполнение завершено пользователем.')
        break
    else:
        # иначе - проверить корректность ввода и осуществить поиск:
        list_for_find = list(str_for_find.split(sep=' '))

        # проверка: если введён нецифровой символ
        flag_alpha_in_input = False  # флаг 'введена не цифра'
        for i in range(len(list_for_find)):
            if list_for_find[i].isdigit() == False:
                flag_alpha_in_input = True
                continue
        if flag_alpha_in_input == True:
            print('Введены, нецифровые символы! Повторите ввод...')
            flag_alpha_in_input = False
            continue  # не начинать поиск

        list_for_find_sorted = [ int(i) for i in list_for_find ]
        list_for_find_sorted.sort()

        # проверка: если введено меньше или больше 6 номеров
        if len(list_for_find_sorted) < 6:
            print('Введено менее шести номеров! Повторите ввод...')
            continue  # не начинать поиск
        if len(list_for_find_sorted) > 6:
            print('Введено более шести номеров! Повторите ввод...')
            continue  # не начинать поиск

        # проверка: если введено число более 49
        flag_num_greate_49 = False  # флаг 'введено число более 49'
        for i in range(6):
            if list_for_find_sorted[i] > 49:
                flag_num_greate_49 = True
                print('Введено, как минимум, одно число большее 49! Повторите ввод...')
                break  # не начинать поиск
        if flag_num_greate_49 == True:
            flag_num_greate_49 = False
            continue  # не начинать поиск

        print(loter_func.search_in_dataframe(list_for_find_sorted, df))
        print()


'''
if __name__ == '__main__':
    main()
'''

'''
print(list_hot_cold[i], sep=' ', end=' ')

# cooking list & dicts for future hold data -------------------------------
list49 = []
for i in range(1, 50):
    list49.append(str(i))                       # [1, 2, 3, ... 49]
dict49_last_data = dict.fromkeys(list49, '')    # {'1':'', '2':'', '3':'',... '49':''}
dict49_A = dict.fromkeys(list49, 0)             # {'1':0, '2':0, '3':0,... '49':0}
dict49_B = dict49_A.copy()                      # {'1':0, '2':0, '3':0,... '49':0}
dict49_C = dict49_A.copy()                      # {'1':0, '2':0, '3':0,... '49':0}
dict49_D = dict49_A.copy()                      # {'1':0, '2':0, '3':0,... '49':0}
dict49_E = dict49_A.copy()                      # {'1':0, '2':0, '3':0,... '49':0}
dict49_F = dict49_A.copy()                      # {'1':0, '2':0, '3':0,... '49':0}
del(i)

# get info about database & dicts with data -------------------------------
with open('loter_results.tmp', 'r', encoding='utf-8') as f:
    amount_of_draws = 0
    for line in f:
        data = line.split(';')              # 1;2000-11-20;1;2;3;4;5;6\n
        date_of_num = data[1]               # 2000-11-20
        dict49_A[data[2]] += 1              # {'1':1, '2':0, '3':0,... '49':0}
        dict49_B[data[3]] += 1              # {'1':0, '2':1, '3':0,... '49':0}
        dict49_C[data[4]] += 1              # {'1':0, '2':0, '3':1,... '49':0}
        dict49_D[data[5]] += 1              # {'1':0,... '4':1,... '49':0}
        dict49_E[data[6]] += 1              # {'1':0,... '5':1,... '49':0}
        dict49_F[data[7].rstrip()] += 1     # {'1':0,... '6':1,... '49':0}
        # fill "dict49_last_data" with nums win data:
        for i in range(2, 8):
            for j in range(1, 50):
                if str(j) == data[i].strip():
                    dict49_last_data[str(j)] = date_of_num  # {'1':'2000-11-20',... '49':''}
                else:
                    continue
        amount_of_draws += 1
        # print('-', '\b', '\\', '\b', '|', '\b', '/', '\b', sep='', end='')
        print('.', sep='', end='')
    sorted_dict49_last_data = dict(sorted(dict49_last_data.items(), key=lambda x: x[1], reverse=False))
    sorted_dict49_A = dict(sorted(dict49_A.items(), key=lambda x: x[1], reverse=True))
    sorted_dict49_B = dict(sorted(dict49_B.items(), key=lambda x: x[1], reverse=True))
    sorted_dict49_C = dict(sorted(dict49_C.items(), key=lambda x: x[1], reverse=True))
    sorted_dict49_D = dict(sorted(dict49_D.items(), key=lambda x: x[1], reverse=True))
    sorted_dict49_E = dict(sorted(dict49_E.items(), key=lambda x: x[1], reverse=True))
    sorted_dict49_F = dict(sorted(dict49_F.items(), key=lambda x: x[1], reverse=True))
'''




    # print info about database -------------------------------------------
'''
    print('- frequency in channel A:', sorted_dict49_A, '- frequency in channel B:', sorted_dict49_B, '- frequency in channel C:', sorted_dict49_C, '- frequency in channel D:', sorted_dict49_D, '- frequency in channel E:', sorted_dict49_E, '- frequency in channel F:', sorted_dict49_F, sep='\n', end='\n\n')
'''
    # print('- last dates of win numbers:')
    # for key1 in dict49_last_data.keys():
        # print(key1, dict49_last_data[key1], sep='\t')
    # print(dict49_last_data, "\n")
    # /print info about database ------------------------------------------


    # DIAGRAM "LAST DATES OF WIN NUMBERS" =====================================
"""
    # build diagram "last dates of win numbers" ---------------------------
    numX = list(sorted_dict49_last_data.values())
    numY = list(sorted_dict49_last_data.keys())
    fig, ax = plt.subplots()
    # draw diagram from numX and numY data by green dots
    plt.scatter(numX, numY, color="#00ee00", marker='o')
    plt.title("last dates of win numbers")
    plt.ylabel("numbers")
    plt.xlabel("dates")
    plt.grid(True)
    # range X and Y axes of coordinates
    ax.set(xlim=(numX[0], numX[len(numX)-1]), ylim=(0, 50))
    # axes step major/minor
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
    # labels for axes
    Yax = ax.get_yaxis()
    Ylabels = Yax.get_ticklabels()
    for label in Ylabels:
        label.set_color('green')
        label.set_rotation(0)
        label.set_fontsize(6)
    Xax = ax.get_xaxis()
    Xlabels = Xax.get_ticklabels()
    for label in Xlabels:
        label.set_color('green')
        label.set_rotation(45)
        label.set_fontsize(6)
    fig.savefig("loter_results_dates_of_win_numbers_draws.png", transparent=False, dpi=600)
    # plt.show()
    # /build diagram "last dates of win numbers" --------------------------
"""
    # \DIAGRAM "LAST DATES OF WIN NUMBERS" ====================================






# DIAGRAM OF RESULTS LAST (USER TYPING) DRAWS =================================
"""
# print('Building diagram of results last (user typing) draws...', end=' ')
# diagram of results all draws from user typing to last draw
# coordinates for diagram add to numX, numY:
# X - draw_num (repeat 6 times), Y - 6 numbers from 1 to 49
# for example, X = [5, 5, 5, 5, 5, 5], Y = [6, 29, 23, 44, 27, 37]
numX, numY = [], []
with open('loter_results.csv', 'r', encoding='utf-8') as ff:
    count = 0
    for line in ff:
        data = line.split(';')
        count += 1
        for ii in range(1, 7):
            numX.append(int(data[0]))
        for jj in range(2, 8, 1):
            numY.append(int(data[jj]))

# build diagram:
fig, ax = plt.subplots()
# draw diagram from numX and numY data by blue dots
plt.scatter(numX, numY, color="#0000ee", marker='o')
plt.title("results of last " + str(count_of_draw_for_analyze) + " draws")
plt.ylabel("numbers")
plt.xlabel("draws")
plt.grid(True)
# range X and Y axes of coordinates
ax.set(xlim=(tmp_draw_count - 1, amount_of_draws + 1), ylim=(0, 50))
# axes step major/minor
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# labels for axes
Yax = ax.get_yaxis()
Ylabels = Yax.get_ticklabels()
for label in Ylabels:
    label.set_color('blue')
    label.set_rotation(0)
    label.set_fontsize(6)
Xax = ax.get_xaxis()
Xlabels = Xax.get_ticklabels()
for label in Xlabels:
    label.set_color('blue')
    label.set_rotation(90)
    label.set_fontsize(6)
fig.savefig("loter_results_last_" + str(count_of_draw_for_analyze) + "_draws.png", transparent=False, dpi=600)
# print('done!')
# plt.show()
"""
# \DIAGRAM OF RESULTS LAST (USER TYPING) DRAWS ================================

'''
# print('Building diagram of repeat numbers for last (user typing amount) draws...', end=' ')
list_one_draw = []      # list [1,25,34,43,45,47]
list_all_draws = []     # list of lists [[1,25,34,43,45,47],[6,11,15,17,31,33],[],...]
numX, numY = [], []
list49 = []             # for dict generation '49 keys - 49 zeros'
for i in range(1, 50):
    list49.append(str(i))
dict49 = dict.fromkeys(list49, 0)   #{'1':0, '2':0, '3':0, '4':0,... '49':0}
with open('loter_results.csv', 'r', encoding='utf-8') as fff:
    reader = csv.reader(fff)
    count = 0
    for line in fff:
        data = line.split(';')
        for i in range(2, 8):
            list_one_draw.append(int(data[i]))
        list_all_draws.append(list_one_draw)
        list_one_draw = []
        count += 1
    for i in range(0, len(list_all_draws)):
        for j in range(0, len(list_all_draws[i])):
            dict49[str(list_all_draws[i][j])] += 1
    numX = list(dict49.keys())
    numY = list(dict49.values())
'''

# DIAGRAM AMOUNT REPEATS OF WIN NUMBERS =======================================
"""
# build diagram amount repeats of win numbers:
fig, ax = plt.subplots()
# draw diagram from numX and numY data by blue dots
plt.scatter(numX, numY, s=20, color="#ee0000", marker='o')
plt.title("amount repeats of win numbers in last " + str(count_of_draw_for_analyze) + " draws")
plt.ylabel("amount")
plt.xlabel("numbers")
plt.grid(True)
# range X and Y axes of coordinates
ax.set(xlim=(-1, 50), ylim=(sorted(numY)[0]-1, sorted(numY)[48]+1))
# axes step major/minor
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# labels for axes
Yax = ax.get_yaxis()
Ylabels = Yax.get_ticklabels()
for label in Ylabels:
    label.set_color('red')
    label.set_rotation(0)
    label.set_fontsize(10)
Xax = ax.get_xaxis()
Xlabels = Xax.get_ticklabels()
for label in Xlabels:
    label.set_color('red')
    label.set_rotation(90)
    label.set_fontsize(10)
fig.savefig("loter_results_frequences_in_last_" + str(count_of_draw_for_analyze) + "_draws.png", transparent=False, dpi=600)
# plt.show()
"""
# \DIAGRAM AMOUNT REPEATS OF WIN NUMBERS ======================================

'''
# print("\nFrequency numbers:\n", dict49)
sorted_dict49 = dict(sorted(dict49.items(), key=lambda x: x[1], reverse=True))
# sorted_dict49 = dict(sorted(dict49.items(), key=lambda x: x[1]))
# print("\nResults by increase numbers (blue nums -> red nums):\n", sorted_dict49)
list_for_rand = list(sorted_dict49.keys())
# print("Sorted numbers only (without amount of win):\n", list_for_rand)
list_of_red =  []
for red in range(0, 12):
    list_of_red.append(list_for_rand[red])
print("- 12 red (hot) numbers by decrease:", list_of_red)
list_of_blue =  []
for blue in range(len(list_for_rand)-12, len(list_for_rand)):
    list_of_blue.append(list_for_rand[blue])
print("- 12 blue (cold) numbers by decrease:", list_of_blue)
print("\n- frequency win numbers by decrease (red nums -> blue nums):\n", sorted_dict49)
print("\n- sorted last dates of win numbers:")
# for key2 in sorted_dict49_last_data.keys():
    # print(key2, sorted_dict49_last_data[key2], sep='\t')
print(sorted_dict49_last_data, "\n")
print("Appears numbers by freq:", "Appears numbers by numbs:", "Appears numbers by date:", sep='\t')
print("Numb", "Freq", "Last date", "Numb", "Freq", "Last date", "Numb", "Last date", sep='\t')
k = 1
for key in sorted_dict49:
    print(key, sorted_dict49[key], sorted_dict49_last_data[key],   str(k), dict49[str(k)],  str(dict49_last_data[str(k)]), sep='\t', end='\n')
    k += 1
print("\nAppears numbers by date:")
print("Numb", "Last date", sep='\t')
for key, value in sorted_dict49_last_data.items():
    print(key, '\t', value)
print("\nSee also diagrams draws in this folder...")
with open('loter_results.csv', 'a+', encoding='utf-8') as recepient:
    recepient.write('\nResearch results:\n')
    recepient.write('- amount of all draws in database is ' + str(amount_of_draws) + '\n')
    recepient.write('- latest ' + str(data[0]) + ' draw take place ' + str(data[1]) + '\n')
    recepient.write('- his result: ' + str(data[2]) + ' ' + str(data[3]) + ' ' + str(data[4]) + ' ' + str(data[5]) + ' ' + str(data[6]) + ' ' + str(data[7]) + '\n')
    recepient.write('- your wish make research for ' + str(count_of_draw_for_analyze) + ' last draws (usually prefer 50 - 100)' + '\n')
    recepient.write("- ognev's numbers for future draw: " + str(ognev_nums) + '\n')
    recepient.write('- 12 red (hot) numbers by decrease: ' + str(list_of_red) + '\n')
    recepient.write('- 12 blue (cold) numbers by decrease:: ' + str(list_of_blue) + '\n\n')
    recepient.write('- frequency win numbers by decrease (red nums -> blue nums):\n' + str(sorted_dict49) + '\n\n')
    recepient.write('- sorted last dates of win numbers:\n' + str(sorted_dict49_last_data) + '\n\n')
    recepient.write('- frequency in channel A:\n' + str(sorted_dict49_A) + '\n')
    recepient.write('- frequency in channel B:\n' + str(sorted_dict49_B) + '\n')
    recepient.write('- frequency in channel C:\n' + str(sorted_dict49_C) + '\n')
    recepient.write('- frequency in channel D:\n' + str(sorted_dict49_D) + '\n')
    recepient.write('- frequency in channel E:\n' + str(sorted_dict49_E) + '\n')
    recepient.write('- frequency in channel F:\n' + str(sorted_dict49_F) + '\n\n')
    recepient.write('Appears numbers by freq:\tAppears numbers by numbs:\n')
    recepient.write('Numb\tFreq\tLast date\tNumb\tFreq\tLast date\n')
    k = 1
    for key in sorted_dict49:
        recepient.write(str(key) + '\t' + str(sorted_dict49[key]) + '\t' + sorted_dict49_last_data[key] + '\t' + str(k) + '\t' + str(dict49[str(k)]) + '\t' + str(dict49_last_data[str(k)]) + '\n')
        k += 1
    recepient.write('\nAppears numbers by date:\n')
    recepient.write('Numb\tLast date\n')
    for key, value in sorted_dict49_last_data.items():
        recepient.write(str(key) + '\t' + str(value) + '\n')
try:
    shutil.rmtree("__pycache__")
    print("Folder with cashe-files was deleted.")
except:
    print("If your need, delete folder with cashe-files.")
if platform.system() == "Windows" or platform.system() == "win32":
    os.system('notepad.exe loter_results.csv')
if platform.system() == "Linux":
    os.system('nano loter_results.csv')


    temp_list = list_of_red + list_of_blue
    n = 6
    for i in range(6):
        print('Mix of 6:', secrets.SystemRandom().sample(temp_list, n_gen_items))
    n = 3
    for i in range(6):
        print('3 red + 3 blue:', secrets.SystemRandom().sample(list_of_red, n) + secrets.SystemRandom().sample(list_of_blue, n))

'''



    #input()

'''    comb(n, k, /)
            Number of ways to choose k items from n items without repetition and without order.

            Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
            to zero when k > n.

            Also called the binomial coefficient because it is equivalent
            to the coefficient of k-th term in polynomial expansion of the
            expression (1 + x)**n.

            Raises TypeError if either of the arguments are not integers.
            Raises ValueError if either of the arguments are negative.
'''
