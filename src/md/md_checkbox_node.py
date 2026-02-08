from dataclasses import dataclass, field


@dataclass
class MdCheckboxNode:
	text: str
	done: bool 
	parent: str | None
	children: list[str] = field(default_factory=list)
