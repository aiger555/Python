import unittest
from practice import King, Feudal_lord, Baron, Peasant

class TESTIROV(unittest.TestCase):
    def setUp(self):
        self.k = King('Petr I', 45)
        self.f = Feudal_lord('Fedya', 40)
        self.b = Baron('Bairon', 35)
        self.p = Peasant('Pavel', 30)

    def test_action(self):
        s = self.b.action('Pavel', 'dig up the fields')
        self.assertEqual(s, None)