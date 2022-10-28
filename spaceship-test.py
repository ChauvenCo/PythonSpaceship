import unittest
from spaceship import *
from threading import Timer

class TestMethods(unittest.TestCase):
    def test_get_position(self):
        ship = Spaceship('Arcadia')
        self.assertEqual(ship.GetPosition(), [0, 0])

    def test_get_name(self):
        ship = Spaceship('Arcadia')
        self.assertEqual(ship.GetName(), 'Arcadia')

    def test_moving_spaceship(self):
        ship = Spaceship('Arcadia')
        self.assertEqual(ship.GetPosition(), [0, 0])
        ship.SetDirectionVector(2, 0)

        Timer(5.0, ship.Stop).start()
        ship.Start()
        self.assertEqual(ship.GetPosition(), [10, 0])


if __name__ == '__main__':
    unittest.main()
