# scripts/delete_all_contests.py

from mpi.models import Contest

def run():
    # Get all polls
    all_contests = Contests.objects.all()
    # Delete contests
    all_contests.delete()
