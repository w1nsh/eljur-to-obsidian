from copy import deepcopy

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
			else: # ??? del this string
				'' # ??? del this string
		return res
	

	def _generate_point_text(self, point: MdPointNode) -> str:
		text = ''
		indent = self._generate_indent(point.indent)
		text += indent
		text += ' - '
		if point.is_checkbox:
			if not point.checkbox_is_done:
				text += '[ ] '
			else:
				text += '[x] '
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
	

	def merge_changes_obs(self, old_md: list[MdPointNode], new_md: list[MdPointNode], full_old_md: list[MdPointNode]) -> list[MdPointNode]:
		if old_md and new_md:
			for new_point in new_md:
				for old_point in old_md:
					if self._points_is_clones(old_point, new_point):
						children = self.merge_changes_obs(old_point.children, new_point.children, full_old_md)
						old_point.children = children
						break
				else:
					new_parent = new_point.parent
					if new_parent:
						match = self._search_point(full_old_md, new_parent)
						if match:
							print('add', new_point.text)
							match.append_child(new_point)
							new_point.set_parent(match)
					else:
						old_md.append(new_point)
			return old_md
		elif old_md and not new_md:
			return old_md
		elif not old_md and new_md:
			for new_point in new_md:
				new_parent = new_point.parent
				if new_parent:
					match = self._search_point(full_old_md, new_parent)
					if match:
						match.append_child(new_point)
						new_point.set_parent(match)
				else:
					old_md.append(new_point)
			return old_md
		else:
			return []


	def _search_point(self, points: list[MdPointNode], sought_point: MdPointNode) -> MdPointNode | None:
		"""
		Return match (search_el with some element on points)
		"""
		for point in points:
			if self._points_is_clones(point, sought_point):
				return point
			if point.children:
				res = self._search_point(point.children, sought_point)
				if res:
					return res
		return None


	def _clean_done(
		self,
		points: list[MdPointNode],
	) -> list[MdPointNode]:
		for i, point in enumerate(points):
			if point.children:
				children = self._clean_done(point.children)
				point.children = children
			if point.is_checkbox:
				if point.checkbox_is_done:
					points.pop(i)
		return points


	def _points_is_clones(self, point1: MdPointNode, point2: MdPointNode) -> bool:
		parent1 = point1.parent.text if point1.parent else None
		parent2 = point2.parent.text if point2.parent else None
		return (
			(point1.text == point2.text) and 
			(parent1 == parent2) and
			(point1.indent == point2.indent) and
			(point1.is_checkbox == point2.is_checkbox)
			)