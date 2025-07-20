"""project class"""
import datetime

class Project:
    """project class"""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage=0):
        """set default parameters"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """less than, used for sorting projects"""
        return self.start_date < other.start_date

