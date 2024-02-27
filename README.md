# Health Tracker

The Health Tracker is a Python class that allows users to track their exercise, diet, and sleep metrics, and provides an evaluation of their fitness status based on predefined goals.

## Features

- **Track Exercise**: Record the minutes of exercise.
- **Track Diet**: Record the calories consumed.
- **Track Sleep**: Record the hours of sleep.
- **View Statistics**: Retrieve the recorded exercise, diet, and sleep metrics.
- **Evaluate Fitness**: Determine the fitness status based on predefined goals.

## Getting Started

1. **Installation**:
   - Clone the repository: `git clone https://github.com/your_username/health-tracker.git`
   - Install dependencies: `pip install -r requirements.txt`

2. **Usage**:
   ```python
   from health_tracker import HealthTracker

   tracker = HealthTracker()

   tracker.track_exercise()
   tracker.track_diet()
   tracker.track_sleep()

   stats = tracker.get_stats()
   fitness_status = tracker.evaluate_fitness()
   print("Statistics:", stats)
   print("Fitness Status:", fitness_status)
   ```

3. **Customization**:
   - Adjust goals in the `__init__` method: `exercise_goal`, `calorie_intake_goal`, `sleep_goal`.

4. **Contributing**:
   - Fork the repository.
   - Create a new branch (`git checkout -b feature/improve-tracker`).
   - Make changes and commit (`git commit -am 'Add new feature'`).
   - Push to the branch (`git push origin feature/improve-tracker`).
   - Create a new Pull Request.

## Acknowledgements

- This project was inspired by the need for a simple and effective way to track health metrics.
- Special thanks to the contributors who helped improve this project.
