from dataclasses import dataclass

from config.user.marks_config import MarksConfig
from config.user.homeworks_config import HomeworksConfig


@dataclass
class UserConfig:
	marks_config: MarksConfig
	homeworks_config: HomeworksConfig
	