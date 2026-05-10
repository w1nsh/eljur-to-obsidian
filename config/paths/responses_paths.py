from dataclasses import dataclass

from pathlib import Path


@dataclass
class ResponsesPaths:
	"""
	Dataclass for storing paths to the responses files.
	Storing only absolute paths.

	Attributes:
		assessments (Path): Path to the assessments file.
		diary (Path): Path to the diary file.
		homework (Path): Path to the homeworks file.
		marks (Path): Path to the marks file.
		periods (Path): Path to the periods file.
		rules (Path): Path to the rules file.
		schedule (Path): Path to the schedule file.
	"""
	assessments: Path
	diary: Path
	homework: Path
	marks: Path
	periods: Path
	rules: Path
	schedule: Path
