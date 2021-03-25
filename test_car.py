import unittest
from task11_2 import Car

car_1 = Car('BMW', '560', 2020, 120)
car_2 = Car('BMW', '560', 2020, -10)


class TestCar(unittest.TestCase):
    def test_increase_speeds(self):
        self.assertEqual(car_1.increase_speeds(), 125)

    def test_decrease_speed(self):
        self.assertEqual(car_1.decrease_speed(), 115)

    def test_stop(self):
        self.assertEqual(car_1.stop(), 0)

    def test_reversal_car(self):
        self.assertEqual(car_1.reversal_car(), -120)

    def test_clock(self):
        self.assertEqual(car_1.clock(), 120)

    def test_invalid(self):
        self.assertRaises(ValueError, car_2.decrease_speed)
        with self.assertRaises(ValueError):
            car_2.decrease_speed()


if __name__ == '__main__':
    unittest.main()
