from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker
import random

from users.models import User
from devices.models import Brand, Device, Action


class Command(BaseCommand):
    help = "Create fake Brand, Device and Action objects"

    @transaction.atomic
    def handle(self, *args, **options):
        faker = Faker("en_US")

        user = User.objects.first()

        self.create_brands(faker, user)
        self.create_devices(faker, user)
        self.create_actions(faker, user)


    def create_brands(self, faker, user):
        if Brand.objects.first():
            return

        brands = []
        
        for _ in range(40):
            company = faker.company()
            company_lower_case = company.lower().replace(' ', '_')
            prefix = f"{company_lower_case}_{random.randint(0, 100000)}"
            brands.append(Brand.objects.create(display_name=company, prefix=prefix))
        
        for brand in brands:
            user.contributions.add(brand)
            
        user.save()
        
        self.stdout.write(self.style.SUCCESS("Created brands successfully"))
        
    def create_devices(self, faker, user):
        if Device.objects.first():
            return
        
        devices = []
        
        for _ in range(40):
            device = faker.word()
            devices.append(Device.objects.create(display_name=device, parent_brand=Brand.objects.all().order_by("?").first()))
        
        for device in devices:
            user.contributions.add(device)
            
        user.save()
        
        self.stdout.write(self.style.SUCCESS("Created devices successfully"))
        
    def create_actions(self, faker, user):
        if Action.objects.first():
            return
        
        actions = []
        
        for _ in range(40):
            action = faker.word()
            
            fake_payload = {
                "switch": "On"
            }
            
            actions.append(Action.objects.create(name=action, parent_device=Device.objects.all().order_by("?").first(), payload=fake_payload))
        
        for action in actions:
            user.contributions.add(action)
            
        user.save()
        
        self.stdout.write(self.style.SUCCESS("Created actions successfully"))

