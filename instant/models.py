from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(default=0)
    birth = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    ipv4 = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name

    @staticmethod
    def _bootstrap(count=300, gender='male'):
        from elizabeth import Generic
        g = Generic('en')
        for _ in range(count):
            user = User(full_name=g.personal.full_name(gender),
                        age=g.personal.age(),
                        birth=g.datetime.date(start=1980, end=2000, fmt='%Y-%m-%d'),
                        email=g.personal.email(),
                        ipv4=g.network.ip_v4(),
                        phone=g.personal.telephone(),
                        street=g.address.street_name(),
                        city=g.address.city()
                        )
            user.save()
