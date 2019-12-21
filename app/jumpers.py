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

from . import jumpers_constants as jc


class Jumper:
    def __init__(self, surname, name, age, height, weight, inrun, takeoff, flight, landing, mental, form):
        self.surname = surname
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.inrun = inrun
        self.takeoff = takeoff
        self.flight = flight
        self.landing = landing
        self.mental = mental
        self.form = form
        self.normalize()

    def normalize(self):
        # Make sure that all values are in proper ranges.
        if self.age < jc.AGE_ADULT:  # Currently, we are creating adults only.
            self.age = jc.AGE_ADULT
        elif self.age > jc.AGE_MAX_MAX:
            self.age = jc.AGE_MAX_MAX
        if self.height < jc.HEIGHT_MIN_MIN:
            self.height = jc.HEIGHT_MIN_MIN
        elif self.height > jc.HEIGHT_MAX_MAX:
            self.height = jc.HEIGHT_MAX_MAX
        # Instead of checking jumper's weight, we are checking his BMI.python
        if self.bmi() < jc.BMI_MIN_MIN:
            self._bmi_set_min()
        elif self.bmi() > jc.BMI_MAX_MAX:
            self._bmi_set_max()
        if self.inrun < jc.SKILL_MIN:
            self.inrun = jc.SKILL_MIN
        elif self.inrun > jc.SKILL_MAX:
            self.inrun = jc.SKILL_MAX
        if self.takeoff < jc.SKILL_MIN:
            self.takeoff = jc.SKILL_MIN
        elif self.takeoff > jc.SKILL_MAX:
            self.takeoff = jc.SKILL_MAX
        if self.flight < jc.SKILL_MIN:
            self.flight = jc.SKILL_MIN
        elif self.flight > jc.SKILL_MAX:
            self.flight = jc.SKILL_MAX
        if self.landing < jc.SKILL_MIN:
            self.landing = jc.SKILL_MIN
        elif self.landing > jc.SKILL_MAX:
            self.landing = jc.SKILL_MAX
        if self.mental < jc.SKILL_MIN:
            self.mental = jc.SKILL_MIN
        elif self.mental > jc.SKILL_MAX:
            self.mental = jc.SKILL_MAX
        # For is not a skill, a rather dynamic variable.
        # Still, is bound to certain ranges and we can check it.
        if self.form < jc.SKILL_MIN:
            self.form = jc.SKILL_MIN
        elif self.form > jc.SKILL_MAX:
            self.form = jc.SKILL_MAX

    def bmi(self):
        return round(self.weight / ((self.height * self.height) / 10000), 1)

    def _bmi_set_min(self):
        # TODO: Fix that naive approach!
        while True:
            self.weight += 1
            if self.bmi() >= jc.BMI_MIN_MIN:
                break

    def _bmi_set_max(self):
        # TODO: Fix that naive approach!
        while True:
            self.weight -= 1
            if self.bmi() <= jc.BMI_MAX_MAX:
                break

    def calculate_relative_score(self):
        inrun_score = round(
            (self.inrun + random.randint(jc.SKILL_MIN, self.inrun) + random.randint(jc.SKILL_MIN, jc.SKILL_MAX)) / 2
        )
        takeoff_score = round(
            (self.takeoff + random.randint(jc.SKILL_MIN, self.takeoff) + random.randint(jc.SKILL_MIN, jc.SKILL_MAX)) *
            1.5
        )
        flight_score = round(
            (self.flight + random.randint(jc.SKILL_MIN, self.flight) + random.randint(jc.SKILL_MIN, jc.SKILL_MAX)) *
            1.25
        )
        landing_score = round(
            (self.landing + random.randint(jc.SKILL_MIN, self.landing) + random.randint(jc.SKILL_MIN, jc.SKILL_MAX)) / 3
        )
        mental_score = round(
            (self.mental + random.randint(jc.SKILL_MIN, self.mental) + random.randint(jc.SKILL_MIN, jc.SKILL_MAX)) / 2
        )
        form_score = round(
            (self.form + random.randint(jc.SKILL_MIN, self.form) + random.randint(jc.SKILL_MIN, jc.SKILL_MAX)) / 2
        )
        final_score = inrun_score + takeoff_score + flight_score + landing_score + mental_score + form_score
        return final_score
