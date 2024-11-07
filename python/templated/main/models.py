from django.db import models

# Create your models here.
class Order(models.Model):
    '''Model definition for Order.'''
    name = models.CharField(default='', max_length=100)
    email = models.CharField(default='', max_length=100)
    tell= models.CharField(default='', max_length=100)
    business = models.CharField(default='', max_length=100)
    service = models.CharField(default='', max_length=50)
    city = models.CharField(default='', max_length=50)
    communication_preference = models.CharField(default='', max_length=10)
    class Meta:
        '''Meta definition for Order.'''

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.service

class Contact(models.Model):
    '''Model definition for Contact.'''
    name = models.CharField(default='', max_length=100)
    email = models.CharField(default='', max_length=100)
    subject = models.CharField(default='', max_length=100)
    message = models.CharField(default='', max_length=1000)
    class Meta:
        '''Meta definition for Contact.'''

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.subject