from deepface import DeepFace
import gradio as gr
import cv2
import numpy as np

def verify_faces(img1, img2):
    # Save uploaded images temporarily
    cv2.imwrite("temp1.jpg", cv2.cvtColor(img1, cv2.COLOR_RGB2BGR))
    cv2.imwrite("temp2.jpg", cv2.cvtColor(img2, cv2.COLOR_RGB2BGR))
    
    try:
        # Perform verification
        result = DeepFace.verify("temp1.jpg", "temp2.jpg")
        
        if result["verified"]:
            return f"These images are of the same person\nConfidence: {result['distance']:.2f}"
        else:
            return f"These images are of different people\nDistance: {result['distance']:.2f}"
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Create Gradio interface
iface = gr.Interface(
    fn=verify_faces,
    inputs=[
        gr.Image(label="Upload First Image"),
        gr.Image(label="Upload Second Image")
    ],
    outputs=gr.Textbox(label="Result"),
    title="Face Verification",
    description="Upload two images to check if they show the same person."
)

# Launch the interface
if __name__ == "__main__":
    iface.launch(share=True)