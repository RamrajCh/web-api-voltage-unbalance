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
        return round(float(self.voltage_y) * float(self.current_y), 4)
    
    @property
    def power_r(self):
        return round(float(self.voltage_r) * float(self.current_r), 4)
    
    @property
    def power_b(self):
        return round(float(self.voltage_b) * float(self.current_b), 4)

    @property
    def error(self):
        max_v = max(float(self.voltage_r), float(self.voltage_y), float(self.voltage_b))
        min_v = min(float(self.voltage_r), float(self.voltage_y), float(self.voltage_b))
        return (max_v - min_v) > 15


    def __str__(self):
        return f"Parameter value for {self.created.strftime('%Y-%m-%d %H:%M:%S')}"