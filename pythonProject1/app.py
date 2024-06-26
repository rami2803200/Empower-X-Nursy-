from flask umport Flask

flask, request, send_file, render_template
import tempfile
from text2speech import text2speech
from speech2text import speech2text

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True, port=8080)