def api(app, mysql, jsonify):

    #USUARIOS
    @app.route('/api/users', methods=["GET", "POST"])
    def get_users():
        query = mysql.connection.cursor()
        query.execute('SELECT * FROM users')
        data = query.fetchall()
        query.close()
        
        return jsonify(data)
    
    #CASOS
    @app.route('/api/v1/getcases', methods=["GET", "POST"])
    def get_cases():
        query = mysql.connection.cursor()
        query.execute('SELECT * FROM cases')
        cases = query.fetchall()
        query.close()

        cases_list = [{'id': row[0], 'description': row[1],'dateCase':row[2]} for row in cases]
        
        return jsonify(cases_list)
