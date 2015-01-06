from mpi.models import Org

print("Creating orgs ...")

o1 = Org(org_id=1, org_name='Impact', idea_budget=500) 
o1.save()

o2 = Org(org_id=2, org_name='SAP', idea_budget=100) 
o2.save()

o3 = Org(org_id=3, org_name='Sybase', idea_budget=50) 
o3.save()

Org.objects.all()
