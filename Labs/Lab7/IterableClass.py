class IterableClass(object):
    """Ітерований клас для лабораторної 7"""
    def __init__(self, begin, end, step = 1):    
        if (begin < end and step > 0) or (begin > end and step < 0):            
            self._range = [i for i in range(begin, end, int(step))]
        elif begin > end:
            self._range = [i for i in range(begin, end, -1)]
        else:
            self._range = [i for i in range(begin, end)]
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._range):
            ret = self._range[self._index]
            self._index += 1
            return ret
        else:
            raise StopIteration
