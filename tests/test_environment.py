import sys

from workstation_python.environment import python_environment


def test_python_environment():
    environment = python_environment()

    assert environment["executable"] == sys.executable
    assert environment["python"]
    assert environment["platform"]
