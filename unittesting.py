import unittest
import dataloader as dl

class TestDataLoader(unittest.TestCase):
	def testFileExistsAndLoads(self):
		data = dl.loadData("numbers.txt");
		self.assertEqual(1, data[0]);

if __name__ == '__main__':
    unittest.main()