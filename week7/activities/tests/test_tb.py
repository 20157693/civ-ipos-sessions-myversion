import io
import unittest
from contextlib import redirect_stdout

import tb


class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        tb.add_task(tasks, "Study")
        self.assertEqual(tasks, [("Study", False)])

    def test_mark_task_completed(self):
        tasks = [("Study", False), ("Sleep", False)]
        tb.mark_task_completed(tasks, 0)
        self.assertEqual(tasks[0], ("Study", True))

    def test_delete_task(self):
        tasks = [("Study", False), ("Sleep", False)]
        tb.delete_task(tasks, 0)
        self.assertEqual(tasks, [("Sleep", False)])

    def test_sort_tasks(self):
        tasks = [("Zoo", False), ("Alpha", False), ("Moon", True)]
        tb.sort_tasks(tasks)
        self.assertEqual(
            tasks,
            [("Alpha", False), ("Moon", True), ("Zoo", False)],
        )

    def test_binary_search_found_after_sort(self):
        tasks = [("Zoo", False), ("Alpha", False), ("Moon", True)]
        tb.sort_tasks(tasks)
        index = tb.binary_search(tasks, "Moon")
        self.assertEqual(index, 1)

    def test_binary_search_not_found(self):
        tasks = [("Alpha", False), ("Moon", True), ("Zoo", False)]
        index = tb.binary_search(tasks, "Study")
        self.assertEqual(index, -1)

    def test_list_tasks_output(self):
        tasks = [("Study", False), ("Sleep", True)]
        out = io.StringIO()
        with redirect_stdout(out):
            tb.list_tasks(tasks)
        printed = out.getvalue()
        self.assertIn("0. [ ] Study", printed)
        self.assertIn("1. [X] Sleep", printed)

    def test_list_tasks_empty(self):
        out = io.StringIO()
        with redirect_stdout(out):
            tb.list_tasks([])
        self.assertIn("No tasks available.", out.getvalue())


if __name__ == "__main__":
    unittest.main()