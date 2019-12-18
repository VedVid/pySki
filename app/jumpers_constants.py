# -*- coding: utf-8 -*-


"""

Copyright 2019 Tomasz "Ved" Nowakowski <toalak@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""


# Player skill is in range between 0 and 100.
SKILL_MIN = 0
SKILL_MAX = 100
# 12-18 is junior, retires between 32 and 40;
# unusually, player can jump up to 50 birthday.
AGE_MIN = 12
AGE_MAX = 40
AGE_MAX_MAX = 50
AGE_ADULT = 18
AGE_RETIRE = 32
# Usually, players are between 165 and 190 cm height;
# but exceptions exists.
HEIGHT_MIN = 165
HEIGHT_MIN_MIN = 150
HEIGHT_MAX = 190
HEIGHT_MAX_MAX = 210
# Weight calculation is based on BMI;
# as usual, there is "usual" range and exceptions.
BMI_MIN = 21
BMI_MIN_MIN = 17
BMI_MAX = 24
BMI_MAX_MAX = 28
