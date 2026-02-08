import json
from dotenv import load_dotenv
import os

from src.eljur.eljur_parser import 	EljurParser
from src.eljur.json_parser import JsonParser
from src.school.subject_list import SubjectList
from src.school.subject import Subject
from src.app import App
from src.utils.date import Date


load_dotenv(dotenv_path='config/.env')

login = os.getenv('ELJUR_LOGIN') 
password = os.getenv('ELJUR_PASSWORD') 
school_class = os.getenv('ELJUR_SCHOOL_CLASS')
vendor = os.getenv('ELJUR_VENDOR')
devkey = os.getenv('ELJUR_DEVKEY')

ep = EljurParser(login, password, devkey, school_class, vendor)
jp = JsonParser()
sl = SubjectList()
app = App(jp, sl)
d = Date()

raw_from_date = '12.01.2026'
raw_to_date = '03.02.2026'

from_date = d.convert_date_to_json_format(raw_from_date)
to_date = d.convert_date_to_json_format(raw_to_date)


# date of last pars homework (for download from this date to current date)
# dates of parts of year, number current part (for отсутствия смешения marks)

ep.authenticate()

with open('responses\\marks.json', 'w', encoding='utf-8') as f:
	marks = ep.get_marks(from_date, to_date)
	json.dump(marks, f, indent=4, ensure_ascii=False)
	
with open('responses\\homework.json', 'w', encoding='utf-8') as f:
	homeworks = ep.get_homework(from_date, to_date)
	json.dump(homeworks, f, indent=4, ensure_ascii=False)
	
print('Success parsing.')

app.set_subject_list('responses/marks.json')
app.set_subjects_marks('responses/marks.json')
app.set_subjects_homeworks('responses/homework.json')

print('Success update data.')

subject_list = sl.subject_list
with open('C:\\Users\\anton\\Documents\\Main\\Школьное\\Homework.md', 'w', encoding='utf-8') as f:
	for subject in subject_list:
		f.write(f'\n\n - {subject.name}\n')
		homeworks = subject.homeworks
		f.write(f'     - Mark List: {subject.marks.marks}\n')
		f.write(f'     - Average: {subject.marks.average()}\n')
		f.write(f'     - Desired Mark: {subject.desired_mark}\n')
		f.write('     - Homeworks\n')
		for day_homework_list in homeworks:
			day_homework = day_homework_list.homework
			date = day_homework_list.date
			f.write(f'         - [ ] {date}\n')
			for homework in day_homework:
				f.write(f'             - [ ] {homework}\n')
			for file in day_homework_list.files:
				f.write(f'                 - [{file.filename}]({file.file_link})\n')
				