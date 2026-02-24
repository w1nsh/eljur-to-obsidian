from src.md.md_parser import MdParser


mdp = MdParser(
	"C:\\Users\\anton\\Documents\\Main\\Школьное\\TEST_DATA.md", 
	'utf-8',
	4,
	2,
)

text = mdp.read()
lines = mdp.split_to_lines(text)
ress = mdp.md_to_ast(lines)
with open('C:\\Users\\anton\\Documents\\Main\\Школьное\\RES_TEST.md', 'w', encoding='utf-8') as f:
	for point in ress:
		# print(f'Text: {point.text}\n')
		f.write(f'Text: {point.text}\n')
		# print(f'Indent: {point.indent}\n')
		f.write(f'Indent: {point.indent}\n')
		# print(f'Parent: {point.parent}\n')
		f.write(f'Parent: {point.parent}\n')
		# print(f'Is Checkvbox: {point.is_checkbox}\n')
		f.write(f'Is Checkvbox: {point.is_checkbox}\n')
		# print(f'Checkbox Is Done: {point.checkbox_is_done}\n\n')
		f.write(f'Checkbox Is Done: {point.checkbox_is_done}\n\n')
		if point.children:
			for child in point.children:
					f.write(f'Text: {child.text}\n')
					f.write(f'Indent: {child.indent}\n')
					f.write(f'Parent: {child.parent}\n')
					f.write(f'Children: {child.children}\n')
					f.write(f'Is Checkvbox: {child.is_checkbox}\n')
					f.write(f'Checkbox Is Done: {child.checkbox_is_done}\n\n')
