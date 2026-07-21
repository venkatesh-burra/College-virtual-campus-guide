from django.db import models


class Course(models.Model):
    """Stores course details offered by QIS College."""

    course_name = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    annual_fee = models.DecimalField(max_digits=10, decimal_places=2)
    eligibility = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/', blank=True, null=True)

    class Meta:
        ordering = ['course_name']

    def __str__(self):
        return self.course_name
