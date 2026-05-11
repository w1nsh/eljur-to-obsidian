from dataclasses import dataclass

from config.paths.auxiliary.homeworks_paths import HomeworksPaths
from config.paths.auxiliary.marks_paths import MarksPaths


@dataclass
class MdAuxiliaryPaths:
	"""
	Dataclass for storing paths to auxiliary files related to MD files.

	Attributes:
		homeworks (HomeworksPaths): Paths to auxiliary md homeworks files.
		marks (MarksPaths): Paths to auxiliary md marks files.
	"""
	homeworks: HomeworksPaths
	marks: MarksPaths
