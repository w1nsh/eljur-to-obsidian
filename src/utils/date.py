from datetime import datetime, timedelta


class Date:
	"""
	Class for operations with dates.
	"""

	@staticmethod
	def to_eljur(
		date: str,
	) -> str:
		"""
		Convert date from 'dd.mm.yyyy' format to 'yyyymmdd' format.

		Args:
			date (str): Date in 'dd.mm.yyyy' format.

		Returns:
			str: Date in 'yyyymmdd' format.
		"""
		date_format = datetime.strptime(date, '%d.%m.%Y')
		new_date_format = date_format.strftime('%Y%m%d')
		return new_date_format
	

	@staticmethod
	def to_basic(
		date: str,
	) -> str:
		"""
		Convert date from 'yyyymmdd' format to 'dd.mm.yyyy' format.

		Args:
			date (str): Date in 'yyyymmdd' format.

		Returns:
			str: Date in 'dd.mm.yyyy' format.
		"""
		date_format = datetime.strptime(date, '%Y%m%d')
		new_date_format = date_format.strftime('%d.%m.%Y')
		return new_date_format
	

	@staticmethod
	def interval(
		from_date: str, 
		to_date: str, 
		eljur_format: bool = False,
	) -> list[str]:
		"""
		Finds the interval between dates.

		Args:
			from_date (str): Start date.
			to_date (str): End date.
			eljur_format (Optional[bool]): If True, the dates will be in 'yyyymmdd' format, else 'dd.mm.yyyy'. Defaults to False.
		Returns:
			list[str]: List of dates in the interval.s
		"""
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
		"""
		Finds the current date.

		Args:
			eljur_format (Optional[bool]): If True, the returned date will be in 'yyyymmdd' format, else 'dd.mm.yyyy'. Defaults to False.
		
		Returns:
			str: Current date.
		"""
		format = '%Y%m%d' if eljur_format else '%d.%m.%Y'
		current_date = datetime.now().strftime(format)
		return current_date
		