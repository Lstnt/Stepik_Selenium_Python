str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together:{str1}, then goes {str2}, and then {str3}")
actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")


def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()

