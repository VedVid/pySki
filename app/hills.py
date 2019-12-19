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


import random

from . import hills_constants as hc


class Hill:
    def __init__(self, country, city, size, k, hs):
        self.country = country
        self.city = city
        self.size = size
        self.k = k
        self.hs = hs
        self._normalize()

    def _normalize(self):
        if not self._country_exists():
            self.country = random.choice(list(hc.MAIN_COUNTRIES.values()))
        # Package for choosing city in specific country would help...
        if not self.city:
            self.city = "Unknown city"
        # Below: check hill size and k-point.
        if self.size not in hc.SIZES:
            self.size = hc.BIG_NAME  # Create a big hill by default.
        if self.size == hc.SMALL_NAME:
            if self.k < hc.SMALL_K_MIN:
                self.k = hc.SMALL_K_MIN
            elif self.k > hc.SMALL_K_MAX:
                self.k = hc.SMALL_K_MAX
            if self.hs < hc.SMALL_HS_MIN:
                self.hs = hc.SMALL_HS_MIN
            elif self.hs > hc.SMALL_HS_MAX:
                self.hs = hc.SMALL_HS_MAX
        elif self.size == hc.MEDIUM_NAME:
            if self.k < hc.MEDIUM_K_MIN:
                self.k = hc.MEDIUM_K_MIN
            elif self.k > hc.MEDIUM_K_MAX:
                self.k = hc.MEDIUM_K_MAX
            if self.hs < hc.MEDIUM_HS_MIN:
                self.hs = hc.MEDIUM_HS_MIN
            elif self.hs > hc.MEDIUM_HS_MAX:
                self.hs = hc.MEDIUM_HS_MAX
        elif self.size == hc.NORMAL_NAME:
            if self.k < hc.NORMAL_K_MIN:
                self.k = hc.NORMAL_K_MIN
            elif self.k > hc.NORMAL_K_MAX:
                self.k = hc.NORMAL_K_MAX
            if self.hs < hc.NORMAL_HS_MIN:
                self.hs = hc.NORMAL_HS_MIN
            elif self.hs > hc.NORMAL_HS_MAX:
                self.hs = hc.NORMAL_HS_MAX
        elif self.size == hc.BIG_NAME:
            if self.k < hc.BIG_K_MIN:
                self.k = hc.BIG_K_MIN
            elif self.k > hc.BIG_K_MAX:
                self.k = hc.BIG_K_MAX
            if self.hs < hc.BIG_HS_MIN:
                self.hs = hc.BIG_HS_MIN
            elif self.hs > hc.BIG_HS_MAX:
                self.hs = hc.BIG_HS_MAX
        elif self.size == hc.HUGE_NAME:
            if self.k < hc.HUGE_K_MIN:
                self.k = hc.HUGE_K_MIN
            elif self.k > hc.HUGE_K_MAX:
                self.k = hc.HUGE_K_MAX
            if self.hs < hc.HUGE_HS_MIN:
                self.hs = hc.HUGE_HS_MIN
            elif self.hs > hc.HUGE_HS_MAX:
                self.hs = hc.HUGE_HS_MAX

    def _country_exists(self):
        for _, v in hc.COUNTRIES:
            if self.country == v:
                return True
        return False
