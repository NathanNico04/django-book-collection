from django.db import models
from django.contrib.auth.models import User


# Model Collection (Question 3)
class Collec(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


# Model Element (Question 12)
class Element(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField()
    collection = models.ForeignKey(
        Collec, on_delete=models.CASCADE, related_name="elements"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
