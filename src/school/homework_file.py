from dataclasses import dataclass


@dataclass
class HomeworkFile:
	filename: str | None = None
	file_link: str | None = None
	