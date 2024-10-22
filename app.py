# importing the PEGASUS Transformer model
import streamlit as st
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from sentence_splitter import SentenceSplitter
#  split_text_into_sentences

#initialize model
model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)


# setting up the model and function definition for model
def get_response(input_text, num_return_sequences):
    batch = tokenizer.prepare_seq2seq_batch([input_text], truncation=True, padding='longest', max_length=60,
                                            return_tensors="pt").to(torch_device)
    translated = model.generate(**batch, max_length=60, num_beams=10, num_return_sequences=num_return_sequences,
                                temperature=1.5)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text


# test input sentence
text = ""

# printing response
get_response(text, 5)

get_response(text, 1)

# Takes the input paragraph and splits it into a list of sentences
# from sentence_splitter import SentenceSplitter, split_text_into_sentences

# Do a for loop to iterate through the list of sentences and paraphrase each sentence in the iteration

st.title("Paraphrasing: ")
context = st.text_area("Enter your text: ")
st.write(text)

# Takes the input paragraph and splits it into a list of sentences
splitter = SentenceSplitter(language='en')
sentence_list = splitter.split(context)
# Do a for loop to iterate through the list of sentences and paraphrase each sentence in the iteration
paraphrase = []

for i in sentence_list:
    a = get_response(i, 1)
    paraphrase.append(a)
# creating the second split
paraphrase2 = [' '.join(x) for x in paraphrase]

# Combine the above split lists into a paragraph
paraphrase3 = [' '.join(x for x in paraphrase2)]
paraphrased_text = str(paraphrase3).strip('[]').strip("'")
# paraphrased_text # Comparison of the original (context variable) and the paraphrased version (paraphrase3 variable)

st.write(paraphrased_text)
