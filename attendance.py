from transformers import pipeline

# Load the image classification model
face_recognition = pipeline('image-classification', model='microsoft/resnet-50')

def recognize_faces(image_path):
    # Load image and perform recognition
    results = face_recognition(image_path)
    return results
