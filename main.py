from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello,world!'
@app.route('/armstrong/<int:n>')

def armstrong(n):
    sum=0
    order=len(str(n))
    copy_num=n
    while(n>0):
        digit=n%10
        sum+=digit**order
        n=n//10
    if sum==copy_num:
        print(f"{copy_num} is an armstrong number")
        return True
    else:
        print(f"{copy_num} is not an armstrong number")
        return False
if __name__ == "__main__":
    app.run(debug=True)
