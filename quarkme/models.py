from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import JSONField
from django.utils import timezone

GENDER = (
        (u'Male', u'Male'),
        (u'Female', u'Female'),
    )
EXPERIENCE = (
    ('less than one year', 'less than one year'),
    ('one to three year', 'one to three year'),
    ('three to eight year', 'three to eight year'),
    ('greater than eight year', 'greater than eight year')
)
STATUS = (
    ('verified', 'verified'),
    ('unverified', 'unverified')
)


class Preferences(models.Model):
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
    subject = models.CharField(max_length=200, blank=False)
    Class = models.CharField(max_length=20, blank=False)
    boards = models.CharField(max_length=200, blank=False)
    prices = models.FloatField(blank=False)


class Student(models.Model):
    appuser = models.ForeignKey(User)
    addresses = ArrayField(models.CharField(max_length=200), blank=True)
    phone_number = PhoneNumberField(unique=True, blank=True)
    DOB = models.DateField(blank=True)
    gender = models.CharField(max_length=5, choices=GENDER, blank=True)
    education_info = JSONField(blank=True)
    """
    education_info = {"current_std": "", "board": "", "school_name": ""}
    """
    parent_contact_details = JSONField(blank=True)
    """
    parent_contact_details = {"contact": [{"name": "", "phone_number": ""}, {"name": "", "phone_number": ""}]}
    """


class AllotmentDetails(models.Model):
    booking_id = models.CharField(max_length=16,unique=True, blank=False)
    student = models.ForeignKey(Student)
    promo_code = models.CharField(max_length=50, blank=True)
    payment_info = JSONField(blank=False)
    """
    payment_info = {"transaction_number": "", "payment_mode": "", "amount": ""}
    transaction number will be filled after payment_status becomes True
    """
    payment_status = models.BooleanField(default=False)
    booking_confirmed = models.BooleanField(default=False)
    commision_rate = models.FloatField(blank=False)
    time_of_allotment = timezone.now()
    class_details = JSONField(blank=False)
    """
    class_details = {"start_time": "", "number_of_hours": "", "location": ""}
    """


class Tutor(models.Model):

    appuser = models.ForeignKey(User)
    addresses = ArrayField(models.CharField(max_length=200))
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    phone_number = PhoneNumberField(unique=True, blank=True)
    DOB = models.DateField(blank=True)
    gender = models.CharField(max_length=5, choices=GENDER, blank=True)
    experience = models.CharField(max_length=30, choices=EXPERIENCE, blank=True)
    educational_qualifications = JSONField(blank=True)
    occupation = JSONField(blank=True)
    """
    occupation = {"current_occupation": "example", "previous_occupation": ["example1", "example2"]}
    """
    rating = models.FloatField(default=0.0)
    no_of_hours_taught = models.FloatField(default=0.0)
    bank_details = JSONField(blank=True)
    """
    bank_details = {"accountnumber": "", "bank_name": "", "ifsc_code": ""}
    """
    total_earnings = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, default='unverified')
    bonus = models.FloatField(default=0.0)
    allotment_details = models.ManyToManyField(AllotmentDetails)
    preferences = models.ManyToManyField(Preferences)


class TutionCentre(models.Model):
    pass
