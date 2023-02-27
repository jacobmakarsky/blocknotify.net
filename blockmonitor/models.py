from django.db import models


class PhoneVerification(models.Model):
    phone = models.CharField(max_length=13)  # international numbers: 123-123-123-1234
    challenge = models.CharField(max_length=6)
    address = models.CharField(max_length=42)  # "0x" + 40 hex

    def __str__(self):
        return self.phone + ':' + self.challenge + ':' + self.address
