import openai
import os
import time

openai.api_base = "http://localhost:4891/v1"
# openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"

# Set up the prompt and other parameters for the API request
prompts = [
    "sisters_age: when I was 6, my sister was half my age. Now I am 80. How old is my sister now? Calculate this step by step.",
    "js_ascii: write a JavaScript program to generate and print out the ascii character and hexadecimal codes for 0 to 7f",
    "dry_socks: Tom washed 10 pairs of socks. The socks are now wet from the wash, so Tom hangs the 10 pairs of socks outside to dry. 10 hours later, he comes back outside to check on the socks. He feels each sock and notices they are all dry. He takes them back inside because they are all dry. How long will it take Tom to dry seven pairs of socks presuming the same weather conditions?" ,
    "TOT_socks: Three experts with exceptional logical thinking skills are collaboratively answering a question using a Tree of Thoughts method. Each expert will share their thought process in detail, taking into account the previous thoughts of others and emitting any errors. They will iteratively refine and expand upon each other's ideas, giving credit where it's due. The process continues until a conclusive answer is found. Organize the entire response in a markdown format. The question is, \"Tom washed 10 pairs of socks. The socks are now wet from the wash, so Tom hangs the 10 pairs of socks outside to dry. 10 hours later, he comes back outside to check on the socks. He feels each sock and notices they are all dry. He takes them back inside because they are all dry. How long will it take Tom to dry seven pairs of socks presuming the same weather conditions?\"",
    "railway: Explain origin of standard gauge for railways",
    "math_X_power: In 8^X+2^X=130 show how to solve for X",
    "math_qubic: in ax^3+bx^2+c*x+d=0, use the cardano's formula to get the value for x where a=1, b=0, c=1 and d=-130",
    "math_qubic_simple: in x^3+x-130=0, use the cardano's formula to get the value for x"
    "python_math: in ax^3+bx^2+c*x+d=0, write a python program to solve for all possible values of x",
]

# model = "gpt-3.5-turbo"
# model = "mpt-7b-chat"
models = [
    "gpt4all-j-v1.3-groovy",
    "mpt-7b-chat",
    "ggml-wizardLM-7B.ggmlv3.q8_0",
    "ggml-vic7b-q5_1",
    "ggml-vic13b-q8_0",
    "ggml-nous-gpt4-vicuna-13b",
    "ggml-nous-hermes-13b.ggmlv3.q6_K"
    "ggml-30b-Lazarus.ggmlv3.q5_1",
    "ggml-airoboros-33b-gpt4-1.2.ggmlv3.q4_1",
]


def queryModel(model, prompt):
    # Make the API request
    response_ = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=4096,
        temperature=0.28,
        top_p=0.95,
        n=1, # this does not seem to be number of cores
        echo=True,
        stream=False
    )

    return response_


for model in models:
    modelPath = "data/" + model
    if not os.path.exists(modelPath):
        # Create model directory if it does not exist
        os.mkdir(modelPath)

    for i in range(len(prompts)):
        parts = prompts[i].split(": ")
        fileName, prompt = parts
        filePath = modelPath + "/" + fileName + ".txt"

        if os.path.exists(filePath):
            print("Already have results for", filePath, "skipping")
        else:
            response = ''
            print("Testing", i, "model", model, ", and prompt: ", prompt)
            start_time = time.time()
        
            try:
                response = queryModel(model, prompt)
            except:
                response = 'Error'
                print("Error")
                
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'Time elapsed: {elapsed_time:.2f} seconds')

            # Print the generated completion
            print("Response", response)
    
            print("Saving to", filePath)
            with open(filePath, "w") as file:
                file.write(str(response))

            filePath2 = modelPath + "/" + fileName + "-time.txt"
            with open(filePath2, "w") as file:
                file.write(f'Time elapsed: {elapsed_time:.2f} seconds')

print("Done")
