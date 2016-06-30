# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree import widgets
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Benson'

doc = """
Raven's matrices to measure cognitive ability.
"""


class Constants(BaseConstants):
    name_in_url = 'ravens'
    players_per_group = None
    num_rounds = 1
    practice_one_answer = "four"
    practice_two_answer = "four"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_payoffs(self):
        for p in self.get_players():
            if p.raven_1 == "four":
                p.points += 1
            if p.raven_2 == "four":
                p.points += 1
            if p.raven_3 == "one":
                p.points += 1
            if p.raven_4 == "three":
                p.points += 1
            if p.raven_5 == "eight":
                p.points += 1
            if p.raven_6 == "six":
                p.points += 1
            p.payoff = p.points
            print(p.payoff)


class Player(BasePlayer):
    points = models.IntegerField(default=0)

    CHOICES = [("one", ""), ("two", ""), ("three", ""), ("four", ""), ("five", ""), ("six", "")]
    CHOICES_8 = [("one", ""), ("two", ""), ("three", ""), ("four", ""),
                 ("five", ""), ("six", ""), ("seven", ""), ("eight", "")]

    raven_p1 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES_8)
    raven_p2 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES)
    raven_1 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES)
    raven_2 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES_8)
    raven_3 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES)
    raven_4 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES)
    raven_5 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES_8)
    raven_6 = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=CHOICES_8)

    def practice_one(self):
        return self.raven_p1 == Constants.practice_one_answer

    def practice_two(self):
        return self.raven_p2 == Constants.practice_two_answer