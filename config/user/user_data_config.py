from dataclasses import dataclass

from config.user.marks_config import MarksConfig
from config.user.homeworks_config import HomeworksConfig


@dataclass
class UserDataConfig:
	marks: MarksConfig
	homeworks: HomeworksConfig
	