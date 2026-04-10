from dataclasses import dataclass

from pathlib import Path


@dataclass
class SettingsPaths:
	env: Path
	config: Path
	eljur_cache: Path
	user_hash: Path
