from django.db import models

class Airport(models.Model):
    airport_code = models.CharField(max_length=10)
    duration = models.PositiveIntegerField(help_text="Duration from parent")

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    POSITION_CHOICES = (
        ('left', 'Left'),
        ('right', 'Right'),
    )
    position = models.CharField(
        max_length=5,
        choices=POSITION_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.airport_code
