import json
from pathlib import Path
from typing import Any

from src.eljur.homework_file import HomeworkFile
from src.eljur.homework import Homework
from src.eljur.mark_list import MarkList
from src.eljur.subject import Subject
from src.eljur.student import Student
from src.eljur.period import Period
from src.utils.date import Date


class ResponseParser:
	"""
	Class for reading and parsing responses files of the Eljur API.

	Reading files, parse it, convert that data to dataclasses.

	Attributes:
		_encoding (str): Encoding for reading files.
	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		"""
		Initializes ResponsesParser object.

		Args:
			encoding (str): Encoding for reading files.
		"""
		self._encoding = encoding


	def load_periods(
		self,
		periods: Path,
		user_id: str,
	) -> list[Period]:
		"""
		Loads and formates periods data.

		Args:
			periods (Path): Path to the periods file.
			user_id (str): User ID for correct loading periods.

		Returns:
			list[Period]: List of the periods.
		"""
		formatted_periods: list[Period] = []
		periods_data = self._read_json(periods)
		student = periods_data['response']['result']['students'][user_id]
		for period in student['periods']:
			start = Date.to_basic(period.get('start'))
			end = Date.to_basic(period.get('end'))
			if (
				not period.ambigious
				and start
				and end
			):
				formatted_period = Period(
					start=start,
					end=end,
				)
				formatted_periods.append(formatted_period)
		return formatted_periods


	def load_homeworks(
		self,
		homeworks: Path,
		user_id: str,
		subject_list: list[Subject],
	) -> list[Subject]:
		"""
		Loads homeworks to the subject list.

		Use after calling load_subject_list.

		Args:
			homeworks (Path): Path to the homeworks file.
			user_id (str): User ID for correct loading homeworks.
			subject_list (list[Subject]): Subject list.
		Returns:
			list[Subject]: Subject list with homeworks.
		"""
		homeworks_data = self._read_json(
			homeworks,
		)
		days = homeworks_data['response']['result']['students'][user_id]['days']
		for day in days:
			date = Date.to_basic(day)
			lessons = days[day]['items']
			for lesson in lessons.values():
				lesson_name = lesson['name']
				lesson_homeworks = lesson['homework']
				lesson_files = lesson.get('files', [])
				for subject in subject_list:
					if subject.name == lesson_name:
						similar_subject = subject
				files_to_homework_id: dict[int, list[HomeworkFile]] = {}
				for lesson_file in lesson_files:
					file_to_homework_id = lesson_file['to_id']
					filename = lesson_file['filename']
					file_link = lesson_file['link']
					file = HomeworkFile(filename, file_link)
					if file_to_homework_id in files_to_homework_id:
						files_to_homework_id[file_to_homework_id].append(file)
					else:
						files_to_homework_id[file_to_homework_id] = [file]
				homework_list = []
				for lesson_homework in lesson_homeworks.values():
					lesson_homework_value = lesson_homework['value']
					lesson_homework_id = lesson_homework['id']
					files = files_to_homework_id.get(lesson_homework_id, [])
					homework = Homework(
						date,
						lesson_homework_value,
						files,
					)
					homework_list.append(homework)
				similar_subject.homeworks.extend(homework_list)
		return subject_list


	def load_marks(
		self,
		marks: Path,
		user_id: str,
		subject_list: list[Subject],
	) -> list[Subject]:
		"""
		Loads marks to the subject list.

		Use after calling load_subject_list.

		Args:
			marks (Path): Path to the marks file.
			user_id (str): User id for correct load marks.
			subject_list (list[Subject]): Subject list.
		Returns:
			list[Subject]: Subject list with marks.
		"""
		marks_data = self._read_json(
			marks,
		)
		student = marks_data['response']['result']['students'][user_id] # типа user_id
		lessons = student['lessons']
		for lesson in lessons:
			lesson_name = lesson['name']
			lesson_marks = lesson['marks']
			mark_list = []
			for mark in lesson_marks:
				if mark['count']:
					mark_value = mark['convert']
					mark_list.append(mark_value)
			for subject in subject_list:
				if subject.name == lesson_name:
					subject.marks = MarkList(
						mark_list,
					)
		return subject_list


	def load_suject_list(
		self,
		marks: Path,
		user_id: str,
	) -> list[Subject]:
		"""
		Loads user's subject list.

		Subject have name, without another data.

		Args:
			marks (Path): Path to the marks file.
			user_id (str): User id for correct load subjects.
		
		Returns:
			list[Subject]: Subject list.
		"""
		subject_list = []
		marks_data = self._read_json(
			marks,
		)
		student = marks_data['response']['result']['students'][user_id] # типа user_id
		lessons = student['lessons']
		for lesson in lessons:
			subject = Subject(
				lesson['name']
			)
			subject_list.append(subject)
		return subject_list


	def get_user_ids(
		self,
		rules: Path,
	) -> list[Student]:
		"""
		Gets user pairs of the id and name.

		Args:
			rules (Path): Path to the rules file.

		Returns:
			list[Student]: List of the pairs.
		"""
		students_ids = []
		rules_data = self._read_json(
			rules,
		)
		students = rules_data['response']['result']['relations']['students']
		for student_id in students:
			student_name = students[student_id]['title']
			students_ids.append(
				Student(
					id=student_id,
					name=student_name,
				)
			)
		return students_ids


	def _read_json(
		self,
		file: Path,
	) -> dict[str, Any]:
		"""
		Reads json file and returns him data.

		Args:
			file (Path): Path to the json file.

		Returns:
			dict[str, Any]: Json data.
		"""
		return json.loads(file.read_text(self._encoding))
	