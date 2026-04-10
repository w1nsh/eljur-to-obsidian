from dataclasses import dataclass

from config.paths.paths import Paths
from config.user.user_config import UserConfig
from config.user.user_eljur_config import UserEljurConfig


@dataclass
class Config:
	paths: Paths
	user_config: UserConfig
	user_eljur_config: UserEljurConfig
