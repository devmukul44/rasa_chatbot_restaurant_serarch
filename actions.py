from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
from action_util import send_mail, search_restaurants, create_message, validate_location
from tabulate import tabulate


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('price')

		results = search_restaurants(City=loc, Cuisine=cuisine, budget=budget)
		response = create_message(results)

		body_boundry = "\n" + "-"*50 + "\n"
		body_header = f"\nTop 5 Restaurants for your Query - Location: {loc}, Cuisine: {cuisine}, Budget: {budget}\n\n\n"

		param = body_boundry + body_header + response + body_boundry

		dispatcher.utter_message(param)
		return [SlotSet('location',loc)]


class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		to_user = tracker.get_slot('email')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('price')

		results = search_restaurants(City=loc, Cuisine=cuisine, budget=budget)
		response = results.head(10).to_html(index=False)

		body_header = f"\nTop 10 Restaurants for your Query - Location: {loc}, Cuisine: {cuisine}, Budget: {budget}\n\n"
		send_mail(to_user, body_header, response)
		return [SlotSet('email', to_user)]


class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_loc'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		res = validate_location(location)
		print(f"we_operate: {res}")
		return [SlotSet('check_resp',res)]




