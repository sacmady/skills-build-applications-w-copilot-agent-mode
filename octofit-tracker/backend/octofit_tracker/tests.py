from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="pass", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.activity = Activity.objects.create(user=self.user, type="run", duration=30, distance=5.0)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), "Test Team")

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)

    def test_activity_fields(self):
        self.assertEqual(self.activity.type, "run")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.distance, 5.0)

    def test_workout_fields(self):
        self.assertEqual(self.workout.name, "Pushups")
        self.assertEqual(self.workout.description, "Do 20 pushups")

    def test_leaderboard_fields(self):
        self.assertEqual(self.leaderboard.team, self.team)
        self.assertEqual(self.leaderboard.points, 100)
