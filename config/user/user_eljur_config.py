from dataclasses import dataclass


@dataclass
class UserEljurConfig:
	login: str
	password: str
	school_class: str
	vendor: str
	devkey: str
	auth_token: str
