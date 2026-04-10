from dataclasses import dataclass
from pathlib import Path

from config.user.settings_paths import SettingsPaths
from config.paths.responses_paths import ResponsesPaths


@dataclass
class Paths:
	settings_paths: SettingsPaths
	responses_paths: ResponsesPaths
	base_dir: Path
