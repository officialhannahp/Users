from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 120)
    age = models.IntegerField(max_length = 2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        s =  '\n'
        s += f'id: {self.id}\n'
        s += f'first_name: {self.first_name}\n'
        s += f'last_name: {self.last_name}\n'
        s += f'email: {self.email}\n'
        return s