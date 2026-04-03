from dotenv import load_dotenv
from os import getenv

from src.eljur.eljur_parser import EljurParser


load_dotenv(dotenv_path='config/.env')

login = getenv('ELJUR_LOGIN')
password = getenv('ELJUR_PASSWORD')
school_class = getenv('ELJUR_SCHOOL_CLASS')
vendor = getenv('ELJUR_VENDOR')
devkey = getenv('ELJUR_DEVKEY')

if login and password and school_class and vendor and devkey:
	ep = query = EljurParser(
		login=login,
		password=password,
		school_class=school_class,
		vendor=vendor,
		devkey=devkey
	)

	ep.authenticate()

	date_from = '20260327'
	date_to = '20260327'
	res = ep.get_schedule_get(
		from_date=date_from,
		to_date=date_to,
		school_class=True,
		rings=True,
	)
	print(res)
