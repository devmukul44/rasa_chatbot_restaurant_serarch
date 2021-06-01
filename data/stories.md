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
    - slot{"location": "pune"}
    - utter_ask_email_conformation
* deny
    - utter_goodbye


## complete path - deny at end
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


## no small talk
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


## all 3 in the start
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "price": "low"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "low"}
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


## location and cuisine in start
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget_for_two
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
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


## location and cuisine in start - no email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget_for_two
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_conformation
* deny
    - utter_goodbye


## location and cuisine in start - we dont serve
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye


## location and price in start - no small talk
* restaurant_search{"location": "patna", "price": "high"}
    - slot{"location": "patna"}
    - slot{"price": "high"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - utter_ask_email_conformation
* affirm
    - utter_ask_email_address
* send_email{"email": "mukul.dev@outlook.com"}
    - slot{"email": "mukul.dev@outlook.com"}
    - action_send_mail
    - utter_mail_sent
* affirm
    - utter_goodbye


## location and price in start - no small talk - no email
* restaurant_search{"location": "patna", "price": "high"}
    - slot{"location": "patna"}
    - slot{"price": "high"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - utter_ask_email_conformation
* deny
    - utter_goodbye


## combination location, cuisine - deny at end
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
* deny
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
* deny
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


## cuisine first - dont serve
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "rajpura"}
    - slot{"location": "rajpura"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
* affirm
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
* send_email{"email": "abc@xyz.org"}
    - slot{"email": "abc@xyz.org"}
    - action_send_mail
    - utter_mail_sent
* deny
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
    - slot{"price": "low"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
* deny
    - utter_goodbye


## complete path - price first - no small talk
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_loc
    - slot{"check_resp": true}
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
* affirm
    - utter_goodbye


## complete path cuisine price - no small talk - no email
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_loc
    - slot{"check_resp": true}
    - utter_ask_budget_for_two
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "goa"}
    - utter_ask_email_conformation
* deny
    - utter_goodbye


## complete path - price first
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_cuisine
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_loc
    - slot{"check_resp": true}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
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


## complete path - price first - restaurant not found
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_cuisine
    - utter_ask_location
* restaurant_search{"location": "jagadhri"}
    - slot{"location": "jagadhri"}
    - action_check_loc
    - slot{"check_resp": false}
    - utter_we_dont_operate
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

