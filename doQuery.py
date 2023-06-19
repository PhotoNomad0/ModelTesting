import openai

openai.api_base = "http://localhost:4891/v1"
#openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"

# Set up the prompt and other parameters for the API request
prompts = ["Who is Michael Jordan?"]

# model = "gpt-3.5-turbo"
#model = "mpt-7b-chat"
models = ["gpt4all-j-v1.3-groovy", "mpt-7b-chat"]


def queryModel(model, prompt):
    # Make the API request
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=50,
        temperature=0.28,
        top_p=0.95,
        n=1,
        echo=True,
        stream=False
    )
    return response

for model in models:
    for prompt in prompts:
        print ("Testing model", model," and prompt", prompt)
        response = queryModel(model, prompt)

        # Print the generated completion
        print(response)
        
print("Done")
