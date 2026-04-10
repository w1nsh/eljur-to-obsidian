from pathlib import Path

from config.user.config_parser import ConfigParser
from config.user.config import Config


class ConfigManager:
	def __init__(
		self,
		base_dir: Path,
		paths_file: Path,
		encoding: str = 'utf-8',
	) -> None:
		self._base_dir = base_dir
		self._paths_file = paths_file
		self._encoding = encoding


	def load_config(
		self,
	) -> Config:
		"""
		Load config.

		Load config, store it in `self._config`, and return it.

		Returns:
			Config: configuration dataclass.
		"""
		config_parser = ConfigParser(
			self._base_dir,
			self._paths_file,
			self._encoding,
		)
		paths = config_parser.load_paths()
		user_config = config_parser.load_user_config()
		user_eljur_config = config_parser.load_user_eljur_config()
		self._config = Config(
			paths,
			user_config,
			user_eljur_config,
		)
		return self._config


	def homeworks_set_need(
		self,
		need: bool,
	) -> None:
		"""
		High-level interface of `HomeworksConfig.set_need`.

		Sets new value of the class attribute need.

		Args:
			need (bool): New value of the class attribute.
		"""
		self._config.user_config.homeworks_config.set_need(need)


	def homeworks_set_path(
		self,
		path: Path,
	) -> None:
		"""
		High-level interface of `HomeworksConfig.set_path`.

		Sets new path to the file for storing information about user's homeworks.

		Args:
			path (Path): New path to file.
		"""
		self._config.user_config.homeworks_config.set_path(path)


	def homeworks_set_from_date(
		self,
		from_date: str,
	) -> None:
		"""
		High-level interface of `HomeworksConfig.set_from_date`.

		Sets new date start of the range.

		Args:
			from_date (str): New date start of the range.
		"""
		self._config.user_config.homeworks_config.set_from_date(from_date)


	def homeworks_set_to_date(
		self,
		to_date: str,
	) -> None:
		"""
		High-level interface of `HomeworksConfig.set_to_date`.

		Sets new date end of the range.

		Args:
			to_date (str): New date end of the range.
		"""
		self._config.user_config.homeworks_config.set_to_date(to_date)


	def marks_set_need(
		self,
		need: bool,
	) -> None:
		"""
		High-level interface of 'MarksConfig.set_need`.

		Sets new value of the class attribute need.

		Args:
			need (bool): New value of the class attribute.
		"""
		self._config.user_config.marks_config.set_need(need)


	def marks_set_path(
		self,
		path: Path,
	) -> None:
		"""
		High-level interface of 'MarksConfig.set_path`.

		Sets new path to the file for storing information about user's marks.

		Args:
			path (Path): New path to file.
		"""
		self._config.user_config.marks_config.set_path(path)


	def marks_set_from_date(
		self,
		from_date: str,
	) -> None:
		"""
		High-level interface of `MarksConfig.set_from_date`.

		Sets new date start of the range.

		Args:
			from_date (str): New date start of the range.
		"""
		self._config.user_config.marks_config.set_from_date(from_date)


	def marks_set_to_date(
		self,
		to_date: str,
	) -> None:
		"""
		High-level interface of `MarksConfig.set_to_date`.

		Sets new date end of the range.

		Args:
			to_date (str): New date end of the range.
		"""
		self._config.user_config.marks_config.set_to_date(to_date)


	def marks_set_desired_mark(
		self,
		subject_name: str,
		desired_mark: int,
	) -> None:
		"""
		High-level interface of `MarksConfig.set_desired_mark`.

		Sets desired mark for a selected subject by subject name.
		
		Args:
			subject_name (str): Subject name for a search subject.
			desired_mark (int): New desired mark of the subject.
		"""
		self._config.user_config.marks_config.set_desired_mark(subject_name, desired_mark)
