import unittest
import datetime
from .tasks import Task, Tasks


class TestTomorrowTaskList(unittest.TestCase):
    def test_empty(self):
        task_list = Tasks()
        self.assertListEqual(task_list.tomorrow(), [])

    def test_filters_other_days(self):
        task_list = Tasks()
        task_list.add_task(Task("do the laundry"))
        next_week = datetime.date.today() + datetime.timedelta(days=7)
        task_list.add_task(Task("important meeting", date=next_week))
        self.assertListEqual(task_list.tomorrow(), [])

    def test_finds_tomorrows_tasks(self):
        task_list = Tasks()
        next_week = datetime.date.today() + datetime.timedelta(days=7)
        task_list.add_task(Task("important meeting", date=next_week))
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        task_list.add_task(Task("John's birthday", date=tomorrow))

        result = task_list.tomorrow()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "John's birthday")


class TestTodayTaskList(unittest.TestCase):
    def test_empty(self):
        task_list = Tasks()
        self.assertListEqual(task_list.today(), [])

    def test_filters_other_days(self):
        task_list = Tasks()
        next_week = datetime.date.today() + datetime.timedelta(days=7)
        task_list.add_task(Task("important meeting", date=next_week))
        self.assertListEqual(task_list.today(), [])

    def test_finds_todays_tasks(self):
        task_list = Tasks()
        task_list.add_task(Task("important meeting"))

        result = task_list.today()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "important meeting")
