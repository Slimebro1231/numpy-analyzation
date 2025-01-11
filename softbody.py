class task:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.start = 1
        self.end = 15
        self.total_hours = 0
        self.day_tasks = [day_task()] * self.end - self.start + 1

    @staticmethod
    def update_tasks(total_tasks_list):
        pass
    def total_external_pressure(total_tasks_list):
        pressure = 0
        for task in total_tasks_list:
            for day in task.day_tasks:
                pressure += day.internal_pressure
        return pressure
    
    

# pressure = Force / day
class day_task:
    def __init__(self):
        self.hours = 0
        self.internal_pressure = 0
        self.external_pressure = 0
        self.density = 1
    


# It will maintain its own volume
# task with most density gets sorted first. 
# total density is calculated by summing all densities and divide by days alloted
# Total internal pressure is equal to total external pressure
# total internal pressure is equal to (total density*total days) / hours or average of all daily pressure
# daily external pressure is equal to daily density / daily hours
# total hours = sum of daily hours

# total day_tasks per day is equal to looping through all tasks and summing the day that matches
# total mass per day is equal to sum of density* hour per day
# density is the same as urgency, or importance that it cannot change
# 
