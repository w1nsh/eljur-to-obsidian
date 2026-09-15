from dataclasses import dataclass, field

from src.eljur.homework_file import HomeworkFile


@dataclass
class Homework:
	date: str
	value: str
	files: list[HomeworkFile]
