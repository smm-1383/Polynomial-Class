# Poly

Poly class is a class for doing simple things like add, subtract, multiply, divide, mode and derivative and applying division-mod(divmod) on polynomials.


## Usage

```python
from Poly import Poly

# make an instance
po = Poly('3*h**4-5h**3+h-2', 'h')

# returns derivative of po as a polynomial object
po.derivative()

# returns divided polynomial and its mod in a tuple
divmod(po, Poly('4x**2+2'))
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.