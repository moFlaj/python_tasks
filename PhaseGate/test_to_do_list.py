
import to_do_list
import unittest


class TestToDoList(unittest.TestCase):

	def setUp(self):
		tasks = list()

	def test_view_all_tasks_exists(self):
		to_do_list.add_a_task(task)

	def confirms_delete_task_is_in_existence(self):
		to_do_list.delete_task(run)

	def test_delete_task_confirmation(self):
		tasks = ["Go home", "Run home"]
		actual = to_do_list.delete_task(tasks[1])
		expected = ['Go home']
		self.assertAlmostEqual(actual,expected)

	def mark_task_as_complete_exists(self):
		mark_task_as_complete("run")
		
	def test_is_marked_on_competion(self):
		tasks = ["Go home", "Run home"]
		actual = to_do_list.mark_task_as_complete(tasks[1])
		expected = ['Go home', '[X]Run home']
		self.assertAlmostEqual(actual,expected)

	def list_is_passed_as_argument_for_list_app(self):
		try:
			tasks = ["Go home", "Run home"]
			if type(tasks) == list:
				to_do_list_check(tasks)
	
			else:
				raise ValueError("Illegal parameter passed.")
		except ValueError as e:
			print(e.args[0])
		self.assertRaises("Illegal parameter passed.")

	
			

	
		



