from django.db import models

# Create your models here.

class Parameter(models.Model):
    voltage_r = models.CharField(max_length=10)
    voltage_y = models.CharField(max_length=10)
    voltage_b = models.CharField(max_length=10)
    current_r = models.CharField(max_length=10)
    current_y = models.CharField(max_length=10)
    current_b = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Parameters"
        ordering = ('-created',)

    @property
    def power_y(self):
        return float(self.voltage_y) * float(self.current_y)
    
    @property
    def power_r(self):
        return float(self.voltage_r) * float(self.current_r)
    
    @property
    def power_b(self):
        return float(self.voltage_b) * float(self.current_b)

    #@property
    # def error(self):


    def __str__(self):
        return f"Parameter value for {self.created.strftime('%Y-%m-%d %H:%M:%S')}"