import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

print("hi")
model_name = 'gpt2'
print("hi2")
model = AutoModelForCausalLM.from_pretrained(model_name)
print("hi3")
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("hi4")

input_text = "how are you? tell me a nice fact?"
print("hi5")
inputs = tokenizer(input_text, return_tensors='pt')
print("hi6")
print(inputs)
print("hi7")

outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))