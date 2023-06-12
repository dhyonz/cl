from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Unit(models.Model):
    unit_Name = models.CharField(_("Unit Name"), max_length=10, default=None, blank=True, null=True)
    unit_Desc = models.CharField(_("Unit Description"), max_length=30, default=None, blank=True, null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['unit_Name'], name='unique_nameUnit')
        ]
    def __str__(self):
        return self.unit_Name