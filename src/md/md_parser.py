import re


class MdParser:
	def __init__(self, filepath: str, encoding: str) -> None:
		self.filepath = filepath
		self.encoding = encoding


	def read(self, filepath: str | None = None, encoding: str | None = None) -> str:
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
	

	def set_nesting_lvl(self, lines) -> None:
		pass
