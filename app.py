from flask import Flask, request, render_template, session, url_for, abort, redirect
app = Flask(__name__)
import dbdb
app.secret_key = '1234'


@app.route('/')
def test():
    return render_template("test.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/result')
def main():
    if 'user' in session:
        return render_template("main.html")
    return redirect(url_for('login'))

@app.route('/method', methods=['GET', 'POST'])
def method():
    num = request.form["num"]
    name = request.form["name"]
    if dbdb.select_num(num, name)!= None:
          session['user'] = num
          return '''
                <script> alert("로그인 되었습니다");
                location.href="/result"
                </script>
                '''
    else:
        return '''
                <script> alert("학번 또는 이름을 확인하세요");
                location.href="/result"
                </script>
                '''

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('test'))



if __name__ == '__main__':
     app.run(debug=True)