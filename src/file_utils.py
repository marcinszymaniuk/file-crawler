import hashlib
import os

class FileUtils:

    def md5(self, fname):
        hash = hashlib.md5()
        with open(fname) as f:
            for chunk in iter(lambda: f.read(4096), ""):
                hash.update(chunk)
        return hash.hexdigest()

    def contentEquals(self, fname1, fname2):
        self.BUFFER_SIZE = 10 * 1024 * 1024
        with open(fname1) as f1:
           with open(fname2) as f2:
              while True:
                  bytes1 = f1.read(self.BUFFER_SIZE)
                  bytes2 = f2.read(self.BUFFER_SIZE)
                  if not bytes1 and not bytes2:
                    break
                  if not bytes1:
                      return False
                  if not bytes2:
                      return False
                  if bytes1 != bytes2:
                    return False
        return True

    def sizeEquals(self, fname1, fname2):
        statinfo1 = os.stat(fname1)
        statinfo2 = os.stat(fname2)
        return statinfo1.st_size==statinfo2.st_size