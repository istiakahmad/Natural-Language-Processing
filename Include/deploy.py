from flask import *
from sentiment_model import sentiment

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_message = request.form['istiak']
        result = str(sentiment(input_message))
        # return 'Result is:  ' + result
        return render_template('index.html', result2 = result)
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True, port=8080)



