#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import torch.nn as nn
import torch.nn.functional as F
import copy
import ast
import numpy as np
from random import randint


# In[ ]:


class NGramModel(nn.Module):
  def __init__(self, vocabulary_size, context_size, dimensions):
    super(NGramModel, self).__init__()
    self.embedding = nn.Embedding(vocabulary_size, dimensions)
    self.linear1 = nn.Linear(context_size * dimensions, 254)
    self.dropout1 = nn.Dropout(0.1)
    self.linear2 = nn.Linear(254, 128)
    self.dropout2 = nn.Dropout(0.1)
    self.linear3 = nn.Linear(128, vocabulary_size)
  def forward(self, inputs):
    embeds = self.embedding(inputs).view(1, -1)
    out = F.relu(self.linear1(embeds))
    out = self.dropout1(out)
    out = F.relu(self.linear2(out))
    out = self.dropout1(out)
    out = F.log_softmax(self.linear3(out), dim=1)
    return out


# In[ ]:


def decrypt_value(value, dictionary):
  for key in dictionary.keys():
    if dictionary[key] == value:
      return key
  else:
    print("Unknown value")
    return None


# In[ ]:


with open("./src/models/word_to_ix.txt", "r", encoding="utf-8") as word_to_ix_file:
    word_to_ix = ast.literal_eval(word_to_ix_file.read())
    
print(len(word_to_ix))
print(word_to_ix["Jay"])


# In[ ]:


PATH = "./src/models/"

model_name_list = ["model_context_2_layers_254_128_epoch_220.pth", "model_context_3_layers_254_128_epoch_100.pth",
              "model_context_4_layers_254_128_epoch_160.pth", "model_context_5_layers_254_128_epoch_180.pth"]

model_list = []
for idx in range(4):
    model = NGramModel(len(word_to_ix), 2+idx, 40)
    model.load_state_dict(torch.load(PATH + model_name_list[idx]))
    model.eval()
    model_list.append(model)


# In[ ]:


starting_sentences = ["Before a", "I ain't", "I never", "Then I", "Nasty Nas", "And I'm", "I said",
                     "I rock", "With more", "Rest in"]

for idx, sentence in enumerate(starting_sentences):
    sentence = sentence.split(" ")
    word1, word2 = sentence[0], sentence[1]
    lyrics = word1 + " " + word2 + " "
    #########2########
    model = model_list[0]
    input = torch.tensor([word_to_ix[word1], word_to_ix[word2]], dtype=torch.long)
    prediction = list(model(input).cpu().detach().numpy()[0])
    prediction_tempo = copy.deepcopy(prediction)
    prediction_tempo.sort()
    prediction_tempo.reverse()
    summation = sum(prediction_tempo[:4])
    probabilities = [pred/summation for pred in prediction_tempo[:4]]
    random_index = np.random.choice(np.arange(1, 5), p=probabilities)
    #value = prediction.index(prediction_tempo[random_index])
    value = prediction.index(prediction_tempo[0])
    value = decrypt_value(value, word_to_ix)
    word3 = value
    lyrics += value
    lyrics += " "
    #########3########
    model = model_list[1]
    input = torch.tensor([word_to_ix[word1], word_to_ix[word2], word_to_ix[word3]], dtype=torch.long)
    prediction = list(model(input).cpu().detach().numpy()[0])
    prediction_tempo = copy.deepcopy(prediction)
    prediction_tempo.sort()
    prediction_tempo.reverse()
    summation = sum(prediction_tempo[:3])
    probabilities = [pred/summation for pred in prediction_tempo[:3]]
    random_index = np.random.choice(np.arange(1, 4), p=probabilities)
    value = prediction.index(prediction_tempo[random_index])
    value = decrypt_value(value, word_to_ix)
    word4 = value
    lyrics += value
    lyrics += " "
    #########4########
    model = model_list[2]
    input = torch.tensor([word_to_ix[word1], word_to_ix[word2], word_to_ix[word3], word_to_ix[word4]], dtype=torch.long)
    prediction = list(model(input).cpu().detach().numpy()[0])
    prediction_tempo = copy.deepcopy(prediction)
    prediction_tempo.sort()
    prediction_tempo.reverse()
    summation = sum(prediction_tempo[:2])
    probabilities = [pred/summation for pred in prediction_tempo[:2]]
    random_index = np.random.choice(np.arange(1, 3), p=probabilities)
    value = prediction.index(prediction_tempo[random_index])
    value = decrypt_value(value, word_to_ix)
    word5 = value
    lyrics += value
    lyrics += " "
    #########5########
    model = model_list[3]
    length = randint(1, 7)
    for _ in range(length):
        input = torch.tensor([word_to_ix[word1], word_to_ix[word2], word_to_ix[word3], word_to_ix[word4], word_to_ix[word5]], dtype=torch.long)
        prediction = list(model(input).cpu().detach().numpy()[0])
        prediction_tempo = copy.deepcopy(prediction)
        prediction_tempo.sort()
        prediction_tempo.reverse()
        summation = sum(prediction_tempo[:4])
        probabilities = [pred/summation for pred in prediction_tempo[:4]]
        random_index = np.random.choice(np.arange(1, 5), p=probabilities)
        value = prediction.index(prediction_tempo[random_index])
        value = decrypt_value(value, word_to_ix)
        lyrics += value
        lyrics += " "
        word1 = word2
        word2 = word3
        word3 = word4
        word4 = word5
        word5 = value
    lyrics += ".\n"
    print(lyrics)


# In[ ]:


starting_sentences = ["the mic", "I am", "believe me", "I take",
                     "when we", "I go", "with my"]

verse = ""
for sentence in starting_sentences:
  lyrics_length = randint(20, 60)
  sentence = sentence.split(" ")
  word1, word2 = sentence[0], sentence[1]
  lyrics = word1 + " " + word2 + " "

  for _ in range(lyrics_length):
    input = torch.tensor([word_to_ix[word1], word_to_ix[word2]], dtype=torch.long)
    prediction = list(model(input).cpu().detach().numpy()[0])
    prediction_tempo = copy.deepcopy(prediction)
    prediction_tempo.sort()
    prediction_tempo.reverse()
    
    summation = sum(prediction_tempo[:3])
    probabilities = [pred/summation for pred in prediction_tempo[:3]]
    
    random_index = np.random.choice(np.arange(1, 4), p=probabilities)

    value = prediction.index(prediction_tempo[random_index])

    value = decrypt_value(value, word_to_ix)

    lyrics += value
    lyrics += " "
    
    

    word1 = word2
    word2 = value

  print(lyrics)


# In[ ]:





# In[ ]:




