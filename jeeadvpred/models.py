from django.db import models

# Create your models here.
class rank(models.Model):
    institute_name = models.CharField(max_length=200)
    branch_name    = models.CharField(max_length=200)
    allotted_quota = models.CharField(max_length=20)
    category       = models.CharField(max_length=200)
    seat_pool      = models.CharField(max_length=200)
    opening_rank   = models.IntegerField()
    closing_rank   = models.IntegerField()
  
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.institute_name, self.branch_name, self.allotted_quota,self.category, self.seat_pool, self.opening_rank, self.closing_rank)   

