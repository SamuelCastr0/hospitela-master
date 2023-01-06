from django.db import models
from django.contrib.auth.models import AbstractUser


class HospitalUser(AbstractUser):
    is_attendant = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_medic = models.BooleanField(default=False)

    def set_user_occupation(self, occupation):
        if occupation == 1:
            self.is_attendant = True
        elif occupation == 2:
            self.is_attendant = True
            self.is_nurse = True
        elif occupation == 3:
            self.is_attendant = True
            self.is_nurse = True
            self.is_medic = True

    def __str__(self):
        return f'{self.username}'
