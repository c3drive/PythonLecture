import pytest

from power import power, times, divide


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8
    with pytest.raises(TypeError):
        power("3", "2")


def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6


# if文とelseのreturnがカバー
def test_divide():
    num1 = 4
    num2 = 2
    assert divide(num1, num2) == 2


# if文とif trueのreturnがカバー
def test_divide_zero():
    num1 = 4
    num2 = 0
    assert divide(num1, num2) is None


# install
# (venv) pythontest () :$ pip install pytest

# terminalで実行
# (venv) pythontest () :$ pytest tests/
# (venv) pythontest () :$ pytest tests/test_power_pytest.py
# (venv) pythontest () :$ pytest tests/test_power_pytest.py -v

# カバレッジを見る
# install
# (venv) pythontest () :$ pip install pytest-cov

# terminalで実行
# (venv) pythontest () :$ pip install pytest-cov

# report形式
# missingが網羅されなかった行を表示
# (venv) pythontest () :$ pytest tests/test_power_pytest.py --cov=power --cov-report=term-missing

# html形式でレポートを出力
# (venv) pythontest () :$ pytest tests/test_power_pytest.py --cov=power --cov-report=html
# -> /htmlcov/index.htmlができる

# xml形式で追記する(--cov-append）　cov-appendなしだとxmlが上書きされる。
# プロジェクトが大きく、１つのテスト実行で全てカバーできないような場合使う（ほとんどのプロジェクトが1つのxmlに対してテスト結果を追記していく）
# (venv) pythontest () :$ pytest tests/test_power_pytest.py --cov=power --cov-report xml --cov-append



