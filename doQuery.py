import openai
import os

openai.api_base = "http://localhost:4891/v1"
# openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"

# Set up the prompt and other parameters for the API request
prompts = ["js_ascii: write a JavaScript program to generate and print out the ascii character and hexadecimal codes for 0 to 7f",
           "sisters_age: when I was 6, my sister was half my age. Now I am 80. How old is my sister now? Calculate this step by step."]

# model = "gpt-3.5-turbo"
# model = "mpt-7b-chat"
models = ["gpt4all-j-v1.3-groovy", "mpt-7b-chat"]


def queryModel(model, prompt):
    # Make the API request
    response_ = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=4096,
        temperature=0.28,
        top_p=0.95,
        n=1,
        echo=True,
        stream=False
    )
    return response_


for model in models:
    # Create a new directory
    modelPath = "data/" + model
    if not os.path.exists(modelPath):
        os.mkdir(modelPath)

    for i in range(len(prompts)):
        parts = prompts[i].split(": ")
        fileName, prompt = parts
        filePath = modelPath + "/" + fileName + ".txt"

        if os.path.exists(filePath):
            print("Already have results for", filePath, "skipping")
        else:
            print("Testing", i, "model", model, ", and prompt: ", prompt)
            response = queryModel(model, prompt)
    
            # Print the generated completion
            print("Response", response)
    
            # Open a file for writing using with statement
            print("Saving to", filePath)
            with open(filePath, "w") as file:
                # Write some text to the file
                file.write(response)

print("Done")
