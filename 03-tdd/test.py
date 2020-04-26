import unittest
import datetime
from tasks import Task, Tasks


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


class TestTodayTasksList(unittest.TestCase):
    def test_empty(self):
        tasks_obj = Tasks()
        self.assertListEqual(tasks_obj.today(), [])

    def test_filter_other_days(self):
        tasks_obj = Tasks()
        next_days = datetime.date.today() + datetime.timedelta(days=4)
        tasks_obj.add_task(Task('Today', date=next_days))
        next_days += datetime.timedelta(days=3)
        tasks_obj.add_task(Task('Next Date', date=next_days))

        today_list = tasks_obj.today()
        # print(today_list)
        self.assertListEqual(today_list, [])

    def test_filter_today_tasks(self):
        tasks_obj = Tasks()
        tasks_obj.add_task(Task("Today"))
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tasks_obj.add_task(Task('Tomorrow', date=tomorrow))

        today_tasks = tasks_obj.today()
        self.assertEqual(len(today_tasks), 1)
        self.assertTrue(today_tasks[0].title == 'Today')

