import gpt4all

prompt = "when I was 6, my sister was half my age. Now I am 80. How old is my sister now? Calculate this step by step."
model = "ggml-mpt-7b-chat.bin"
# modelPath_ = '/Users/blm/Library/ApplicationSupport/nomic.ai/GPT4All'
modelPath_ = '/Volumes/T7/LLMs'

gptj = gpt4all.GPT4All(
    model_name=model,
    model_path=modelPath_,
    allow_download=True,
)
messages = [{"role": "user", "content": prompt}]
response_ = gptj.chat_completion(messages)
