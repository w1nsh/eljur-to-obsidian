from pathlib import Path
from dataclasses import dataclass

from config.paths.auxiliary.md_auxiliary_paths import MdAuxiliaryPaths


@dataclass
class AuxiliaryPaths:
	"""
	Dataclass for storing paths to auxiliary files.

	Attributes:
		desired_marks (Path): Path to the desired marks file.
		md (MdAuxiliaryPaths): Md auxiliary paths.
	"""
	desired_marks: Path
	md: MdAuxiliaryPaths
