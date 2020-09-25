from django.db import models

class NutritionModel(models.Model):

    sl_no = models.CharField(null=True, blank=True, verbose_name="Sl no")
    sub_domain = models.CharField(null=True, blank=True,verbose_name="Sub-domain")
    indicators =models.TextField(null=True, blank=True,verbose_name="Indicators")
    national_indicator_reference =models.CharField(null=True, blank=True,max_length=10,verbose_name="National indicator reference")
    sector =models.CharField(null=True, blank=True,max_length=20,verbose_name="Sector")
    data_collab = models.CharField(null=True, blank=True,max_length=100,verbose_name="Ministry/ Agencies for data collaboration")
    variable_required =models.TextField(null=True, blank=True,verbose_name="Variable required")
    data_sources =models.CharField(null=True, blank=True,max_length=10,verbose_name="Data sources@")


    def __str__(self):
        return self.sl_no


