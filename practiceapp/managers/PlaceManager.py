from django.db import models

class PlaceManager(models.Manager):

    def get_hitanshi(self):
        return super(PlaceManager,self).get_queryset().filter(name='hitanshi')

    def get_all(self):
        return super(PlaceManager,self).get_queryset().all()

    def create(self,**kwargs):
        kwargs.update({'address':'surat'})
        return super(PlaceManager,self).create(**kwargs)

