import requests

# Get user input
print("Enter the nitrogen level of the soil:")
nitrogen = float(input())
print("Enter the phosphorus level of the soil:")
phosphorus = float(input())
print("Enter the potassium level of the soil:")
potassium = float(input())

# Create a JSON payload with the soil data
data = {'nitrogen': nitrogen, 'phosphorus': phosphorus, 'potassium': potassium}
class Soil:
    def __init__(self, nitrogen, phosphorus, potassium):
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.potassium = potassium

    def get_fertility(self):
        return f"Nitrogen: {self.nitrogen}, Phosphorus: {self.phosphorus}, Potassium: {self.potassium}"

class Crop:
    def __init__(self, name, nitrogen_requirement, phosphorus_requirement, potassium_requirement):
        self.name = name
        self.nitrogen_requirement = nitrogen_requirement
        self.phosphorus_requirement = phosphorus_requirement
        self.potassium_requirement = potassium_requirement

    def is_suitable(self, soil):
        if soil.nitrogen >= self.nitrogen_requirement and soil.phosphorus >= self.phosphorus_requirement and soil.potassium >= self.potassium_requirement:
            return True
        else:
            return False

def get_best_crop(soil, crops):
    suitable_crops = [crop for crop in crops if crop.is_suitable(soil)]
    if suitable_crops:
        return suitable_crops[0].name
    else:
        return "No suitable crop found"

# Dataset of crops
crops = [
    Crop("Wheat", 5, 10, 15),
    Crop("Rice", 15, 20, 25),
    Crop("Maize", 10, 15, 20),
    Crop("Sugarcane", 20, 25, 30)
]

# Get user input
print("Enter the nitrogen level of the soil:")
nitrogen = float(input())
print("Enter the phosphorus level of the soil:")
phosphorus = float(input())
print("Enter the potassium level of the soil:")
potassium = float(input())

# Create a Soil object with the user-input values
soil = Soil(nitrogen, phosphorus, potassium)

# Print the soil fertility and the best crop to plant
print("Soil Fertility:", soil.get_fertility())
print("Best Crop to Plant:", get_best_crop(soil, crops))
# Make a POST request to the /crop endpoint
response = requests.post('http://localhost:5000/crop', json=data)

# Parse the JSON response
best_crop = response.json()['best_crop']

# Print the best crop to plant
print("Best Crop to Plant:", best_crop)