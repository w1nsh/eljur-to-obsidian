from dataclasses import dataclass, field

from src.school.homework_file import HomeworkFile


@dataclass
class Homework:
	date: str
	homework: list[str] = field(default_factory=list)
	files: list[HomeworkFile] = field(default_factory=list)


	def append_file(self, file: HomeworkFile) -> None:
		self.files.append(file)

	
	def append_homework(self, homework: str) -> None:
		self.homework.append(homework)


	@property
	def has_files(self) -> bool:
		return bool(self.files)
	