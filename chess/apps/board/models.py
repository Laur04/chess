from django.db import models
from django.contrib.auth import get_user_model

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class Run(models.Model):
    id = models.AutoField(primary_key=True)
    submitting_user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    custom_name = models.CharField(max_length=50, blank=True, null=True)
    time_ran = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    input_image = models.ImageField(null=False, blank=False, upload_to="input_image", storage=gd_storage)
    method = models.IntegerField(null=False, blank=False)
    successful = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        if self.custom_name != "":
            return "{} ({} - {})".format(self.custom_name, self.id, self.submitting_user.username)
        else:
            return "Run {} ({} - {})".format(self.id, self.id, self.submitting_user.username)

    def display_str(self):
        if self.custom_name != "":
            return self.custom_name
        else:
            return "Run {}".format(self.id)

class HarrisCorners(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE)

    output_image = models.ImageField(null=False, blank=False, upload_to="HarrisCorners/output_image", storage=gd_storage)

    def __str__(self):
        return "Run {} - Harris Corners".format(self.run.id)
