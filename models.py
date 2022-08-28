from django.contrib.auth.models import AbstractUser
from django.db import models


############################################################

class User(AbstractUser):
    pass

############################################################

class Category(models.Model):
    name = models.CharField(max_length = 64, blank = True)

    def __str__(self):
        return f"{self.name}"

############################################################

class Lot(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "authorUser")
    name = models.CharField(max_length = 128)
    description = models.CharField(max_length = 2048)
    bid = models.DecimalField(max_digits = 7, decimal_places = 2)
    urlimage = models.URLField(max_length = 512, blank = True)
    uploadimage = models.ImageField(upload_to ="uploads/", blank = True, default="uploads/default.jpg")    
    category = models.ManyToManyField(Category, blank = False) #, default = 10
    usersWhoAddToWatchlist = models.ManyToManyField(User, blank = True, related_name = "watchingUsers")
    statusActive = models.BooleanField(default = True)
    dirtyHack = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.id}: {self.name}"

#############################################################

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 500, blank = False)
    lot = models.ForeignKey(Lot, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.id}: {self.author} {self.comment} {self.lot}"

#############################################################

class Bids(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete = models.CASCADE)
    userBid = models.DecimalField(max_digits = 7, decimal_places = 2)

    def __str__(self):
        return f"{self.id}: {self.lot} {self.author} {self.userBid}"        
            
#############################################################

        
