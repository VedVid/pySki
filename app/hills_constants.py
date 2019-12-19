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
class SmallHill:
    name = "small"
    k_min = 20
    k_max = 44
    k_usual = 35
    hs_min = 20
    hs_max = 49
    hs_average = round((hs_min + hs_max) / 2)


# Data for medium hills
class MediumHill:
    name = "medium"
    k_min = 45
    k_max = 74
    k_usual = 65
    hs_min = 50
    hs_max = 84
    hs_average = round((hs_min + hs_max) / 2)


# Data for normal hills
class NormalHill:
    name = "normal"
    k_min = 75
    k_max = 99
    k_usual = 90
    hs_min = 85
    hs_max = 109
    hs_average = round((hs_min + hs_max) / 2)


# Data for big hills
class BigHill:
    name = "big"
    k_min = 100
    k_max = 169
    k_usual = 120
    hs_min = 110
    hs_max = 184
    hs_average = round((hs_min + hs_max) / 2)


# Data for huge hills
class HugeHill:
    name = "huge"
    k_min = 170
    k_max = 210
    k_usual = 200
    hs_min = 185
    hs_max = 220
    hs_average = round((hs_min + hs_max) / 2)


# Hill sizes
SIZES = (SmallHill.name, MediumHill.name, NormalHill.name, BigHill.name, HugeHill.name)

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
