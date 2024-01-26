from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )
    # Check this CODE!
    # Calculate total sum of pledges for a project using a property
    @property
    def total_amount(self):
        result = 0
        for each_pledge in self.pledges:
            result += each_pledge.amount
        return result


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )

# class Comment(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="comments")
#     body = models.TextField()
#     author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name="comments")
#     visible = models.BooleanField(default=True)