from flask import Flask, render_template, url_for, request, jsonify


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Get Input Text from POST Request
    input_text = request.json.get("text")  
    
    if not input_text:
        # Response to send if the input_text is undefined
        response = {
                    "status": "error",
                    "message": "Please enter your review!"
                  }
        return jsonify(response)
    else:  
        predicted_emotion,predicted_emotion_img_url = predict(input_text)
        
        # Response to send if the input_text is not undefined
        response = {
                    "status": "success",
                    
                   }

        # Send Response         
        return jsonify(response)
       
app.run(debug=True)



    