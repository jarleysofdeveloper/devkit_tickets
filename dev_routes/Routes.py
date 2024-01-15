def routes(app, render_template, session, request, mysql, jsonify, redirect, url_for):
    
    @app.route('/')
    def index():
       if "username" in session:
            return redirect(url_for('home'))
       return render_template('index.html')
    
    @app.route('/', methods=["GET", "POST"])
    def login():
        
        if request.method == "POST":
            
            user = request.form.get('username')
            password = request.form.get('password')
            
            query = mysql.connection.cursor()
            query.execute('SELECT id,name,username FROM users where username = %s and password = %s ', (user, password))
            user = query.fetchone()
            query.close()

            if user:
                session["id"] = user[0]
                session["name"] = user[1]
                session["username"] = user[2]
                return redirect(url_for('home'))
            return redirect(url_for('index'))



        return render_template('index.html')
    
    @app.route('/logout')
    def logout():
        session.pop("username", None)

        return redirect(url_for('index'))
    
    @app.route('/home')
    def home():
        if "username" in session:
            return render_template('home.html')
        return redirect(url_for("index"))
    
    @app.route('/home/cases')
    def cases():
        return render_template('cases/viewCases.html')
