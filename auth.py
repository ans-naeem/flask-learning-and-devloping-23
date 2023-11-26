from flask import Blueprint,render_template,url_for,request,redirect

auth=Blueprint('auth',__name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup' ,methods=['post'])
def signup_post():
    email=request.form.get('exampleInputEmail1')
    password=request.form.get('exampleInputPassword1')
    checkbox=request.form.get('exampleCheck1')
    print(email ,password)
    return render_template('index.html',email=email,password=password,check=checkbox)



@auth.route('/dashboard')
def dashboard():
    return "This is gona be dashboard"

@auth.route('/profile')
def profile():
    return render_template('profile.html')