from django.shortcuts import render,redirect
from .models import Contact,User

from django.conf import settings
from django.core.mail import send_mail

import random

# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	if request.method=='POST':
		Contact.objects.create(
			name = request.POST['name'],
			email = request.POST['email'],
			mobile = request.POST['mobile'],
			remarks = request.POST['remarks'],

			)
		msg = 'Contact saved successfully'
		contacts = Contact.objects.all().order_by('-id')[:2]
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:	
		contacts = Contact.objects.all().order_by('-id')[:2]
		return render(request,'contact.html',{'contacts':contacts})
	
def signup(request):
	if request.method=='POST':
		try:
			User.objects.get(email = request.POST['email'])
			msg = 'Email Already Registered'
			return render(request,'signup.html',{'msg':msg})
		except:	
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname = request.POST['fname'],
					lname = request.POST['lname'],
					email = request.POST['email'],
					mobile = request.POST['mobile'],
					gender = request.POST['gender'],
					address = request.POST['address'],
					password = request.POST['password'],
					profile_pic = request.FILES['profile_pic']
				)
				msg = 'Sign Up Successfully'
				return render(request,'index.html',{'msg':msg})
			else:	
				msg = 'Password & Confirm Password Does Not Matched'
				return render(request,'signup.html',{'msg':msg})
	else:	
		return render(request,'signup.html')

def login(request):
	if request.method=='POST':
		try:
			user = User.objects.get(email = request.POST['email'])
			if user.password==request.POST['password']:
				request.session['fname'] = user.fname
				request.session['email'] = user.email
				request.session['profile_pic'] = user.profile_pic.url
				msg = 'Login Successfully'
				return render(request,'index.html',{'msg':msg})
			else:
				msg = 'Invalid Password'
				return render(request,'login.html',{'msg':msg})
		except:	
			msg = 'Email Not Registered'
			return render(request,'signup.html',{'msg':msg})
	else:		
		return render(request,'login.html')
	
def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		return render(request,'login.html')
	except:
		return render(request,'login.html')	
	
def forgetpassword(request):
	if request.method=='POST':
		try:
			user =  User.objects.get(email = request.POST['email'])
			otp = random.randint(1000,9999)
			subject = 'Otp For Forget Password'
			message = f'Hi {user.fname}, thank you for registering in geeksforgeeks. Here your Otp {str(otp)} .'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp_verification.html',{'email':user.email,'otp':otp})
		except Exception as e:
			print(e)
			print(user)
			msg = 'entered Email Is Not Registered '
			return render(request,'forgetpassword.html',{'msg':msg})
	else:	
		return render(request,'forgetpassword.html')
	
def otp_verification(request):
	forget_email = request.POST['email']
	otp = request.POST['otp']
	uotp = request.POST['uotp']

	if otp == uotp :
		msg = 'Otp Entered Successfully'
		return render(request,'new_password.html',{'msg':msg,'foremail':forget_email})
	else:
		msg = 'Entered Otp Does Not Match'
		return render(request,'new_password.html',{'msg':msg})
	
def new_password(request):
	new_password = request.POST['new-password']
	cnew_password = request.POST['cnew-password']

	
	user = User.objects.get(email = request.POST['hemail'])
	if new_password == cnew_password:
		user.password = new_password
		user.save()
		msg = 'Password Updated Successfully'
		return render(request,'login.html',{'msg':msg})
	else:
		msg = 'Entered New Password & Does Not Match'
		return render(request,'new_password.html',{'msg':msg})
	

def changepassword(request):
	if request.method=='POST':
		user = User.objects.get(email = request.session['email'])
		if user.password == request.POST['old-new-password']:
			if request.POST['cnew-password'] == request.POST['new-password']:
				user.password = request.POST['new-password']
				user.save()
				return redirect('logout')
			else:
				msg = 'Entered New Password & Does Not Match'
				return render(request,'changepassword.html',{'msg':msg})
		else:
			msg = 'Entered Old Password Does Not Match'
			return render(request,'changepassword.html',{'msg':msg})			
	else:
		return render(request,'changepassword.html')

def editprofile(request):
	user = User.objects.get(email = request.session['email'])
	if request.method=='POST':
		user.fname = request.POST['fname']
		user.lname = request.POST['lname']
		user.mobile = request.POST['mobile']
		user.gender = request.POST['gender']
		user.address = request.POST['address']
		try:
			user.profile_pic = request.FILES['profile_pic']
		except:
			pass	
		user.save()
		request.session['profile_pic'] = user.profile_pic.url
		return redirect('logout')
	else:
		return render(request,'editprofile.html',{'user':user})