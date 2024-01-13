def routes(app, render_template):
    
    @app.route('/')
    def index():
       return render_template('index.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/home')
    def home():
        return render_template('home.html')
    
    @app.route('/home/cases')
    def cases():
        return render_template('cases/viewCases.html')
