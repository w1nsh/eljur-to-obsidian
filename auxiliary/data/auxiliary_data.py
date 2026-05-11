from dataclasses import dataclass

from auxiliary.data.desired_mark import DesiredMark
from auxiliary.data.md_auxiliary_data import MdAuxiliaryData


@dataclass
class AuxiliaryData:
	"""
	Dataclass for storing auxiliary data.

	Attributes:
		desired_marks (list[DesiredMark]):
			List of the pairs of subject and him desired mark.
		md (MdAuxiliaryData): Markdown auxiliary data.
	"""
	desired_marks: list[DesiredMark]
	md: MdAuxiliaryData
