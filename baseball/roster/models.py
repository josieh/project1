from django.db import models

# Create your models here.

class Player(models.Model):
    number = models.IntegerField(max_length=2)
    name = models.CharField(max_length=50)
    imgurl = models.TextField(max_length = 700)
    action = models.TextField(max_length = 700)
    dominant_hand = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    height = models.CharField(max_length=3)
    weight = models.CharField(max_length=3)
    year = models.CharField(max_length=10)
    hometown = models.CharField(max_length=75)
    high_school = models.CharField(max_length=75)
    batting_avg = models.DecimalField(decimal_places=5, max_digits=5)
    gp_gs = models.CharField(max_length=7)
    at_bats = models.IntegerField(max_length=6)
    runs = models.IntegerField(max_length=6)
    hits = models.IntegerField(max_length=6)                                 
    doubles = models.IntegerField(max_length=6)
    homeruns = models.IntegerField(max_length=6)
    rbi = models.IntegerField(max_length=6)
    total_bases = models.IntegerField(max_length=6)
    slugging = models.DecimalField(decimal_places=5, max_digits=5)
    walks = models.IntegerField(max_length=6)
    strikeouts = models.IntegerField(max_length=6)
    on_base_percentage = models.DecimalField(decimal_places=5, max_digits=5)
    assists = models.IntegerField(max_length=6)
    errors = models.IntegerField(max_length=6)
    story = models.TextField (unique=False)
    
    
    class Meta(object):
        verbose_name_plural = "Players"
        ordering = ('number', 'name')
    
    def __unicode__(self):
        return U'%s | %s' %(self.name, self.number)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        
class Coach(models.Model):
    firstname = models.TextField(null=True)
    lastname = models.TextField(null=True)
    title = models.TextField(null=True)
    story = models.TextField(null=True)
    coaching_age = models.IntegerField(null=True, max_length=2)
    
    
    class Meta(object):
        verbose_name_plural = "Coaches"
        ordering = ('lastname','coaching_age')
    
    def __unicode__(self):
        return self.lastname
    
    def save(self, *args, **kwargs):
        self.lastname = self.lastname()
        super(Coach, self).save(*args, **kwargs)