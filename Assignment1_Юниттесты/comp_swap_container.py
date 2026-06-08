
class CompSwapList:
    
    def __init__(self, data):
        self._data = list(data)
        self._comps = 0
        self._swaps = 0
    
    def less(self, i, j):
        self._comps += 1
        return self._data[i] < self._data[j]
    
    def swap(self, i, j):
        self._swaps += 1
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def reset_stats(self):
        self._comps = 0
        self._swaps = 0
    
    @property
    def comps(self):
        return self._comps
    
    @property
    def swaps(self):
        return self._swaps
    
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __iter__(self):
        return iter(self._data)
    
    def __repr__(self):
        return repr(self._data)