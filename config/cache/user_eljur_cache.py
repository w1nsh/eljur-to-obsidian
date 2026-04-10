from dataclasses import dataclass

from config.cache.user_eljur_role import UserEljurRole


@dataclass
class UserEljurCache:
	role: UserEljurRole
	user_ids: list[dict[str, str]]
	selected_user_id: str
 