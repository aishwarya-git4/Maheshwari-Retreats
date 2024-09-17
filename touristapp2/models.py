from django.db import models
from django.forms import model_to_dict
import json
import datetime
class Storage(models.Model):
    name=models.CharField(max_length=30,null=False,blank=False)
    place=models.CharField(max_length=30,null=False,blank=False)
    img=models.ImageField(upload_to='static/img')
    
class Membershipmodel(models.Model):
    COUNTRY_CHOICES=(('India','India'),('Outside India','Outside India'))
    name=models.CharField(max_length=30,null=False,blank=False)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    country=models.CharField(max_length=20,choices=COUNTRY_CHOICES,default='India')
    special_request=models.TextField(blank=False,null=False)

class Bookingmodel(models.Model):
    LOCATION_CHOICES=(('Janjehli Resort','Janjehli Resort'),('Kandaghat Shimla Resort','Kandaghat Shimla Resort'),
                      ('Kanatal Resort','Kanatal Resort'),('Mussoorie Resort','Mussoorie Resort'))
    PERSONS_CHOICES=((1,1),(2,2),(3,3),(4,4))
    MEMBERSHIP_CHOICES=(('Yes','Yes'),('No','No'))
    ROOM_CHOICES=(('S','Studio Apartment'),('1','1-Bedroom Apartment'),('2','2-Bedroom Apartment'))
    name=models.CharField(max_length=30,null=False,blank=False)
    email=models.EmailField()
    check_in_date=models.CharField(max_length=30,null=False,blank=False)
    check_out_date=models.CharField(max_length=30,null=False,blank=False)
    destination=models.CharField(max_length=30,choices=LOCATION_CHOICES,null=False,blank=False)
    no_of_persons=models.IntegerField(choices=PERSONS_CHOICES,null=False,blank=False)
    have_you_availed_membership=models.CharField(max_length=30,choices=MEMBERSHIP_CHOICES,null=False,blank=False)
    type_of_room=models.CharField(max_length=30,choices=ROOM_CHOICES,null=False,blank=False)
    room_num=models.IntegerField(null=False,blank=False,default=0)
    '''def to_json(self):
        data = model_to_dict(self)
        data['check_in_date_and_time']=self.check_in_date_and_time.isoformat()
        data['check_out_date_and_time']=self.check_out_date_and_time.isoformat()
        return json.dumps(data)'''

class Roomsmodel(models.Model):
    name=models.CharField(max_length=30,null=False)
    studio=models.IntegerField()
    onebed=models.IntegerField()
    twobed=models.IntegerField()

class Feedbackmodel(models.Model):
    name=models.TextField(max_length=100,null=False,blank=False)
    home=models.TextField(max_length=100,null=False,blank=False,default='Velliangiri Hills,Coimbatore')
    feedback=models.TextField(max_length=300)
    
                         

# Create your models here.
