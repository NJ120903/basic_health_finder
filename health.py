class HealthTracker:
    def __init__(self):
        self.exercise_minutes = 0
        self.diet_calories = 0
        self.sleep_hours = 0
        self.exercise_goal = 150  # 150 minutes per week
        self.calorie_intake_goal = 2500  # Your personal calorie intake goal
        self.sleep_goal = 7  # 7-9 hours per night

    def track_exercise(self):
        minutes = int(input("Enter the minutes of exercise: "))
        self.exercise_minutes += minutes

    def track_diet(self):
        calories = int(input("Enter the calories consumed: "))
        self.diet_calories += calories

    def track_sleep(self):
        hours = float(input("Enter the hours of sleep: "))
        self.sleep_hours += hours

    def get_stats(self):
        return {
            "exercise_minutes": self.exercise_minutes,
            "diet_calories": self.diet_calories,
            "sleep_hours": self.sleep_hours
        }

    def evaluate_fitness(self):
        exercise_status = "fit" if self.exercise_minutes >= self.exercise_goal else "unfit"
        diet_status = "fit" if self.diet_calories >= self.calorie_intake_goal else "unfit"
        sleep_status = "fit" if self.sleep_hours >= self.sleep_goal else "unfit"
        return {
            "exercise_status": exercise_status,
            "diet_status": diet_status,
            "sleep_status": sleep_status
        }

# Example usage
tracker = HealthTracker()

tracker.track_exercise()
tracker.track_diet()
tracker.track_sleep()

stats = tracker.get_stats()
fitness_status = tracker.evaluate_fitness()
print("Statistics:", stats)
print("Fitness Status:", fitness_status)