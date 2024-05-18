import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logs.file',
                    filemode='a',
                    format='ERROR! %(asctime)s:%(levelname)s%(message)s')

# try:
#     print(10/0)
# except BaseException as ex:
#     logging.exception(ex)

def division(a: int, b: int):
    if b == 0:
        return ZeroDivisionError
    if type(b) == str:
        return TypeError
    return a / b
