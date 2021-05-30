## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "mukul.dev@outlook.com"}
    - slot{"email": "mukul.dev@outlook.com"}
    - action_send_mail
    - utter_mail_sent
    - utter_goodbye

## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "price": "low"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "medium"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "mukul.dev@outlook.com"}
    - slot{"email": "mukul.dev@outlook.com"}
    - action_send_mail
    - utter_mail_sent
* affirm
    - utter_goodbye


## we dont operate
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "yamunanagar"}
    - slot{"location": "yamunanagar"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye

<!-- validated till here -->

## email denied 
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget_for_two
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "punw"}
    - utter_ask_email_conformation
* deny
    - utter_goodbye


## complete path - deny end
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "mukul.dev@outlook.com"}
    - slot{"email": "mukul.dev@outlook.com"}
    - action_send_mail
    - utter_mail_sent
* deny
    - utter_goodbye


## combination location, cuisine
* greet
    - utter_greet
* restaurant_search{"location": "kolkata", "cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget_for_two
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "mukul.dev@outlook.com"}
    - slot{"email": "mukul.dev@outlook.com"}
    - action_send_mail
    - utter_mail_sent
* affirm
    - utter_goodbye


## combination location, price
* greet
    - utter_greet
* restaurant_search{"location": "kolkata", "price": "high"}
    - slot{"location": "delhi"}
    - slot{"price": "high"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "mukul.dev@outlook.com"}
    - slot{"email": "mukul.dev@outlook.com"}
    - action_send_mail
    - utter_mail_sent
* affirm
    - utter_goodbye


## cuisine first
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget_for_two
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "mukul.dev@outlook.com"}
    - slot{"email": "mukul.dev@outlook.com"}
    - action_send_mail
    - utter_mail_sent
    - utter_goodbye


## cuisine,price first
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "medium"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "medium"}
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "faridabad"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "mukul.dev@outlook.com"}
    - slot{"email": "mukul.dev@outlook.com"}
    - action_send_mail
    - utter_mail_sent
* affirm
    - utter_goodbye


## cuisine,price first - location not serve
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "medium"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "medium"}
    - utter_ask_location
* restaurant_search{"location": "ambala"}
    - slot{"location": "ambala"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
* affirm
    - utter_goodbye


## we dont operate, all entity provided
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"cuisine": "italian", "location": "mumbai", "price": "low"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "medium"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
* deny
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "mexican", "location": "New Delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "New Delhi"}
    - slot{"price": "low"}
    - action_check_loc
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - utter_ask_email_conformation
* send_email{"email": "devmukul44@gmail.com"}
    - slot{"email": "devmukul44@gmail.com"}
    - action_send_mail
    - slot{"email": "devmukul44@gmail.com"}
    - utter_mail_sent
    - utter_goodbye
* goodbye
    - utter_goodbye


## interactive_story_3
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget_for_two
* restaurant_search{"price": " medium"}
    - slot{"price": " medium"}
    - action_search_restaurants
    - slot{"location": "faridabad"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "devmukul44@gmail.com"}
    - slot{"email": "devmukul44@gmail.com"}
    - action_send_mail
    - slot{"email": "devmukul44@gmail.com"}
    - utter_mail_sent
    - utter_goodbye
* affirm
    - utter_goodbye

