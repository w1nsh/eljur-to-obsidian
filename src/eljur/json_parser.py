from pathlib import Path
import json

from src.utils.date import Date


class JsonParser:
	def __init__(
		self,
		encoding: str,
	) -> None:
		self._encoding = encoding


	def load_subject_list(
		self,
		marks_path: Path,
		user_id: str,
	) -> list[str]:
		subject_list = []
		marks_text = marks_path.read_text(self._encoding)
		marks_dict = json.loads(marks_text)
		students = marks_dict['response']['result']['students']
		lessons = students[user_id]['lessons']
		for lesson in lessons:
			lesson_name = lesson['name']
			subject_list.append(lesson_name)
		return subject_list


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


	def load_homeworks(
		self,
		homeworks_path: Path,
	) -> dict[str, dict[str, list[dict[str, str]]]]:
		subjects: dict[str, dict] = {}
		homeworks_str = homeworks_path.read_text(self._encoding)
		homeworks_dict = json.loads(homeworks_str)
		days = homeworks_dict['response']['result']['days']
		for day in days:
			date = Date.to_basic(day)
			lessons = days[day]['items']
			for lesson in lessons:
				homeworks: list[dict[str, str]] = []
				files: dict[str, list[dict[str, str]]] = {}
				lesson_name = lesson['name']
				raw_files = lesson.get('files', {})
				raw_homeworks = lesson['homework']
				for raw_file in raw_files.values():
					file_id = raw_file['id']
					filename = raw_file['filename']
					file_link = raw_file['link']
					file = {
						'name': filename,
						'link': file_link,
					}
					if files.get(file_id):
						files[file_id].append(file)
					else:
						files[file_id] = [file]
				for raw_homework in raw_homeworks.values():
					homework = {}
					homework_id = raw_homework['id']
					homework_value = raw_homework['value']
					homework['value'] = homework_value
					if homework_id in files.keys():
						homework['files'] = files[homework_id]
					else:
						homework['files'] = []
					homeworks.append(homework)
				if subjects.get(lesson_name):
					subjects[lesson_name][date] = homeworks
				else:
					subjects[lesson_name] = {
						date: homeworks
					}
		return subjects


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
