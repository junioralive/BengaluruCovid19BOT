from logging import getLogger
import telebot
from covid_india import states
from telebot import types
import requests
from telebot.apihelper import get_updates

bot_token='PUT YOUR TOKEN HERE'
bot = telebot.TeleBot(bot_token)

#Start Command
@bot.message_handler(commands=["start"])
def sendmessage(message):
    starttxt='''Welcome To Covid Bengaluru Assistant Bot
For My Command List 
Click Here -> /help'''
    bot.reply_to(message,format(starttxt))

#Help Command
@bot.message_handler(commands=["help"])
def send_totalcases(message):
    helptxt='''1./start 
2./Covid19 
3./Cases 
4./BBMP 
5./Oxygen 
6./HomeICU 
7./OnlineDoctor
8./Covaccine'''
    bot.reply_to(message,text="My Available Commands Are: \n" + format(helptxt))


#BBMP HELPLINE NUMBERS
@bot.message_handler(commands=["BBMP"])
def sendmessage(message):

    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('/Yelahanka Zone')
    itembtnb = types.KeyboardButton('/Mahadevpura Zone')
    itembtnc = types.KeyboardButton('/Bommanahalli Zone')
    itembtnd = types.KeyboardButton('/RRNagar Zone')
    itembtne = types.KeyboardButton('/Dasarahalli Zone')
    itembtez = types.KeyboardButton('/EastZone')
    itembtwz = types.KeyboardButton('/WestZone')
    itembtsz = types.KeyboardButton('/SouthZone')

    markup.row(itembtna, itembtnb,)
    markup.row(itembtnc,itembtnd, itembtne)
    markup.row(itembtez,itembtwz,itembtsz)
    bot.reply_to(message,"For BBMP HelpLine Number, Please Choose Locality:", reply_markup=markup)

@bot.message_handler(commands=["Yelahanka"])
def sendmessage(message):
    bot.reply_to(message,"For BBMP HelpLine in Yelahanka, Please Contact: 9480685964")

@bot.message_handler(commands=["Mahadevpura"])
def sendmessage(message):
    bot.reply_to(message,"For BBMP HelpLine in Mahadevpura, Please Contact: 8023010101")

@bot.message_handler(commands=["Bommanahalli"])
def sendmessage(message):
    bot.reply_to(message,"For BBMP HelpLine in Bommanahalli, Please Contact: 8884666670")

@bot.message_handler(commands=["RRNagar"])
def sendmessage(message):
    bot.reply_to(message,"For BBMP HelpLine in RR Nagar, Please Contact: 8028601050")

@bot.message_handler(commands=["Dasarahalli"])
def sendmessage(message):
    bot.reply_to(message,"For BBMP HelpLine in Dasarahalli, Please Contact: 8028394909")

@bot.message_handler(commands=["EastZone"])
def sendmessage(message):
    bot.reply_to(message,"For BBMP HelpLine in East Zone, Please Contact: 7411038024")

@bot.message_handler(commands=["WestZone"])
def sendmessage(message):
    bot.reply_to(message,"For BBMP HelpLine in West Zone, Please Contact: 8068248454")

@bot.message_handler(commands=["SouthZone"])
def sendmessage(message):
    bot.reply_to(message,"For BBMP HelpLine in South Zone, Please Contact: 8431816718")

#Home ICU 
@bot.message_handler(commands=["HomeICU"])
def sendmessage(message):

    markup = types.ReplyKeyboardMarkup()
    itembth1 = types.KeyboardButton('/HIC1')
    itembth2 = types.KeyboardButton('/HIC2')
    itembth3 = types.KeyboardButton('/HIC3')
    itembth4 = types.KeyboardButton('/HIC4')

    markup.row(itembth1, itembth2)
    markup.row(itembth3,itembth4)
    bot.reply_to(message,"For Home ICU Supply, Please Choose:", reply_markup=markup)

@bot.message_handler(commands=["HIC1"])
def sendmessage(message):
    bot.reply_to(message,"Service Provider:YNB HealthCare, Location:Bengaluru , POC Name:Unknown , Contact Number: 8100188188 , Updated on:06/05/21")

@bot.message_handler(commands=["HIC2"])
def sendmessage(message):
    bot.reply_to(message,"Service Provider:Shilpa Proteo Home Care, Location:Bengaluru , POC Name:Shilpa , Contact Number: 8548847577 , Updated on:06/05/21")

@bot.message_handler(commands=["HIC3"])
def sendmessage(message):
    bot.reply_to(message,"Service Provider:Home ICU Set Up, Location:Bengaluru , POC Name:Daniel , Contact Number: 7708638625 , Updated on:06/05/21")

@bot.message_handler(commands=["HIC4"])
def sendmessage(message):
    bot.reply_to(message,"Service Provider:Dr Roy, Location:Bengaluru , POC Name:Dr Roy , Contact Number: 8988980202 , Updated on:10/05/21")

#Online Doctor
@bot.message_handler(commands=["OnlineDoctor"])
def sendmessage(message):

    markup = types.ReplyKeyboardMarkup()
    itembdoctor1 = types.KeyboardButton('/doctor1')
    itembdoctor2 = types.KeyboardButton('/doctor2')
    itembdoctor3 = types.KeyboardButton('/doctor3')
    itembdoctor4 = types.KeyboardButton('/doctor4 (minimal fee)')
    itembdoctor5 = types.KeyboardButton('/doctor5 (free)')
    itembdoctor6 = types.KeyboardButton('/doctor6')
    itembdoctor7 = types.KeyboardButton('/doctor7')
    itembdoctor8 = types.KeyboardButton('/doctor8')

    markup.row(itembdoctor1, itembdoctor2)
    markup.row(itembdoctor3,itembdoctor4,itembdoctor5)
    markup.row(itembdoctor6,itembdoctor7,itembdoctor8)
    bot.reply_to(message,"For Online Doctor Consultation, Please Choose Doctors:", reply_markup=markup)

@bot.message_handler(commands=["doctor1"])
def sendmessage(message):
    bot.reply_to(message,"Doctor's Name: Dr Keshav Murthy , Contact number: 9448084990 , Consultation Charges:Unknown , Consultation for:Online Consultation for COVID and NON-COVID Patients")

@bot.message_handler(commands=["doctor2"])
def sendmessage(message):
    bot.reply_to(message,"Doctor's Name: Dr. Akshaya kinagi , Online consultation: https://apollo247.onelink.me/MGY5/6a74fcc7 , Consultation Charges:Unknown , Consultation for:General Physician")

@bot.message_handler(commands=["doctor3"])
def sendmessage(message):
    bot.reply_to(message,"Doctor's Name: Dr Bharath , Contact number: 9886655588 , Consultation Charges:Unknown , Consultation for:Teleconsultation for COVID")

@bot.message_handler(commands=["doctor4"])
def sendmessage(message):
    bot.reply_to(message,"Doctor's Name: Dr Pushpa , Contact number: 9902041576 , Consultation Charges: Minimal charges(patient need not worry about cost) , Consultation for:Teleconsultation for COVID")

@bot.message_handler(commands=["doctor5"])
def sendmessage(message):
    bot.reply_to(message,"Doctor's Name: Dr Vikram Aruna , Contact number: 9035327121 , Consultation Charges: FREE , Consultation for:Teleconsultation for COVID")

@bot.message_handler(commands=["doctor6"])
def sendmessage(message):
    bot.reply_to(message,"Doctor's Name: Dr Ajith kumar , Contact number: 9986180751 , Consultation Charges:Unknown , Consultation for:Teleconsultation for COVID")

@bot.message_handler(commands=["doctor7"])
def sendmessage(message):
    bot.reply_to(message,"Doctor's Name: Dr Lohit , Contact number: 9620496969 , Consultation Charges:Unknown , Consultation for:Teleconsultation for COVID")

@bot.message_handler(commands=["doctor8"])
def sendmessage(message):
    bot.reply_to(message,"Doctor's Name: Dr Swati Muttanna , Contact number: 9513355273 , Consultation Charges:Unknown , Consultation for:Teleconsultation for COVID")

#oxygen
@bot.message_handler(commands=["Oxygen"])
def sendmessage(message):
    bot.reply_to(message,"For Oxygen Supply Details Please Go to Link, This SpreedSheet Is Updated EveryDay: https://docs.google.com/spreadsheets/d/1IiJWOnbwWOVie3GQ7LW6sbK2mckV0rkRXv_XjvzArDQ/edit?usp=sharing ")

#HomeTesting
@bot.message_handler(commands=["HomeTest"])
def sendmessage(message):
    bot.reply_to(message,"Sorry,This Comamand Is Not Yet Added")

#Covid Info
@bot.message_handler(commands=["Covid19"])
def sendmessage(message):

    markup = types.ReplyKeyboardMarkup()
    itembsym = types.KeyboardButton("/Symptoms")
    itembprv = types.KeyboardButton("/Preventions")

    markup.row(itembsym, itembprv)
    bot.reply_to(message,"For Covid19 Choose:", reply_markup=markup)

#Symptoms
@bot.message_handler(commands=["Symptoms"])
def sendmessage(message):

    covidinfo1='''  Most common symptoms:
• fever
• dry cough
• tiredness
\n
Less common symptoms:
• aches and pains
• sore throat
• diarrhoea
• conjunctivitis
• headache
• loss of taste or smell
• a rash on skin, or discolouration of fingers or toes"'''
    bot.reply_to(message,text=format(covidinfo1))

#Prevention
@bot.message_handler(commands=["Preventions"])
def sendmessage(message):

    covidinfo2='''Protect yourself and others around you by knowing the facts and taking appropriate precautions. Follow advice provided by your local health authority.
\n
 To prevent the spread of COVID-19:
    • Clean your hands often. Use soap and water, or an alcohol-based hand rub.
    • Maintain a safe distance from anyone who is coughing or sneezing.
    • Wear a mask when physical distancing is not possible.
    • Don’t touch your eyes, nose or mouth.
    • Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
    • Stay home if you feel unwell.
    • If you have a fever, cough and difficulty breathing, seek medical attention.
\n
 Calling in advance allows your healthcare provider to quickly direct you to the right health facility. This protects you, and prevents the spread of viruses and other infections.
\n
 Masks :-
\n
 Masks can help prevent the spread of the virus from the person wearing the mask to others. Masks alone do not protect against COVID-19, and should be combined with physical distancing and hand hygiene. Follow the advice provided by your local health authority.'''
    bot.reply_to(message,text=format(covidinfo2))


#CoVin Bot
@bot.message_handler(commands=["Covaccine"])
def sendmessage(message):

    covininfo='''  Hey there!👋
Welcome to CoVin Assist bot. 

This Bot will weekly check slots availability in your area and Notify. 
\n
To check Vaccine Slots Availability Go To @C19VinBot'''
    bot.reply_to(message,text=format(covininfo))

'''#Cases List For Urban Rural
@bot.message_handler(commands=["Cases"])
def sendmessage(message):

    markup = types.ReplyKeyboardMarkup()
    itemburb = types.KeyboardButton("/BengaluruUrban")
    itembrul = types.KeyboardButton("/BengaluruRural")

    markup.row(itemburb, itembrul)
    bot.reply_to(message,"Choose Between Bengaluru Urban And Bengaluru Rural:", reply_markup=markup)

#Covid Banglore Ubran
r = requests.get("https://pomber.github.io/covid19/timeseries.json")
kar_total = r.json()["KA"]["districts"]['Bengaluru Urban']['total']
covidstat= kar_total
Bngurb = str(covidstat).replace("{","").replace("}", "").replace("'","").replace(",","")

@bot.message_handler(commands=["BengaluruUrban"])
def send_totalcases(message):
    bot.reply_to(message,text="The Total Covid Cases,For Bengaluru Urban: \n" + format(Bngurb))

#Covid Banglore Rural
r = requests.get("https://api.covid19india.org/v3/data.json")
kar_total = r.json()["KA"]["districts"]['Bengaluru Rural']['total']
covidstat= kar_total
Bngrul = str(covidstat).replace("{","").replace("}", "").replace("'","").replace(",","")

@bot.message_handler(commands=["BengaluruRural"])
def send_totalcases(message):
    bot.reply_to(message,text="The Total Covid Cases,For Bengaluru Rural: \n" + format(Bngrul))'''


print("BOT Online")
bot.polling()
