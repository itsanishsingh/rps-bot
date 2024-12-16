# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# computer_choice & determine_winner functions refactored from
# https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py, MIT liscence


class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    def computer_choice(self):
        generatednum = random.randint(1, 3)
        rps_map = {1: "rock", 2: "paper", 3: "scissors"}

        return rps_map[generatednum]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # play rock paper scissors
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"You chose {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"The computer chose {comp_choice}")

        if user_choice == comp_choice:
            dispatcher.utter_message(text="It was a tie!")
            return []

        match user_choice:
            case "rock":
                match comp_choice:
                    case "paper":
                        text = "The computer won this round."
                    case "scissors":
                        text = "Congrats, you won!"
            case "paper":
                match comp_choice:
                    case "rock":
                        text = "Congrats, you won!"
                    case "scissors":
                        text = "The computer won this round."
            case "scissors":
                match comp_choice:
                    case "rock":
                        text = "The computer won this round."
                    case "paper":
                        text = "Congrats, you won!"

        dispatcher.utter_message(text=text)

        return []
