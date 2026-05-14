import json
from os import getenv
from typing import Any
from pathlib import Path

from dotenv import load_dotenv

from config.user.config import UserDataConfig, UserEljurConfig, Config
from config.user.marks_config import MarksConfig
from config.user.homeworks_config import HomeworksConfig
from config.paths.paths import Paths, SettingsPaths, ResponsesPaths
from config.paths.auxiliary.auxiliary_paths import AuxiliaryPaths
from config.paths.auxiliary.md_auxiliary_paths import MdAuxiliaryPaths
from config.paths.auxiliary.homeworks_paths import HomeworksPaths
from config.paths.auxiliary.marks_paths import MarksPaths


class ConfigParser:
	"""
	Class for parsing config files and loading data from them.
	
	Attributes:
		_encoding (str): Encoding for reading files.
	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		"""
		Initializes ConfigParser object.

		Args:
			encoding (str): Encofing for reading files.
		"""
		self._encoding = encoding


	def load_config(
		self,
		base_dir: Path,
		paths_path: Path,
	) -> Config:
		"""
		Loads config.

		Loads config and returns it.

		Args:
			base_dir (Path): Base directory of the project.
			paths_path (Path): Path to the file with technical paths.

		Returns:
			Config: Configuration dataclass.
		"""
		paths = self.load_paths(
				base_dir=base_dir,
				paths_path=paths_path,
			)
		return Config(
			paths=paths,
			user_data=self.load_user_config(
				paths.settings.config,
			),
			user_eljur=self.load_eljur_config(
				paths.settings.env,
			)
		)


	def load_paths(
		self,
		base_dir: Path,
		paths_path: Path,
	) -> Paths:
		"""
		Loads paths file. Create a Paths dataclass.

		All paths is relative to the base directory of the project.

		Args:
			base_dir (Path): Base directory of the project.
			paths_path (Path): Relative path to the file with paths.

		Returns:
			Paths: Paths to all technical files of the project.
		"""
		paths = self._load_json(base_dir / paths_path)
		auxiliary_paths = paths['auxiliary']
		settings_paths = paths['settings']
		responses_paths = paths['responses']
		axiliary = self._load_auxiliary_paths(
			base_dir=base_dir,
			auxiliary_paths=auxiliary_paths,
		)
		settings = self._load_settings_paths(
			base_dir=base_dir,
			settings_paths=settings_paths,
		)
		responses = self._load_responses_paths(
			base_dir=base_dir,
			responses_paths=responses_paths,
		)
		return Paths(
			auxiliary=axiliary,
			settings=settings,
			responses=responses,
			base_dir=base_dir,
		)


	def load_user_config(
		self,
		config_path: Path,
	) -> UserDataConfig:
		"""
		Loads user data config.
		
		Creates a UserDataConfig dataclass.

		Args:
			config_path (Path):
				Absolute path to the user data config file.

		Returns:
			UserDataConfig: User data configuration.
		"""
		user_config = self._load_json(config_path)
		marks = user_config['marks']
		homeworks = user_config['homeworks']
		marks_config = self._load_marks_config(
			marks_config=marks,
		)
		homeworks_config = self._load_homeworks_config(
			homeworks_config=homeworks,
		)
		return UserDataConfig(
			marks=marks_config,
			homeworks=homeworks_config
		)


	def load_eljur_config(
		self,
		env_path: Path,
	) -> UserEljurConfig:
		"""
		Loads user Eljur config.
		
		Creates a UserEljurConfig dataclass.

		Args:
			env_path (Path):
				Absolute path to the .env config file.
		
		Returns:
			UserEljurConfig: User Eljur configuration.
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
		return UserEljurConfig(
			login if login else '',
			password if password else '',
			school_class if school_class else '',
			vendor if vendor else '',
			devkey if devkey else '',
			auth_token if auth_token else '',
		)


	def _load_auxiliary_paths(
		self,
		base_dir: Path,
		auxiliary_paths: dict[str, Any],
	) -> AuxiliaryPaths:
		"""
		Loads auxiliary paths from dict, and returns it.

		Args:
			base_dir (Path): Base directory of the project.
			auxiliary_paths (dict): Auxiliary paths dictionary.

		Returns:
			AuxiliaryPaths: Paths to auxiliary files.
		"""
		return AuxiliaryPaths(
			desired_marks=base_dir / auxiliary_paths['desired_marks'],
			md=MdAuxiliaryPaths(
				homeworks=HomeworksPaths(
					starts_with=base_dir / auxiliary_paths['md']['homeworks']['starts_with'],
					ends_with=base_dir / auxiliary_paths['md']['homeworks']['ends_with'],
				),
				marks=MarksPaths(
					starts_with=base_dir / auxiliary_paths['md']['marks']['starts_with'],
					ends_with=base_dir / auxiliary_paths['md']['marks']['ends_with'],
				),
			),
		)
	

	def _load_settings_paths(
		self,
		base_dir: Path,
		settings_paths: dict[str, Any],
	) -> SettingsPaths:
		"""
		Loads settings paths from dict, and returns it.

		Args:
			base_dir (Path): Base directory of the project.
			settings_paths (dict): Settings paths dictionary.

		Returns:
			SettingsPaths: Paths to settings files.
		"""
		return SettingsPaths(
			env=base_dir / settings_paths['env'],
			config=base_dir / settings_paths['config'],
		)


	def _load_responses_paths(
		self,
		base_dir: Path,
		responses_paths: dict[str, Any],
	) -> ResponsesPaths:
		"""
		Loads responses paths from dict, and returns it.

		Args:
			base_dir (Path): Base directory of the project.
			responses_paths (dict): Responses paths dictionary.

		Returns:
			ResponsesPaths: Paths to responses files.
		"""
		return ResponsesPaths(
			assessments=base_dir / responses_paths['assessments'],
			diary=base_dir / responses_paths['diary'],
			homeworks=base_dir / responses_paths['homeworks'],
			marks=base_dir / responses_paths['marks'],
			periods=base_dir / responses_paths['periods'],
			rules=base_dir / responses_paths['rules'],
			schedule=base_dir / responses_paths['schedule'],
		)


	def _load_marks_config(
		self,
		marks_config: dict[str, Any],
	) -> MarksConfig:
		"""
		Loads marks config from dict, and returns it as MarksConfig.

		Args:
			marks_config (dict[str, Any]): Marks config dictionary.

		Returns:
			MarksConfig: Marks user configuration.
		"""
		return MarksConfig(
			need=marks_config['need'],
			path=marks_config['path'],
			from_date=marks_config['from'],
			to_date=marks_config['to'],
		)


	def _load_homeworks_config(
		self,
		homeworks_config: dict[str, Any],
	) -> HomeworksConfig:
		"""
		Loads homeworks config from dict, and returns it as HomeworksConfig.

		Args:
			homeworks_config (dict[str, Any]): Homeworks config dictionary.

		Returns:
			HomeworksConfig: Homeworks user configuration.
		"""
		return HomeworksConfig(
			need=homeworks_config['need'],
			path=homeworks_config['path'],
			from_date=homeworks_config['from'],
			to_date=homeworks_config['to'],
		)


	def _load_json(
		self,
		path: Path,
	) -> dict[str, Any]:
		"""
		Loads json file and returns it as a dictionary.

		Args:
			path (Path): Absolute path to the json file.

		Returns:
			dict[str, Any]: Content of the json file as a dictionary.
		"""
		json_string = path.read_text(encoding=self._encoding)
		json_dict = json.loads(json_string)
		return json_dict
	