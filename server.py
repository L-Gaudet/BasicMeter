from flask import Flask, render_template, request
from backend import loginProcess
app = Flask(__name__)

# SPOTIPY_CLIENT_ID = "add419895c1f4fd09ed9638c2858f10e"
# SPOTIPY_CLIENT_SECRET = "271b39b9429d4a319858ef19db87289a"
# SPOTIPY_REDIRECT_URI  = "https://basicmeter.uc.r.appspot.com/"

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    if request.form.get('actionlogin') == 'Login with Spotify':
      basicPercent = loginProcess()
      # basicPercent = os.system("python3 backend.py")
      # subprocess.run('python3 backend.py')
      # basicPercent = subprocess.check_output(['backend.py'])
      # print(basicPercent)
      return render_template('loggedin.html', basicPercent=basicPercent)
    else:
      pass
  elif request.method == 'GET':
    return render_template('landing.html')

if __name__ == '__main__':
  app.run()