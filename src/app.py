from pathlib import Path

from config.user.config_manager import Config, ConfigManager
from config.user.marks_config import MarksConfig
from config.user.homeworks_config import HomeworksConfig
from src.utils.date import Date
from src.eljur.eljur_parser import EljurParser
from src.eljur.json_parser import JsonParser
from src.school.subject_list import SubjectList
from src.school.subject import Subject
from src.school.mark_list import MarkList
from src.school.homework import Homework, HomeworkFile


class App:
	def __init__(
		self,
		base_dir: Path,
		paths_path: Path,
		encoding: str = 'utf-8',
	) -> None:
		self._base_dir = base_dir
		self._paths_file = paths_path
		self._encoding = encoding
		self._config_manager = ConfigManager(
			base_dir,
			paths_path,
			encoding
		)
		self._json_parser = JsonParser(encoding)
		self._subject_list = SubjectList()


	def _load_config(
		self,
	) -> None:
		self._config = self._config_manager.load_config()


	def _eljur_login(
		self,
	) -> None:
		if not self._config.user_eljur_config.auth_token:
			self._eljur_parser = EljurParser(
				self._config.user_eljur_config.devkey,
				self._config.user_eljur_config.vendor,
				self._config.user_eljur_config.school_class,
				login=self._config.user_eljur_config.login,
				password=self._config.user_eljur_config.password,
			)
			access = self._eljur_parser.authenticate()
			if access:
				auth_token = self._eljur_parser.get_auth_token()
				# add token to config and write it to .env file
			# else:
				# Add error auth failed
		else:
			self._eljur_parser = EljurParser(
				self._config.user_eljur_config.devkey,
				self._config.user_eljur_config.vendor,
				self._config.user_eljur_config.school_class,
				auth_token=self._config.user_eljur_config.auth_token,
			)


	def _get_start_periods_dates(
		self,
		periods_path: Path,
		user_id: str,
	) -> list[str]:
		periods = self._eljur_parser.get_periods(user_id, show_disabled=True)
		# JSON WRITER ADD WRITE PERIODS TO JSON FROM ELJUR
		start_dates = self._json_parser.load_start_period_dates(periods_path, user_id)
		return start_dates


	def _update_homeworks_dates(
		self,
		homeworks_config: HomeworksConfig,
	) -> None:
		current_date = Date.current_date()
		last_to_date = homeworks_config.to_date
		homeworks_config.set_from_date(last_to_date)
		homeworks_config.set_to_date(current_date)

	
	def _update_marks_dates(
		self,
		marks_config: MarksConfig,
	) -> None:
		current_date = Date.current_date()

		last_to_date = marks_config.to_date
		marks_config.set_from_date(last_to_date)

		marks_config.set_to_date(current_date)


	def _load_subject_list(
		self, 
		user_id: str,
	) -> None:
		# works only with marks.json
		subject_list = self._json_parser.load_subject_list(
			self._config.paths.responses_paths.marks,
			user_id,
		)
		for subject in subject_list: # adds desired marks
			subject_obj = Subject(subject, 5)
			self._subject_list.append_subject(subject_obj)


	def _load_subjects_marks(
		self,
		json_name: str,
		user_id: str | None = None,
	) -> None:
		lessons_marks = self._json_parser.load_marks(json_name, user_id)
		subject_list = self._subject_list.subject_list
		for subject in subject_list:
			marks = lessons_marks.get(subject.name, [])
			mark_list = MarkList(marks)
			subject.set_marks(mark_list)


	def _load_subjects_homeworks(
		self,
		json_name: str,
	) -> None:
		dict_homeworks = self._json_parser.load_homework(json_name)
		subjects = self._subject_list.subject_list
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
