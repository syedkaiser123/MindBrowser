from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import re
from datetime import datetime
from django.contrib.auth.models import Group
from management.models import Manager


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str,
                            help="User Name")
        parser.add_argument('-p', '--password', type=str,
                            help="Password" )
        parser.add_argument('-f', '--first_name', type=str,
                            help="First Name" )
        parser.add_argument('-l', '--last_name', type=str,
                            help="Last Name" )
        parser.add_argument('-a', '--address', type=str,
                            help="Address" )
        parser.add_argument('-d', '--dob', type=str,
                            help="DOB" )
        parser.add_argument('-c', '--company', type=str,
                            help="Company" )

    def handle(self, *args, **options):
        username = options.get("username", None)
        password = options.get("password", None)
        first_name = options.get("first_name", None)
        last_name = options.get("last_name", None)
        address = options.get("address", None)
        dob = options.get("dob", None)
        company = options.get("company", None)

        if User.objects.filter(username=username).count():
            print("Username Already exist, please try another username")
        else:
            user = User.objects.create_user(username=username, password=password, email=None)
            if Group.objects.filter(name='Manager').count():
                user.group = Group.objects.get(name="Manager")
            else:
                user.group = Group.objects.create(name='Manager')
            if not Group.objects.filter(name='Employee').count():
                Group.objects.create(name='Employee')
            user_details = {
                'user': user,
                'first_name': first_name,
                'last_name': last_name,
                'address': address,
                'dob': dob,
                'company': company,
            }

            manager = Manager.objects.create(**user_details)
            if manager:
                print("Successfully created")
