from django.db import models


class ContactModel(models.Model):
    """
    Contact Model returns data back to the admin page
    information can be viewed.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Contact Model")

    def __str__(self):
        return f"Message {self.subject} from {self.first_name}"
