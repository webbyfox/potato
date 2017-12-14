from djangae.contrib.gauth.common.models import GaeAbstractBaseUser, GaeUserManager

class User(GaeAbstractBaseUser):
    objects = GaeUserManager()

    def __str__(self):
    	return self.email