from django.db import models
import datetime
import uuid

RECURRENCE_CHOICES = [
    ('N', 'None'),
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly'),
    ('Y', 'Yearly')
]

DEPARTMENT_CHOICES = [
    ('AE', 'Aerospace Engineering'),
    ('BB', 'Biosciences and Bioengineering'),
    ('ChE', 'Chemical Engineering'),
    ('CH', 'Chemistry'),
    ('CE', 'Civil Engineering'),
    ('CSE', 'Computer Science & Engineering'),
    ('ES', 'Earth Sciences'),
    ('EE', 'Electrical Engineering'),
    ('ESE', 'Energy Science and Engineering'),
    ('ESED', 'Environmental Science and Engineering'),
    ('HSS', 'Humanities & Social Science'),
    ('IEOR', 'Industrial Engineering & Operations Research'),
    ('MA', 'Mathematics'),
    ('ME', 'Mechanical Engineering'),
    ('MM', 'Metallurgical Engineering & Materials Science'),  # Fixed duplicate
    ('PH', 'Physics'),
    ('IDC', 'Industrial Design Centre'),
    ('SOM', 'Shailesh J. Mehta School of Management'),
    ('Other', 'Other')
]

DEGREE_CHOICES = [
    ('B.Tech', 'B.Tech'),
    ('M.Tech', 'M.Tech'),
    ('PhD', 'PhD'),
    ('MS', 'MS'),
    ('MBA', 'MBA'),
    ('M.Des', 'M.Des'),
    ('M.Sc', 'M.Sc'),
    ('MA', 'MA'),
    ('B.Des', 'B.Des'),
    ('B.Sc', 'B.Sc'),
    ('BA', 'BA'),
    ('Other', 'Other')
]

BODY_CATEGORY_CHOICES = [
    ('Club', 'Club'),
    ('Tech Team', 'Tech Team'),
    ('Community', 'Community'),
    ('Others', 'Others')
]


class BodyCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, choices=BODY_CATEGORY_CHOICES, default='Club')

    def __str__(self):
        return self.name


class Body(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(BodyCategory, on_delete=models.CASCADE, related_name='bodies')
    contact_email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='')
    roll_number = models.CharField(max_length=20, default='', unique=True)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=100, default='CE')
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=100, default='B.Tech')
    body = models.ForeignKey(Body, on_delete=models.CASCADE, related_name='users', null=True, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    organiser = models.ForeignKey(Body, on_delete=models.CASCADE, related_name='events')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', null=True, blank=True)
    venue = models.TextField(max_length=20, null=True)
    start_time = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    end_time = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    recurrence = models.CharField(max_length=220, choices=RECURRENCE_CHOICES)  # Fixed field type
    recur_start = models.DateField(default=datetime.date.today, null=True, blank=True)
    recur_end = models.DateField(default=datetime.date.today, null=True, blank=True)

    def __str__(self):
        return self.title
