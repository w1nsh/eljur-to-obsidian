from dataclasses import dataclass, field

from src.eljur.mark_list import MarkList
from src.eljur.homework import Homework


@dataclass
class Subject:
	name: str
	desired_mark: int | None = None
	homeworks: list[Homework] = field(default_factory=list)
	marks: MarkList = field(default_factory=lambda: MarkList([]))
