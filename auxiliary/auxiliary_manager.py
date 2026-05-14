from pathlib import Path

from auxiliary.data.auxiliary_data import AuxiliaryData
from auxiliary.auxiliary_parser import AuxiliaryParser
from auxiliary.auxiliary_writer import AuxiliaryWriter
from src.school.subject import Subject
from config.paths.auxiliary.auxiliary_paths import AuxiliaryPaths


class AuxiliaryManager:
	"""
	Class for managing and work with auxiliary data.

	Attributes:
		parser (AuxiliaryParser): 
			Auxiliary parser for loading data from files.
		writer (AuxiliaryWriter):
			Auxiliary writer for writing data to files.
		auxiliary_data (AuxiliaryData): Auxiliary data.
		_encofing (str): Encofing for reading and writing files.
	"""

	def __init__(
		self,
		encoding: str,
		auxiliary_paths: AuxiliaryPaths
	) -> None:
		"""
		Initializes an Auxiliary Manager class object.

		Loads AuxiliaryData during initialization.

		Args:
			encoding (str): Encofing for reading and writing files.
			auxiliary_paths (AuxiliaryPaths):
				All paths to auxiliary files.
		"""
		self._encoding = encoding
		self.parser = AuxiliaryParser(encoding)
		self.writer = AuxiliaryWriter(encoding)
		self.load_auxiliary_data(auxiliary_paths)


	def write_homeworks_starts(
		self,
		homeworks_starts: Path,
	) -> None:
		"""
		Writes homeworks starts with data.

		Args:
			homeworks_starts (Path):
				Path to the homeworks starts with file.
		"""
		md = self.auxiliary_data.md.homeworks.starts_with
		self.writer.write_md(
			md,
			homeworks_starts,
		)


	def write_homeworks_ends(
		self,
		homeworks_ends: Path,
	) -> None:
		"""
		Writes homeworks ends with data.

		Args:
			homeworks_ends (Path):
				Path to the homeworks ends with file.
		"""
		md = self.auxiliary_data.md.homeworks.ends_with
		self.writer.write_md(
			md,
			homeworks_ends,
		)


	def write_marks_starts(
		self,
		marks_starts: Path,
	) -> None:
		"""
		Writes marks starts with data.

		Args:
			marks_starts (Path):
				Path to the marks starts with file.
		"""
		md = self.auxiliary_data.md.marks.starts_with
		self.writer.write_md(
			md,
			marks_starts,
		)


	def write_marks_ends(
		self,
		marks_ends: Path,
	) -> None:
		"""
		Writes marks ends with data.

		Args:
			marks_ends (Path):
				Path to the marks ends with file.
		"""
		md = self.auxiliary_data.md.marks.ends_with
		self.writer.write_md(
			md,
			marks_ends,
		)


	def load_auxiliary_data(
		self,
		auxiliary_paths: AuxiliaryPaths,
	) -> None:
		"""
		Loads auxiliary dataclass.

		Use only after ConfigManager.load_config() (because paths).

		Args:
			auxiliary_paths (AuxiliaryPaths):
				All paths to auxiliary files.
		"""
		self.auxiliary_data = self.parser.load_auxiliary_data(
			desired_marks=auxiliary_paths.desired_marks,
			homeworks_starts_with=auxiliary_paths.md.homeworks.starts_with,
			homeworks_ends_with=auxiliary_paths.md.homeworks.ends_with,
			marks_starts_with=auxiliary_paths.md.marks.starts_with,
			marks_ends_with=auxiliary_paths.md.marks.ends_with,
		)


	def write_desireds(
		self,
		desired_marks: Path,
		subject_list: list[Subject],
	) -> None:
		"""
		Writes desired marks.

		Writes desired marks by list of Subject's.
		Subject's - object of truth, not DesiredMark's.

		Args:
			desired_marks (Path): Path to the desired marks file.
			subject_list (list[Subject]):
				List of the Subject's for obtaining data.
		"""
		desireds = self._generate_desireds(
			subject_list,
		)
		self.writer.write_desireds(
			desired_marks,
			desireds,
		)


	def _generate_desireds(
		self,
		subject_list: list[Subject],
	) -> list[dict[str, str | int]]:
		"""
		Generates list of the subject and him desired mark pairs.

		Args:
			subject_list (list[Subject]): Subject list.
		
		Returns:
			list[dict[str, str | int]]: List of the pairs.
		"""
		desireds = []
		for subject in subject_list:
			desireds.append(
				{
					"subject": subject.name,
					"desired": subject.desired_mark,
				}
			)
		return desireds
