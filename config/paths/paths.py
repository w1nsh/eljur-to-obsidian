from dataclasses import dataclass
from pathlib import Path

from config.paths.settings_paths import SettingsPaths
from config.paths.responses_paths import ResponsesPaths
from config.paths.auxiliary.auxiliary_paths import AuxiliaryPaths

@dataclass
class Paths:
	"""
	Dataclass for storing paths to all technical files in the project.
	Storing only absolute paths.

	Attributes:
		auxiliary (AuxiliaryPaths): Paths to all auxiliary files.
		settings (SettingsPaths): Paths to all settings files.
		responses (ResponsesPaths): Paths to all responses files.
		base_dir (Path): Base directory of the project.
	"""
	auxiliary: AuxiliaryPaths
	settings: SettingsPaths
	responses: ResponsesPaths
	base_dir: Path
