from dataclasses import dataclass
from pathlib import Path

from config.paths.settings_paths import SettingsPaths
from config.paths.responses_paths import ResponsesPaths


@dataclass
class Paths:
	"""
	Dataclass for storing paths to all technical files in the project.
	Storing only absolute paths.

	Attributes:
		settings (SettingsPaths): Paths to all settings files.
		responses (ResponsesPaths): Paths to all responses files.
		base_dir (Path): Base directory of the project.
	"""
	settings: SettingsPaths
	responses: ResponsesPaths
	base_dir: Path
