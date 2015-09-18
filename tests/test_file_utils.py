import unittest

from src.file_utils import FileUtils


class TestDuplicates(unittest.TestCase):
    def testMD5(self):
      self.assertEqual(FileUtils().md5("../test_files/test.txt"),
                       FileUtils().md5("../test_files/test_duplicate.txt"))

    def testCompareContent(self):
      self.assertTrue(FileUtils().contentEquals("../test_files/test.txt", "../test_files/test_duplicate.txt"))

    def testCompareContentVeryLarge(self):
      self.assertTrue(FileUtils().contentEquals("/Users/marcin/tmp/sample.txt", "/Users/marcin/tmp/sample.txt"))

    def testCompareContentWithMismatch(self):
      self.assertFalse(FileUtils().contentEquals("../test_files/test.txt", "../test_files/test2.txt"))

    def testCompareSizeWithMismatch(self):
      self.assertFalse(FileUtils().sizeEquals("../test_files/test.txt", "../test_files/test2.txt"))

    def testCompareSize(self):
      self.assertTrue(FileUtils().sizeEquals("../test_files/test.txt", "../test_files/test_duplicate.txt"))