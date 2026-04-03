import json

from src.utils.date import Date


class JsonParser:
	def get_subject_list(
			self, 
			json_name: str, 
			user_id: str | None = None
	) -> list[str]:
		subject_list = []
		with open(json_name, 'r', encoding='utf-8') as f:
			marks_json = json.load(f)
			try:
				students = marks_json['response']['result']['students']
				if not user_id:
					user_id = list(students.keys())[0]
				lessons = students[user_id]['lessons']
				for lesson in lessons:
					lesson_name = lesson['name']
					subject_list.append(lesson_name)
				return subject_list
			except Exception as e:
				raise Exception(f'Error parsing marks JSON (get_subject_list): {e}')
	

	def parse_marks(
			self,
			json_name: str,
			user_id: str | None = None,
	) -> dict[str, list[int]]:
		lessons_marks = {}
		with open(json_name, 'r', encoding='utf-8') as f:
			marks_json = json.load(f)
			try:
				students = marks_json['response']['result']['students']
				if not user_id:
					user_id = list(students.keys())[0]
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
			except Exception as e:
				raise Exception(f'Error parsing marks JSON (parse_marks): {e}')


	def parse_homework(
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


	def parse_homework_dates(
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
