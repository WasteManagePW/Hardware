from django.db import models

class Sensor(models.Model):
    latitude = models.FloatField(default=12.34)
    longitude = models.FloatField(default=56.78)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"lat:{self.latitude}:long:{self.longitude}:city:{self.city}"

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"value:{self.value}:timestamp:{self.timestamp}"
