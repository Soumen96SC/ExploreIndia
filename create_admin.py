from django.contrib.auth.models import User

user = User.objects.create_superuser(username="admin", password="admin", email="admin@gmail.com")
user.save()
