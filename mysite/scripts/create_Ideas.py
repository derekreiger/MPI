from mpi.models import Idea
import datetime

print("Creating ideas...")

i1 = Idea(user_id=1, idea_id=1, subject='idea 1', description='idea 1 desc', post_date=datetime.datetime.now(), deactive_date=datetime.datetime.now(), points=0) 
i1.save()

i2 = Idea(user_id=1, idea_id=2, subject='idea 2', description='idea 2 desc', post_date=datetime.datetime.now(), deactive_date=datetime.datetime.now(), points=0) 
i2.save()

i2 = Idea(user_id=3, idea_id=3, subject='idea 3', description='idea 3 desc', post_date=datetime.datetime.now(), deactive_date=datetime.datetime.now(), points=0) 
i2.save()

i2 = Idea(user_id=2, idea_id=4, subject='idea 4', description='idea 4 desc', post_date=datetime.datetime.now(), deactive_date=datetime.datetime.now(), points=0) 
i2.save()

i2 = Idea(user_id=4, idea_id=5, subject='idea 5', description='idea 5 desc', post_date=datetime.datetime.now(), deactive_date=datetime.datetime.now(), points=0) 
i2.save()

Idea.objects.all()
