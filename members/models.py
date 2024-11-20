from django.db import models

class Member(models.Model):
    """ The class defines the model of members

    Args:
        models (Table): It's a table in our Database
    """
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        """This function return the firstname and lastname of a Member

        Returns:
            string: It returns the string of the member object
        """
        return f"{self.firstname} {self.lastname}"