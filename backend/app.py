from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Route to test if server is working
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "FilmSnap backend is running!"})

# Route to handle uploaded image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Save uploaded file to a folder (you can change this later)
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)

        # Here you would later process the image and predict movie title
        return jsonify({"message": f"File {file.filename} uploaded successfully!"})

    return jsonify({"error": "Something went wrong"}), 500

if __name__ == "__main__":
    app.run(debug=True)
