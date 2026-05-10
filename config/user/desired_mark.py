from dataclasses import dataclass


@dataclass
class DesiredMark:
	"""
	Dataclass for storing pairs of subject and him desired mark.

	Attributes:
		subject_name (str): Name of the school subject.
		desired_mark (int): Desired mark of the school subject.
	"""
	subject_name: str
	desired_mark: int
	

	def set_desired_mark(
		self,
		desired_mark: int
	) -> None:
		"""
		Sets a new value of the desired mark.

		Args:
			desired_mark (int): New value of the desired mark.
		"""
		self.desired_mark = desired_mark
