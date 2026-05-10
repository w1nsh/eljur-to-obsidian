from dataclasses import dataclass
from pathlib import Path


@dataclass
class HomeworksConfig:
	"""
	Dataclass for storing parameters about homework.

	Attributes:
		need (bool): The need to display information about homeworks to the user.
		path (Path): Path to the file for storing information about the user's homeworks.
		from_date (str): Start date in 'dd.mm.yyyy' format for a parsing homeworks in the given date range.
		to_date (str): End date in 'dd.mm.yyyy' format for a parsing homeworks in the given date range.
	"""
	need: bool
	path: Path
	from_date: str
	to_date: str


	def set_need(
		self,
		need: bool,
	) -> None:
		"""
		Sets new value of the class attribute need.

		Args:
			need (bool): New value of the class attribute.
		"""
		self.need = need


	def set_path(
		self,
		path:  Path,
	) -> None:
		"""
		Sets new path to the file for storing information about user's homeworks.

		Args:
			path (Path): New path to file.
		"""
		self.path = path


	def set_from_date(
		self,
		from_date: str,
	) -> None:
		"""
		Sets new date start of the range.

		Args:
			from_date (str): New date start of the range.
		"""
		self.from_date = from_date


	def set_to_date(
		self,
		to_date: str,
	) -> None:
		"""
		Sets new date end of the range.

		Args:
			to_date (str): New date end of the range.
		"""
		self.to_date = to_date
