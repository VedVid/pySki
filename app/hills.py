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
from . import jump_generation_constants as jgc


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
            self.size = hc.BigHill.name  # Create a big hill by default.
        if self.size == hc.SmallHill.name:
            if self.k < hc.SmallHill.k_min:
                self.k = hc.SmallHill.k_min
            elif self.k > hc.SmallHill.k_max:
                self.k = hc.SmallHill.k_max
            if self.hs < hc.SmallHill.hs_min:
                self.hs = hc.SmallHill.hs_min
            elif self.hs > hc.SmallHill.hs_max:
                self.hs = hc.SmallHill.hs_max
        elif self.size == hc.MediumHill.name:
            if self.k < hc.MediumHill.k_min:
                self.k = hc.MediumHill.k_min
            elif self.k > hc.MediumHill.k_max:
                self.k = hc.MediumHill.k_max
            if self.hs < hc.MediumHill.hs_min:
                self.hs = hc.MediumHill.hs_min
            elif self.hs > hc.MediumHill.hs_max:
                self.hs = hc.MediumHill.hs_max
        elif self.size == hc.NormalHill.name:
            if self.k < hc.NormalHill.k_min:
                self.k = hc.NormalHill.k_min
            elif self.k > hc.NormalHill.k_max:
                self.k = hc.NormalHill.k_max
            if self.hs < hc.NormalHill.hs_min:
                self.hs = hc.NormalHill.hs_min
            elif self.hs > hc.NormalHill.hs_max:
                self.hs = hc.NormalHill.hs_max
        elif self.size == hc.BigHill.name:
            if self.k < hc.BigHill.k_min:
                self.k = hc.BigHill.k_min
            elif self.k > hc.BigHill.k_max:
                self.k = hc.BigHill.k_max
            if self.hs < hc.BigHill.hs_min:
                self.hs = hc.BigHill.hs_min
            elif self.hs > hc.BigHill.hs_max:
                self.hs = hc.BigHill.hs_max
        elif self.size == hc.HugeHill.name:
            if self.k < hc.HugeHill.k_min:
                self.k = hc.HugeHill.k_min
            elif self.k > hc.HugeHill.k_max:
                self.k = hc.HugeHill.k_max
            if self.hs < hc.HugeHill.hs_min:
                self.hs = hc.HugeHill.hs_min
            elif self.hs > hc.HugeHill.hs_max:
                self.hs = hc.HugeHill.hs_max

    def _country_exists(self):
        for _, v in hc.COUNTRIES:
            if self.country == v:
                return True
        return False

    def generate_jumps(self):
        lmin = round((self.k / 100) * jgc.JUMP_LEN_MIN_PC) * ()
        lmax = round((self.k / 100) * jgc.JUMP_LEN_MAX_PC)
        lengths = [l for l in range(lmin, lmax)]
