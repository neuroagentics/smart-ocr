import easyocr
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image):
    bounds = reader.readtext(np.array(image))
    extracted = "\n".join([item[1] for item in bounds])
    return extracted
