from src.md.md_point_node import MdPointNode
from src.school.subject_list import SubjectList


class MdWriter:
	def __init__(
		self, 
		filepath: str,
		encoding: str,
		tab_size: int,
		multiline_indent: int,
	) -> None:
		self.filepath = filepath
		self.encoding = encoding
		self.tab_size = tab_size
		self.multiline_indent = multiline_indent


	def generate_subject_ast(
		self,
		subject_list: SubjectList
	) -> list[MdPointNode]:
		main_points = []
		for subject in subject_list.subject_list:
			subject_text = subject.name
			subject_indent = 0
			subject_point = MdPointNode(
				subject_text,
				subject_indent
			)
			main_points.append(subject_point)
			for homework in subject.homeworks:
				date_text = homework.date
				date_indent = 1
				date_point = MdPointNode(
					date_text,
					date_indent,
					is_checkbox=True,
					checkbox_is_done=False,
				)
				subject_point.append_child(date_point)
				date_point.set_parent(subject_point)
				for daily_homework in homework.homework:
					homework_text = daily_homework
					homework_indent = 2
					homework_point = MdPointNode(
						homework_text,
						homework_indent,
						is_checkbox=True,
						checkbox_is_done=False,
					)
					date_point.append_child(homework_point)
					homework_point.set_parent(date_point)
					for file in homework.files:
						file_text = f'[{file.filename}]({file.file_link})'
						file_indent = 3
						file_point = MdPointNode(
							file_text,
							file_indent
						)
						homework_point.append_child(file_point)
						file_point.set_parent(homework_point)
		return main_points
	

	def ast_to_md(self, points: list[MdPointNode]) -> str:
		res = ''
		for point in points:
			text = self._generate_point_text(point)
			res += text
			if point.children:
				res += self.ast_to_md(point.children)
			else:
				''
		return res
	

	def _generate_point_text(self, point: MdPointNode) -> str:
		text = ''
		indent = self._generate_indent(point.indent)
		text += indent
		text += ' - '
		if point.is_checkbox:
			if point.checkbox_is_done:
				text += '[x] '
			else:
				text += '[ ] '
		text += self._del_new_str(point.text)
		text += '\n'
		return text


	def _generate_indent(self, indent: int) -> str:
		indent_str = ''
		for _ in range(indent):
			indent_str += '\t'
		return indent_str


	def _del_new_str(self, text: str) -> str:
		return text.replace('\n', '')
