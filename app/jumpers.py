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
        return round(self.weight / (self.height * self.height), 1)

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
