import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd


WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
# zomato
ZomatoData = pd.read_csv('zomato.csv', encoding = "ISO-8859-1")
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)


def send_mail(to_user, body_txt, body_html):
    from_user = 'projectstemp1@gmail.com' # create your gmail id and paste here
    password = 'projectstemp123' # create your gmail id and paste here
    print(f"sending mail to: {to_user}")

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(from_user, password)
        subject = 'Chatbot - Top Restaurants for you'
        msg = MIMEMultipart()
        msg['From'] = from_user
        msg['TO'] = to_user
        msg['Subject'] = subject
        body_header = '''Hi User, \n \n'''
        body_footer = \
'''
\n\nThanks & Regards
Team: Chatbot!
For more information reply on same mail. Our Team will connect with you soon
'''
        msg.attach(MIMEText(body_header + body_txt,'plain'))
        msg.attach(MIMEText(body_html,'html'))
        msg.attach(MIMEText(body_footer,'plain'))
        text = msg.as_string()
        server.sendmail(from_user,to_user,text)
        server.close()
        print("mail sent!")
    except Exception as e:
        print(e)


def search_restaurants(City, Cuisine, budget):
    budget = budget.lower().strip()
    print(f"searching restaurants for query - Location: {City}, Cuisine: {Cuisine}, Budget: {budget}")
    cost_column = ZomatoData['Average Cost for two']
    if budget == 'low':
        cost_filter = cost_column <= 300
    elif budget == 'medium':
        cost_filter = ((cost_column > 300) & (cost_column < 700))
    elif budget == 'high':
        cost_filter = cost_column >= 700
    else:
        cost_filter = None
    
    TEMP = ZomatoData[
        (ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) &
        (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) &
        (cost_filter)
    ].sort_values(['Aggregate rating', 'Average Cost for two'], ascending=[False, True])
    return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]


def create_message(results, number_messages:int=5):
    response = ""
    if results.shape[0] == 0:
        response= "no results"
    else:
        for restaurant in results.iloc[:number_messages].iterrows():
            restaurant = restaurant[1]
            response=response + F"""Found: "{restaurant['Restaurant Name']}" in "{restaurant['Address']}" has been rated "{restaurant['Aggregate rating']}" with avg cost "{restaurant['Average Cost for two']}" \n\n\n"""
    return response


def validate_location(loc):
    if loc.lower() in list(map(str.lower, WeOperate)):
        return(True)
    else:
        return(False)





