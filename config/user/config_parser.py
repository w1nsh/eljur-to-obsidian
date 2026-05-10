import json
from os import getenv
from typing import Any
from pathlib import Path

from dotenv import load_dotenv

from config.user.config import UserDataConfig, UserEljurConfig
from config.user.marks_config import MarksConfig, DesiredMark
from config.user.homeworks_config import HomeworksConfig
from config.paths.paths import Paths, SettingsPaths, ResponsesPaths


class ConfigParser:
	"""
	Class for parsing config files and loading data from them.
	
	Attributes:
		_base_dir (Path): base directory of the project.
		_paths_path (Path): path to the file with paths.
		_encoding (str): encoding for reading files.
		_paths (Paths): paths to all technical files and directories used in the project.
	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		self._encoding = encoding


	def load_paths(
		self,
		base_dir: Path,
		paths_path: Path,
	) -> Paths:
		"""
		Loads paths file. Create a Paths dataclass.

		All paths is relative to the base directory of the project.

		Args:
			base_dir (Path): base directory of the project.
			paths_path (Path): relative path to the file with paths.

		Returns:
			Paths: paths to all technical files of the project.
		"""
		paths_dict = self._load_json(base_dir / paths_path)
		settings_paths_dict = paths_dict['settings']
		responses_paths_dict = paths_dict['responses']
		settings_paths = SettingsPaths(
			env=base_dir / settings_paths_dict['env'],
			config=base_dir / settings_paths_dict['config'],
		)
		responses_paths = ResponsesPaths(
			assessments=base_dir / responses_paths_dict['assessments'],
			diary=base_dir / responses_paths_dict['diary'],
			homework=base_dir / responses_paths_dict['homework'],
			marks=base_dir / responses_paths_dict['marks'],
			periods=base_dir / responses_paths_dict['periods'],
			rules=base_dir / responses_paths_dict['rules'],
			schedule=base_dir / responses_paths_dict['schedule'],
		)
		self._paths = Paths(
			settings=settings_paths,
			responses=responses_paths,
			base_dir=base_dir,
		)
		return self._paths


	def load_user_data_config(
		self,
		config_path: Path,
	) -> UserDataConfig:
		"""
		Loads user data config. Create a UserDataConfig dataclass.

		Args:
			config_path (Path): absolute path to the user data config file.

		Returns:
			UserDataConfig: user data configuration.
		"""
		user_config_dict = self._load_json(config_path)
		marks_config_dict = user_config_dict['marks']
		homeworks_config_dict = user_config_dict['homeworks']
		marks_config = MarksConfig(
			need=marks_config_dict['need'],
			path=marks_config_dict['path'],
			from_date=marks_config_dict['from'],
			to_date=marks_config_dict['to'],
			subjects=[
				DesiredMark(
					subject_name=subject_dict['name'],
					desired_mark=subject_dict['desired_mark']
				)
				for subject_dict in marks_config_dict['subjects']
			]
		)
		homeworks_config = HomeworksConfig(
			need=homeworks_config_dict['need'],
			path=homeworks_config_dict['path'],
			from_date=homeworks_config_dict['from'],
			to_date=homeworks_config_dict['to']
		)
		user_data_config = UserDataConfig(
			marks=marks_config,
			homeworks=homeworks_config
		)
		return user_data_config


	def load_user_eljur_config(
		self,
		env_path: Path,
	) -> UserEljurConfig:
		"""
		Loads user Eljur config. Create a UserEljurConfig dataclass.

		Args:
			env_path (Path): absolute path to the .env config file.
		
		Returns:
			UserEljurConfig: user Eljur configuration.
		"""
		if env_path.exists():
			load_dotenv(env_path)
			login = getenv('ELJUR_LOGIN')
			password = getenv('ELJUR_PASSWORD')
			school_class = getenv('ELJUR_SCHOOL_CLASS')
			vendor = getenv('ELJUR_VENDOR')
			devkey = getenv('ELJUR_DEVKEY')
			auth_token = getenv('ELJUR_AUTH_TOKEN')
		else:
			login = None
			password = None
			school_class = None
			vendor = None
			devkey = None
			auth_token = None
		user_eljur_config = UserEljurConfig(
			login if login else '',
			password if password else '',
			school_class if school_class else '',
			vendor if vendor else '',
			devkey if devkey else '',
			auth_token if auth_token else '',
		)
		return user_eljur_config


	def _load_json(
		self,
		path: Path,
	) -> dict[str, Any]:
		"""
		Loads json file and returns it as a dictionary.

		Args:
			path (Path): absolute path to the json file.

		Returns:
			dict[str, Any]: content of the json file as a dictionary.
		"""
		json_string = path.read_text(encoding=self._encoding)
		json_dict = json.loads(json_string)
		return json_dict
	