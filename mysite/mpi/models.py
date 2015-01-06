from django.db import models

class Org(models.Model):
    org_id  = models.IntegerField(primary_key=True)
    org_name = models.CharField(max_length=32)
    contest_start = models.DateField(null=True)
    contest_end= models.DateField(null=True)
    idea_budget = models.IntegerField(default=500)

    def __unicode__(self):
	return self.org_name

class User(models.Model):
    org = models.ForeignKey(Org)
    user_id = models.BigIntegerField(primary_key=True)
    # TODO Add username?
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    idea_points = models.IntegerField(default=500)
    idea_points_awarded = models.IntegerField(default=0)
    
    def __unicode__(self):
	return self.first_name + " " + self.last_name

class Idea(models.Model):
    user = models.ForeignKey(User)
    idea_id = models.BigIntegerField(primary_key=True)
    subject = models.CharField(max_length=64)
    description = models.CharField(max_length=2000)
    post_date = models.DateTimeField()
    deactive_date = models.DateTimeField()
    points = models.IntegerField(default=0)

    def __unicode__(self):
	return str(self.idea_id)
