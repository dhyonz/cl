from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from units.models import Unit

# Create your models here.

class PreventiveMaintenance(models.Model):
    wo_Number = models.CharField(_('WO Number'), max_length=20, default=None, blank=True, null=True)
    pvm_Number = models.CharField(_('Preventive Maintenance Number'), max_length=20, default=None, blank=True, null=True)
    unit_Maintenance = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    insp_Date = models.DateField(_('Inspection Date'), null=True, blank=True)
    pic = models.ForeignKey(User, related_name='PIC', on_delete=models.CASCADE, blank=True, null=True)
    crew_1 = models.ForeignKey(User, related_name='Crew1', on_delete=models.CASCADE, blank=True, null=True)
    crew_2 = models.ForeignKey(User, related_name='Crew2', on_delete=models.CASCADE, blank=True, null=True)
    crew_3 = models.ForeignKey(User, related_name='Crew3', on_delete=models.CASCADE, blank=True, null=True)
    ### Values
    nox = models.FloatField(_('NOx'), default=None, blank=True, null=True)
    nox_Remark = models.CharField(_('NOx Remark'), max_length=50, default=None, blank=True, null=True)
    so2 = models.FloatField(_('SO2'), default=None, blank=True, null=True)
    so2_Remark = models.CharField(_('SO2 Remark'), max_length=50, default=None, blank=True, null=True)
    co2 = models.FloatField(_('CO2'), default=None, blank=True, null=True)
    co2_Remark = models.CharField(_('CO2 Remark'), max_length=50, default=None, blank=True, null=True)
    co = models.FloatField(_('CO'), default=None, blank=True, null=True)
    co_Remark = models.CharField(_('CO Remark'), max_length=50, default=None, blank=True, null=True)
    o2 = models.FloatField(_('O2'), default=None, blank=True, null=True)
    o2_Remark = models.CharField(_('O2 Remark'), max_length=50, default=None, blank=True, null=True)
    dust = models.FloatField(_('Dust'), default=None, blank=True, null=True)
    dust_Remark = models.CharField(_('Dust Remark'), max_length=50, default=None, blank=True, null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['wo_Number'], name='unique_woNumber'),
            models.UniqueConstraint(fields=['pvm_Number'], name='unique_pvmNumber'),
        ]
    def __str__(self):
        return self.wo_Number