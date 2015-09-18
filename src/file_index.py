from src.exceptions import CustomException


class FileIndex:
    def __init__(self):
        self.entries={}

    def add(self, entry):
        existing_entry = self.entries.get(entry.md5)
        entry.merge(existing_entry)
        self.entries[entry.md5]=entry

    def get(self, md5):
        return self.entries.get(md5)




class FileIndexEntry:
    def __init__(self, md5, file_path):
        self.md5=md5
        self.files=[file_path]

    def merge(self, entry):
        if entry and entry.md5!=self.md5:
            raise CustomException("Mismatch of md5 in index entries: {0}!={1} ".format(self.md5, entry.md5))
        if entry:
            self.files.extend(entry.files)

