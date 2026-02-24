import re

from src.md.md_point_node import MdPointNode


class MdParser:
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


	def read(
		self, 
		filepath: str | None = None, 
		encoding: str | None = None
	) -> str:
		if not filepath:
			filepath = self.filepath
		if not encoding:
			encoding = self.encoding
		with open(filepath, 'r', encoding=encoding) as f:
			text = f.read()
		return text


	def split_to_lines(self, text: str) -> list[str]:
		lines = text.splitlines()
		return lines
	

	def md_to_ast(self, lines: list[str]) -> list[MdPointNode]:
		main_points = []
		parents = []
		last_point = None
		multiline_line = ''
		for line in lines:
			line_is_point = self._is_point(line)
			if not line_is_point:
				format_line = '\n'
				print(1)
				if last_point:
					for _ in range(last_point.indent):
						format_line += '\t'
						print(2)
					for _ in range(self.multiline_indent):
						format_line += ' '
						print(3)
				text = self._get_text(line, is_checkbox=False, is_multiline=True)
				format_line += text
				multiline_line += format_line
				print(4)
				if last_point:
					if multiline_line:
						last_point.append_text(multiline_line)
						multiline_line = ''
				continue
			indent = self._get_indent_level(line)
			is_checkbox = self._is_checkbox(line)
			text = self._get_text(line, is_checkbox, is_multiline=False)
			if is_checkbox:
				done = self._is_done_checkbox(line)
			else:
				done = None
			point = MdPointNode(
				text,
				indent,
				is_checkbox=is_checkbox,
				checkbox_is_done=done,
			)
			if indent == 0:
				main_points.append(point)
			if last_point:
				last_indent = last_point.indent
				if indent > last_indent:
					parents.append(last_point)
				if indent < last_indent:
					while parents and indent <= parents[-1].indent:
						parents.pop()
			if parents:
				parent_indent = parents[-1].indent
				if indent == parent_indent + 1:
					point.set_parent(parents[-1])
					parents[-1].append_child(point)
			last_point = point
		return main_points


	def _get_indent_level(self, line: str) -> int:
		pattern = r'([\t ]*) - '
		res = re.match(
			pattern,
			line,
		)
		tab_spaces_line = res.group(1)
		tabs = tab_spaces_line.count('\t')
		spaces = tab_spaces_line.count(' ')
		total_tabs = tabs + (spaces // self.tab_size)
		return total_tabs
	

	def _get_text(
			self, 
			line: str, 
			is_checkbox: bool, 
			is_multiline: bool
		) -> str:
		if is_checkbox:
			pattern = r'\s* - \[[ x]\] (.*)'
		else:
			pattern = r'\s* - (.*)'
		if is_multiline:
			pattern = r'\s*'
			for _ in range(self.multiline_indent):
				pattern += r' '
			pattern += r'(.*)'
		text_lines = re.match(
			pattern,
			line,
		)
		if is_multiline and not text_lines:
			pattern = r'(.*)'
			text_lines = re.match(
				pattern,
				line,
			)
		if text_lines and len(text_lines.groups()) == 1:
			text_line = text_lines.group(1)
			return text_line
		elif text_lines and len(text_lines.groups()) >= 2:
			raise SyntaxError(f'''
						Line "{line}" has 2 more matches with the pattern.
						Pattern "{pattern}" 
						''')
		else:
			raise SyntaxError(f'''
						Line "{line}" has 0 matches with the pattern.
						Pattern "{pattern}" 
						''')


	def _is_point(self, line: str) -> bool:
		pattern = r'\s* - '
		res = re.match(
			pattern,
			line,
		)
		if res:
			return True
		return False


	def _is_checkbox(self, line: str) -> bool:
		pattern = r'\s* - \[[ x]\] '
		res = re.match(
			pattern,
			line,
		)
		if res:
			return True
		return False


	def _is_done_checkbox(self, line: str) -> bool:
		pattern = r'\s* - \[x\]'
		res = re.match(
			pattern,
			line,
		)
		if res:
			return True
		return False
