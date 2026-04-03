from dotenv import load_dotenv
from os import getenv
import json

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

	res = ep.get_periods(show_disabled=False)
	with open('responses/periods_sd.json', 'w', encoding='utf-8') as f:
		json.dump(res, f, ensure_ascii=False, indent=4)
