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


import country_list


# Data for small hills
SMALL_NAME = "small"
SMALL_K_MIN = 20
SMALL_K_MAX = 44
SMALL_K_USUAL = 35
SMALL_HS_MIN = 20
SMALL_HS_MAX = 49
# Data for medium hills
MEDIUM_NAME = "medium"
MEDIUM_K_MIN = 45
MEDIUM_K_MAX = 74
MEDIUM_K_USUAL = 65
MEDIUM_HS_MIN = 50
MEDIUM_HS_MAX = 84
# Data for normal hills
NORMAL_NAME = "normal"
NORMAL_K_MIN = 75
NORMAL_K_MAX = 99
NORMAL_K_USUAL = 90
NORMAL_HS_MIN = 85
NORMAL_HS_MAX = 109
# Data for big hills
BIG_NAME = "big"
BIG_K_MIN = 100
BIG_K_MAX = 169
BIG_K_USUAL = 120
BIG_HS_MIN = 110
BIG_HS_MAX = 184
# Data for huge hills
HUGE_NAME = "huge"
HUGE_K_MIN = 170
HUGE_K_MAX = 210
HUGE_K_USUAL = 200
HUGE_HS_MIN = 185
HUGE_HS_MAX = 220

SIZES = (SMALL_NAME, MEDIUM_NAME, NORMAL_NAME, BIG_NAME, HUGE_NAME)

COUNTRIES = dict(country_list.countries_for_language("en"))
# MAIN_COUNTRIES uses COUNTRIES data, with the same formatting.
MAIN_COUNTRIES = {
    "AT": "Austria",
    "CH": "Switzerland",
    "CZ": "Czechia",
    "DE": "Germany",
    "FI": "Finland",
    "NO": "Norway",
    "PL": "Poland",
    "SI": "Slovenia",
}
