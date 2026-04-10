from dataclasses import dataclass


@dataclass
class UserEljurConfig:
	login: str | None
	password: str | None
	school_class: str | None
	vendor: str | None
	devkey: str | None
	auth_token: str | None
