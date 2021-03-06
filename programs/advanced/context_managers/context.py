from ftplib import FTP

class Closer:
    '''A context manager to automatically close an object with a close method
    in a with statement.'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        try:
           self.obj.close()
        except AttributeError: # obj isn't closable
           print('Not closable.')
           return True # exception handled successfully



with Closer(FTP('ftp.somesite.com')) as conn:
        conn.dir()

conn.dir()

with Closer(int(5)) as i:
        i += 1

print(i)