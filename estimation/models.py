from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class User(models.Model):
  """base user model"""
  name = models.CharField(max_length=50)
  username = models.CharField(
    _('username'),
    max_length=20,
    unique=True,
  )
  phone = models.CharField(
      _('phone number'),
      validators=[RegexValidator(regex=r'^0[0-9]{10}$')],
      max_length=11,
      help_text='e.g. 01712345678',
      unique=True
  )
  email = models.EmailField(blank=True)
  is_active = models.BooleanField(_('active'), default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'username'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
    return self.name

class CSO(User):
  """cso model"""
  password = models.CharField(
    _('password'),
    max_length=50,
    validators=[RegexValidator(regex=r'^[a-zA-Z0-9]{8,}$')]
  )

  def __str__(self):
    return self.name

class Tag(models.Model):
  """tag model"""
  name = models.CharField(max_length=15)

  def __str__(self):
    return self.name

class Designer(User):
  """designer model"""
  salary = models.FloatField()
  category = models.CharField(max_length=1)
  tag = models.ManyToManyField(Tag)

  def __str__(self):
    return self.name

class Task(models.Model):
  """task model"""
  name = models.CharField(
    _('name'),
    max_length=50
  )
  
  REQUIRED_FIELDS = ['name']
  
  def __str__(self):
    return self.name

class Vendor(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(blank=True)
  contact_no = models.CharField(
    _('contact number'),
    validators=[RegexValidator(regex=r'^0[0-9]{10}$')],
    max_length=12,
    help_text='e.g. 01712345678',
    unique=True
  )
  address = models.CharField(max_length=100)
  category = models.CharField(max_length=1)

  REQUIRED_FIELDS = ['name']
  
  def __str__(self):
    return self.name

class Service(models.Model):
  name = models.CharField(
    max_length=100, unique=True
  )

  REQUIRED_FIELDS = ['name']

  def __str__(self):
    return self.name

class Estimation(models.Model):
  """estimation model"""
  # task thakte pare
  name = models.CharField(
    _("name"),
    max_length=50
  )
  description = models.CharField(max_length=1000)
  cso = models.ForeignKey(CSO, on_delete=models.CASCADE) # cso who created the estimation
  estimated_duration_months = models.IntegerField()
  estimated_cost = models.FloatField()
  designers = models.ManyToManyField(Designer)
  tags = models.ManyToManyField(Tag)
  vendors = models.ManyToManyField(Vendor)
  
  def __str__(self):
    return self.name

  
  