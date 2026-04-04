from src.eljur.json_parser import JsonParser
from src.school.subject_list import SubjectList
from src.school.subject import Subject
from src.school.mark_list import MarkList
from src.school.homework import Homework, HomeworkFile


class App:
	def __init__(
		self,
		subject_list: SubjectList,
	) -> None:
		self.json_parser = JsonParser()
		self.subject_list = subject_list


	def set_subject_list(
		self, 
		json_name: str, 
		user_id: str | None = None,
	) -> None:
		subject_list = self.json_parser.parse_subject_list(json_name, user_id)
		for subject in subject_list:
			subject_obj = Subject(subject, 5)
			self.subject_list.append_subject(subject_obj)


	def set_subjects_marks(
		self,
		json_name: str,
		user_id: str | None = None,
	) -> None:
		lessons_marks = self.json_parser.parse_marks(json_name, user_id)
		subject_list = self.subject_list.subject_list
		for subject in subject_list:
			marks = lessons_marks.get(subject.name, [])
			mark_list = MarkList(marks)
			subject.set_marks(mark_list)


	def set_subjects_homeworks(
		self,
		json_name: str,
	) -> None:
		dict_homeworks = self.json_parser.parse_homework(json_name)
		subjects = self.subject_list.subject_list
		for subject in subjects:
			subject_name = subject.name
			if subject_name not in dict_homeworks.keys():
				continue
			dates = dict_homeworks[subject_name]
			for date, data in dates.items():
				homework_obj = Homework(date)
				homework_list = data[0]
				if homework_list:
					for homework in homework_list:
						homework_obj.append_homework(homework)
				file_list = data[1]
				if file_list:
					for file in file_list:
						filename = file[0]
						file_link = file[1]
						homework_file_obj = HomeworkFile(filename, file_link)
						homework_obj.append_file(homework_file_obj)
				subject.append_homework(homework_obj)
