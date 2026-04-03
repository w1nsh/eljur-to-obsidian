import requests
import json
from typing import Any


class EljurParser:
	"""
	Class for parsing data from Eljur API.

	Attributes:
		_login (str): The login of the user.
		_password (str): The password of the user.
		_devkey (str): The developer key for API access.
		_school_class (str): The class of the school.
		_vendor (str): The school name.
		_session (requests.Session): The session for making requests.
		_base_url (str): The base URL for API requests.
		_auth_token (str): The authentication token for API access.
	"""

	def __init__(
		self,
		login: str,
		password: str,
		devkey: str,
		school_class: str,
		vendor: str,
	) -> None:
		"""
		Initializing the EljurParser object.

		Args:
			login (str): The login of the user.
			password (str): The password of the user.
			devkey (str): The developer key for API access.
			school_class (str): The class of the school.
			vendor (str): The school name.
		"""
		self._login = login
		self._password = password
		self._devkey = devkey
		self._school_class = school_class
		self._vendor = vendor
		self._session = requests.Session()
		self._base_url = f'https://{self._vendor}.eljur.ru/api'


	def authenticate(
		self,
	) -> bool:
		"""
		Authenticate the user session on Eljur.

		Need to get the auth token.
		Token allows send requests without password and username.

		Returns:
			bool: True if authentication is successful, False otherwise.
		"""
		data = {
			'login': self._login,
			'password': self._password,
			'devkey': self._devkey,
			'vendor': self._vendor,
			'out_format': 'json',
		}
		response = self._post_request('auth', data)
		if response:
			token = response['response']['result']['token']
			self._auth_token = token
			return True
		return False


	def get_rules(
		self,
	) -> dict[str, Any] | None:
		"""
		Gets rights for user Eljur account.

		Need for understanding role of user and him opportunitys.

		Returns:
			dict[str, Any] | None: dictionary if getting rules is successful, None otherwise.
		"""
		response = self._get_request('getrules')
		if response:
			return response


	def get_schedule(
		self,
		from_date: str,
		to_date: str,
		student: str | None = None,
		school_class: bool = False,
		rings: bool = False,
	) -> dict[str, Any] | None:
		"""
		Gets schedule for the given date range.

		Class has larger priority than students.
		If Students is empty requests schedule for all children of user, if user is parent.
		If user is student, he will get schedule for himself.

		Args:
			from_date (str): The start date of the schedule in the format 'yyyymmdd'.
			to_date (str): The end date of the schedule in the format 'yyyymmdd'.
			student (Optional[str]): The ID of the student to get the schedule for. Defaults to None.
			school_class (bool): Whether to get the schedule for the whole class. Defaults to False.
			rings (bool): Whether to include rings information to the schedule. Defaults to False.

		Returns:
			dict[str, Any] | None: dictionary if getting schedule is successful, None otherwise.
		"""
		params = {
			'days': f'{from_date}-{to_date}',
			'rings': rings,
		}
		if school_class:
			params['class'] = self._school_class
		elif student:
			params['students'] = student
		response = self._get_request('getschedule', params)
		if response:
			return response
		

	def get_homework(
		self,
		from_date: str,
		to_date: str,
		student: str | None = None,
		school_class: bool = False,
	) -> dict[str, Any] | None:
		"""
		Gets homework for the given date range.

		Class has larger priority than students.
		If Students is empty requests homework for all children of user, if user is parent.
		If user is student, he will get homework for himself.

		Args:
			from_date (str): The start date of the homework in the format 'yyyymmdd'.
			to_date (str): The end date of the homework in the format 'yyyymmdd'.
			student (Optional[str]): The ID of the student to get the homework for. Defaults to None.
			school_class (bool): Whether to get the homework for the whole class. Defaults to False.

		Returns:
			dict[str, Any] | None: dictionary if getting homework is successful, None otherwise.
		"""
		params = {
			'days': f'{from_date}-{to_date}',
		}
		if school_class:
			params['class'] = self._school_class
		elif student:
			params['students'] = student
		response = self._get_request('gethomework', params)
		if response:
			return response


	def get_assessments(
		self,
		from_date: str,
		to_date: str,
		student: str | None = None,
	) -> dict[str, Any] | None:
		"""
		Gets assessments for the given date range.

		If Students is empty requests assessments for all children of user, if user is parent.
		If user is student, he will get assessments for himself.

		Args:
			from_date (str): The start date of the assessments in the format 'yyyymmdd'.
			to_date (str): The end date of the assessments in the format 'yyyymmdd'.
			student (Optional[str]): The ID of the student to get the assessments for. Defaults to None.

		Returns:
			dict[str, Any] | None: dictionary if getting assessments is successful, None otherwise.
		"""
		params = {
			'days': f'{from_date}-{to_date}',
		}
		if student:
			params['students'] = student
		response = self._get_request('getassessments', params)
		if response:
			return response


	def get_marks(
		self,
		from_date: str,
		to_date: str,
		student: str | None = None,
	) -> dict[str, Any] | None:
		"""
		Gets marks for the given date range.

		If Students is empty requests marks for all children of user, if user is parent.
		If user is student, he will get marks for himself.

		Args:
			from_date (str): The start date of the marks in the format 'yyyymmdd'.
			to_date (str): The end date of the marks in the format 'yyyymmdd'.
			student (Optional[str]): The ID of the student to get the marks for. Defaults to None.

		Returns:
			dict[str, Any] | None: dictionary if getting marks is successful, None otherwise.
		"""
		params = {
			'days': f'{from_date}-{to_date}',
		}
		if student:
			params['students'] = student
		response = self._get_request('newgetmarks', params)
		if response:
			return response


	def get_diary(
		self,
		from_date: str,
		to_date: str,
		student: str | None = None,
		rings: bool = False,
	) -> dict[str, Any] | None:
		"""
		Gets diary information (schedule, homework, marks) for the given date range.

		Result of this method is combination of get_schedule, get_homework and get_assessments methods.
		If Students is empty requests diary for all children of user, if user is parent.
		If user is student, he will get diary for himself.

		Args:
			from_date (str): The start date of the diary in the format 'yyyymmdd'.
			to_date (str): The end date of the diary in the format 'yyyymmdd'.
			student (Optional[str]): The ID of the student to get the diary for. Defaults to None.
			rings (bool): Whether to include rings information to the diary. Defaults to False.

		Returns:
			dict[str, Any] | None: dictionary if getting diary is successful, None otherwise.
		"""
		params = {
			'days': f'{from_date}-{to_date}',
			'rings': rings,
		}
		if student:
			params['students'] = student
		response = self._get_request('newgetdiary', params)
		if response:
			return response


	def _get_request(
		self,
		url_endpoint: str,
		unique_params: dict[str, Any] | None = None,
	) -> dict[str, Any] | None:
		"""
		Sends a GET request to the specified API endpoint with the given parameters.

		Args:
			url_endpoint (str): The API endpoint to send the request to.
			unique_params (Optional[dict[str, Any]]): Additional parameters specific to the request. Defaults to None.

		Returns:
			dict[str, Any] | None: The JSON response from the API if the request is successful, None otherwise.
		"""
		url = f'{self._base_url}/{url_endpoint}'
		params = {
			'auth_token': self._auth_token,
			'devkey': self._devkey,
			'vendor': self._vendor,
			'out_format': 'json',
		}
		if unique_params:
			params.update(unique_params)
		try:
			response = self._session.get(
				url,
				params=params,
				timeout=30,
			)
			response.raise_for_status()
			json_response = response.json()
			return json_response
		except requests.HTTPError as e:
			print(f'HTTP Error: {e}')
		except requests.RequestException as e:
			print(f'Request Exception: {e}')
		except json.JSONDecodeError as e:
			print(f'JSON Decode Error: {e}')
		return None


	def _post_request(
		self,
		url_endpoint: str,
		data: dict[str, Any],
	) -> dict[str, Any] | None:
		"""
		Sends a POST request to the specified API endpoint with the given data.

		Args:
			url_endpoint (str): The API endpoint to send the request to.
			data (dict[str, Any]): The data to be sent in the POST request.
		
		Returns:
			dict[str, Any] | None: The JSON response from the API if the request is successful, None otherwise.
		"""
		url = f'{self._base_url}/{url_endpoint}'
		try:
			response = self._session.post(
				url,
				data=data,
				timeout=30,
			)
			response.raise_for_status()
			json_response = response.json()
			return json_response
		except requests.HTTPError as e:
			print(f'HTTP Error: {e}')
		except requests.RequestException as e:
			print(f'Request Exception: {e}')
		except json.JSONDecodeError as e:
			print(f'JSON Decode Error: {e}')
		return None
