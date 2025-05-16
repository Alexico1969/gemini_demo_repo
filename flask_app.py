from flask import Flask, request, render_template, redirect, url_for
import google.generativeai as genai
from key import api_key

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how AI works")
# print(response.text)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    msg = """
    <p>This website will bring you up to speed in regards to AI.</p>
    <p>You can ask questions about the latest developments in AI,</p>
    <p>or you can ask how you can use AI in a specific situation</p>
    """
    if request.method == "POST":
        question = request.form.get('question')
        intro = """
        You are a helpful assistant for a person who wants to know more about AI.
        Be as helpful as you can, even though the question might be a bit unclear or 
        asks you to do something that is hard or close to impossible. Make the output in html format. 
        The person will look at your output through a web browser. So you can make the output as pretty
        as you want. You don't have to add ```html to the output.
        Here is the question the person has for you:
        """
        prompt = intro + question
        response = model.generate_content(prompt)
        msg = response.text
    return render_template("home.html", message=msg)

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html", message="<h1>About Us</h1><p>This is the About page for the AI assistant website.</p>")

@app.route('/help', methods=['GET'])
def help():
    return render_template("help.html", message="<h1>Help</h1><p>This is the Help page. Here you can find assistance on how to use the website.</p>")

if __name__ == '__main__':
    app.run(debug=True)