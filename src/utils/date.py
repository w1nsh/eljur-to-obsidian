from datetime import datetime, timedelta


class Date:
	@staticmethod
	def to_eljur(
		date: str,
	) -> str:
		date_format = datetime.strptime(date, '%d.%m.%Y')
		new_date_format = date_format.strftime('%Y%m%d')
		return new_date_format
	

	@staticmethod
	def to_basic(
		date: str,
	) -> str:
		date_format = datetime.strptime(date, '%Y%m%d')
		new_date_format = date_format.strftime('%d.%m.%Y')
		return new_date_format
	

	@staticmethod
	def interval(
		from_date: str, 
		to_date: str, 
		eljur_format: bool = False,
	) -> list[str]:
		from_date_format = datetime.strptime(from_date, '%d.%m.%Y')
		to_date_format = datetime.strptime(to_date, '%d.%m.%Y')
		dates = []
		current_date = from_date_format
		format = '%Y%m%d' if eljur_format else '%d.%m.%Y'
		while current_date <= to_date_format:
			dates.append(current_date.strftime(format))
			current_date += timedelta(days=1)
		return dates
	

	@staticmethod
	def current_date(
		eljur_format: bool = False,
	) -> str:
		format = '%Y%m%d' if eljur_format else '%d.%m.%Y'
		current_date = datetime.now().strftime(format)
		return current_date
		