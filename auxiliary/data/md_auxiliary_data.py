from dataclasses import dataclass

from auxiliary.data.homeworks_auxiliary_data import HomeworksAuxiliaryData
from auxiliary.data.marks_auxiliary_data import MarksAuxiliaryData


@dataclass
class MdAuxiliaryData:
	"""
	Dataclass for storing auxiliary md data.

	Attributes:
		homeworks (HomeworksAuxiliaryData): Auxiliary md homeworks data.
		marks (MarksAuxiliaryData): Auxiliary md marks data
	"""
	homeworks: HomeworksAuxiliaryData
	marks: MarksAuxiliaryData
