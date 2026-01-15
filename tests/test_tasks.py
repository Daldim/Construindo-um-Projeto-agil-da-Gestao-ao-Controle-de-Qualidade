import pytest
from src.app import TaskManager


def test_create_task():
    manager = TaskManager()
    task = manager.create_task("Estudar Engenharia de Software")
    assert task.title == "Estudar Engenharia de Software"


def test_create_task_without_title():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.create_task("")


def test_task_priority():
    manager = TaskManager()
    task = manager.create_task("Tarefa crítica", priority="alta")
    assert task.priority == "alta"
