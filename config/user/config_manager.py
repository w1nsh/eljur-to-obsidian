from pathlib import Path
from typing import Any

from config.user.config_parser import ConfigParser
from config.user.config_writer import ConfigWriter
from config.user.config import Config, UserEljurConfig, UserDataConfig


class ConfigManager:
	"""
	Class for managing config data.

	Attributes:
		parser (ConfigParser): config parser for loading data from config files.
		writer (ConfigWriter): config writer for writing data to config files.
		_base_dir (Path): base directory of the project.
		_paths_path (Path): path to the file with technical paths.
		_encoding (str): encoding for reading and writing files.
		_config (Config): configuration dataclass.
	"""

	def __init__(
		self,
		base_dir: Path,
		paths_path: Path,
		encoding: str,
	) -> None:
		self._base_dir = base_dir
		self._paths_path = paths_path
		self._encoding = encoding
		self.parser = ConfigParser(
			encoding,
		)
		self.writer = ConfigWriter(
			encoding,
			)


	def load_config(
		self,
	) -> None:
		"""
		Load config.

		Load config, store it in `self._config`, and return it.

		Returns:
			Config: configuration dataclass.
		"""
		paths = self.parser.load_paths(
			base_dir=self._base_dir,
			paths_path=self._paths_path,
		)
		user_data_config = self.parser.load_user_data_config(
			config_path=paths.settings.config,
		) # add validate to all parameters
		user_eljur_config = self.parser.load_user_eljur_config(
			env_path=paths.settings.env,
		) # add validate to exists
		self._config = Config(
			paths=paths,
			user_data=user_data_config,
			user_eljur=user_eljur_config,
		)


	def get_config(
		self,
	) -> Config:
		"""
		Get config.

		Get config from `self._config` and return it.
		Use only after calling `load_config` method.

		Returns:
			Config: configuration dataclass.
		"""
		return self._config


	def write_env(
		self,
	) -> None:
		"""
		Write data to the .env config file.
		"""
		env_content = self._generate_env(
			self._config.user_eljur,
		)
		self.writer.write_env(
			env_path=self._config.paths.settings.env,
			env_content=env_content,
		)


	def write_config(
		self,
	) -> None:
		"""
		Write data to the user config file.
		"""
		config_content = self._generate_config_content(
			self._config.user_data,
		)
		self.writer.write_config(
			config_path=self._config.paths.settings.config,
			config_content=config_content,
		)


	def _generate_config_content(
		self,
		user_data_config: UserDataConfig,
	) -> dict[str, Any]:
		"""
		Generates content for the user config file.

		Args:
			user_data_config (UserDataConfig): user data configuration.

		Returns:
			dict[str, Any]: content for the user config file.
		"""
		return {
			"marks": {
				"need": user_data_config.marks.need,
				"path": user_data_config.marks.path.as_posix(),
				"from_date": user_data_config.marks.from_date,
				"to_date": user_data_config.marks.to_date,
			},
			"homeworks": {
				"need": user_data_config.homeworks.need,
				"path": user_data_config.homeworks.path.as_posix(),
				"from_date": user_data_config.homeworks.from_date,
				"to_date": user_data_config.homeworks.to_date,
			},
		}


	def _generate_env(
		self,
		user_eljur_config: UserEljurConfig,
	) -> str:
		"""
		Generates content for the .env config file.
		
		Returns:
			str: content for the .env config file.
				Contains data for logging in Eljur.
		"""
		env_content = ''
		env_content += f'ELJUR_LOGIN={user_eljur_config.login}\n'
		env_content += f'ELJUR_PASSWORD={user_eljur_config.password}\n'
		env_content += f'ELJUR_SCHOOL_CLASS={user_eljur_config.school_class}\n'
		env_content += f'ELJUR_VENDOR={user_eljur_config.vendor}\n'
		env_content += f'ELJUR_DEVKEY={user_eljur_config.devkey}\n'
		env_content += f'ELJUR_AUTH_TOKEN={user_eljur_config.auth_token}\n'
		return env_content
