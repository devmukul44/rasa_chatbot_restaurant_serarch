## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- thanks
- thank you
- gratitude
- thanking you
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- obvio
- obviously
- of course
- sure
- yeah
- cool
- go for it
- good
- yep, will do thank you
- I'm sure I will!
- oh awesome!
- Yes
- accept
- I accept
- ok i accept
- I changed my mind. I want to accept it
- ok cool
- alright
- i will!
- ok, I behave now
- yop
- oki doki
- yes please
- yes please!
- jo
- yep if i have to
- amayzing
- confirm
- nice
- coolio
- without a doubt
- definitely yes without a doubt
- yas
- yup
- perfect
- sure thing
- absolutely
- Oh, ok
- Sure
- hm, i'd like that
- i'd like that
- i would like that
- ja
- sure!
- sure
- yes i accept
- Sweet
- amazing!
- how nice!
- cool!
- yay
- yes accept please
- great
- oh cool
- fine
- i will take that
- that sounds just right

## intent:deny
- no
- nope
- no, thanks
- not
- don't send
- don't send email
- not needed
- no need
- no, i don't want
- no thanks
- definitely not
- never
- absolutely not
- i don't think so
- i'm afraid not
- no sir
- no ma'am
- no way
- no sorry
- No, not really.
- nah not for me
- nah
- no and no again
- no go
- no thanks
- decline
- deny
- i decline
- never mind
- nevermind
- I'm not giving you my email address
- no I haven't decided yet if I want to sign up
- I don't want to give it to you
- I'm not going to give it to you
- no i don't 
- not really

## intent:goodbye
- bye
- goodbye
- good bye
- farewell
- Bye bye
- have a good one
- see you
- good by
- cee you later
- good night
- bye
- have a nice day
- see you around
- see you later
- thanks, bye
- thanks
- thanks, have a nice day.
- thanks, let me know if anything is required.
- thanks, all ways at youe service :)
- thanks, talk to you later

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- hi there
- hello
- good morning
- good evening
- good afternoon
- dear sir
- Hi bot
- Hey bot
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- hallo
- heeey
- hi hi
- hey hey hey
- hello
- hola
- hi?
- hey bot!
- hey bot
- yo chatbot
- chatbot
- hello friend
- good morning
- hii
- hello sweet boy
- yoo
- yo
- hey there
- hello sweatheart
- hellooo
- helloooo
- heyo
- hello?
- heya
- howdy
- whats up
- whatsup
- Hei
- Well hello there ;)
- Heya
- Whats up my bot
- hiii
- heyho
- hey, let's talk
- hey let's talk?
- hey let's talk
- hey dude
- hello it is me again
- what up

## intent:restaurant_search
<!-- no entity -->
- search for restaurants
- show me restaurants
- i'm looking for a place to eat
- I want to grab breakfast
- I want to grab lunch
- I want to grab dinner
- I am searching for a dinner spot
- i want to find out restaurant near me
- I need to find a restaurant
- Can you find me a good restaurant?
- Would you be able to search a place to eat?
- A place to have food
- Feeling hungry, can you help
- I am hungry, find a restaurant
- Get me some food quickly
- Pick some place for me to eat quickly
- Where can i get some food to eat
- i'm looking for a restaurant
- how can you help me find a restaurant
- pick a restaurant for me
- please find a restaurant for me
- I'm hungry. Looking out for some good restaurants
- I want to eat
- I am feeling hungry
- I need a new restaurant
- Suggest me a good restaurant
- where should i eat?
- I'm gonna need help finding a restaurant
- Show me an open restaurant
- Find a restaurant for me to eat
<!-- cuisine -->
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Mexican](cuisine)
- can you find me a [chinese](cuisine) restaurant
- show me [chinese](cuisine) restaurants
- [Chinese](cuisine:chinese)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- [North Indian](cuisine)
- [american]{"entity": "cuisine", "value": "American"}
- [American](cuisine)
- Ill prefer [chines]{"entity": "cuisine", "value": "chinese"}
<!-- location -->
- I am looking for some restaurants in [Delhi](location:New Delhi).
- I am looking for some restaurants in [Bangalore](location)
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [pune](location)
- in [Gurgaon](location)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- [Amritsar](location)
- [erode](location)
- [Jammu](location)
- [Kurnool](location)
- Hey, help me find a restaurant in [Mumbai](location)
- I need to find a restaurant in [Kolkata](location)
- [Pune](location)
- [Cyberabad](location)
- [calcuta](location)
- Find a restaurant for me in [Calcutta](location)
- Where should I eat in [Delhi](location)?
- [Delhi NCR](location:New Delhi)
- Suggest me a good restaurant around [New Delhi](location:New Delhi
- [Bengaluru](location)
- [Amratsar](location)
- I need to find this restaurant in [Delhi](location)
- [Dilli](location)
- [Bhubaneshwar](location)
- Show me the closest open restaurant in [Chennai](location)
- [Indore](location)
- [Jodhpur](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [mumbai](location)
- [Italian](cuisine)
- [delhi](location)
- [bengaluru](location)
- please find me a restaurant in [ahmedabad](location)
- Can you suggest some good restaurants in [Rishikesh](location)
- Okay. Show me some in [Allahabad]{"entity": "location", "value": "Prayagraj"}
<!-- cuisine and location -->
- [central](location) [indian](cuisine) restaurant
- show me [chines](cuisine:chinese) restaurants in the [Delhi](location:New Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- I'm gonna need help finding a [indian](cuisine) restaurant in [Mysore](location)
- i'm looking for a [Chinese](cuisine) restaurant in [Lucknow](location)
- Hey, can you help me with locating a [mexican](cuisine) restaurant in [Lakhanpur](location)
- i want a [french](cuisine) restaurant in [Vizag](location)
- What's a good place to eat [mexican](cuisine) food in [Bangalore](location)
- Find a restaurant for me where I can eat [north indian](cuisine) in [Jaipur](location)
- Find a restaurant for me to eat [mexican](cuisine) at [Faridabad](location)
- I am hungry, find me some place to go eat [italian](cuisine) in [Goa](location)
- Would you find a [south indian](cuisine) restaurant for me in [Kozhikode](location)?
- Would you find a [american](cuisine) restaurant for me in [Trivandrum](location)?
- A place to eat [chinase](cuisine) in [Mysuru](location)
- Hey, can you help me with locating a [north indian](cuisine) restaurant in [calcuta](location)
- I want to eat [italian](cuisine) food in [cochin](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- Please find me a [south-indian](cuisine) restaurant in [madras](location)
- Quickly get me a [northindian](cuisine) place in [New Delhi](location)
- Where can i get [south-indina](cuisine) food in [Mangaluru](location)
- i'm looking for a [Chinese](cuisine) restaurant in [cyberabad](location)
- [chinese](cuisine) eating place in [mumbai](location)
- I want to eat [italian](cuisine) food in [Prayagraj](location)
- Okay. I want to eat [south indian](cuisine) in [allahabad](location)
- Okay. Show me some [north indian](cuisine) restaurants in [prayagraj](location)
- What's a good place to eat [mexican](cuisine) food in [chandighar](location)
- please find me [chinese](cuisine) restaurant in [delhi](location:New Delhi)
<!-- cuisine, location, price -->
- can you book a table in [rome](location) in a [moderate](price:medium) price range with [british](cuisine) food for [four](people:4) people
- I want to know [low](price) priced mexican cuisine restaurants
- show me [inexpensive](price:low) [chinese](cuisine) restaurants in [Agra](location)
- show me [medium](price) budget [italian](cuisine) restaurants in [Allahabad](location)
- show me [costly](price:high) [north indian](cuisine) restaurants in [Hyderabad](location)
- find [expensive](price:high) restaurants in [varanasi](location)
- find [costly](price:high) restaurants in [jaipur](location)
- find [medium](price) cost [south indian](cuisine) restaurants in [cuttack](location)
- find restaurants in [delhi]{"entity": "location", "value": "New Delhi"} [low]{"entity": "price", "value": " low"} budget [italian](cuisine)
- find [cheap]{"entity": "price", "value": "low"} [mexican](cuisine) restaurants in [delhi]{"entity": "location", "value": "New Delhi"}
<!-- price -->
- [low](price)
- [medium](price)
- [high](price)
- [low](price:low)
- [medium](price:medium)
- [high](price:high)
- [>700](price:high)
- [<700](price:medium)
- [<300](price:low)
- [>300](price:medium)
- [300-700 range](price:medium)
- [300]{"entity": "price", "value": "low"}


## intent:send_email
- [abc.xyz@gmail.com](email)
- my email id is [lablab@yahoo.com](email)
- email - [jsnjnsjd@outlook.com](email)
- [njw.jjs@gmail.com](email)
- my email is [eww.ejje@gmail.com](email)
- you can send me mail on [ndje.njd@gmail.com](email)
- [ndjen.jndjen@gmail.com](email)
- [dnejnlf.edu.com](email)
- [sd@edu.co.in](email)
- [njsn_ndej@gmail.com](email)
- email id : [bbc@gmail.com](email)
- yes. Please send it to [ahbcdj@dkj.com](email)
- [abcdejsnjw@yahoo.co.in](email)
- [jddk.2jmd@kdl.co.in](email)
- [xyz@sth.edu](email)
- [abc.def@rediffmail.com](email)
- [devmukul44@gmail.com](email)
- yes. its [mukuldev@gmail.com](email)
- yes. Please send it to [devmukul44@gmail.com](email)
- yes. Please send it to [devmukul44@gmail.com](email)
- yes send at [jnjsnxsjnjs@gmail.com](email)
- yes its [jsnjs@gmail.com](email)
- [sndjsn@gmail.com](email)
- [mukul.dev@outlook.com](email)
- yes send me at [njnws@email.com](email)

## synonym:4
- four

## synonym:New Delhi
- Delhi
- dilli
- ncr
- delhi
- delhi
- NewDelhi
- Dilli
- Dellhi
- newdelhi
- Newdelhi
- new delhi
- new Delhi
- new-delhi

## synonym:Mumbai
- mumbai
- bambai
- bombay
- mombai

## synonym:bangalore
- Bangalore
- bngalore
- bengalluru
- Bangalor
- bangalore
- bengaluru

## synonym:Kolkata
- Calcutta
- kolkata
- kolkatta
- calcutta
- calcuta

## synonym:Chennai
- chennai
- madras
- Madras

## synonym:Hyderabad
- hyderabad
- Secunderabad
- secunderabad
- cyberabad
- Cyberabad

## synonym:Mysore
- mysore
- mysuru
- Mysuru

## synonym:Kochi
- kochi
- cochin
- Cochin

## synonym:Chandigarh
- chandigarh
- Chandighar
- chandighar

## synonym:Allahabad
- prayagraj
- Prayagraj
- Allahabad
- allahabad

## synonym:Pondicherry
- pondicherry
- puducherry
- Puducherry

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:south indian
- south-indian
- southindian
- south-indina
- South Indian

## synonym:north indian
- north-indian
- northindian
- north-indina
- North Indian

## synonym:vegetarian
- veggie
- vegg

## synonym:low
- low
- cheap
- budget
- economy
- less than Rs.300
- Less than Rs. 300
- less than 300
- less than Rs.300
- less than Rs. 300
- Lessthan 300
- Lessthan Rs.300
- Lessthan Rs. 300
- less 300
- less Rs.300
- around 300
- 300 or less

## synonym:medium
- medium
- moderately
- moderate
- mid
- average
- in range of 300 to 700
- 300 to 700
- 300-700
- Rs. 300 to 700
- Rs. 300 to Rs. 700
- Rs.300 to 700
- Rs.300 to Rs.700

## synonym:high
- high
- fancy
- expensive
- costly
- More than 700
- >700
- greater than 700
- 700 or more
- luxury
- luxurious
- More than Rs.700
- More than Rs. 700
- more than 700
- more than Rs.700
- more than Rs. 700
- Morethan 700
- Morethan Rs.700
- Morethan Rs. 700
- morethan 700
- morethan Rs.700
- morethan Rs. 700

## regex:greet
- hey[^\s]*

## regex:email
- (/^\S+@\S+\.\S+$/)