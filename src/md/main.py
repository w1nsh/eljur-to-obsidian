from pathlib import Path

from src.eljur.subject import Subject


class Md:
	"""
	Draft md working class.
	"""

	def __init__(
		self,
	) -> None:
		pass


	def marks(
		self,
		marks: Path,
		subject_list: list[Subject],
		starts_with: str,
		ends_with: str,
	) -> None:
		md = starts_with + '\n'
		for subject in subject_list:
			md += f'- {subject.name}\n'
			md += f'	- Average: {subject.marks.average()}\n'
			md += f'	- Desired: {subject.desired_mark}\n'
			md += f'		- For Desired:\n'
			md += f'			- 5: {subject.marks.count_marks_for_desired(5, subject.desired_mark)}\n'
			md += f'			- 4: {subject.marks.count_marks_for_desired(4, subject.desired_mark)}\n'
			md += f'			- 3: {subject.marks.count_marks_for_desired(3, subject.desired_mark)}\n'
			md += f'		- For Current:\n'
			md += f'			- 5: {subject.marks.count_neutral_for_current(5)}\n'
			md += f'			- 4: {subject.marks.count_neutral_for_current(4)}\n'
			md += f'			- 3: {subject.marks.count_neutral_for_current(3)}\n'
			md += f'			- 2: {subject.marks.count_neutral_for_current(2)}\n'
			if subject.name == 'Химия':
				print(subject.marks.marks)
		md += ends_with + '\n'
		marks.write_text(md, encoding='utf-8')
