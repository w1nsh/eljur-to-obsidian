import requests


class EljurParser:
	def __init__(
		self, 
		login: str, 
		password: str, 
		devkey: str, 
		school_class: str, 
		vendor: str
	) -> None:
		self.login = login
		self.password = password
		self.devkey = devkey
		self.school_class = school_class
		self.vendor = vendor
		self.session = requests.Session()
		self._set_base_url()

	
	def _set_base_url(self) -> None:
		self.base_url = f'https://{self.vendor}.eljur.ru/api'


	def authenticate(self) -> bool:
		auth_link = f'{self.base_url}/auth'
		data = {
			'login': self.login,
			'password': self.password,
			'devkey': self.devkey,
			'vendor': self.vendor,
			'out_format': 'json'
		}
		response = self.session.post(
			auth_link,
			data=data
		)
		response.raise_for_status()
		json_response = response.json()
		if json_response.get('response', {}).get('state') == 200:
			token = json_response['response']['result']['token']
			self.auth_token = token
			return True
		else:
			error_message = json_response.get('response', {}).get('error', 'Unknown error')
			print(f'Authentication error: {error_message}')
			return False
	

	def get_rules(self) -> dict:
		rules_link = f'{self.base_url}/getrules'
		params = {
			'auth_token': self.auth_token,
			'devkey': self.devkey,
			'vendor': self.vendor,
			'out_format': 'json'
		}
		response = self.session.get(
			rules_link,
			params=params
		)
		response.raise_for_status()
		json_response = response.json()
		return json_response
		
	
	def get_schedule(
		self, 
		from_date: str, 
		to_date: str, 
		rings: bool = False
	) -> dict:
		# data format: yyyymmdd
		schedule_link = f'{self.base_url}/getschedule'
		days = f'{from_date}-{to_date}'
		params = {
			'auth_token': self.auth_token,
			'devkey': self.devkey,
			'vendor': self.vendor,
			'out_format': 'json',
			'days': days,
			'class': self.school_class,
			'rings': rings
		}
		response = self.session.get(
			schedule_link,
			params=params
		)
		response.raise_for_status()
		json_response = response.json()
		return json_response
	

	def get_homework(self, from_date: str, to_date: str) -> dict:
		# data format: yyyymmdd
		homework_link = f'{self.base_url}/gethomework'
		days = f'{from_date}-{to_date}'
		params = {
			'auth_token': self.auth_token,
			'devkey': self.devkey,
			'vendor': self.vendor,
			'out_format': 'json',
			'days': days,
			'class': self.school_class
		}
		response = self.session.get(
			homework_link,
			params=params
		)
		response.raise_for_status()
		json_response = response.json()
		return json_response
	

	def get_assessments(self, from_date: str, to_date: str) -> dict:
		# data format: yyyymmdd
		assessments_link = f'{self.base_url}/getassessments'
		days = f'{from_date}-{to_date}'
		params = {
			'auth_token': self.auth_token,
			'devkey': self.devkey,
			'vendor': self.vendor,
			'out_format': 'json',
			'days': days,
		}
		response = self.session.get(
			assessments_link,
			params=params
		)
		response.raise_for_status()
		json_response = response.json()
		return json_response
	
	


	def get_marks(self, from_date: str, to_date: str) -> dict:
		# data format: yyyymmdd
		marks_link = f'{self.base_url}/getmarks'
		days = f'{from_date}-{to_date}'
		params = {
			'auth_token': self.auth_token,
			'devkey': self.devkey,
			'vendor': self.vendor,
			'out_format': 'json',
			'days': days,
		}
		response = self.session.get(
			marks_link,
			params=params
		)
		response.raise_for_status()
		json_response = response.json()
		return json_response
	
	
	def get_diary(
		self, 
		from_date: str, 
		to_date: str, 
		rings: bool = False
	) -> dict:
		# data format: yyyymmdd
		diary_link = f'{self.base_url}/getdiary'
		days = f'{from_date}-{to_date}'
		params = {
			'auth_token': self.auth_token,
			'devkey': self.devkey,
			'vendor': self.vendor,
			'out_format': 'json',
			'days': days,
			'class': self.school_class,
			'rings': rings
		}
		response = self.session.get(
			diary_link,
			params=params
		)
		response.raise_for_status()
		json_response = response.json()
		return json_response
