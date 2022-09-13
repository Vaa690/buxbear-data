from django.db import models


class User(models.Model):

    id = models.BigAutoField(primary_key=True)
    email = models.TextField(db_index = True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    is_staff = models.BooleanField(blank=True, null=True, default=False)