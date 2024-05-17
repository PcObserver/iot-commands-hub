from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker

from users.models import User


class Command(BaseCommand):
    help = "Create a fake user and admin"

    @transaction.atomic
    def handle(self, *args, **options):
        faker = Faker("en_US")

        self.create_user(faker)


    def create_user(self, faker):
        if User.objects.all():
            return
        
        # Creates Staff user to log in on Django Admin
        User.objects.create_superuser(
            email="admin@admin.com",
            password="@Abc123456",
            name=faker.name(),
        )
        self.stdout.write(self.style.SUCCESS("Staff user created successfully"))

        # Creates normal user
        User.objects.create_user(
            email="user@user.com",
            password="@Abc123456",
            name=faker.name(),
        )
        self.stdout.write(self.style.SUCCESS("Normal user created successfully"))

