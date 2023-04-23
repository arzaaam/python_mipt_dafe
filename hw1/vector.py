from numbers import Integral, Real
from itertools import zip_longest
from functools import reduce
from array import array


class Vector:

    __components: array
    __repr_lim: int = 5

    def __init__(self, iterable):

        # ВАШ КОД
        k = None
        try:
            k = list(iter(iterable))
        except Exception:
            raise TypeError(f'{type(iterable).__name__} is not iterable; iterable object was expected;')

        try:
            for i in k:
                float(i)
        except Exception:
            raise TypeError(f'unsupported elements type; real numbers were expected;')

        self.__components = array('d', k)


    def __repr__(self):

        #ВАШ КОД
        vec_beg = 'Vector(['
        vec_mid = ''
        if len(self.__components) > self.__repr_lim:
            max_element = self.__repr_lim
            repr_end = ', ...])'
        else:
            max_element = len(self.__components)
            repr_end = '])'

        for i in range(max_element):
            vec_mid += f', {self.__components[i]}'

        vec_mid = vec_mid[2:] if len(vec_mid) > 2 else vec_mid
        vec_repr = vec_beg + vec_mid + repr_end

        return vec_repr
    def __str__(self):

        # ВАШ КОД
        vec_str = '('
        for i in self.__components:
            vec_str += f'{i}, '

        vec_str = vec_str[:-2] if len(vec_str) > 2 else vec_str
        vec_str += ')'

        return vec_str

    def __iter__(self):
        return iter(self.__components)

    def __len__(self):

        # ВАШ КОД
        return len(self.__components)

    def __abs__(self):

        # ВАШ КОД
        l2 = 0
        for i in self.__components:
            l2 += i**2

        return l2**0.5

    def __bool__(self):

        # ВАШ КОД
        if abs(self):
            return True

        return False

    def __getitem__(self, index):

        # ВАШ КОД
        if not(isinstance(index, int | slice)):
            raise TypeError(f'unsupport index type: {type(index).__name__}; Vector indices must be integers or slices;')

        try:
            a = self.__components[index]
        except Exception:
            raise IndexError('Vector index out of range;')

        if isinstance(index, slice):
            return Vector(self.__components[index])

        return self.__components[index]

    def __setitem__(self, index, value):

        # ВАШ КОД
        if not(isinstance(index, int | slice)):
            raise TypeError(f'unsupport index type: {type(index).__name__}; Vector indices must be integers or slices;')

        exception_check = self[index]

        if isinstance(index, int) and not(isinstance(value, Real)):
            raise TypeError(f'unexpected value type: {type(value).__name__}; real number was expected;')

        if isinstance(index, slice) and not(isinstance(value, Vector)):
            raise TypeError(f'unexpected value type: {type(value).__name__}; Vector was expected;')

        if isinstance(index, slice):
            self.__components[index] = value.__components
            return

        self.__components[index] = value

    def __eq__(self, other):

        # ВАШ КОД
        if not isinstance(other, Vector):
            return NotImplemented

        if len(other) != len(self):
            return False

        for i in range(len(self)):
            if other[i] != self[i]:
                return False

        return True

    def __neg__(self):
        
        # ВАШ КОД
        other = Vector(self)
        for i in range(len(other)):
            other[i] = -other[i]

        return other

    def __add__(self, other):

        # ВАШ КОД
        try:
            sum_pair = list(zip_longest(self, other, fillvalue=0))
            sum_vec = Vector([i[0] + i[1] for i in sum_pair])
        except TypeError:
            return NotImplemented

        return sum_vec

    def __radd__(self, other):
        
        # ВАШ КОД
        return self + other

    def __sub__(self, other):

        # ВАШ КОД
        return self + (-other)

    def __mul__(self, scalar):

        # ВАШ КОД
        if not isinstance(scalar, Real):
            return NotImplemented

        ret_vec = Vector([i * scalar for i in self])
        return ret_vec

    def __rmul__(self, scalar):

        # ВАШ КОД
        return self * scalar

    def __matmul__(self, other):

        # ВАШ КОД
        mul_scalar = 0
        try:
            sum_pair = list(zip_longest(self, other, fillvalue=0))
            for i in sum_pair:
                mul_scalar += i[0] * i[1]
        except TypeError:
            return NotImplemented

        return mul_scalar

    def __rmatmul__(self, other):

        # ВАШ КОД
        return self @ other

    def __truediv__(self, scalar):

        # ВАШ КОД
        return self * (1/scalar)
