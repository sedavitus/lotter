import os
import pandas
import matplotlib.pyplot as plt
import math
from time import sleep   # для засыпания перед нештатным exit()

def check_lotter_results_xlsx() -> None:
	"""
	Проверка наличия в текущей директории файла lotter_results.xlsx с архивом тиражей.
	Актуализация файла при наличии нескольких архивов.
	В директории будет оставлен только один, самый поздний архив тиражей.
	Остальные файлы с архивами тиражей будут удалены.
	"""
	print('\nПредварительная проверка наличия и актуализация базы тиражей:')
	print('- текущая рабочая директория', os.getcwd())
	# Находится ли файл с архивом тиражей lotter_results.xlsx в текущей директории:
	list_of_dir = os.listdir()

	other_xlsx_files = []  # для хранения имён типа 'game results 6-49 (06.10.2024 01_41_47).xlsx'
	for i in range(0, len(list_of_dir)):
		if 'game results 6-49' in list_of_dir[i]:
			other_xlsx_files.append(list_of_dir[i])

	if 'lotter_results.xlsx' in list_of_dir:
		# есть ли в директории файл - архив тиражей с правильным именем:
		print('- файл с архивом тиражей находится в текущей директории')
		# дата модификации файла в формате количества секунд, прошедших с начала эпохи:
		time_lotter_results = os.path.getmtime(r'lotter_results.xlsx')
	elif ('lotter_results.xlsx' not in list_of_dir) and (len(other_xlsx_files) != 0):
		# если нет файла с правильным именем, но есть хоть один файл загруженный с сайта лотерей
		os.rename(other_xlsx_files[0], 'lotter_results.xlsx')
		other_xlsx_files.remove(other_xlsx_files[0])
		time_lotter_results = os.path.getmtime(r'lotter_results.xlsx')
		print('- файл, загруженный с сайта лотерей, переименован в lotter_results.xlsx')
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
				if time_lotter_results < os.path.getmtime(f):
					# lotter_results.xlsx более старый, чем f. Удаление старого lotter_results.xlsx
					os.remove('lotter_results.xlsx')
					os.rename(f, 'lotter_results.xlsx')
					other_xlsx_files.remove(f)
					time_lotter_results = os.path.getmtime(r'lotter_results.xlsx')
				else:
					# lotter_results.xlsx новее, чем f. Удаление файла f
					os.remove(f)
					other_xlsx_files.remove(f)
		print('- оставлен наиболее актуальный файл с архивом тиражей, старые файлы удалены')
	else:
		print('- других (непереименованных) файлов с архивами тиражей нет')
	del(list_of_dir)
	return 0


def search_in_dataframe(str_for_find: list, df: pandas.core.frame.DataFrame) -> str:
	"""
	Поиск по базе данных определённой последовательности номеров
	"""
	No1, No2, No3, No4, No5, No6 = str_for_find
	if len(df[(df['N1'] == No1) & (df['N2'] == No2) & (df['N3'] == No3) & (df['N4'] == No4) & (df['N5'] == No5) & (df['N6'] == No6)]) == 0:
		result = 'комбинация не выпадала...'
	else:
        # date_of_result = df['DRAW']
		result = 'комбинация уже выпадала!!!'
	return result


def full_database_statistic(MIN: int, MAX: int, df: pandas.core.frame.DataFrame) -> None:
	"""
	Получение статистических данных полного архива тиражей
	(начиная с первого тиража базы и до самого последнего)
	"""
	print('ОБЩАЯ СТАТИСТИКА ПОЛНОЙ БАЗЫ ТИРАЖЕЙ')
	print('=' * 36)
	print('- лотерея \"Спортлото', MIN, 'из', MAX, '\b\"')
	if MIN == 6 and MAX == 49:
		C_5_48 = int(math.factorial(48) / (math.factorial(5) * math.factorial(48-5)))  # C_5_48
		C_6_49 = int(math.factorial(49) / (math.factorial(6) * math.factorial(49-6)))  # C_6_49 = 13.983.816
		print('- число возможных комбинаций 6 номеров из 49 =', C_6_49)
		print('- число перестановок для 6 номеров =', math.factorial(6))  # 720
		print('- вероятность выпадения в тираже одного номера =', round((C_5_48 / C_6_49), 5))  # 0.12245
		print('- вероятность выпадения в тираже пары номеров =', round(((1 / 49) * (5 / 48)), 5))  # 0.00213
		print('- вероятность выпадения в тираже тройки номеров =', round(((1 / 49) * (5 / 48) * (4 / 47)), 5), '\n')  # 0.00018

		print('- статистика выигрышей за всё время проведения лотереи:\n')
		print('6 номеров угадано', df['WIN6'].sum(axis=0), 'раза, суммы выигрышей:')
		print(df[df['WIN6'] != 0].loc[:, ['DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'WIN6', 'BYN6']], '\n')
		print('5 номеров угадано', df['WIN5'].sum(axis=0), 'раза, пять последних выигрышей:')
		print(df[df['WIN5'] != 0].loc[:, ['DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'WIN5', 'BYN5']].tail(), '\n')
		print('4 номера угадано', df['WIN4'].sum(axis=0), 'раз, пять последних выигрышей:')
		print(df[df['WIN4'] != 0].loc[:, ['DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'WIN4', 'BYN4']].tail(), '\n')
		print('3 номера угадано', df['WIN3'].sum(axis=0), 'раз, пять последних выигрышей:')
		print(df[df['WIN3'] != 0].loc[:, ['DATE', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'WIN3', 'BYN3']].tail(), '\n')

		print('- основные характеристики базы тиражей:\n')
		# Данные из df.describe() сперва собираем в соответствующие списки:
		list_pandas_mean = [int((df.describe()['N1']['mean']).round(0)), int((df.describe()['N2']['mean']).round(0)), int((df.describe()['N3']['mean']).round(0)), int((df.describe()['N4']['mean']).round(0)), int((df.describe()['N5']['mean']).round(0)), int((df.describe()['N6']['mean']).round(0))]
		list_pandas_min = [int(df.describe()['N1']['min']), int(df.describe()['N2']['min']), int(df.describe()['N3']['min']), int(df.describe()['N4']['min']), int(df.describe()['N5']['min']), int(df.describe()['N6']['min'])]
		list_pandas_25p = [int(df.describe()['N1']['25%']), int(df.describe()['N2']['25%']), int(df.describe()['N3']['25%']), int(df.describe()['N4']['25%']), int(df.describe()['N5']['25%']), int(df.describe()['N6']['25%'])]
		list_pandas_50p = [int(df.describe()['N1']['50%']), int(df.describe()['N2']['50%']), int(df.describe()['N3']['50%']), int(df.describe()['N4']['50%']), int(df.describe()['N5']['50%']), int(df.describe()['N6']['50%'])]
		list_pandas_75p = [int(df.describe()['N1']['75%']), int(df.describe()['N2']['75%']), int(df.describe()['N3']['75%']), int(df.describe()['N4']['75%']), int(df.describe()['N5']['75%']), int(df.describe()['N6']['75%'])]
		list_pandas_max = [int(df.describe()['N1']['max']), int(df.describe()['N2']['max']), int(df.describe()['N3']['max']), int(df.describe()['N4']['max']), int(df.describe()['N5']['max']), int(df.describe()['N6']['max'])]
		print('минимальные номера:', *list_pandas_min, '\b,', search_in_dataframe(list_pandas_min, df))
		print('25% номеров <= чем:', *list_pandas_25p, '\b,', search_in_dataframe(list_pandas_25p, df))
		print('50% номеров <= чем:', *list_pandas_50p, '\b,', search_in_dataframe(list_pandas_50p, df))
		print('медианное значение:', *list_pandas_mean, '\b,', search_in_dataframe(list_pandas_mean, df))
		print('75% номеров <= чем:', *list_pandas_75p, '\b,', search_in_dataframe(list_pandas_75p, df))
		print('максимальные номера:', *list_pandas_max, '\b,', search_in_dataframe(list_pandas_max, df), '\n')
	return 0


def add_0_to_not_full_dict(not_full_dict: dict) -> dict:
	"""
	Это вспомогательная функция.
	Нужна для функции 'hot_cold_full_database', которая (используя понятие
	'каналов' - о них см. ниже) подсчитывает 'горячие' и 'холодные' номера
	всего архива тиражей.
	Функция 'add_0_to_not_full_dict' заполняет 'неполные' словари (размер
	которых < 49) нулевыми парами 'ключ: значение', т.е. (0: 0).
	Дополнение нужно для 'выравнивания' размеров 'словарей частотности
	номеров' (которые образуют 'каналы') и формирования из них затем нового
	датафрейма. Примечание: Pandas не формирует новый датафрейм из словарей,
	если эти словари имеют разные размеры.
	"""
	if len(not_full_dict) > 49:
		print('Размер dict, передаваемого в def add_0_to_not_full_dict превышает 49')
	if len(not_full_dict) == 49:
		return not_full_dict
	if len(not_full_dict) < 49:
		list_tmp = list(not_full_dict.keys())
		for i in range(1, 50):
			if i in list_tmp:
				continue
			else:
				not_full_dict[i] = 0
	return not_full_dict


def hot_cold_full_database(df: pandas.core.frame.DataFrame) -> None:
	"""
	Подсчёт 'горячих' и 'холодных' номеров по 6 'каналам' для всех тиражей.
	Концепция 'канала' проста: в каждом тираже выпавшие номера сортируются
	по возрастанию. Это попытка существенно уменьшить количество возможных
	комбинаций. (Номера выпадают, конечно, не по порядку. Однако результат
	всегда подаётся как упорядоченная последовательность. Будь то 234561,
	или 345612, или 456123, или 561234... - результат одинаковый - 123456).
	После - по каждому из 'каналов' считается частота появления каждого из
	номеров и делаются соответствующие выводы: какие номера чаще других
	выпадают в том или ином 'канале'.
	"""
	print("- распределение 'горячих' / 'холодных' номеров по 'каналам', где:")
	print("\tN1...N6 - выпавшие номера или названия 'каналов'")
	print("\tFR1...FR6 - частота выпадения номера в 'канале'\n")
	# с помощью value_counts() можно подсчитать частоту появления номеров по каждому из каналов
	# и сформировать новый dataframe_freq_all_chanels с общим результатом по всем каналам
	# т.к. при формировании датафрейма данные д.быть одного размера (а в каналах есть не все номера),
	# функция 'add_0_to_not_full_dict()' добавит в словари недостающие keys с нулевыми values
	dict_freq_chanel_1 = add_0_to_not_full_dict(dict(df['N1'].value_counts()))
	dict_freq_chanel_2 = add_0_to_not_full_dict(dict(df['N2'].value_counts()))
	dict_freq_chanel_3 = add_0_to_not_full_dict(dict(df['N3'].value_counts()))
	dict_freq_chanel_4 = add_0_to_not_full_dict(dict(df['N4'].value_counts()))
	dict_freq_chanel_5 = add_0_to_not_full_dict(dict(df['N5'].value_counts()))
	dict_freq_chanel_6 = add_0_to_not_full_dict(dict(df['N6'].value_counts()))
	# исходные данные для датафрейма - словарь списков. добавить "No": list_from_1_to_49, если понадобится
	dict_freq_all_chanels = {
		'N1': list(dict_freq_chanel_1.keys()), 'FR1': list(dict_freq_chanel_1.values()),
		'N2': list(dict_freq_chanel_2.keys()), 'FR2': list(dict_freq_chanel_2.values()),
		'N3': list(dict_freq_chanel_3.keys()), 'FR3': list(dict_freq_chanel_3.values()),
		'N4': list(dict_freq_chanel_4.keys()), 'FR4': list(dict_freq_chanel_4.values()),
		'N5': list(dict_freq_chanel_5.keys()), 'FR5': list(dict_freq_chanel_5.values()),
		'N6': list(dict_freq_chanel_6.keys()), 'FR6': list(dict_freq_chanel_6.values())
		}
	# создание датафрейма 'df_freq_all_chanels'
	df_freq_all_chanels = pandas.DataFrame(dict_freq_all_chanels)
	# запись во временный файл 'loter_results.tmp' чтобы избавиться от ненужного индексного столбца
	df_freq_all_chanels.to_csv('lotter_results.tmp', header=True, index=False, lineterminator=',\n', encoding='utf8')  # sep=';', 
	print(df_freq_all_chanels.head(43), '\n')  # даже более 13-ти строк выводить нет смысла - появляются повторы в соседних каналах
	return 0


def graph_channels_full_database(df: pandas.core.frame.DataFrame):
	"""
	Построение графика 'Распределение номеров по каналам'
	"""
	fig, ax = plt.subplots()
	df.groupby('N1')['FR1'].mean().plot(label=r'$канал\ N1$')
	df.groupby('N2')['FR2'].mean().plot(label=r'$канал\ N2$')
	df.groupby('N3')['FR3'].mean().plot(label=r'$канал\ N3$')
	df.groupby('N4')['FR4'].mean().plot(label=r'$канал\ N4$')
	df.groupby('N5')['FR5'].mean().plot(label=r'$канал\ N5$')
	df.groupby('N6')['FR6'].mean().plot(label=r'$канал\ N6$')
	plt.xlabel(r'$номера$')
	plt.xticks(rotation=0)
	plt.ylabel(r'$частота$')
	plt.title(r'распределение номеров по каналам N1, N2, N3, N4, N5, N6')
	plt.grid(True)
	plt.legend(loc='best', fontsize=10)
	fig.savefig("lotter_graph_6_channels.png", transparent=False, dpi=600)
	plt.show()
	return 0


def last_drawing_statistic(amount_of_draws: int, df: pandas.core.frame.DataFrame) -> None:
	"""
	Получение отчёта с подробными результатами последнего тиража
	"""
	print('РЕЗУЛЬТАТЫ ПОСЛЕДНЕГО ТИРАЖА')
	print('=' * 28)
	print('- число тиражей в базе', amount_of_draws)
	print('-', amount_of_draws, '\b-ой тираж состоялся', df['DATE'][amount_of_draws].date(), 'с результатами:', df['N1'][amount_of_draws], df['N2'][amount_of_draws], df['N3'][amount_of_draws], df['N4'][amount_of_draws], df['N5'][amount_of_draws], df['N6'][amount_of_draws])
	if df['WIN6'][amount_of_draws] > 0:
		print('- 6 номеров угадали:', df['WIN6'][amount_of_draws], '\b, выигрыш каждого составил', df['BYN6'][amount_of_draws], 'BYN')
	else:
		print('- 6 номеров не угадал никто')
	if df['WIN5'][amount_of_draws] > 0:
		print('- 5 номеров угадали:', df['WIN5'][amount_of_draws], '\b, выигрыш каждого составил', df['BYN5'][amount_of_draws], 'BYN')
	else:
		print('- 5 номеров не угадал никто')
	if df['WIN4'][amount_of_draws] > 0:
		print('- 4 номера угадали:', df['WIN4'][amount_of_draws], '\b, выигрыш каждого составил', df['BYN4'][amount_of_draws], 'BYN')
	else:
		print('- 4 номера не угадал никто')
	if df['WIN3'][amount_of_draws] > 0:
		print('- 3 номера угадали:', df['WIN3'][amount_of_draws], '\b, выигрыш каждого составил', df['BYN3'][amount_of_draws], 'BYN')
	else:
		print('- 3 номера не угадал никто')
	print('- джекпот по состоянию на', df['DATE'][amount_of_draws].date(), 'составляет', df['JACK'][amount_of_draws], 'BYN', '\n')
	return 0


def results_of_x_last_drawing(USER_AMOUNT_DRAWING: int, df: pandas.core.frame.DataFrame) -> None:
	"""
	Получение краткой статистики по нескольким последним тиражам,
	количество тиражей указывается пользователем в lotter.ini
	"""
	print('РЕЗУЛЬТАТЫ ПОСЛЕДНИХ', USER_AMOUNT_DRAWING, 'ТИРАЖЕЙ')
	print('=' * (21 + len(str(USER_AMOUNT_DRAWING)) + 8))
	print('- тиражи отсортированы по убыванию:')
	print(df.loc[:, 'DATE':'N6'].tail(USER_AMOUNT_DRAWING).sort_values(by='DRAW', ascending=False), '\n')
	return 0


def add_columns_to_database(df: pandas.core.frame.DataFrame) -> None:
	"""
	Добавление в датафрейм дополнительных столбцов
	"""
	# print('РАСЧЁТ И ДОБАВЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ СТОЛБЦОВ')
	# print('=' * 44)
	# DEC - распределение выпавших номеров по десяткам
	df['DEC'] = (df['N1'] // 10).astype(str) + (df['N2'] // 10).astype(str) + (df['N3'] // 10).astype(str) + (df['N4'] // 10).astype(str) + (df['N5'] // 10).astype(str) + (df['N6'] // 10).astype(str)
	# ODD - количество нечётных номеров
	df['ODD'] = df['N1'] % 2 + df['N2'] % 2 + df['N3'] % 2 + df['N4'] % 2 + df['N5'] % 2 + df['N6'] % 2
	# EVN - количество чётных номеров: просто как число всех номеров минус количество чётных
	df['EVN'] = 6 - df['ODD']
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
	df['RPT'] = repeat_nums_list
	# DIF - разница между номерами: самым большим (N6) и самым маленьким (N1)
	df['DIF'] = df['N6'] - df['N1']
	# SUM - сумма номеров
	df['SUM'] = df['N1'] + df['N2'] + df['N3'] + df['N4'] + df['N5'] + df['N6']
	return 0


def anomal_results_drawing(ANOMAL_DRAWING: int, df: pandas.core.frame.DataFrame) -> None:
	print('САМЫЕ НЕОБЫЧНЫЕ РЕЗУЛЬТАТЫ ТИРАЖЕЙ')
	print('=' * 35)
	print('Есть ли в архиве тиражи, в которых выпало по 4, 5, 6 номеров одного десятка?\nЕсть ли тиражи, состоящие только из нечётных или только чётных номеров?\n')
	# четыре номера из первого десятка
	df_temp = df[(df['N1'] <= 9) & (df['N2'] <= 9) & (df['N3'] <= 9) & (df['N4'] <= 9)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали четыре номера из первого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# четыре номера из второго десятка
	df_temp = df[
		((df['N1'] >= 10) & (df['N1'] <= 19) & (df['N2'] <= 19) & (df['N3'] <= 19) & (df['N4'] <= 19)) |
		((df['N2'] >= 10) & (df['N2'] <= 19) & (df['N3'] <= 19) & (df['N4'] <= 19) & (df['N5'] <= 19)) |
		((df['N3'] >= 10) & (df['N3'] <= 19) & (df['N4'] <= 19) & (df['N5'] <= 19) & (df['N6'] <= 19))
		]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали четыре номера из второго десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# четыре номера из третьего десятка
	df_temp = df[
		(df['N1'] >= 20) & (df['N1'] <= 29) & (df['N2'] <= 29) & (df['N3'] <= 29) & (df['N4'] <= 29) |
		(df['N2'] >= 20) & (df['N2'] <= 29) & (df['N3'] <= 29) & (df['N4'] <= 29) & (df['N5'] <= 29) |
		(df['N3'] >= 20) & (df['N3'] <= 29) & (df['N4'] <= 29) & (df['N5'] <= 29) & (df['N6'] <= 29)
		]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали четыре номера из третьего десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# четыре номера из четвёртого десятка
	df_temp = df[
		(df['N1'] >= 30) & (df['N1'] <= 39) & (df['N2'] <= 39) & (df['N3'] <= 39) & (df['N4'] <= 39) |
		(df['N2'] >= 30) & (df['N2'] <= 39) & (df['N3'] <= 39) & (df['N4'] <= 39) & (df['N5'] <= 39) |
		(df['N3'] >= 30) & (df['N3'] <= 39) & (df['N4'] <= 39) & (df['N5'] <= 39) & (df['N6'] <= 39)
		]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали четыре номера из четвёртого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# четыре номера из пятого десятка
	df_temp = df[(df['N3'] >= 40) & (df['N3'] <= 49) & (df['N4'] <= 49) & (df['N5'] <= 49) & (df['N6'] <= 49)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали четыре номера из пятого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# пять номеров из первого десятка
	df_temp = df[(df['N1'] <= 9) & (df['N2'] <= 9) & (df['N3'] <= 9) & (df['N4'] <= 9) & (df['N5'] <= 9)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали пять номеров из первого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# пять номеров из второго десятка
	df_temp = df[
		(df['N1'] >= 10) & (df['N1'] <= 19) & (df['N2'] <= 19) & (df['N3'] <= 19) & (df['N4'] <= 19) & (df['N5'] <= 19) |
		(df['N2'] >= 10) & (df['N2'] <= 19) & (df['N3'] <= 19) & (df['N4'] <= 19) & (df['N5'] <= 19) & (df['N6'] <= 19)
		]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали пять номеров из второго десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# пять номеров из третьего десятка
	df_temp = df[
		(df['N1'] >= 20) & (df['N1'] <= 29) & (df['N2'] <= 29) & (df['N3'] <= 29) & (df['N4'] <= 29) & (df['N5'] <= 29) |
		(df['N2'] >= 20) & (df['N2'] <= 29) & (df['N3'] <= 29) & (df['N4'] <= 29) & (df['N5'] <= 29) & (df['N6'] <= 29)
		]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали пять номеров из третьего десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# пять номеров из четвёртого десятка
	df_temp = df[
		(df['N1'] >= 30) & (df['N1'] <= 39) & (df['N2'] <= 39) & (df['N3'] <= 39) & (df['N4'] <= 39) & (df['N5'] <= 39) |
		(df['N2'] >= 30) & (df['N2'] <= 39) & (df['N3'] <= 39) & (df['N4'] <= 39) & (df['N5'] <= 39) & (df['N6'] <= 39)
		]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали пять номеров из четвёртого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# пять номеров из пятого десятка
	df_temp = df[(df['N2'] >= 40) & (df['N2'] <= 49) & (df['N3'] <= 49) & (df['N4'] <= 49) & (df['N5'] <= 49) & (df['N6'] <= 49)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали пять номеров из пятого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# шесть номеров из первого десятка
	df_temp = df[(df['N1'] <= 9) & (df['N2'] <= 9) & (df['N3'] <= 9) & (df['N4'] <= 9) & (df['N5'] <= 9) & (df['N6'] <= 9)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали шесть номеров из первого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# шесть номеров из второго десятка
	df_temp = df[(df['N1'] >= 10) & (df['N1'] <= 19) & (df['N2'] <= 19) & (df['N3'] <= 19) & (df['N4'] <= 19) & (df['N5'] <= 19) & (df['N6'] <= 19)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали шесть номеров из второго десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# шесть номеров из третьего десятка
	df_temp = df[(df['N1'] >= 20) & (df['N1'] <= 29) & (df['N2'] <= 29) & (df['N3'] <= 29) & (df['N4'] <= 29) & (df['N5'] <= 29) & (df['N6'] <= 29)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали шесть номеров из третьего десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# шесть номеров из четвёртого десятка
	df_temp = df[(df['N1'] >= 30) & (df['N1'] <= 39) & (df['N2'] <= 39) & (df['N3'] <= 39) & (df['N4'] <= 39) & (df['N5'] <= 39) & (df['N6'] <= 39)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали шесть номеров из четвёртого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# шесть номеров из пятого десятка
	df_temp = df[(df['N1'] >= 40) & (df['N1'] <= 49) & (df['N2'] <= 49) & (df['N3'] <= 49) & (df['N4'] <= 49) & (df['N5'] <= 49) & (df['N6'] <= 49)]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали шесть номеров из пятого десятка, (всего', len_df_temp, 'шт):')
		print(df_temp.tail(ANOMAL_DRAWING), '\n')
	# все номера нечётные
	df_temp = df[df['ODD'] == 6]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали только нечётные номера (всего', len_df_temp, 'шт):')
		print(df[df['ODD'] == 6].tail(ANOMAL_DRAWING), '\n')
	# все номера чётные
	df_temp = df[df['EVN'] == 6]
	len_df_temp = len(df_temp)
	if len_df_temp:
		print('- тиражи, в которых выпали только чётные номера (всего', len_df_temp, 'шт):')
		print(df[df['EVN'] == 6].tail(ANOMAL_DRAWING), '\n')
	return 0


def dict_with_full_statistic(df: pandas.core.frame.DataFrame) -> None:
	"""
	Функция собирает статистику, по расчитанным дополнительно столбцам.
	Выполняется сортировка по частоте - самые частотные значения в начале.
	"""
	print('ПОЛНАЯ СТАТИСТИКА АРХИВА ТИРАЖЕЙ В СЛОВАРЯХ')
	print('=' * 44)
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


