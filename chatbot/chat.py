import random
import importlib_resources
import torch
import json
from .nltk_utils import bag_of_words, tokenize
from .model import NeuralNet
from . import modules

# Loading model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with importlib_resources.open_text("chatbot", "intents.json") as f:
    intents = json.load(f)

FILE = "data.pth"
with importlib_resources.path("chatbot",FILE) as f:
    data = torch.load(f)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# chat
bot_name = "Joshua"


def reply(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return (f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        return (f"{bot_name}: I do not understand...")