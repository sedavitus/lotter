import os
import pandas
import secrets


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


def search_in_dataframe(str_for_find: list,
                        df: pandas.core.frame.DataFrame) -> str:
    '''
	Поиск по базе данных определённой последовательности номеров
	'''
    No1, No2, No3, No4, No5, No6 = str_for_find
    if len(df[(df["N1"] == No1) & (df["N2"] == No2) & (df["N3"] == No3) & (df["N4"] == No4) & (df["N5"] == No5) & (df["N6"] == No6)]) == 0:
        result = "ранее не выпадали"
    else:
        # date_of_result = df["DRAW"]
        result = "такая комбинация уже выпадала!!!"
    return result
