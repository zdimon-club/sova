from django.core.management.base import BaseCommand, CommandError
from city.models import City
cities = ['Kherson', 'Kiev', 'Nikolaev']

'''
for i in range(1,60)
    pass




'''

class Command(BaseCommand):
   
    
    def handle(self, *args, **options):

        print('Load cities')
        City.objects.all().delete()
        for item in cities:
            c = City()
            c.name = item
            c.save()
            print('Saving...%s' % item)
        