from dataclasses import dataclass
from pathlib import Path

from config.user.desired_mark import DesiredMark


@dataclass
class MarksConfig:
	"""
	Dataclass for storing parameters about marks.

	Attributes:
		need (bool): The need to display information about marks to the user.
		path (Path): Path to the file for storing information about the user's marks.
		from_date (str): Start date in 'dd.mm.yyyy' format for a parsing marks in the given date range.
		to_date (str): End date in 'dd.mm.yyyy' format for a parsing marks in the given date range.
		subjects (list[DesiredMark]): List of the sets of pairs with subject and desired mark of him.
	"""
	need: bool
	path: Path
	from_date: str
	to_date: str
	subjects: list[DesiredMark]

	
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
		path: Path,
	) -> None:
		"""
		Sets new path to the file for storing information about user's marks.

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
			from_date (str): New date end of the range.
		"""
		self.to_date = to_date


	def set_desired_mark(
		self,
		subject_name: str,
		desired_mark: int,
	) -> None:
		"""
		Sets desired mark for a selected subject by subject name.

		Args:
			subject_name (str): Subject name for a search subject.
			desired_mark (int): New desired mark of the subject.
		"""
		for subject in self.subjects:
			if subject.subject_name == subject_name:
				subject.set_desired_mark(desired_mark)
				break
