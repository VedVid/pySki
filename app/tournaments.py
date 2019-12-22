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

from . import jumps


class Tournament:
    def __init__(self, hill, jumpers, wind):
        self.hill = hill
        self.jumpers = jumpers
        self.wind = wind
        self.qualifications = []

    def generate_jumps(self):
        # Generates list of jump lengths, using weighted list from hill.
        jumps_l = []
        distances = self.hill.generate_jumps_weighted_list()
        for _ in self.jumpers:
            jumps_l.append(self._choose_jump(distances))
        jumps_l = sorted(jumps_l, key=lambda l: l.length_score)
        return jumps_l

    def _choose_jump(self, distances):
        # Chooses one length from all jumps.
        chances = list(distances.keys())
        chance = random.randint(min(chances), max(chances))
        chosen_chance = min(chances, key=lambda x: abs(x - chance))
        chosen_distance = distances[chosen_chance]
        jump = jumps.Jump(chosen_distance, self.length_to_points(chosen_distance))
        return jump

    @staticmethod
    def simulate_jumpers(jumpers):
        # This method calculates the score
        # (arbitrary value, not the tournament points)
        # of every jumper and sorts the list.
        scores = []
        for jumper in jumpers:
            scores.append([jumper, jumper.calculate_relative_score()])
        scores = sorted(scores, key=lambda l: l[1])
        return scores

    def length_to_points(self, jump):
        return round(self.hill.points_per_k + (self.hill.points_per_m * (jump - self.hill.k)), 1)

    def simulate_qualifications(self):
        scores = self.simulate_jumpers(self.jumpers)
        jumps_l = self.generate_jumps()
        for i, score in enumerate(scores):
            # self.qualifications.append(Jumper, jumper-arbitrary-score, Jump)
            self.qualifications.append((score[0], score[1], jumps_l[i]))
        self.qualifications = sorted(self.qualifications, key=lambda l: l[2].length_score, reverse=True)
