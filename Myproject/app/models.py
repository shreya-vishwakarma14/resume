from django.db import models

# Create your models here.
from django.db import models

class Consigner(models.Model):
    name = models.CharField(max_length=255)
    gst_no = models.CharField(max_length=15)
    state_code = models.PositiveIntegerField()
    address = models.CharField(max_length=512)

    def __str__(self):
        return self.name

class Consignee(models.Model):
    name = models.CharField(max_length=255)
    gst_no = models.CharField(max_length=15)
    state_code = models.PositiveIntegerField()
    address = models.CharField(max_length=512)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    truck_no = models.CharField(max_length=15)
    driver_name = models.CharField(max_length=255)
    driver_address = models.CharField(max_length=512)
    contact_no = models.IntegerField()
    engine_no = models.CharField(max_length=30)
    chasis_no = models.CharField(max_length=30)
    dl_no = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=255)
    owner_address = models.CharField(max_length=512)
    owner_contact = models.CharField(max_length=15)
    owner_pan = models.CharField(max_length=10)

    def __str__(self):
        return self.truck_no

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True, editable=False, null=True, blank=True)
    from_field = models.CharField(max_length=255)
    to_field = models.CharField(max_length=255)
    consigner = models.ForeignKey(Consigner, on_delete=models.CASCADE)
    consignee = models.ForeignKey(Consignee, on_delete=models.CASCADE)
    nature_of_goods = models.CharField(max_length=255)
    weight = models.IntegerField()
    freight_rate = models.FloatField()
    freight_total = models.FloatField()
    toll_tax = models.FloatField()
    gr_sr_charges = models.FloatField()
    fooding = models.IntegerField()
    kata = models.CharField(max_length=30)
    gst = models.FloatField()
    advance = models.IntegerField()
    payable_amt = models.FloatField()
    e_way_bill_no = models.CharField(max_length=30)
    date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            # Auto-generate invoice_number with the prefix "nct-" and a unique identifier
            self.invoice_number = f'nct-{self.pk if self.pk else "new"}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.invoice_number} - {self.nature_of_goods}"