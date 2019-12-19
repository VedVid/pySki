# -*- coding: utf-8 -*-


"""

Copyright (c) Tomasz "Ved" Nowakowski <toalak@gmail.com>


Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""


import country_list


# Data for small hills
SMALL_NAME = "small"
SMALL_K_MIN = 20
SMALL_K_MAX = 44
SMALL_K_USUAL = 35
SMALL_HS_MIN = 20
SMALL_HS_MAX = 49
SMALL_HS_AVERAGE = round((SMALL_HS_MIN + SMALL_HS_MAX) / 2)
# Data for medium hills
MEDIUM_NAME = "medium"
MEDIUM_K_MIN = 45
MEDIUM_K_MAX = 74
MEDIUM_K_USUAL = 65
MEDIUM_HS_MIN = 50
MEDIUM_HS_MAX = 84
MEDIUM_HS_AVERAGE = round((MEDIUM_HS_MIN + MEDIUM_HS_MAX) / 2)
# Data for normal hills
NORMAL_NAME = "normal"
NORMAL_K_MIN = 75
NORMAL_K_MAX = 99
NORMAL_K_USUAL = 90
NORMAL_HS_MIN = 85
NORMAL_HS_MAX = 109
NORMAL_HS_AVERAGE = round((NORMAL_HS_MIN + NORMAL_HS_MAX) / 2)
# Data for big hills
BIG_NAME = "big"
BIG_K_MIN = 100
BIG_K_MAX = 169
BIG_K_USUAL = 120
BIG_HS_MIN = 110
BIG_HS_MAX = 184
BIG_HS_AVERAGE = round((BIG_HS_MIN + BIG_HS_MAX) / 2)
# Data for huge hills
HUGE_NAME = "huge"
HUGE_K_MIN = 170
HUGE_K_MAX = 210
HUGE_K_USUAL = 200
HUGE_HS_MIN = 185
HUGE_HS_MAX = 220
HUGE_HS_AVERAGE = round((HUGE_HS_MIN + HUGE_HS_MAX) / 2)

# Hill sizes
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
