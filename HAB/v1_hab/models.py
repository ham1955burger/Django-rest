from django.db import models
from django.utils import timezone

CATEGORY_CHOICES = (
    ('salary', '월급'),
    ('foodExpenses', '식비'),
    ('default', '기타'),
)

STATE_CHOICES = (
    ('receive', '입금'),
    ('pay', '출금'),
)

class HouseholdAccountBook(models.Model):
    date = models.DateField(default=timezone.now)
    price = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=10)
    category = models.CharField(choices=CATEGORY_CHOICES, default='default', max_length=10)
    priority = models.SmallIntegerField(default=0)
    memo = models.CharField(blank=True, max_length=100)

    class Meta:
        ordering = ('-priority'),
