# Linter
# Linterの種類
# 1.Stylistic Lint（Styleをチェック）
# import os, sys 例）1行で二つのモジュールをimportしている
# 2.Logic Lint
# import os, sys 例）importしているライブラリが使われていない

import os, sys
x =1
print           (x,y,z)

# ####################### pycodestyle(Stylistic Lint）元pep8
# (venv) style_guide () :$ pip install pycodestyle

# (venv) style_guide () :$ pycodestyle check_tool.py
# check_tool.py:8:10: E401 multiple imports on one line
# check_tool.py:9:4: E225 missing whitespace around operator
# check_tool.py:10:6: E211 whitespace before '('
# check_tool.py:10:6: E271 multiple spaces after keyword
# check_tool.py:10:19: E231 missing whitespace after ','
# check_tool.py:10:21: E231 missing whitespace after ','

# (venv) style_guide () :$ pycodestyle --show-source check_tool.py
# check_tool.py:8:10: E401 multiple imports on one line
# import os, sys
#          ^
# check_tool.py:9:4: E225 missing whitespace around operator
# x =1
#    ^
# check_tool.py:10:6: E211 whitespace before '('
# print           (x,y,z)
#      ^
# check_tool.py:10:6: E271 multiple spaces after keyword
# print           (x,y,z)
#      ^
# check_tool.py:10:19: E231 missing whitespace after ','
# print           (x,y,z)
#                   ^
# check_tool.py:10:21: E231 missing whitespace after ','
# print           (x,y,z)
#                     ^
#

# (venv) style_guide () :$ pycodestyle --show-pep8 check_tool.py
# check_tool.py:8:10: E401 multiple imports on one line
#     Place imports on separate lines.
#
#     Okay: import os\nimport sys
#     E401: import sys, os
#
#     Okay: from subprocess import Popen, PIPE
#     Okay: from myclas import MyClass
#     Okay: from foo.bar.yourclass import YourClass
#     Okay: import myclass
#     Okay: import foo.bar.yourclass
# （略）

# (venv) style_guide () :$ pycodestyle --statistics -qq check_tool.py
# 1       E211 whitespace before '('
# 1       E225 missing whitespace around operator
# 2       E231 missing whitespace after ','
# 1       E271 multiple spaces after keyword
# 1       E401 multiple imports on one line

# ####################### pyflakes（Logical Lint）
# (venv) style_guide () :$ pyflackes check_tool.py
#
# (venv) style_guide () :$ pyflakes check_tool.py
# check_tool.py:8:1 'os' imported but unused
# check_tool.py:8:1 'sys' imported but unused
# check_tool.py:10:20 undefined name 'y'
# check_tool.py:10:22 undefined name 'z'

# ####################### flake8（pycodestyleとpyflakesのラッパーライブラリ）
# (venv) style_guide () :$ pip install flake8

# (venv) style_guide () :$ flake8 check_tool.py
# check_tool.py:8:1: F401 'os' imported but unused
# check_tool.py:8:1: F401 'sys' imported but unused
# check_tool.py:8:10: E401 multiple imports on one line
# check_tool.py:9:4: E225 missing whitespace around operator
# check_tool.py:10:6: E271 multiple spaces after keyword
# check_tool.py:10:6: E211 whitespace before '('
# check_tool.py:10:19: E231 missing whitespace after ','
# check_tool.py:10:20: F821 undefined name 'y'
# check_tool.py:10:21: E231 missing whitespace after ','
# check_tool.py:10:22: F821 undefined name 'z'


# ####################### pylint（flake8より厳しいLinter）
# (venv) style_guide () :$ pip install pylint

# (venv) style_guide () :$ pylint check_tool.py
# ************* Module check_tool
# check_tool.py:92:0: C0305: Trailing newlines (trailing-newlines)
# check_tool.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# check_tool.py:8:0: C0410: Multiple imports on one line (os, sys) (multiple-imports)
# check_tool.py:9:0: C0103: Constant name "x" doesn't conform to UPPER_CASE naming style (invalid-name)
# check_tool.py:10:19: E0602: Undefined variable 'y' (undefined-variable)
# check_tool.py:10:21: E0602: Undefined variable 'z' (undefined-variable)
# check_tool.py:8:0: W0611: Unused import os (unused-import)
# check_tool.py:8:0: W0611: Unused import sys (unused-import)
#
# -------------------------------------
# Your code has been rated at -43.33/10


