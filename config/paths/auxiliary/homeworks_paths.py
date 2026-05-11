from pathlib import Path
from dataclasses import dataclass


@dataclass
class HomeworksPaths:
	"""
	Dataclass for storing paths to auxiliary md homeworks files.

	Attributes:
		starts_with (Path): Path to the md homeworks starts with file.
		ends_with (Path): Path to the md homeworks ends with file.
	"""
	starts_with: Path
	ends_with: Path
