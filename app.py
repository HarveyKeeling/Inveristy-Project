from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Don't steal my API Key !
openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(prompt):
    model_name = 'gpt-3.5-turbo'
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a UK government assistant chatbot. Concisely direct users to the relevant sections on the gov.uk website providing the website link first."},
            {"role": "user", "content": prompt},
        ],
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == '__main__':
    app.run(debug=True)
