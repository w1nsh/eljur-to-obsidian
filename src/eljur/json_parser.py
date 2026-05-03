from pathlib import Path
import json

from src.utils.date import Date


class JsonParser:
	def __init__(
		self,
		encoding: str = 'utf-8',
	) -> None:
		self._encoding = encoding


	# def load_subject_list(
	# 	self,
	# 	json_path: Path,
	# 	user_id: str | None = None,
	# ) -> list[str]:
	# 	# works with only marks Json
	# 	subject_list = []
	# 	with open(json_path, 'r', encoding='utf-8') as f:
	# 		marks_json = json.load(f)
	# 		try:
	# 			students = marks_json['response']['result']['students']
	# 			if not user_id:
	# 				user_id = list(students.keys())[0]
	# 			lessons = students[user_id]['lessons']
	# 			for lesson in lessons:
	# 				lesson_name = lesson['name']
	# 				subject_list.append(lesson_name)
	# 			return subject_list
	# 		except Exception as e:
	# 			raise Exception(f'Error parsing marks JSON (get_subject_list): {e}')


	def load_subject_list(
		self,
		marks_path: Path,
		user_id: str,
	) -> list[str]:
		# works only with marks.json
		subject_list = []
		marks_text = marks_path.read_text(self._encoding)
		marks_dict = json.loads(marks_text)
		students = marks_dict['response']['result']['students']
		lessons = students[user_id]['lessons']
		for lesson in lessons:
			lesson_name = lesson['name']
			subject_list.append(lesson_name)
		return subject_list


	# def load_marks(
	# 	self,
	# 	json_name: str,
	# 	user_id: str | None = None,
	# ) -> dict[str, list[int]]:
	# 	lessons_marks = {}
	# 	with open(json_name, 'r', encoding='utf-8') as f:
	# 		marks_json = json.load(f)
	# 		try:
	# 			students = marks_json['response']['result']['students']
	# 			if not user_id:
	# 				user_id = list(students.keys())[0]
	# 			lessons = students[user_id]['lessons']
	# 			for lesson in lessons:
	# 				lesson_name = lesson['name']
	# 				marks = lesson['marks']
	# 				mark_list = []
	# 				for mark in marks:
	# 					if mark['count']:
	# 						mark_value = mark['convert']
	# 						mark_list.append(mark_value)
	# 				lessons_marks[lesson_name] = mark_list
	# 			return lessons_marks
	# 		except Exception as e:
	# 			raise Exception(f'Error parsing marks JSON (parse_marks): {e}')


	def load_marks(
		self,
		marks_path: Path,
		user_id: str,
	) -> dict[str, list[int]]:
		lessons_marks = {}
		marks_text = marks_path.read_text(self._encoding)
		marks_dict = json.loads(marks_text)
		students = marks_dict['response']['result']['students']
		lessons = students[user_id]['lessons']
		for lesson in lessons:
			lesson_name = lesson['name']
			marks = lesson['marks']
			mark_list = []
			for mark in marks:
				if mark['count']:
					mark_value = mark['convert']
					mark_list.append(mark_value)
			lessons_marks[lesson_name] = mark_list
		return lessons_marks


	def load_homework(
		self,
		json_name: str,
	) -> dict[str, dict[str, tuple[list[str], list[tuple[str, str]]]]]:
		lsns_hw = {}
		with open(json_name, 'r', encoding='utf-8') as f:
			hw_json = json.load(f)
			try:
				days = hw_json['response']['result']['days']
				for day in days:
					lsns = days[day]['items']
					date = Date.to_basic(day)
					for lsn in lsns:
						date_hw = {}
						lsn_name = lsn['name']
						hws = lsn['homework']
						files = lsn.get('files', {}).get('file', [])
						hw_list = [hw['value'] for hw in hws.values()]
						if files:
							file_list = [(file['filename'], file['link']) for file in files]
						else:
							file_list = []
						date_hw[date] = (hw_list, file_list)
						dt_hw = lsns_hw.get(lsn_name, {})
						if not dt_hw:
							lsns_hw[lsn_name] = date_hw
						else:
							lsns_hw[lsn_name].update(date_hw)
				return lsns_hw
			except Exception as e:
				raise Exception(f'Error parsing homeworks JSON (parse_homework): {e}')
			

	def load_homeworks2(
		self,
		homeworks_path: Path,
	) -> dict[str, dict[str, tuple[list[str], list[tuple[str, str]]]]]:
		lessons_homeworks = {}
		homeworks_text = homeworks_path.read_text(self._encoding)
		homeworks_dict = json.loads(homeworks_text)
		days = homeworks_dict['response']['result']['days']
		for day in days:
			lessons = days[day]['items']
			date = Date.to_basic(day)
			for lesson in lessons:
				date_homework = {}
				lesson_name = lesson['name']
				lesson_homeworks = lesson['homework']
				lesson_files = lesson.get('files', {}).get('file', [])
				homeworks_list = []
				for homework in lesson_homeworks.values():
					homework = homework['value']
					homeworks_list.append(homework)
				file_list = []
				for file in lesson_files:
					filename = file['filename']
					file_link = file['link']
					file_list.append((filename, file_link))
				date_homework[date] = (homeworks_list, file_list)
				date_homework = lessons_homeworks.get(lesson_name, {})
				if not lessons_homeworks:
					lessons_homeworks[lesson_name] = date_homework
				else:
					lessons_homeworks[lesson_name].update(date_homework)
			return lessons_homeworks


	def load_homework_dates(
		self,
		json_name: str,
	) -> list[str]:
		with open(json_name, 'r', encoding='utf-8') as f:
			homeworks_json = json.load(f)
			date_list = []
			try:
				days = homeworks_json['response']['result']['days']
				for day in days:
					date = Date.to_basic(day)
					date_list.append(date)
				return date_list
			except Exception as e:
				raise Exception(f'Error parsing homeworks JSON (parse_homework_dates): {e}')


	def load_start_period_dates(
		self,
		periods_path: Path,
		user_id: str,
	) -> list[str]:
		periods_text = periods_path.read_text(self._encoding)
		periods_dict = json.loads(periods_text)
		start_period_dates = []
		periods = periods_dict['response']['result']['students'][user_id]['periods']
		for period in periods:
			start_date = Date.to_basic(period['start'])
			start_period_dates.append(start_date)
		return start_period_dates
