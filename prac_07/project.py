"""
Estimated Time: 30 minutes
Actual Time: 55 minutes
"""

import datetime


class Project:
    """
    A class to represent a project.
    """
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a project object with given attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

def __lt__(self, other):
    """Define less than operator for sorting by priority."""
    return self.priority < other.priority


def is_complete(self):
    """Check if the project is completed."""
    return self.completion_percentage == 100


def update(self, new_completion_percentage=None, new_priority=None):
    if new_completion_percentage is not None:
        self.completion_percentage = int(new_completion_percentage)
    if new_priority is not None:
        self.priority = int(new_priority)