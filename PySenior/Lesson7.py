class Calculator:
    denominator: int
    __name = 'Calculator'
    def __init__(self, value):
        self.denominator = value

    def __str__(self):
        return f'calculator has {self.denominator}'

    @staticmethod
    def show_info(txt: str):
        print(f'{txt} {Calculator.__name}')

    def __call__(self, numerator):
        return f'{numerator}/{self.denominator} = {numerator / self.denominator}'


calc = Calculator(2)
print(calc)
print(calc(5))


def calculation(symbol: str):
    def operation(a: int, b: int) -> str:
        return f'{a} {symbol} {b} = {a / b}'
    return operation


Calculator.show_info('Hello')
divide = calculation('/')
msg_result = divide(5, 2)
print(msg_result)
