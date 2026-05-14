from pathlib import Path
import json

from auxiliary.data.marks_auxiliary_data import MarksAuxiliaryData
from auxiliary.data.homeworks_auxiliary_data import HomeworksAuxiliaryData
from auxiliary.data.md_auxiliary_data import MdAuxiliaryData
from auxiliary.data.desired_mark import DesiredMark
from auxiliary.data.auxiliary_data import AuxiliaryData


class AuxiliaryParser:
	"""
	Class for parsing auxiliary data from files.

	Attributes:
		_encoding (str): Encoding for reading files.	
	"""

	def __init__(
		self,
		encoding: str
	) -> None:
		"""
		Initialize AuxiliaryParser object.

		Args:
			encoding (str): Encoding for reading files.
		"""
		self._encoding = encoding


	def load_auxiliary_data(
		self,
		desired_marks: Path,
		homeworks_starts_with: Path,
		homeworks_ends_with: Path,
		marks_starts_with: Path,
		marks_ends_with: Path,
	) -> AuxiliaryData:
		"""
		Loads auxiliary data.

		Args:
			desired_marks (Path): Path to the desired marks file.
			homeworks_starts_with (Path): Path to the homeworks starts with file.
			homeworks_ends_with (Path): Path to the homeworks ends with file.
			marks_starts_with (Path): Path to the marks starts with file.
			marks_ends_with (Path): Path to the marks ends with file.
			
		Returns:
			AuxiliaryData: Auxiliary data.
		"""
		return AuxiliaryData(
			desired_marks=self.load_desired_marks(
				desired_marks=desired_marks,
			),
			md=self.load_md_data(
				homeworks_starts_with=homeworks_starts_with,
				homeworks_ends_with=homeworks_ends_with,
				marks_starts_with=marks_starts_with,
				marks_ends_with=marks_ends_with,
			)
		)


	def load_md_data(
		self,
		homeworks_starts_with: Path,
		homeworks_ends_with: Path,
		marks_starts_with: Path,
		marks_ends_with: Path,
	) -> MdAuxiliaryData:
		"""
		Loads md auxiliary data.

		Args:
			homeworks_starts_with (Path): Path to the homeworks starts with file.
			homeworks_ends_with (Path): Path to the homeworks ends with file.
			marks_starts_with (Path): Path to the marks starts with file.
			marks_ends_with (Path): Path to the marks ends with file.
			
		Returns:
			MdAuxiliaryData: Auxiliary md data.
		"""
		return MdAuxiliaryData(
			homeworks=self.load_homeworks_data(
				starts_with=homeworks_starts_with,
				ends_with=homeworks_ends_with,
			),
			marks=self.load_marks_data(
				starts_with=marks_starts_with,
				ends_with=marks_ends_with,
			)
		)


	def load_marks_data(
		self,
		starts_with: Path,
		ends_with: Path,
	) -> MarksAuxiliaryData:
		"""
		Loads marks auxiliary data.

		Args:
			starts_with (Path): Path to the starts with file.
			ends_with (Path): Path to the ends with file.
			
		Returns:
			MarksAuxiliaryData: Auxiliary md marks data.
		"""
		return MarksAuxiliaryData(
			starts_with=self.load_marks_starts_with(
				starts_with,
			),
			ends_with=self.load_marks_ends_with(
				ends_with,
			)
		)


	def load_homeworks_data(
		self,
		starts_with: Path,
		ends_with: Path,
	) -> HomeworksAuxiliaryData:
		"""
		Loads homeworks auxiliary data.

		Args:
			starts_with (Path): Path to the starts with file.
			ends_with (Path): Path to the ends with file.

		Returns:
			HomeworksAuxiliaryData: Auxiliary md homeworks data.
		"""
		return HomeworksAuxiliaryData(
			starts_with=self.load_homeworks_starts_with(
				starts_with,
			),
			ends_with=self.load_homeworks_ends_with(
				ends_with,
			)
		)


	def load_desired_marks(
		self,
		desired_marks: Path,
	) -> list[DesiredMark]:
		"""
		Loads desired marks of subjects, and return it.

		Attributes:
			desired_marks_path (Path): Path to the desired marks file.

		Returns:
			list[DesiredMark]: List of the pairs of subject and him desired mark.
		"""
		desired_marks_string = desired_marks.read_text(self._encoding)
		desired_marks_pairs = json.loads(desired_marks_string)
		desired_marks_list = []
		for pair in desired_marks_pairs:
			desired_mark = DesiredMark(
				subject_name=pair['subject'],
				desired_mark=pair['desired']
			)
			desired_marks_list.append(desired_mark)
		return desired_marks_list
	

	def load_homeworks_starts_with(
		self,
		homeworks_starts_with_path: Path,
	) -> str:
		"""
		Loads homeworks starts with file and return it.

		Attributes:
			homeworks_starts_with_path (Path): Path to the file.
		
		Returns:
			str: Text of the file.
		"""
		return homeworks_starts_with_path.read_text(self._encoding)
		

	def load_homeworks_ends_with(
		self,
		homeworks_ends_with_path: Path,
	) -> str:
		"""
		Loads homeworks ends with file and return it.

		Attributes:
			homeworks_ends_with_path (Path): Path to the file.
		
		Returns:
			str: Text of the file.
		"""
		return homeworks_ends_with_path.read_text(self._encoding)
	

	def load_marks_starts_with(
		self,
		marks_starts_with_path: Path,
	) -> str:
		"""
		Loads marks starts with file and return it.

		Attributes:
			marks_starts_with_path (Path): Path to the file.
		
		Returns:
			str: Text of the file.
		"""
		return marks_starts_with_path.read_text(self._encoding)
	

	def load_marks_ends_with(
		self,
		marks_ends_with_path: Path,
	) -> str:
		"""
		Loads marks ends with file and return it.

		Attributes:
			marks_ends_with_path (Path): Path to the file.
		
		Returns:
			str: Text of the file.
		"""
		return marks_ends_with_path.read_text(self._encoding)
	