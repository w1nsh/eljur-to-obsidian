from pathlib import Path

from config.user.user_eljur_config import UserEljurConfig


class ConfigWriter:
	"""
	Class for writing data to config files.
	"""

	def __init__(
		self,
		encoding: str,
	) -> None:
		self._encoding = encoding


	def write_env(
		self,
		env_path: Path,
		user_eljur_config: UserEljurConfig,
	) -> None:
		env_content = ''
		env_content += f'ELJUR_LOGIN={user_eljur_config.login}\n'
		env_content += f'ELJUR_PASSWORD={user_eljur_config.password}\n'
		env_content += f'ELJUR_SCHOOL_CLASS={user_eljur_config.school_class}\n'
		env_content += f'ELJUR_VENDOR={user_eljur_config.vendor}\n'
		env_content += f'ELJUR_DEVKEY={user_eljur_config.devkey}\n'
		env_content += f'ELJUR_AUTH_TOKEN={user_eljur_config.auth_token}\n'
		env_path.write_text(env_content, encoding=self._encoding)
