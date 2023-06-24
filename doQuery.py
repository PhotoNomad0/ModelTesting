import openai
import gpt4all
import os
import time
from urllib.request import urlopen
import json

usePythonBindings = True

if usePythonBindings:
    # for GPT4ALL Chat UI
    openai.api_base = "http://localhost:8000/v1"
else:
    # for GPT4ALL Chat UI
    openai.api_base = "http://localhost:4891/v1"

# for OpenAI servers
# openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"


# Set up the prompt and other parameters for the API request
prompts = [
    {
        "id": "define_llm",
        "prompt": "explain use of LLM's in AI research",
    },
    {
        "id": "sisters_age",
        "prompt": "when I was 6, my sister was half my age. Now I am 80. How old is my sister now? Calculate this step by step.",
    },
    {
        "id": "math_story_steps",
        "prompt": "In Science class, Sara needed 8 test tubes for 3 different experiments. The first experiment required 2 test tubes and the other two experiments required the same number of test tubes. How many test tubes were needed for each of the other two experiments?",
    },
    {
        "id": "math_story_geometric",
        "prompt": "Harmony used discarded paper to make notepads for her friends. She would fold five letter size pieces of paper three times then cut along the lines. She would then stack the smaller note papers and staple them together. How long would one notepad last if someone wrote ten notes per day?",
    },
    {
        "id": "math_story_rate",
        "prompt": "Before Cam broke his right arm, he was able to type 9 words per minute on his phone.  After he broke his arm, he had to use his left hand for a while, and he could only type 6 words per minute. What is the difference between the number of words he could type in 5 minutes before and after he broke his arm",
    },
    {
        "id": "math_division",
        "prompt": "In the morning, Emily decided to create some designs with her cereal bits. In total, she created 9 designs and used 63 cereal bits. About how many cereal bits were in each design? Do you think she used an equal number of cereal bits in each design?",
    },
    {
        "id": "js_ascii",
        "prompt": "write a JavaScript program to generate and print out the ascii character and hexadecimal codes for 0 to 7f",
    },
    {
        "id": "railway",
        "prompt": "Explain origin of standard gauge for railways",
    },
    {
        "id": "math_X_power",
        "prompt": "In 8^X+2^X=130 show how to solve for X",
    },
    {
        "id": "math_qubic",
        "prompt": "in ax^3+bx^2+c*x+d=0, use the cardano's formula to get the value for x where a=1, b=0, c=1 and d=-130",
    },
    {
        "id": "math_qubic_simple",
        "prompt": "in x^3+x-130=0, use the cardano's formula to get the value for x"
    },
    {
        "id": "python_math",
        "prompt": "in ax^3+bx^2+c*x+d=0, write a python program to solve for all possible values of x",
    },
    {
        "id": "dry_socks",
        "prompt": "Tom washed 10 pairs of socks. The socks are now wet from the wash, so Tom hangs the 10 pairs of socks outside to dry. 10 hours later, he comes back outside to check on the socks. He feels each sock and notices they are all dry. He takes them back inside because they are all dry. How long will it take Tom to dry seven pairs of socks presuming the same weather conditions?" ,
    },
    {
        "id": "TOT_socks",
        "prompt": "Three experts with exceptional logical thinking skills are collaboratively answering a question using a Tree of Thoughts method. Each expert will share their thought process in detail, taking into account the previous thoughts of others and emitting any errors. They will iteratively refine and expand upon each other's ideas, giving credit where it's due. The process continues until a conclusive answer is found. Organize the entire response in a markdown format. The question is, \"Tom washed 10 pairs of socks. The socks are now wet from the wash, so Tom hangs the 10 pairs of socks outside to dry. 10 hours later, he comes back outside to check on the socks. He feels each sock and notices they are all dry. He takes them back inside because they are all dry. How long will it take Tom to dry seven pairs of socks presuming the same weather conditions?\"",
    },
]

ignoredModels = [
    # {
    #     "model": "gpt4all-j-v1.3-groovy",
    #     "reason": "out of memory on reload, or redownloads",
    # },
    # {
    #     "model": "mpt-7b",
    #     "reason": "same?"
    # },
]

# model = "gpt-3.5-turbo"
# model = "mpt-7b-chat"
models = [
    # "ggml-30b-Lazarus.ggmlv3.q4_1.bin",
    # "ggml-30b-Lazarus.ggmlv3.q5_1.bin"
    # "ggml-airoboros-33b-gpt4-1.2.ggmlv3.q2_K.bin",
    # "ggml-airoboros-33b-gpt4-1.2.ggmlv3.q5_0.bin",
    # "ggml-airoboros-33b-gpt4-1.2.ggmlv3.q4_1.bin",
    # "ggml-chronos-hermes-13b.ggmlv3.q8_0.bin",
    # "GPT4All-13B-snoozy.ggmlv3.q4_0.bin",
    # "ggml-llama-30b-supercot.ggmlv3.q2_K.bin",
    # "nous-hermes-13b.ggmlv3.q4_0.bin"
    # "ggml-vic7b-q5_1.bin",
    # "ggml-vic13b-q8_0.bin",
    # "ggml-wizard-13b-uncensored.bin"
    # "ggml-Wizard-Vicuna-30B-Uncensored.ggmlv3.q2_K.bin",
    # "ggml-Wizard-Vicuna-30B-Uncensored.ggmlv3.q5_1.bin",
    # "wizardLM-13B-Uncensored.ggmlv3.q4_0.bin",
    # "ggml-wizardLM-7B.ggmlv3.q8_0.bin",
    # "ggml-WizardLM-Uncensored-SuperCOT-Storytelling.ggmlv3.q2_K.bin",
    
    "ggml-WizardLM-30B-Uncensored-SuperCOT-Storytelling.ggmlv3.q4_1.bin",
    "ggml-mpt-7b-instruct.bin",
    "ggml-Wizard-Vicuna-30B-Uncensored.ggmlv3.q4_0.bin",
    "ggml-Wizard-Vicuna-13B-Uncensored.ggmlv3.q6_K.bin"
    
    # "ggml-gpt4all-j-v1.3-groovy.bin",
    # "ggml-mpt-7b-chat.bin",

#     "wizardLM-7B.ggmlv3.q8_0",
#     "vic7b-q5_1",
#     "ggml-vic13b-q8_0",
#     "nous-gpt4-vicuna-13b",
#     "nous-hermes-13b.ggmlv3.q6_K"
#     "30b-Lazarus.ggmlv3.q5_1",
#     "airoboros-33b-gpt4-1.2.ggmlv3.q4_1",
]

modelPath_ = '/Users/blm/Library/ApplicationSupport/nomic.ai/GPT4All'

# files = os.listdir(modelPath_)
# models = []
# for file in files:
#     if (file.find('.bin') >= 0):
#         models.append(file)
# print("Models found", models)

def runModelQuery(model, prompt, reload):
    # gptj = gpt4all.GPT4All(
    #     model_name=model,
    #     model_path=modelPath_,
    #     allow_download=False,
    # )
    # messages = [{"role": "user", "content": prompt}]
    # response_ = gptj.chat_completion(messages)

    # # Make the API request
    # # NOTE: only seems to work with bundled models, not any side-loaded
    response_ = openai.Completion.create(
        model=model,
        prompt=prompt,
        # reload=reload,
        max_tokens=4096,
        temperature=0.28,
        top_p=0.95,
        n=1, # this does not seem to be number of cores
        echo=True,
        stream=False,
        timeout=1800, # seconds
        allow_download=False,
    )

    return response_


def getModels():
    # fetch the models
    response = urlopen(openai.api_base + '/models')
    data_json = json.loads(response.read())
    # print the json response
    print("models=", data_json)
    models = []
    for item in data_json['data']:
        if 'filename' in item:
            model = item['filename']
            root_ = model
        else:
            model = item['id']
            root_ = item['root']

        print("id", model, ", root", root_)

        if model != 'chatgpt-gpt-3.5-turbo' and model != 'chatgpt-gpt-4':
            models.append(model)
        if model != root_:
            print("differs!")
    
    return models


def trimModel(model):
    name = model
    length = len(name)
    
    if (name.find('.bin') > 0):
        name = name[0:length-4]

    if (name.find('ggml-') == 0):
        name = name[5:]
        
    return name


def filter(models):
    list = []
    for model in models:
        found = False
        for ignore in ignoredModels:
            if model.find(ignore['model']) >= 0:
                found = True
        
        if not found:
            list.append(model)
        else:
            print("Skipping model", model)
            
    return list


# models = getModels()

models = filter(models)
print("models", models)

for model in models:
    reload = False
    modelPath = "data/" + trimModel(model)
    if not os.path.exists(modelPath):
        # Create model directory if it does not exist
        os.mkdir(modelPath)

    for i in range(len(prompts)):
        prompt_ = prompts[i]
        id_ = prompt_['id']
        fileName = id_
        prompt = prompt_['prompt']
        filePath = modelPath + "/" + fileName + ".txt"

        if os.path.exists(filePath):
            print("Already have results for", filePath, "skipping")
        else:
            response = ''
            print("Testing", i, "reload", reload, ", model", model, ", and prompt: ", prompt)
            start_time = time.time()
 
            # try:
            response = runModelQuery(model, prompt, reload)
            # except:
            #     response = 'Error'
            #     print("Error")
            #     exit(0)
                
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'Time elapsed: {elapsed_time:.2f} seconds')

            reload = False
            choices = response.choices
            choice = choices[0] if choices else ""
            action_text = choice.text.strip() if choice else ""
    
            # Print the generated completion
            print("action_text", action_text)
    
            model_used = response.model.strip() if response else ""
            if model_used != model:
                print("model used", model_used, "does not match model requested", model)

            print("Saving to", filePath)
            with open(filePath, "w") as file:
                file.write(str(response))

            filePath2 = modelPath + "/" + fileName + "-response.txt"
            with open(filePath2, "w") as file:
                file.write(str(action_text))

            filePath3 = modelPath + "/" + fileName + "-time.txt"
            with open(filePath3, "w") as file:
                file.write(f'Time elapsed: {elapsed_time:.2f} seconds')

print("Done")
