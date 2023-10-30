from flask_wtf import FlaskForm as Form
from wtforms import RadioField, SubmitField

class QuizForm(Form):
  question_1 = RadioField(u"What is net income?", choices=[("a","What you make per decade"),("b","What you steal per person"),("c","Income after taxes (take home pay)")])
  question_2 = RadioField(u"______ is an individual that lends money or extends credit.", choices=[("a","A co-signer"),("b","A payer"),("c","A creditor")])
  question_3 = RadioField(u"What is a budget?", choices=[("a","How much you're getting in income"),("b","A spending plan"),("c","An account of some kind")])
  question_4 = RadioField(u"A 401(k) is a type of tax-advantage defined-contribution account designed to help you save for what withdrawal from working life?", choices=[("a","Retirement"),("b","Vacation"), ("c","Sick Days")])
  question_5 = RadioField(u"What is a debit card?", choices=[("a","A cars that draws on funds directly deposited with the card provider"),("b","A card that allows customers to borrow money from the provider"), ("c","Free money")])
  submit = SubmitField("Submit Now")
