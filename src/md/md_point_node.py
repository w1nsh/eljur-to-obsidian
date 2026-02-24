from dataclasses import dataclass, field
from typing import Optional

@dataclass
class MdPointNode:
	text: str
	indent: int
	parent: Optional['MdPointNode'] = None
	children: list['MdPointNode'] = field(default_factory=list)
	is_checkbox: bool = False
	checkbox_is_done: bool | None = None 


	def set_parent(self, parent: 'MdPointNode') -> None:
		self.parent = parent


	def append_child(self, child: 'MdPointNode') -> None:
		self.children.append(child)


	def append_text(self, new_text: str) -> None:
		self.text += new_text
