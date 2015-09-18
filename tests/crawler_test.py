import unittest
from os.path import isfile, join, isdir, islink, realpath, abspath, relpath

from src.crawler import FSCrawler
from src.file_index import FileIndex, FileIndexEntry


class CrawlerTest(unittest.TestCase):
    def test_build_index_f1(self):
        index = FSCrawler().build_index("../test_files")
        print(index)

        entry = index.get('008cc01fbdd6007b55339634f182d738')
        self.assertEquals(2, len(entry.files))
        files=sorted(entry.files)
        file1 = files[0]
        file2 = files[1]
        self.assertEquals('../test_files/dir2/subdir1/f1_copy.txt',relpath(file2))
        self.assertEquals('../test_files/dir1/subdir1/f1.txt',relpath(file1))

    def test_build_index_f2(self):
        index = FSCrawler().build_index("../test_files")
        print(index)

        entry = index.get('ea6d6de3d75edc82f3429929ef9cb585')
        self.assertEquals(3, len(entry.files))
        files=sorted(entry.files)
        file1 = files[0]
        file2 = files[1]
        file3 = files[2]
        self.assertEquals('../test_files/dir1/subdir1/f2.txt',relpath(file1))
        self.assertEquals('../test_files/dir1/subdir2/f2_copy.txt',relpath(file2))
        self.assertEquals('../test_files/dir2/subdir1/f2_copy.txt',relpath(file3))

    def test_build_index_f3(self):
        index = FSCrawler().build_index("../test_files")
        print(index)

        entry = index.get('22624e3ee8c4cddaa8f7494a8a098ed6')
        self.assertEquals(1, len(entry.files))
        file1 = entry.files[0]
        self.assertEquals('../test_files/dir2/subdir1/f3.txt',relpath(file1))

    def test_compare_files(self):
        duplicates = FSCrawler().compare_files(['../test_files/dir1/subdir1/f2.txt','../test_files/dir1/subdir2/f2_copy.txt', '../test_files/dir1/subdir1/f1.txt'])
        expected = {
                    '../test_files/dir1/subdir1/f2.txt': {'../test_files/dir1/subdir1/f2.txt', '../test_files/dir1/subdir2/f2_copy.txt'}
        }

        self.assertEquals(expected, duplicates)

    def test_get_duplicates(self):
        index = FileIndex()
        duplicates = 'md5_duplicates'
        non_duplicates = 'md5_non_duplicates'
        index.add(FileIndexEntry(duplicates, '../test_files/dir1/subdir1/f2.txt'))
        index.add(FileIndexEntry(duplicates, '../test_files/dir1/subdir2/f2_copy.txt'))
        index.add(FileIndexEntry(duplicates, '../test_files/dir1/subdir1/f1.txt'))
        index.add(FileIndexEntry(duplicates, '../test_files/dir2/subdir1/f1_copy.txt'))
        index.add(FileIndexEntry(non_duplicates, '../test_files/test_duplicate.txt'))
        index.add(FileIndexEntry(non_duplicates, '../test_files/dir2/subdir1/f3.txt'))

        index_with_duplicates = FSCrawler().get_duplicates(index)
        print(index_with_duplicates)

        expected=\
            {'../test_files/dir2/subdir1/f1_copy.txt': {'../test_files/dir1/subdir1/f1.txt', '../test_files/dir2/subdir1/f1_copy.txt'},
             '../test_files/dir1/subdir2/f2_copy.txt':  {'../test_files/dir1/subdir1/f2.txt', '../test_files/dir1/subdir2/f2_copy.txt'}
            }

        self.assertEquals(expected, index_with_duplicates)



