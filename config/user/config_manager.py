from pathlib import Path
from typing import Any

from config.user.config_parser import ConfigParser
from config.user.config_writer import ConfigWriter
from config.user.config import Config, UserEljurConfig, UserDataConfig


class ConfigManager:
	"""
	Class for managing config data.

	Attributes:
		parser (ConfigParser):
			Config parser for loading data from config files.
		writer (ConfigWriter):
			Config writer for writing data to config files.
		config (Config): Configuration dataclass.
		_encoding (str): Encoding for reading and writing files.
	"""

	def __init__(
		self,
		base_dir: Path,
		paths_path: Path,
		encoding: str,
	) -> None:
		"""
		Initializes ConfigManager object.

		Loads Config during initialization.

		Args:
			base_dir (Path): Base directory of the project.
			paths_path (Path): Path to the file with technical paths.
			encoding (str): Encofing for reading and writing files.
		"""
		self._encoding = encoding
		self.parser = ConfigParser(
			encoding,
		)
		self.writer = ConfigWriter(
			encoding,
		)
		self.config = self.parser.load_config(
			base_dir=base_dir,
			paths_path=paths_path,
		)


	def get_config(
		self,
	) -> Config:
		"""
		Gets config.

		Gets config from `self.config` and returns it.
		Use only after calling `load_config` method.

		Returns:
			Config: configuration dataclass.
		"""
		return self.config


	def write_env(
		self,
	) -> None:
		"""
		Writes data to the .env config file.
		"""
		content = self._generate_env(
			self.config.user_eljur,
		)
		self.writer.write_env(
			self.config.paths.settings.env,
			content,
		)


	def write_config(
		self,
	) -> None:
		"""
		Writes data to the user config file.
		"""
		config_content = self._generate_config_content(
			self.config.user_data,
		)
		self.writer.write_config(
			self.config.paths.settings.config,
			config_content,
		)


	def _generate_config_content(
		self,
		user_data_config: UserDataConfig,
	) -> dict[str, Any]:
		"""
		Generates content for the user config file.

		Args:
			user_data_config (UserDataConfig):
				User data configuration.

		Returns:
			dict[str, Any]: Content for the user config file.
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

		Args:
			user_eljur_config (UserEljurConfig):
				User Eljur configuration.
		
		Returns:
			str: Content for the .env config file.
				Contains data for logging in Eljur.
		"""
		content = ''
		content += f'ELJUR_LOGIN={user_eljur_config.login}\n'
		content += f'ELJUR_PASSWORD={user_eljur_config.password}\n'
		content += f'ELJUR_SCHOOL_CLASS={user_eljur_config.school_class}\n'
		content += f'ELJUR_VENDOR={user_eljur_config.vendor}\n'
		content += f'ELJUR_DEVKEY={user_eljur_config.devkey}\n'
		content += f'ELJUR_AUTH_TOKEN={user_eljur_config.auth_token}\n'
		return content
