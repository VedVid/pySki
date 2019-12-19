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


class Tournament:
    def __init__(self, hill, jumpers):
        self.hill = hill
        self.jumpers = jumpers

    def generate_jumps(self):
        jumps = []
        distances = self.hill.generate_jumps_weighted_list()

    def _choose_jump(self, jumps):
        # TODO:
        # It is very naive approach and should be changed.
        # Maybe just swap keys with values?
        chances = list(jumps.values())
        lengths = list(jumps.keys())
        chance = random.randint(min(chances), max(chances))
        chance_chosen = min(chances, key=lambda x: abs(x-chance))
        for l, ch in jumps.items():
            if ch == chance_chosen:
                return l
