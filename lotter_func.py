import os
import pandas
import math


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
	if len(df[(df["N1"] == No1) & (df["N2"] == No2) & (df["N3"] == No3) & (df["N4"] == No4) & (df["N5"] == No5) & (df["N6"] == No6)]) == 0:
		result = "ранее не выпадали"
	else:
        # date_of_result = df["DRAW"]
		result = "такая комбинация уже выпадала!!!"
	return result


def full_database_statistic(MIN: int, MAX: int, df: pandas.core.frame.DataFrame) -> None:
	"""
	Получение статистических данных полного архива тиражей
	(начиная с первого тиража базы и до самого последнего)
	"""
	print('ОБЩАЯ СТАТИСТИКА ПОЛНОЙ БАЗЫ ТИРАЖЕЙ')
	print('-' * 36)
	print('- лотерея \"Спортлото', MIN, 'из', MAX, '\b\"')
	if MIN == 6 and MAX == 49:
		C_5_48 = int(math.factorial(48) / (math.factorial(5) * math.factorial(48-5)))  # C_5_48
		C_6_49 = int(math.factorial(49) / (math.factorial(6) * math.factorial(49-6)))  # C_6_49 = 13.983.816
		print('- число возможных комбинаций 6 номеров из 49 =', C_6_49)
		print('- число перестановок для 6 номеров =', math.factorial(6))  # 720
		print('- вероятность выпадения в тираже одного номера =', round((C_5_48 / C_6_49), 5))  # 0.12245
		print('- вероятность выпадения в тираже пары номеров =', round(((1 / 49) * (5 / 48)), 5))  # 0.00213
		print('- вероятность выпадения в тираже тройки номеров =', round(((1 / 49) * (5 / 48) * (4 / 47)), 5))  # 0.00018
		print('- основные характеристики базы тиражей:')
		# Данные из df.describe() сперва собираем в соответствующие списки:
		list_pandas_mean = [int((df.describe()['N1']['mean']).round(0)), int((df.describe()['N2']['mean']).round(0)), int((df.describe()['N3']['mean']).round(0)), int((df.describe()['N4']['mean']).round(0)), int((df.describe()['N5']['mean']).round(0)), int((df.describe()['N6']['mean']).round(0))]
		list_pandas_min = [int(df.describe()['N1']['min']), int(df.describe()['N2']['min']), int(df.describe()['N3']['min']), int(df.describe()['N4']['min']), int(df.describe()['N5']['min']), int(df.describe()['N6']['min'])]
		list_pandas_25p = [int(df.describe()['N1']['25%']), int(df.describe()['N2']['25%']), int(df.describe()['N3']['25%']), int(df.describe()['N4']['25%']), int(df.describe()['N5']['25%']), int(df.describe()['N6']['25%'])]
		list_pandas_50p = [int(df.describe()['N1']['50%']), int(df.describe()['N2']['50%']), int(df.describe()['N3']['50%']), int(df.describe()['N4']['50%']), int(df.describe()['N5']['50%']), int(df.describe()['N6']['50%'])]
		list_pandas_75p = [int(df.describe()['N1']['75%']), int(df.describe()['N2']['75%']), int(df.describe()['N3']['75%']), int(df.describe()['N4']['75%']), int(df.describe()['N5']['75%']), int(df.describe()['N6']['75%'])]
		list_pandas_max = [int(df.describe()['N1']['max']), int(df.describe()['N2']['max']), int(df.describe()['N3']['max']), int(df.describe()['N4']['max']), int(df.describe()['N5']['max']), int(df.describe()['N6']['max'])]
		print('\tминимальные номера:', *list_pandas_min, '\b,', search_in_dataframe(list_pandas_min, df))
		print('\t25% номеров <= чем:', *list_pandas_25p, '\b,', search_in_dataframe(list_pandas_25p, df))
		print('\t50% номеров <= чем:', *list_pandas_50p, '\b,', search_in_dataframe(list_pandas_50p, df))
		print('\tмедианное значение:', *list_pandas_mean, '\b,', search_in_dataframe(list_pandas_mean, df))
		print('\t75% номеров <= чем:', *list_pandas_75p, '\b,', search_in_dataframe(list_pandas_75p, df))
		print('\tмаксимальные номера:', *list_pandas_max, '\b,', search_in_dataframe(list_pandas_max, df), '\n')
	return 0


def last_drawing_statistic(amount_of_draws: int, df: pandas.core.frame.DataFrame) -> None:
	"""
	Получение отчёта с подробными результатами последнего тиража
	"""
	print('РЕЗУЛЬТАТЫ ПОСЛЕДНЕГО ТИРАЖА')
	print('-' * 28)
	print('- число тиражей в базе', amount_of_draws)
	print('-', amount_of_draws, '\b-ой тираж состоялся', df['DATE'][amount_of_draws].date(), 'с результатами:', df['N1'][amount_of_draws], df['N2'][amount_of_draws], df['N3'][amount_of_draws], df['N4'][amount_of_draws], df['N5'][amount_of_draws], df['N6'][amount_of_draws])
	if df['WIN6'][amount_of_draws] > 0:
		print('- 6 номеров угадали:', df['WIN6'][amount_of_draws], '\b, выигрыш каждого составил', df['BYN6'][amount_of_draws], 'BYN')
	else:
		print('- 6 номеров не угадал никто')
	if df['WIN6'][amount_of_draws] > 0:
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
	количество тиражей указывается польхователем в lotter.ini
	"""
	print('РЕЗУЛЬТАТЫ ПОСЛЕДНИХ', USER_AMOUNT_DRAWING, 'ТИРАЖЕЙ')
	print('-' * (21 + len(str(USER_AMOUNT_DRAWING)) + 8))
	print('- тиражи отсортированы по убыванию:')
	print(df.loc[:, "DATE":"N6"].tail(USER_AMOUNT_DRAWING).sort_values(by="DRAW", ascending=False), '\n')
	return 0
