from pathlib import Path
from typing import Any
import json


class ConfigWriter:
	"""
	Class for writing data to config files.

	Attributes:
		_encoding (str): Encoding for writing files.
	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		"""
		Initializes ConfigWriter object.

		Args:
			encoding (str): Encofing for writing files.
		"""
		self._encoding = encoding


	def write_env(
		self,
		env: Path,
		content: str,
	) -> None:
		"""
		Writes data to the .env config file.

		Args:
			env (Path): Path to the .env config file.
			content (str): Content to write to the .env config file.
		"""
		env.write_text(
			content,
			encoding=self._encoding,
		)


	def write_config(
		self,
		config: Path,
		content: dict[str, Any],
	) -> None:
		"""
		Writes data to the config file.

		Args:
			config (Path): Absolute path to the config file.
			content (dict[str, Any]): Content to write to the config file.
		"""
		json_string = json.dumps(
			content,
			indent=4,
			ensure_ascii=False
		)
		config.write_text(json_string, encoding=self._encoding)
