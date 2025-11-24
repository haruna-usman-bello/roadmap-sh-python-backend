"""Task Tracker CLI Application Test Suite."""
from unittest import TestCase, main
from task_tracker import TaskTracker


class TestTaskTrackerCLI(TestCase):
    """Test cases for Task Tracker CLI application."""

    def setUp(self):
        """Set up a new TaskTracker instance before each test."""
        self.tracker = TaskTracker()

    def test_show_available_flags(self):
        """Test displaying available command flags."""
        self.tracker.show_avalible_flags()

    def test_add_task(self):
        """Test adding a new task."""
        initial_task_count = len(self.tracker.tasks)
        self.tracker.add_task("Test task 1")
        self.tracker.add_task("Test task 2")
        self.assertEqual(len(self.tracker.tasks), initial_task_count + 2)
        self.assertEqual(
            self.tracker.tasks[-1]['description'], "Test task 2")

    def test_list_tasks(self):
        """Test listing tasks."""
        self.tracker.add_task("Test task for listing")
        self.tracker.list_tasks()
        self.tracker.list_tasks(status_filter='todo')

    def test_update_task(self):
        """Test updating a task."""
        self.tracker.add_task("Task to be updated")
        task_id = self.tracker.tasks[-1]['id']
        self.tracker.update_task(task_id, "Updated task description")
        self.assertEqual(
            self.tracker.tasks[-1]['description'], "Updated task description")

    def test_delete_task(self):
        """Test deleting a task."""
        self.tracker.add_task("Task to be deleted")
        task_id = self.tracker.tasks[-1]['id']
        initial_task_count = len(self.tracker.tasks)
        self.tracker.delete_task(task_id)
        self.assertEqual(len(self.tracker.tasks), initial_task_count - 1)

    def test_mark_task(self):
        """Test marking a task's status."""
        self.tracker.add_task("Task to be marked")
        task_id = self.tracker.tasks[-1]['id']
        self.tracker.mark_task(task_id, 'in-progress')
        self.assertEqual(
            self.tracker.tasks[-1]['status'], 'in-progress')
        self.tracker.mark_task(task_id, 'done')
        self.assertEqual(
            self.tracker.tasks[-1]['status'], 'done')


if __name__ == '__main__':
    main()
