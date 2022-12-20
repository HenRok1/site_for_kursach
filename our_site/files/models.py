from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length= 255, blank=False, null=False)
    file = models.FileField(upload_to= 'files/',null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name

