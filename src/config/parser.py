from pathlib import Path
from typing import Any
import json

from src.config.responses_paths import ResponsesPaths
from src.config.templates import TemplatesConfig
from src.config.dates import DatesConfig
from src.config.homeworks import HomeworksConfig
from src.config.marks import MarksConfig
from src.config.secrets.main import SecretsConfig
from src.config.program import ProgramConfig
from src.config.user import UserConfig
from src.config.main import Config
from src.config.secrets.parser import SecretsParser


class ConfigParser:
	"""

	"""

	def __init__(
		self,
		encoding: str,
		eto: Path,
	) -> None:
		self._encoding = encoding
		self._eto = eto


	def load_config(
		self,
		config: Path,
	) -> Config:
		config_json = self._load_json(
			config,
		)
		user = self._user(
			config_json['user'],
		)
		program = self._program(
			config_json['program'],
		)
		secrets = self._secrets(
			program.env			
		)
		return Config(
			user=user,
			program=program,
			secrets=secrets,
		)


	def _load_json(
		self,
		file: Path,
	) -> dict[str, Any]:
		json_string = file.read_text(encoding=self._encoding)
		json_dict = json.loads(json_string)
		return json_dict


	def _user(
		self,
		user: dict[str, Any],
	) -> UserConfig:
		marks = self._marks(
			user['marks'],
		)
		homeworks = self._homeworks(
			user['homeworks'],
		)
		return UserConfig(
			marks=marks,
			homeworks=homeworks,
		)


	def _homeworks(
		self,
		homeworks: dict[str, Any],
	) -> HomeworksConfig:
		need = homeworks['need']
		path = Path(homeworks['path'])
		dates = self._dates(
			homeworks['date'],
		)
		templates = self._templates(
			homeworks['template'],
		)
		return HomeworksConfig(
			need=need,
			path=path,
			dates=dates,
			templates=templates,
		)


	def _marks(
		self,
		marks: dict[str, Any],
	) -> MarksConfig:
		homeworks = self._homeworks(
			marks,
		)
		desired = marks['desired']
		return MarksConfig(
			need=homeworks.need,
			path=homeworks.path,
			dates=homeworks.dates,
			templates=homeworks.templates,
			desired=desired,
		)


	def _dates(
		self,
		dates: dict[str, Any],
	) -> DatesConfig:
		start = dates['start']
		end = dates['end']
		return DatesConfig(
			start=start,
			end=end,
		)


	def _templates(
		self,
		templates: dict[str, Any],
	) -> TemplatesConfig:
		starts_with = self._eto / templates['starts_with']
		ends_with = self._eto / templates['ends_with']
		return TemplatesConfig(
			starts_with=starts_with,
			ends_with=ends_with,
		)


	def _program(
		self,
		program: dict[str, Any],
	) -> ProgramConfig:
		env = self._eto / program['env']
		responses = self._responses(
			program['responses'],
		)
		return ProgramConfig(
			env=env,
			responses=responses,
		)


	def _responses(
		self,
		responses: dict[str, Any],
	) -> ResponsesPaths:
		assessments = self._eto / responses['assessments']
		diary = self._eto / responses['diary']
		homeworks = self._eto / responses['homeworks']
		marks = self._eto / responses['marks']
		periods = self._eto / responses['periods']
		rules = self._eto / responses['rules']
		schedule = self._eto / responses['schedule']
		return ResponsesPaths(
			assessments=assessments,
			diary=diary,
			homeworks=homeworks,
			marks=marks,
			periods=periods,
			rules=rules,
			schedule=schedule,
		)


	def _secrets(
		self,
		env: Path,
	) -> SecretsConfig:
		secrets_parser = SecretsParser(
			encoding=self._encoding,
			env=env,
		)
		return secrets_parser.secrets()
