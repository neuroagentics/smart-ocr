import gradio as gr
from sam_utils import segment_image
from ocr_utils import extract_text

def process_image(img):
    segmented = segment_image(img)
    extracted_text = extract_text(segmented)
    return segmented, extracted_text

demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil"),
    outputs=[gr.Image(type="pil"), "text"],
    title="Smart OCR",
    description="Semantic segmentation + OCR for documents"
)

if __name__ == "__main__":
    demo.launch()
