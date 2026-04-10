import json
from os import getenv
from typing import Any
from pathlib import Path

from dotenv import load_dotenv

from config.user.config import UserConfig, UserEljurConfig
from config.user.marks_config import MarksConfig, DesiredMark
from config.user.homeworks_config import HomeworksConfig
from config.paths.paths import Paths, SettingsPaths, ResponsesPaths


class ConfigParser:
	def __init__(
		self,
		base_dir: Path,
		paths_file: Path,
		encoding: str = 'utf-8',
	) -> None:
		self._base_dir = base_dir
		self._paths_file = paths_file
		self._encoding = encoding


	def load_paths(
		self,
	) -> Paths:
		paths_dict = self._load(self._paths_file)
		settings_paths_dict = paths_dict['settings']
		responses_paths_dict = paths_dict['responses']
		settings_paths = SettingsPaths(
			env=self._base_dir / settings_paths_dict['env'],
			config=self._base_dir / settings_paths_dict['config'],
			eljur_cache=self._base_dir / settings_paths_dict['eljur_cache'],
			user_hash=self._base_dir / settings_paths_dict['user_hash'],
		)
		responses_paths = ResponsesPaths(
			assessments=self._base_dir / responses_paths_dict['assessments'],
			diary=self._base_dir / responses_paths_dict['diary'],
			homework=self._base_dir / responses_paths_dict['homework'],
			marks=self._base_dir / responses_paths_dict['marks'],
			periods=self._base_dir / responses_paths_dict['periods'],
			rules=self._base_dir / responses_paths_dict['rules'],
			schedule=self._base_dir / responses_paths_dict['schedule'],
		)
		paths = Paths(
			settings_paths=settings_paths,
			responses_paths=responses_paths,
			base_dir=self._base_dir,
		)
		self._paths = paths
		return self._paths


	def load_user_config(
		self,
	) -> UserConfig:
		user_config_dict = self._load(self._base_dir / self._paths.settings_paths.config)
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
		user_config = UserConfig(
			marks_config=marks_config,
			homeworks_config=homeworks_config
		)
		return user_config


	def load_user_eljur_config(
		self,
	) -> UserEljurConfig:
		load_dotenv(self._base_dir / self._paths.settings_paths.env)
		login = getenv('ELJUR_LOGIN')
		password = getenv('ELJUR_PASSWORD')
		school_class = getenv('ELJUR_SCHOOL_CLASS')
		vendor = getenv('ELJUR_VENDOR')
		devkey = getenv('ELJUR_DEVKEY')
		auth_token = getenv('ELJUR_AUTH_TOKEN')
		user_eljur_config = UserEljurConfig(
			login,
			password,
			school_class,
			vendor,
			devkey,
			auth_token,
		)
		return user_eljur_config


	def _load(
		self,
		path: Path,
	) -> dict[str, Any]:
		data = json.loads(path.read_text(encoding=self._encoding))
		return data
	