class MultiArray:

    def __init__(self,*dimensions):
        assert len(dimensions) > 1, "The array must have 2 or more dimensions!"
        self._dims = dimensions

        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions must be > 0"
            size *= d

        self._elements = Array(size)
        self._factors = Array(len(dimensions))
        self._computeFactors()

    def numDims(self):
        return len(self._dims)

    def length(self, dim):
        assert dim > 0 and dim < len(self._dims), "Dimension component out of range"
        return len(self._dims[dim-1])

    def clear(self, value):
        self._elements.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "Invalid number of array subscripts"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript is out of range"
        return self._elements[index]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "Invalid number of array subscritps"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript is out of range"
        self._elements[index] = value

    def _computeIndex(self, idx):
        offset = 0
        for i in range(idx):
            offset += idx[i]*self._factors[i]
        assert offset <= len(self._elements)
        return offset


