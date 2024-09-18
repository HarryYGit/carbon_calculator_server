from django.db import models

# Create your models here.
## create carbon task model
## defin data to the task

class Task_Carbon(models.Model):

    # input factors

    #driving distance float
    distance = models.FloatField()

    # MPG (miles per gallon) of the car
    mpg = models.FloatField()

    # AFEC (average fuel efficiency coefficient)
    afec = models.FloatField()

    #emission factor (kg CO2 per gallon) default as 8.89
    emission_factor = models.FloatField(default=8.89)

    # output result
    result = models.FloatField(default=0.00)

    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emission calculation on {self.created_at}"

