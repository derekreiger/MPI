from mpi.models import Org, User, Idea
print("Clearing ideas ...")
all_ideas= Idea.objects.all()
all_ideas.delete()
print("Clearing users ...")
all_users = User.objects.all()
all_users.delete()
print("Clearing orgs ...")
all_orgs = Org.objects.all()
all_orgs.delete()