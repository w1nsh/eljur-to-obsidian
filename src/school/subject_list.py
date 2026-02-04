from dataclasses import dataclass, field

from src.school.subject import Subject


@dataclass
class SubjectList:
	subject_list: list[Subject] = field(default_factory=list)


	def append_subject(self, subject: Subject) -> None:
		self.subject_list.append(subject)
