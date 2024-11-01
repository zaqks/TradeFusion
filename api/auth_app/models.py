from django.db import models
from django.utils.crypto import get_random_string

# user


class Wilaya(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} - {self.name}"


class CustomUser(models.Model):
    class UserType(models.TextChoices):
        CUSTOMER = "C", "Customer"
        OWNER = "O", "Owner"
        GUEST = "G", "Guest"

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13, null=True)

    password = models.CharField(null=True, max_length=64)

    last_logged = models.DateTimeField(auto_now=True)

    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.CUSTOMER,
    )

    name = models.CharField(null=True, max_length=64)
    surname = models.CharField(null=True, max_length=64)
    wil = models.ForeignKey(Wilaya, models.CASCADE, null=True)

    def is_auth(email, pwd):
        return CustomUser.objects.filter(
            email=email, password=make_password(pwd)
        ).exists()

    def __str__(self):
        return self.email


# session


class CustomSessionManager(models.Manager):
    def new_session(self, customer=None):
        # generate a unique session
        token = get_random_string(32)
        while self.filter(token=token).exists():
            token = get_random_string(32)
        #
        obj = self.model(customer=customer, token=token)
        obj.save()

        return obj

    def get_user_from_request(self, request_query):
        user = None
        try:
            # get the session first
            session = self.get_session_from_request(request_query)
            if session:
                user = session.customer
        except:
            pass

        return user

    def get_session_from_request(self, request_query):
        session = None
        try:
            # get the session first
            session = self.get(token=request_query["token"])
        except:
            pass

        return session

    def is_auth(self, request_query):
        auth = False

        try:
            auth = self.filter(token=request_query["token"]).exists()
        except:
            pass

        return auth


class CustomerSession(models.Model):
    customer = models.ForeignKey(CustomUser, models.CASCADE, null=True)
    token = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)

    objects = CustomSessionManager()
