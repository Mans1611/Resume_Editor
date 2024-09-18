from transformers import BertTokenizer, BertModel,BertConfig
import torch
import torch.nn as nn
import torch.nn.functional as F


vocab_size = 30522        ## default for BERT model
max_length = 768  
model_name = 'bert-base-uncased'

config = BertConfig.from_pretrained(model_name)  
config.max_position_embeddings = max_length   ## here I change the postion embedding of the bert model, to be able to be added with the tokens embedding tokens.

class Expand_Embedding(nn.Module):
    def __init__(self,vocab_size=vocab_size,hidden_dim=512):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size,hidden_dim)
    
    def forward(self,text):
        return self.embedding(text)
class Embedding:
    '''
        This Class is using the Bert Model to encode the text into embedding of dimnsion of (n,768,768)
        where: 
            n -> is the batch size e.g (number of text, or number of resumes), in our case it will be 1 in most case.
            dim = 1 ,768 -> the max length of the string (number of tokens), default from bert is almost 30566, wich is the default unique words the the model train on.
            dim = 2 ,768 -> each token representation into embedding for example word: building ->is represented by 768 embedding vector, which is the dim=2.
    '''
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)  # getting the tokenizer which splits the sentences into tokens (subwords)
        self.bert_model = BertModel(config=config)                  # converting the words_id into embedding 
    
    def get_embedding(self,text):
        '''
            This function take a text as an input and convert it to embedding tensor 
            parameters :
                text (str) : the text that will be embedded.
            
            return:
                tensor(torch.Tensor):(n,768,768)
        '''
        tokens = self.tokenizer(text,return_tensors='pt',padding='max_length',max_length=max_length)
        
        with torch.no_grad():   ## stopping the gradient, I just want to get embedding, without adjusting the weights
            output = self.bert_model(**tokens)
            embedding = output.last_hidden_state ## here the last hiddent state is the output of the last layer 
        return embedding
    

 
if __name__ == '__main__':
    embeder = Embedding()
    tokens = embeder.get_embedding("mansour how are you doing")
    print(tokens.shape)