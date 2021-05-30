from action_util import *
import pandas as pd


## Mail Test
# send_mail(
# 	"devmukul44@gmail.com",
# 	"checking message"
# 	)


## search_restaurants Test
results = search_restaurants('new delhi', 'north indian', 'high')
print(results)

print(results.head().style)


## create_message Test
print(create_message(results))


# ## validate_location Test
# print(validate_location("new delhi"))
