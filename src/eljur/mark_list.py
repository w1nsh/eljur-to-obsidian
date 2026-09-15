class MarkList:
	"""
	
	"""

	def __init__(
		self,
		marks: list[int],
	) -> None:
		"""
		
		"""
		self.marks = marks


	def average(
		self,
		marks: list[int] | None = None,
	) -> float:
		"""
		Calculates average value of the marks.

		Args:
			marks (list[int]): List of the marks.
				If marks if not transferred uses copy self.marks.

		Returns:
			float: Average value.
		"""
		if not marks:
			if self.marks:
				marks = self.marks.copy()
			else:
				return 0
		avg = sum(marks) / len(marks)
		return avg
	

	def count_marks_for_desired(
		self,
		mark: int,
		desired_mark: int,
	) -> int:
		"""
		Calculate count of the concrete mark to for desired marks.

		Args:
			mark (int): Concrete mark.
			desired_mark (int): Desired mark.

		Returns:
			int: Count of the concrete marks.
		"""
		if not desired_mark:
			return 0
		if mark < desired_mark:
			return 0
		count = 0
		marks = self.marks.copy()
		avg = self.average(marks)
		min_need_mark = desired_mark - 0.5
		while avg < min_need_mark:
			count += 1
			marks.append(mark)
			avg = self.average(marks)
		return count
	

	def count_neutral_for_current(
		self,
		mark: int,
	) -> int:
		"""
		Calculates count of the concrete mark
		without affecting to the current mark.

		Args:
			mark (int): Concrete mark.
		
		Returns:
			int: Count of the concrete mark.
		"""
		count = -1
		marks = self.marks.copy()
		avg = self.average(marks)
		current_mark = round(avg)
		round_avg = round(avg)
		if mark == current_mark:
			return 999
		while round_avg == current_mark:
			count += 1
			marks.append(mark)
			avg = self.average(marks)
			round_avg = round(avg)
		return count
