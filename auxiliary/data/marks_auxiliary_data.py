from dataclasses import dataclass


@dataclass
class MarksAuxiliaryData:
	"""
	Dataclass for storing auxiliary md marks data.

	Attributes:
		starts_with (str): Md marks starts with data.
		ends_with (str): Md marks ends with data.
	"""
	starts_with: str
	ends_with: str
