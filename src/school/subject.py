from dataclasses import dataclass, field

from src.school.mark_list import MarkList
from src.school.homework import Homework


@dataclass
class Subject:
	name: str
	desired_mark: int
	homeworks: list[Homework] = field(default_factory=list)
	marks: MarkList = field(default_factory=lambda: MarkList([]))


	def set_marks(
		self,
		marks: MarkList,
	) -> None:
		self.marks = marks


	def set_homeworks(
		self,
		homeworks: list[Homework],
	) -> None:
		self.homeworks = homeworks


	def set_desired_mark(
		self,
		desired_mark: int,
	) -> None:
		self.desired_mark = desired_mark


	def append_homework(
		self,
		homework: Homework,
	) -> None:
		self.homeworks.append(homework)
