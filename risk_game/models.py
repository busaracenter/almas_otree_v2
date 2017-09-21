# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

# </standard imports>

author = 'Benson'

doc = """
In this Game, six different coins with different amounts for heads and tails.
Subjects can choose which coin they want to ip and then get the money that's associated with either heads or tails.
"""


class Constants(BaseConstants):
    name_in_url = 'risk_game'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def make_random_toss_one(self):
        for p in self.get_players():
            p.random_coin_toss_one = random.choice(["Heads", "Tails"])

    def make_random_toss_two(self):
        for p in self.get_players():
            p.random_coin_toss_two = random.choice(["Heads", "Tails"])

    def menu_a_points(self):
        points = 0
        for p in self.get_players():
            if p.decision_one == "Coin 1":
                if p.random_coin_toss_one == "Heads":
                    points = 0
                else:
                    points = 2880

            elif p.decision_one == "Coin 2":
                if p.random_coin_toss_one == "Heads":
                    points = 240
                else:
                    points = 2400

            elif p.decision_one == "Coin 3":
                if p.random_coin_toss_one == "Heads":
                    points = 480
                else:
                    points = 1920

            elif p.decision_one == "Coin 4":
                if p.random_coin_toss_one == "Heads":
                    points = 720
                else:
                    points = 1440

            elif p.decision_one == "Coin 5":
                if p.random_coin_toss_one == "Heads":
                    points = 840
                else:
                    points = 1200

            elif p.decision_one == "Coin 6":
                if p.random_coin_toss_one == "Heads":
                    points = 960
                else:
                    points = 960

            elif p.decision_one == "Coin 7":
                if p.random_coin_toss_one == "Heads":
                    points = 1080
                else:
                    points = 720
        return points

    def menu_b_points(self):
        points = 0
        for p in self.get_players():
            if p.decision_two == "Coin 1":
                if p.random_coin_toss_two == "Heads":
                    points = 0
                else:
                    points = 2160

            elif p.decision_two == "Coin 2":
                if p.random_coin_toss_two == "Heads":
                    points = 240
                else:
                    points = 1920

            elif p.decision_two == "Coin 3":
                if p.random_coin_toss_two == "Heads":
                    points = 480
                else:
                    points = 1680

            elif p.decision_two == "Coin 4":
                if p.random_coin_toss_two == "Heads":
                    points = 720
                else:
                    points = 1440

            elif p.decision_two == "Coin 5":
                if p.random_coin_toss_two == "Heads":
                    points = 960
                else:
                    points = 1200

            elif p.decision_two == "Coin 6":
                points = 1080

            elif p.decision_two == "Coin 7":
                if p.random_coin_toss_two == "Heads":
                    points = 1200
                else:
                    points = 960
        return points

    def set_payoff(self):
        points = self.menu_a_points() + self.menu_b_points()
        for p in self.get_players():
            p.participant.vars["game_payoff"]["risk_game"] = points
            p.participant.vars["carrying_payoff"] += points
            p.risk_games_points = points
            p.payoff = points


class Player(BasePlayer):
    CHOICE_ONE = (
        ("Coin 1", "Coin 1: 0 tokens if heads and 2880 tokens if tails"),
        ("Coin 2", "Coin 2: 240 tokens if heads and 2400 tokens if tails"),
        ("Coin 3", "Coin 3: 480 tokens if heads and 1920 tokens if tails"),
        ("Coin 4", "Coin 4: 720 tokens if heads and 1440 tokens if tails"),
        ("Coin 5", "Coin 5: 840 tokens if heads and 1200 tokens if tails"),
        ("Coin 6", "Coin 6: 960 tokens if heads and 960 tokens if tails"),
        ("Coin 7", "Coin 7: 1080 tokens if heads and 720 tokens if tails"),
    )

    CHOICE_TWO = (
        ("Coin 1", "Coin 1: 0 tokens if heads and 2160 tokens if tails"),
        ("Coin 2", "Coin 2: 240 tokens if heads and 1920 tokens if tails"),
        ("Coin 3", "Coin 3: 480 tokens if heads and 1680 tokens if tails"),
        ("Coin 4", "Coin 4: 720 tokens if heads and 1440 tokens if tails"),
        ("Coin 5", "Coin 5: 960 tokens if heads and 1200 tokens if tails"),
        ("Coin 6", "Coin 6: 1080 tokens if heads and 1080 tokens if tails"),
        ("Coin 7", "Coin 7: 1200 tokens if heads and 960 tokens if tails"),
    )

    decision_one = models.CharField(choices=CHOICE_ONE, widget=widgets.RadioSelect())
    random_coin_toss_one = models.CharField()

    decision_two = models.CharField(choices=CHOICE_TWO, widget=widgets.RadioSelect())
    random_coin_toss_two = models.CharField()
    risk_games_points = models.IntegerField()
