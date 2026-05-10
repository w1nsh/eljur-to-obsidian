from pathlib import Path

from config.user.config_parser import ConfigParser
from config.user.config_writer import ConfigWriter
from config.user.config import Config


class ConfigManager:
	def __init__(
		self,
		base_dir: Path,
		paths_file: Path,
		encoding: str,
	) -> None:
		self._base_dir = base_dir
		self._paths_file = paths_file
		self._encoding = encoding
		self.config_parser = ConfigParser(
			base_dir,
			paths_file,
			encoding,
		)
		self.config_writer = ConfigWriter(
			encoding,
			)


	def load_config(
		self,
	) -> Config:
		"""
		Load config.

		Load config, store it in `self._config`, and return it.

		Returns:
			Config: configuration dataclass.
		"""
		paths = self.config_parser.load_paths()
		user_config = self.config_parser.load_user_config() # add validate to all parameters
		user_eljur_config = self.config_parser.load_user_eljur_config() # add validate to exists
		config = Config(
			paths,
			user_config,
			user_eljur_config,
		)
		return config
