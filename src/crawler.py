from os import listdir
from os.path import isfile, join, isdir, islink, realpath, abspath, relpath

from src.file_index import FileIndex, FileIndexEntry
from file_utils import FileUtils


class FSCrawler:
    file_utils=FileUtils()
    def build_index(self, path):
        #dir queue to check
        dir_queue=list()
        visited=set()
        dir_queue.append(path)
        file_index=FileIndex()
        file_utils=FileUtils()
        while dir_queue:
            path=dir_queue.pop(0)
            content = listdir(path)
            print("----"+path)
            for f in content:
                print(f)
                f_path = self.calculate_absolute_path(f, path)
                if f_path in visited:
                    continue
                if isdir(f_path):
                    dir_queue.append(f_path)
                    visited.add(f_path)
                elif isfile(f_path):
                    md5=file_utils.md5(f_path)
                    file_index.add(FileIndexEntry(md5,f_path))
                    visited.add(f_path)
        return file_index

    def calculate_absolute_path(self, f, path):
        f_path = join(path, f)
        if islink(f_path):
            f_path = realpath(f_path)
        f_path = abspath(f_path)
        return f_path

    #iterates over index containing md5 based duplicate candidates and map with actual duplicates.
    def get_duplicates(self, index):
        duplicates = {}
        for e in index.entries:
            dups_in_entry = self.compare_files(index.entries[e].files)
            duplicates.update(dups_in_entry)
        return duplicates


    #gets list of duplicate candidates, compare files and returns map representing groups of actual duplicates
    def compare_files(self, file_list):
        duplicates={}
        dont_check=set();
        for i in range(len(file_list)):
            print i

            if file_list[i] in dont_check:
                continue
            dont_check.add(file_list[i])
            for j in range(i+1, len(file_list)):
                are_equals = FSCrawler.file_utils.contentEquals(file_list[i], file_list[j])
                if are_equals:
                    if not duplicates.get(file_list[i]):
                        duplicates[file_list[i]]={file_list[i]}
                    duplicates[file_list[i]].add(file_list[j])
                    dont_check.add(file_list[j])
        return duplicates

