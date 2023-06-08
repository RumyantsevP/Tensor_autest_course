
# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните
#
import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

# Создаем тест с параметрами, используя @pytest.mark.parametrize
@pytest.mark.parametrize('args, result',
                         [pytest.param((6, 2), 3, marks=pytest.mark.smoke),  # Маркируем набор данных как "smoke"
                         ((0, 5), 0),
                         pytest.param(('a', 9), 'TypeError', marks=pytest.mark.skip('bad test')),  # Скипаем набор данных
                         ((6, -2), -3),
                         ((10, 0), 'division by zero')])
def test_division(args, result):
    try:
        assert all_division(*args) == result
    except Exception as err:
        assert err.args[0] == result

