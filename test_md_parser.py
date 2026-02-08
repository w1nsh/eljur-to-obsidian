from src.md.md_parser import MdParser


mdp = MdParser("C:\\Users\\anton\\Documents\\Main\\Школьное\\Homework.md", 'utf-8')

file = mdp.read()
lines = mdp.split_to_lines(file)
print(lines)
