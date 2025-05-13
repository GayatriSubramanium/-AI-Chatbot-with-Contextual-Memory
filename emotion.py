from transformers import pipeline

classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion")

def get_emotion(text):
    result = classifier(text)
    return result[0]['label']
