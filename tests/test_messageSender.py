import unittest
import complimentr


class TestMessageSender(unittest.TestCase):

  def test_random_compliments(self):
    compliment = complimentr.messageSender.get_random_compliment_from_list()
    print(compliment)
    self.assertIsNotNone(compliment)

if __name__ == '__main__':
    unittest.main()
