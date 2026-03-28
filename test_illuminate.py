from src.md.md_point_node import MdPointNode


chb1 = MdPointNode(
	'checkbox',
	indent=0,
	is_checkbox=True,
	checkbox_is_done=False,
)

chb2 = MdPointNode(
	'checkbox',
	indent=0,
	is_checkbox=True,
	checkbox_is_done=False,
)


print(chb1 == chb2, chb1 is chb2)
