def routes(app, render_template, session, request, mysql, jsonify, redirect, url_for):
    
    @app.route('/')
    def index():
       return render_template('index.html')
    
    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            
            user = request.form.get('username')
            password = request.form.get('password')
            
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM users where username = %s and password = %s ', (user, password))
            user = query.fetchall()
            query.close()

            return jsonify(user)


        return render_template('login.html')
    
    @app.route('/home')
    def home():
        return render_template('home.html')
    
    @app.route('/home/cases')
    def cases():
        return render_template('cases/viewCases.html')
