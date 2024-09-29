import Flask
from flask import request, jsonify
from soil_crop import Soil, Crop, get_best_crop  # Import the Soil, Crop, and get_best_crop functions from the above code

app = Flask(__name__)

# Dataset of crops
crops = [
    Crop("Wheat", 5, 10, 15),
    Crop("Rice", 15, 20, 25),
    Crop("Maize", 10, 15, 20),
    Crop("Sugarcane", 20, 25, 30)
]

@app.route('/soil', methods=['POST'])
def get_soil_fertility():
    data = request.get_json()
    nitrogen = data['nitrogen']
    phosphorus = data['phosphorus']
    potassium = data['potassium']
    soil = Soil(nitrogen, phosphorus, potassium)
    return jsonify({'fertility': soil.get_fertility()})

@app.route('/crop', methods=['POST'])
def get_best_crop_to_plant():
    data = request.get_json()
    nitrogen = data['nitrogen']
    phosphorus = data['phosphorus']
    potassium = data['potassium']
    soil = Soil(nitrogen, phosphorus, potassium)
    best_crop = get_best_crop(soil, crops)
    return jsonify({'best_crop': best_crop})

if __name__ == '__main__':
    app.run(debug=True)