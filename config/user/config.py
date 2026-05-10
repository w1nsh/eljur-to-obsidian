from dataclasses import dataclass

from config.paths.paths import Paths
from config.user.user_config import UserConfig
from config.user.user_eljur_config import UserEljurConfig


@dataclass
class Config:
	"""
	Dataclass for storing main configuration parameters.

	Attributes:
		paths (Paths):
			Paths to all files and directories used in the project.
		user_config (UserConfig):
			User app configuration.
		user_eljur_config (UserEljurConfig):
			User Eljur configuration.
			Data for logging in Eljur.
	"""
	paths: Paths
	user_config: UserConfig
	user_eljur_config: UserEljurConfig
