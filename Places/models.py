from django.db import models

# Create your models here.

Categories =[
    ("Forts", "Forts"),
    ("Wildlife", "Wildlife"),
    ("Palaces", "Palaces"),
    ("Lakes", "Lakes"),
    ("Museum", "Museum"),
    ("Religious Places", "Religious Places"),
    ("Others", "Others")
]

Parking = [
    ("Have", "Have"),
    ("Don't have", "Don't have")
]

class TouristSpot(models.Model):
    id = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    fee = models.CharField(max_length=100)
    tollfreeno = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Maplink = models.CharField(max_length=1000, default="")
    timings = models.CharField(max_length=100)
    parking = models.CharField(max_length=30, choices=Parking, default="")
    category = models.CharField(max_length=30, choices=Categories, default=1)
    images = models.ImageField(upload_to='pics')
    

    def __str__(self):
        return self.name

class TravelAgencie(models.Model):
    id = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=100)
    firmname = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    contact_name = models.CharField(max_length=100, default="")
    contact_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    maplink = models.CharField(max_length=1000, default="")
    vehicle = models.CharField(max_length=100, default="")
    Facilities = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100)
    images = models.ImageField(upload_to='travelagentpics')


    def __str__(self):
        return self.firmname

class Contact(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name
    
    def contact(self):
        self.save()
    

class Comment(models.Model):
    place = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    comments = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def comment(self):
        self.save()

class Hotel(models.Model):
    place = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    distance = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(default=1)
    image = models.ImageField(upload_to='hotelpics')

    def __str__(self):
        return self.name