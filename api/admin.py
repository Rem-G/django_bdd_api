from django.contrib import admin
from .models import *

list_tables = [com_1968, com_1975, com_1982, com_1990, com_1999, com_2006, com_2011, com_2016]

for table in list_tables:
	admin.site.register(table)