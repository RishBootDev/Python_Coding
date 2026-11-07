class Employee:
	# Class variables are shared by every Employee instance.
	company = "Example Corp"
	employee_count = 0

	def __init__(self, name):
		self.name = name
		Employee.employee_count += 1

	@staticmethod
	def show_company_info():
		"""A static method has no automatic self or cls parameter."""
		print(f"Company: {Employee.company}")
		print(f"Employees created: {Employee.employee_count}")


if __name__ == "__main__":
	first = Employee("Alex")
	second = Employee("Sam")

	# Both instances access the same class-level field.
	print(first.company)
	print(second.company)

	# Change the field on the class; both instances now see the new value.
	Employee.company = "New Example Corp"
	print(first.company)
	print(second.company)

	# Static methods can be called using either the class or an instance.
	Employee.show_company_info()
	first.show_company_info()
