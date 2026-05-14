from pathlib import Path
import json


class AuxiliaryWriter:
	"""
	Class for writing auxiliary data to the files.

	Attributes:
		_encoding (str): Encoding for writing files.
	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		"""
		Initialize AuxiliaryWriter object.

		Args:
			encoding (str): Encoding for writing files.
		"""
		self._encoding = encoding


	def write_md(
		self,
		md: str,
		md_file: Path,
	) -> None:
		"""
		Writes any md files.

		Uses for writing hw/m s/e with data.

		Args:
			md (str): Data to writing to the file.
			md_file (Path): Path to the file.
		"""
		md_file.write_text(md)


	def write_desireds(
		self,
		desired_marks: Path,
		desireds: list[dict[str, str | int]],
	) -> None:
		"""
		Writes desired marks to the json file.

		Args:
			desired_marks (Path): Path to the json file.
			desireds (list[dict[str, str | int]]):
				List of the subject and him desired mark pairs.	
		"""
		desireds_json = json.dumps(
			desireds,
			ensure_ascii=False,
			indent=4,
		)
		desired_marks.write_text(
			desireds_json,
			self._encoding,
		)
		