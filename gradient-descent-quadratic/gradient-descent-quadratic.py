def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    for _ in range(steps):
        dfx = 2*a*x0 + b  
        x0 -= lr * dfx

    return x0