from django.core.management.base import BaseCommand
from octofit_tracker.models.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='captain@marvel.com', team=marvel)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date=date.today())
        Activity.objects.create(user=captain, type='Cycling', duration=45, calories=400, date=date.today())
        Activity.objects.create(user=superman, type='Swimming', duration=60, calories=500, date=date.today())
        Activity.objects.create(user=batman, type='Walking', duration=20, calories=100, date=date.today())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body', difficulty='Medium')
        Workout.objects.create(name='Squats', description='Lower body', difficulty='Easy')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=800, rank=1)
        Leaderboard.objects.create(team=dc, points=700, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
