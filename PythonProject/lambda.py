#aAnonymous functions are functions without names.
# The anonymous functions are useful when you need to use them once.

(lambda x:
(x % 2 and 'odd' or 'even'))(3)

(lambda x: x * x)(3)

(lambda x, y, z: x + y + z)(1, 2, 3)

(lambda x, y, z=3: x + y + z)(1, 2)

(lambda x, y, z=3: x + y + z)(1, y=2)

(lambda *args: sum(args))(1,2,3)

(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)