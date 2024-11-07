import os 
from PIL import Image

dossier = "C:/Users/PaulE/Documents/CompanyLTD/Dataset"
image_dossier = "Person"
output_dossier = "temporary"
def load_images(image_directory):
    for filename in os.listdir(image_directory):
        if filename.endswith('.jpg'):  
            image_path = os.path.join(image_directory, filename)
            image = Image.open(image_path)
            yield image

images = load_images(dossier+"/"+image_dossier)
os.makedirs(dossier + "/" + output_dossier, exist_ok=True)

for i, img in enumerate(images):
    img.save(dossier +f"/{output_dossier}/" +f"processed_image_{i}.png")
