from mpi.models import User

print("Creating users...")

u1 = User(org_id=1, user_id=1, first_name='Mike', last_name='Watkins',email='Mike.Watkins@impact123.com', idea_points=500, idea_points_awarded=0) 
u1.save()

u2 = User(org_id=1, user_id=2, first_name='Brad', last_name='Prille',email='Brad.Prille@impact123.com', idea_points=500, idea_points_awarded=0) 
u2.save()

u3 = User(org_id=1, user_id=3, first_name='Don', last_name='Watt',email='Don.Watt@impact123.com', idea_points=500, idea_points_awarded=0) 
u3.save()

u4 = User(org_id=1, user_id=4, first_name='Derek', last_name='Reiger',email='Derek.Reiger@impact123.com', idea_points=500, idea_points_awarded=0) 
u4.save()

User.objects.all()
