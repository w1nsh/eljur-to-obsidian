from pathlib import Path

from src.eljur.parser import EljurParser
from src.eljur.response_parser import ResponseParser

from src.config.parser import ConfigParser

from src.utils.date import Date

from src.md.main import Md


# Constants
ETO = Path(__file__).parent
CONFIG = ETO / 'config' / 'config.json'
ENCODING = 'utf-8'


# Config Parser init
cp = ConfigParser(
	encoding=ENCODING,
	eto=ETO,
)


# Config loading
config = cp.load_config(
	config=CONFIG,
)


# Eljur systems init
ep = EljurParser(
	encoding=ENCODING,
	devkey=config.secrets.devkey,
	vendor=config.secrets.vendor,
	school_class=config.secrets.school_class,
	login=config.secrets.login,
	password=config.secrets.password,
)
erp = ResponseParser(
	encoding=ENCODING,
)


# Eljur data parsing
print(ep.authenticate())
marks = ep.get_marks(
	from_date=Date.to_eljur(config.user.marks.dates.start),
	to_date=Date.to_eljur(config.user.marks.dates.end),
)
ep.write(
	response=marks,
	response_file=config.program.responses.marks,
)


# Eljur data converting
subject_list = erp.load_suject_list(
	marks=config.program.responses.marks,
	user_id='413',
)
subject_list = erp.load_marks(
	marks=config.program.responses.marks,
	user_id='413',
	subject_list=subject_list,
)


# Md init
md = Md()


# Marks writing
md.marks(
	marks=config.user.marks.path,
	subject_list=subject_list,
	starts_with=config.user.marks.templates.starts_with.read_text(encoding=ENCODING),
	ends_with=config.user.marks.templates.ends_with.read_text(encoding=ENCODING),
)
