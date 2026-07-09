import pickle
with open("trained_model.pkl", "rb") as f:
    model = pickle.load(f)

with open('text_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def check_illegal_chat(chat_messages, model, vectorizer, threshold=0.2):

    chat_vectorized = vectorizer.transform(chat_messages)
    predictions = model.predict(chat_vectorized)
    num_suspicious = sum(predictions)
    percentage_suspicious = num_suspicious / len(chat_messages)
    return percentage_suspicious > threshold


