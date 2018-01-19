from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


# **********************************************************************************************************************
# *** BOT
# **********************************************************************************************************************
class PlayerBot(Bot):

    def play_round(self):

        page = self.subsession.round_number

        # ------------------------------------------------------------------------------------------------------------ #
        # submit instructions page
        # ------------------------------------------------------------------------------------------------------------ #
        if Constants.instructions:
            if page == 1:
                yield (views.Instructions)

        # ------------------------------------------------------------------------------------------------------------ #
        # make decisions
        # ------------------------------------------------------------------------------------------------------------ #
        if Constants.indifference == True:
            previous_choices = [p.choice for p in self.player.in_previous_rounds()]
            if 'I' not in previous_choices:
                yield (views.Decision, {'choice': random.choice(['A', 'B', 'I'])})
        else:
            yield (views.Decision, {'choice': random.choice(['A', 'B'])})

        # ------------------------------------------------------------------------------------------------------------ #
        # submit results page
        # ------------------------------------------------------------------------------------------------------------ #
        if Constants.results:
            if page == Constants.num_choices:
                yield (views.Results)