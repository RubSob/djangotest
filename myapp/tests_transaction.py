from django.test import TransactionTestCase
from myapp.models import Animal

class AnimalTransactionTest(TransactionTestCase):
    def test_database_commit(self):
        a = Animal.objects.create(name="dog", sound="bark")
        self.assertTrue(Animal.objects.filter(name="dog").exists())