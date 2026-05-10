from dataclasses import dataclass

from pathlib import Path


@dataclass
class SettingsPaths:
	"""
	Dataclass for storing paths to the settings files.
	Storing only absolute paths.

	Attributes:
		env (Path): Path to the .env file.
		config (Path): Path to the config.json file.
	"""
	env: Path
	config: Path
