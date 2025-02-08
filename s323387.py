import numpy as np

def f0(x: np.ndarray) -> np.ndarray:
    return np.minimum(np.add(np.tanh(np.tanh(np.cosh(1.11997858020315))), np.add(np.negative(x[1]), np.add(np.square(0.6528258878453492), x[0]))), np.add(np.negative(np.remainder(np.negative(x[1]), np.multiply(1.7584125144807357, x[1]))), np.add(x[0], np.multiply(x[1], np.tanh(1.7319312973914491)))))

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
    return np.add(np.multiply(np.multiply(np.cosh(np.add(-2.6000121306461272, -3.2150906456657626)), np.multiply(np.add(x[2], x[2]), np.negative(x[0]))), np.multiply(x[1], np.subtract(np.exp(5.560625554341413), np.cosh(x[0])))), np.multiply(np.multiply(np.square(-4.943296862710281), x[0]), np.square(np.exp(5.369873197780641))))

def f3(x: np.ndarray) -> np.ndarray:
    return np.add(np.multiply(np.multiply(-4.545991072645782, np.cos(-1.166098590091753)), np.subtract(np.add(x[2], np.exp(x[1])), np.absolute(np.cosh(x[1])))), np.add(np.subtract(np.negative(np.multiply(x[1], 2.055937107636824)), np.add(-4.804168082064881, x[2])), np.add(np.cosh(np.divide(x[0], -1.0814122259190357)), np.subtract(np.absolute(x[0]), np.remainder(x[1], -4.562096723325096)))))

def f4(x: np.ndarray) -> np.ndarray:
    return np.add(np.add(np.add(np.sin(np.cos(x[1])), np.cos(np.minimum(x[1], x[1]))), np.add(np.cos(x[1]), np.cos(x[1]))), np.add(np.add(np.cos(np.subtract(x[1], 0.010079400223165003)), np.cos(x[1])), np.subtract(np.sinh(np.cos(x[1])), np.add(-3.8176015332518403, np.power(0.5905406461535465, 1.1707846494319254)))))

def f5(x: np.ndarray) -> np.ndarray:
    return np.multiply(-6.027046665958086e-15, np.power(np.add(np.power(np.divide(x[0], 0.5130358016128974), np.arctan(5.079953468300546)), np.power(0.06510063674299789, np.cos(x[1]))), np.add(np.multiply(np.subtract(5.061849862519098, x[1]), 0.06510063674299789), x[1])))

def f6(x: np.ndarray) -> np.ndarray:
    return np.add(np.add(x[1], np.maximum(np.subtract(x[1], 0.0715542326500378), np.negative(4.120292756672327))), np.negative(np.subtract(np.minimum(x[0], 4.155045641154721), np.arctan(np.subtract(x[0], x[1])))))

def f7(x: np.ndarray) -> np.ndarray:
    return np.multiply(np.exp(np.sin(np.cosh(np.minimum(1.8537698499292565, x[1])))), np.power(np.exp(x[1]), np.add(np.tanh(np.maximum(-1.3819979974952137, x[0])), np.minimum(np.maximum(-0.3072630359351072, x[1]), np.maximum(-1.6618842110811194, x[0])))))

def f8(x: np.ndarray) -> np.ndarray:
    return np.multiply(np.add(np.sinh(np.negative(x[5])), np.sinh(np.cbrt(np.square(x[4])))), np.add(np.multiply(np.multiply(-5.225190448882802, np.add(5.7514722132214136, -0.15288156941239528)), np.add(5.7514722132214136, np.cos(x[5]))), np.multiply(np.absolute(np.add(0.7098169053893928, x[5])), np.tan(np.log(5.393727864805511)))))