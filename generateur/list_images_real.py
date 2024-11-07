import os 
from PIL import Image

dossier = "C:/Users/PaulE/Documents/CompanyLTD/Dataset"
image_dossier = "Person"

output_dossier = "temporary"


os.makedirs(dossier + "/" + output_dossier, exist_ok=True)

images = [Image.open(os.path.join(dossier+"/" +image_dossier, filename)) for filename in os.listdir(dossier+"/"+image_dossier) if filename.endswith('.jpg')]
for i, img in enumerate(images):
    img.save(dossier +f"/{output_dossier}/" +f"processed_image_{i}.png")