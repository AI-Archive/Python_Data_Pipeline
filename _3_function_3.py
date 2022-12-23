# 1 파라미터가 없는 함수
def func1():
    """ 1 파라미터가 없는 함수 """
    print("파라미터를 받지 않은 함수")

def func2(param1):
    """ 2 파라미터가 있는 함수 """
    print(param1)


def func3():
    """ 3 반환값이 있는 함수 """
    print("반환값이 있는 함수")
    return
    print("끝")

def func4(param1, param2='Python'):
    """ 4 기본 인자값이 정의된 파라미터 """
    print(param1, param2)
    return f'{param1} {param2}'

# def func5(param1='Python', param2):
#     """ 5 에러 : 기본 인자가 정의된 파라미터는 
#           기본인자가 없는 파라미터 정의 후에 정의되야 함 """

