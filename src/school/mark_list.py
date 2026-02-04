class MarkList:
	def __init__(self, marks: list[int]) -> None:
		self.marks = marks


	def append_mark(self, mark: int) -> None:
		self.marks.append(mark)


	def set_marks(self, marks: list[int]) -> None:
		self.marks = marks


	def average(self, marks: list[int] | None = None) -> float:
		if not marks:
			marks = self.marks.copy()
		avg = sum(marks) / len(marks)
		return avg
	

	def count_concrete_marks_for_desired(self, concrete_mark: int , desired_mark: int) -> int:
		if concrete_mark < desired_mark:
			return 0
		count = 0
		marks = self.marks.copy()
		avg = self.average(marks)
		min_need_mark = desired_mark - 0.5
		while avg < min_need_mark:
			count += 1
			marks.append(concrete_mark)
			avg = self.average(marks)
		return count
	

	def count_neutral_marks_for_current_mark(self, concrete_mark: int) -> int:
		count = 0
		marks = self.marks.copy()
		avg = self.average(marks)
		current_mark = round(avg)
		round_avg = round(avg)
		if concrete_mark == current_mark:
			return 999
		while round_avg == current_mark:
			count += 1
			marks.append(concrete_mark)
			avg = self.average(marks)
			round_avg = round(avg)
		count -= 1
		return count
