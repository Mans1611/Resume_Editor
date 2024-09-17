import torch.nn as nn
import torch.nn.functional as F
from transformers import BertTokenizer, BertModel
model_name = 'bert-base-uncased'


class Embedding:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.bert_model = BertModel.from_pretrained(model_name)
    
    def get_embedding(self,text):
        tokens = self.tokenizer(text,return_tensor='pt',padding=True,max_length=500)
        return tokens 
    
    
if __name__ == '__main__':
    print('hello')