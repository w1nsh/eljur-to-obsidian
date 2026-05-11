from pathlib import Path
from dataclasses import dataclass


@dataclass
class MarksPaths:
	"""
	Dataclass for storing paths to auxiliary md marks files.

	Attributes:
		starts_with (Path): Path to the md marks starts with file.
		ends_with (Path): Path to the md marks ends with file.
	"""
	starts_with: Path
	ends_with: Path
