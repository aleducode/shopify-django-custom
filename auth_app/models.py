from shopify_auth.models import AbstractShopUser
from django.utils import timezone

class AuthAppShopUser(AbstractShopUser):
    pass

    def save(self, *args, **kwargs):
        self.last_login = timezone.now()
        return super(AuthAppShopUser, self).save(*args, **kwargs)
        


