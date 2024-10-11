import unittest
import tests_12_3

objST = unittest.TestSuite()

objST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
objST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(objST)

import unittest
def skip_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_run(self):
        pass

    @skip_frozen
    def test_walk(self):
        pass

    @skip_frozen
    def test_challenge(self):
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_frozen
    def test_first_tournament(self):
        pass

    @skip_frozen
    def test_second_tournament(self):
        pass

    @skip_frozen
    def test_third_tournament(self):
        pass

if __name__ == '__main__':
    unittest.main()
