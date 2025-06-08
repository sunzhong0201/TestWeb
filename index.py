# 导入Flask类
from flask import Flask,render_template

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由和视图函数
@app.route('/')
def index():
    return 'hello success！!'

@app.route('/home')
def home():
    # return 'Hello, World!'
    return render_template('index.html')


# 运行应用
if __name__ == '__main__':
    # app.run(debug=True)
    app.run()