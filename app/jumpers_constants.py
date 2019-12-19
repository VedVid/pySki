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


# Player skill is in range between 0 and 100.
SKILL_MIN = 0
SKILL_MAX = 100
# 12-18 is junior, retires between 32 and 40;
# unusually, player can jump up to 50 birthday.
AGE_MIN = 12
AGE_MAX = 40
AGE_MAX_MAX = 50
AGE_ADULT = 18
AGE_RETIRE = 32
# Usually, players are between 165 and 190 cm height;
# but exceptions exists.
HEIGHT_MIN = 165
HEIGHT_MIN_MIN = 150
HEIGHT_MAX = 190
HEIGHT_MAX_MAX = 210
# Weight calculation is based on BMI;
# as usual, there is "usual" range and exceptions.
BMI_MIN = 21
BMI_MIN_MIN = 17
BMI_MAX = 24
BMI_MAX_MAX = 28
