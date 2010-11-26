from django.db import models
import unittest

class MyFuncTestCase(unittest.TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEqual(my_func(a, 0), 'larry')
        self.assertEqual(my_func(a, 10, 'curly')


"""
The following code is written to test the models
"""
from django.utils import unittest

import os

APP_LABEL = os.path.splitext(os.path.basename(__file__))[0]

os.environ["DJANGO_SETTINGS_MODULE"] = "django.conf.global_settings"
from django.conf import global_settings

global_settings.INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    APP_LABEL,
)
global_settings.DATABASE_ENGINE = "MySQL"
global_settings.DATABASE_NAME = ":memory:"

from django.core.management import sql
from django.db import models, connection

from django.core.management.color import no_style
STYLE = no_style()

def create_table(*models):
#    create all tables for the given models
    cursor = connection.cursor()
    def execute(statments):
        for statement in statments:
            cursor.execute(statement)

    for model in models:
        execute(connection.creation.sql_create_model(model. STYLE)[0])
        execute(connection.creation.sql_indexes_for_model(model, STYLE))
        execute(sql.custom_sql_for_model(model, STYLE))
        execute(connection.creation.sql_for_many_to_many(model, STYLE))
#End of tester code
"""
if __name__ == "__main__":
    print "- create the model tabels...",
    from django.core import management
    management.call_command('syncdb', verbosity=1, interactive=False)
    print "OK"


    create_table(School)

    instance = School(SchoolName="UCSC")
    print instance
    for field in instance._meta.fields:
      print field, field.SchoolName

    print instance._meta.pk

    print "-END -"
"""