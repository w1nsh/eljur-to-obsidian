from dataclasses import dataclass


@dataclass
class HomeworksAuxiliaryData:
	"""
	Dataclass for storing auxiliary md homeworks data.

	Attributes:
		starts_with (str): Md homeworks starts with data.
		ends_with (str): Md homeworks ends with data.
	"""
	starts_with: str
	ends_with: str
