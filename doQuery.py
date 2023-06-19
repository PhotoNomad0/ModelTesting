import openai

openai.api_base = "http://localhost:4891/v1"
# openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"

# Set up the prompt and other parameters for the API request
prompts = ["write a JavaScript program to generate and print out the ascii character and hexadecimal codes for 0 to 7f",
           "when I was 6, my sister was half my age. Now I am 80. How old is my sister now? Calculate this step by step."]

# model = "gpt-3.5-turbo"
# model = "mpt-7b-chat"
models = ["gpt4all-j-v1.3-groovy", "mpt-7b-chat"]


def queryModel(model, prompt):
    # Make the API request
    response_ = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=50,
        temperature=0.28,
        top_p=0.95,
        n=1,
        echo=True,
        stream=False
    )
    return response_


for model in models:
    for prompt in prompts:
        print("Testing model", model, " and prompt", prompt)
        response = queryModel(model, prompt)

        # Print the generated completion
        print("Response", response)

print("Done")
