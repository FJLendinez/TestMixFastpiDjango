from django.db import models

from users import password as pwd


class UserModel(models.Model):
    username = models.CharField(primary_key=True, max_length=40)
    full_name = models.CharField(max_length=250)
    location = models.TextField()
    password = models.CharField(max_length=128)

    is_admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if getattr(self, '_password', None):
            self.password = pwd.get_password_hash(self._password)
            delattr(self, '_password')
        return super(UserModel, self).save(*args, **kwargs)

    @staticmethod
    def login(username, password):
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            # In order to avoid Timing attack
            pwd.get_password_hash(password)
            return None

        verified, updated_password_hash = pwd.verify_and_update_password(
            password, user.password
        )
        if not verified:
            return None
        return user

    @staticmethod
    def register(username, password):
        user = UserModel(username=username)
        user._password = password
        user.save()
        return user