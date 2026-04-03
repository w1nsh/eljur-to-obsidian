import json
from dotenv import load_dotenv
import os

from src.eljur.eljur_parser import 	EljurParser
from src.eljur.json_parser import JsonParser
from src.school.subject_list import SubjectList
from src.school.subject import Subject
from src.app import App
from src.utils.date import Date
from src.md.md_writer import MdWriter
from src.md.md_parser import MdParser


load_dotenv(dotenv_path='config/.env')

login = os.getenv('ELJUR_LOGIN') 
password = os.getenv('ELJUR_PASSWORD') 
school_class = os.getenv('ELJUR_SCHOOL_CLASS')
vendor = os.getenv('ELJUR_VENDOR')
devkey = os.getenv('ELJUR_DEVKEY')

ep = EljurParser(login, password, devkey, school_class, vendor)
jp = JsonParser()
sl = SubjectList()
app = App(sl)
mdw = MdWriter('C:\\Users\\anton\\Documents\\Main\\Школьное\\mdw_test.md', 'utf-8', 4, 2)
mdp = MdParser(
	"C:\\Users\\anton\\Documents\\Main\\Школьное\\mdw_test.md", 
	'utf-8',
	4,
	2,
)

raw_mark_from_date = '12.01.2026'
raw_mark_to_date = '08.03.2026'

raw_homework_from_date = '02.03.2026'
raw_homework_to_date = '03.03.2026'

mark_from_date = Date.to_eljur(raw_mark_from_date)
mark_to_date = Date.to_eljur(raw_mark_to_date)

homework_from_date = Date.to_eljur(raw_homework_from_date)
homework_to_date = Date.to_eljur(raw_homework_to_date)


# date of last pars homework (for download from this date to current date)
# dates of parts of year, number current part (for отсутствия смешения marks)

ep.authenticate()

with open('responses\\marks.json', 'w', encoding='utf-8') as f:
	marks = ep.get_marks(mark_from_date, mark_to_date)
	json.dump(marks, f, indent=4, ensure_ascii=False)
	
with open('responses\\homework.json', 'w', encoding='utf-8') as f:
	homeworks = ep.get_homework(homework_from_date, homework_to_date)
	json.dump(homeworks, f, indent=4, ensure_ascii=False)
	
print('Success parsing.')

app.set_subject_list('responses/marks.json')
app.set_subjects_marks('responses/marks.json')
app.set_subjects_homeworks('responses/homework.json')

print('Success update data.')

subject_list = sl.subject_list

text = mdp.read()
lines = mdp.split_to_lines(text)
mdp_ast = mdp.md_to_ast(lines)


with open('C:\\Users\\anton\\Documents\\Main\\Школьное\\mdw_test.md', 'w', encoding='utf-8') as f:
	sl_ast = mdw.generate_subject_ast(sl)
	merge_ast = mdw.merge_changes(mdp_ast, sl_ast, mdp_ast)
	merge_ast = mdw._clean_done(merge_ast)
	if merge_ast:
		md = mdw.ast_to_md(merge_ast)
		f.write(md)
	else:
		print('Empty md')

# text = mdp.read()
# lines = mdp.split_to_lines(text)
# mp = mdp.md_to_ast(lines)

# with open('C:\\Users\\anton\\Documents\\Main\\Школьное\\mdw_test.md', 'w', encoding='utf-8') as f:
# 	md = mdw.ast_to_md(mp)
# 	f.write(md)
