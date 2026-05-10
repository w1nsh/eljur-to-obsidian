from pathlib import Path
from typing import Any
import json

from config.user.user_eljur_config import UserEljurConfig


class ConfigWriter:
	"""
	Class for writing data to config files.

	Attributes:
		_encoding (str): encoding for writing files.
	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		self._encoding = encoding


	def write_env(
		self,
		env_path: Path,
		env_content: str,
	) -> None:
		"""
		Writes data to the .env config file.

		Args:
			env_path (Path): path to the .env config file.
			env_content (str): content to write to the .env config file.
		"""
		env_path.write_text(env_content, encoding=self._encoding)


	def write_config(
		self,
		config_path: Path,
		config_content: dict[str, Any],
	) -> None:
		"""
		Writes data to the config file.

		Args:
			config_path (Path): absolute path to the config file.
			config_content (dict[str, Any]): content to write to the config file.
		"""
		json_string = json.dumps(
			config_content,
			indent=4,
			ensure_ascii=False
		)
		config_path.write_text(json_string, encoding=self._encoding)
