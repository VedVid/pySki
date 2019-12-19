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
