def routes(app, render_template, session, request, mysql, jsonify, redirect, url_for, socketio,join_room, generate_password_hash, check_password_hash):
    
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
            query.execute('SELECT id,name,username,password,email,role FROM users where username = %s ', [user])
            user = query.fetchone()
            query.close()

            if user:
                password_hash = user[3]

                if check_password_hash(password_hash, password):
                    session["id"] = user[0]
                    session["name"] = user[1]
                    session["username"] = user[2]
                    session["email"] = user[4]
                    session["role"] = user[5]
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
    
    @app.route('/signup', methods=["GET","POST"])
    def signup():
        if request.method == "POST":
            name = request.form.get('name')
            email = request.form.get('email')
            username = request.form.get('username')
            password = request.form.get('password')

            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

            query = mysql.connection.cursor()
            result = query.execute('INSERT INTO users(name,username,password,email) VALUES(%s,%s,%s,%s)',(name,username,hashed_password,email))
            mysql.connection.commit()
            query.close()

            if result == 1:
                return redirect(url_for('index'))
            else:
                return render_template('signup.html')
            
        return render_template('signup.html')

    #--------------------------------------------------------------------------#
    #hace la actualizacion en tiempo real de los datos
    @socketio.on('reload_table')
    def handle_reload_table():
        if "username" in session:
            join_room('all_users')
            socketio.emit('update_table_data', room='all_users')


