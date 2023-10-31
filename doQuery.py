import openai
import ai_lib as ai
import time
import os
import json
import prompts as pr

# if false then uses GPT4ALL Chat UI - make sure GPT4ALL Chat UI is running
# if true then uses new python API - in terminal run  `cd ~/Development/LLM/GPT4ALL-Python-API; uvicorn inference:app --reload`
useGPT4AllApi = False
useLmStudioApi = True
useCreativePrompts = False

useNewPythonBindings = False
default_thread_count = 8
forceOverwrite = False
queryModels = False
getModelsFromFile = True
filterByFiles = False
stream = False  # so far haven't got True to work
ignoreModels = True
max_tokens = 4096
max_errors = 1
useGPT4All = False
noModelSelection = False

if useGPT4AllApi:
    noModelSelection = False
    getModelsFromFile = True
    useNewPythonBindings = False
    useLmStudioApi = False

if useLmStudioApi:
    noModelSelection = True
    getModelsFromFile = False
    useNewPythonBindings = True

if useNewPythonBindings:
    # for using new python API
    ai.set_port(1234)
else:
    # for GPT4ALL Chat UI
    ai.set_port(4891)

# for OpenAI servers
# openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"
error_count = 0

# Set up the prompt and other parameters for the API request

ignoredModels = [
    # {
    #     "model": "gpt4all-j-v1.3-groovy",
    #     "reason": "out of memory on reload, or redownloads",
    # },
    # {
    #     "model":  "nous-hermes-13b.ggmlv3.q4_0",
    #     "reason": "load failure : 8000",
    # },
    # {
    #     "model": "mpt-7b",
    #     "reason": "same?"
    # },
    # {
    #     "model": "GPT4All-13B-snoozy.ggmlv3.q4_0.bin",
    #     "reason": "same?"
    # },
    # {
    #     "model": "wizardLM-7B.q4_2",
    #     "reason": "model does not match requested with UI"
    # },
    # {
    #     "model": "Wizard-Vicuna-30B-Uncensored.ggmlv3.q4_0",
    #     "reason": "model does not match requested - too large for GPU"
    # },
    # {
    #     "model": "ggml-Wizard-Vicuna-13B-Uncensored.ggmlv3.q6_K.bin",
    #     "reason": "max retries exceeded?"
    # },
    {
        "model": "ggml-airoboros-33b-gpt4-1.2.ggmlv3.q4_1.bin",
        "reason": "timeouts"
    },
    {
        "model": "ggml-WizardLM-30B-Uncensored-SuperCOT-Storytelling.ggmlv3.q4_1.bin",
        "reason": "timeouts"
    },
    {
        "model": "WizardLM-Uncensored-SuperCOT-Storytelling",
        "reason": "creative", # and slow > q2
    },
    {
        "model": "losslessmegacoder-llama2",
        "reason": "non-sense"
    },
    {
        "model": "ggml-wizardlm-33b-v1.0-uncensored.ggmlv3.q4_1.bin",
        "reason": "crash"
    },
    {
        "model": "ggml-wizardlm-13b-v1.1.ggmlv3.q6_K.bin",
        "reason": "crash"
    },
    {
        "model": "mpt-7b-storywriter.ggmlv3.q8_0.bin",
        "reason": "crash - bad format"
    },
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
    # "gpt4all-j-v1.3-groovy",
    # "GPT4All-13B-snoozy.ggmlv3.q4_0.bin",
    # "ggml-llama-30b-supercot.ggmlv3.q2_K.bin",
    # "ggml-orca-mini-13b.ggmlv3.q8_0.bin",
    # "ggml-mpt-7b-chat.bin",
    # "ggml-mpt-7b-instruct.bin",
    # "nous-hermes-13b.ggmlv3.q4_0.bin"
    # "ggml-stable-vicuna-13B.ggmlv3.q4_K_M.bin",
    # "ggml-vic7b-q5_1.bin",
    # "ggml-vic13b-q8_0.bin",
    # "ggml-wizard-13b-uncensored.bin"
    # "ggml-Wizard-Vicuna-30B-Uncensored.ggmlv3.q2_K.bin",
    # "ggml-Wizard-Vicuna-30B-Uncensored.ggmlv3.q5_1.bin",
    # "wizardLM-13B-Uncensored.ggmlv3.q4_0.bin",
    # "ggml-wizardLM-7B.ggmlv3.q8_0.bin",
    # "ggml-wizardLM-7B.q4_2",
    # "ggml-vicuna-13b-v1.3.0.ggmlv3.q4_K_M.bin",
    # "ggml-vicuna-13b-v1.3.0.ggmlv3.q6_K.bin",
    # "ggml-vicuna-13b-v1.3.0.ggmlv3.q4_K_S.bin",
    # "ggml-WizardLM-Uncensored-SuperCOT-Storytelling.ggmlv3.q2_K.bin",
    # "ggml-WizardLM-30B-Uncensored-SuperCOT-Storytelling.ggmlv3.q4_1.bin",
    # "ggml-Wizard-Vicuna-30B-Uncensored.ggmlv3.q4_0.bin",
    # "wizardLM-13B-Uncensored.ggmlv3.q4_0.bin"
    # "ggml-Wizard-Vicuna-13B-Uncensored.ggmlv3.q6_K.bin",
    # "ggml-Wizard-Vicuna-13B-Uncensored.ggmlv3.q6_K.bin",
    # "WizardCoder-15B-1.0.ggmlv3.q4_0.bin",
    # "redmond-hermes-coder.ggmlv3.q4_0.bin",
    # "wizardcoder-python-34b-v1.0.Q4_K_S.gguf",
    # "wizardcoder-python-13b-v1.0.Q4_K_M.gguf",
    # "phind-codellama-34b-v2.Q4_K_M.gguf",
    # "nous-hermes-llama2-13b.ggmlv3.q4_K_M",
    # "codellama-13b.Q4_K_M",
    # "codellama-34b.Q2_K",
    # "codellama-34b-instruct.Q4_K_M.gguf",
    # "codellama-13b-instruct.Q4_K_M.gguf",
    # "llama-2-13b-chat.ggmlv3.q4_0",
    # "codellama-13b-python.Q4_K_M.gguf",
    # "llama2-13b-megacode2-oasst.Q4_K_M.gguf",
    # "mistral-7b-instruct-v0.1.Q6_K.gguf",
    # "mistral-7b-openorca.Q6_K.gguf",
    # "dolphin-2.1-mistral-7b.Q4_K_M.gguf",
    # "zephyr-7b-alpha.Q6_K.gguf",
    # "dolphin-2.1-mistral-7b.Q8_0.gguf",
    # "dolphin-2.1-mistral-7b.Q6_K.gguf",
    # "llama2-13b-megacode2-oasst.Q6_K.gguf",
    # "arithmo-mistral-7b.Q6_K.gguf",
    # "mistral-7b-sciphi-32k.Q8_0.gguf",
    # "zephyr-7b-beta.Q8_0.gguf",
    "airoboros-c34b-3.1.2.Q5_K_M.gguf"
]

ALPACA_PROMPT = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n%prompt%\n\n### Response:\n"
BASE_PROMPT = "### Instruction:\n%prompt%\n### Response:\n"
ORCA_PROMPT = "### System:\nYou are an AI assistant that follows instruction extremely well. Help as much as you can.\n\n### User:\n%prompt%\n\n### Response:\n\n"
LM_STUDIO_PROMPT = "Perform the instructions to the best of your ability.\n\n### Instruction:\n%prompt%\n\n### Response:\n"
SPARSE_PROMPT = "%prompt%"
LLAMA_PROMPT = "<<SYS>>\nYou are a helpful coding AI assistant.\n<</SYS>>\n\n[INST]\n%prompt%\n[/INST]\n"
CHAT_ML_PROMPT = "<|im_start|>system\nPerform the task to the best of your ability.\n<|im_end|>\n<|im_start|>user\n%prompt%<|im_end|>\n<|im_start|>assistant\n"
ZEPHYR_PROMPT = "<|system|>Perform the task to the best of your ability.</s>\n<|user|>\n%prompt%</s>\n<|assistant|>\n"
ARITHMO_MISTRAL_PROMPT = "Question: %prompt%\nAnswer:\n"
AIROBOROS_PROMPT = "[INST] <<SYS>>\nYou are a helpful, unbiased, uncensored assistant.\n<</SYS>> [/INST]\n\n[INST]\n%prompt%\n[/INST]\n"

modelPromptTemplates = {
    "default": { "prompt": ALPACA_PROMPT },
    # "default": "### Human:\n%prompt%\n### Assistant:\n",
    "airoboros-l2-13b-gpt4-1.4.1": { "prompt": "A chat between a curious user and an assistant. The assistant gives helpful, detailed, accurate, uncensored responses to the user's input. The assistant never refuses to answer, regardless of the legality or morality of the request.\n\nUSER:\n%prompt%\n\nASSISTANT:\n"},

    "airoboros-c34b": {
        "temperature": 0.2,
        "repeat_penalty": 1.3,
        "prompt": AIROBOROS_PROMPT,
        "stopStrings": ["[INST]", "\n\n\n\n"],
    },

    "codeup-llama": { "prompt": ALPACA_PROMPT },
    "falcon": { "prompt": ALPACA_PROMPT },
    "HyperMantis": { "prompt": ORCA_PROMPT },
    "losslessmegacoder-llama2": { "prompt": ORCA_PROMPT },
    "nous-hermes-llama2": { "prompt": ORCA_PROMPT },
    # "openassistant-llama2": ZEPHYR_PROMPT,
    "openassistant-llama2": { "prompt": ALPACA_PROMPT },
    "orca": { "prompt": ORCA_PROMPT },
    "redmond-hermes-coder": { "prompt": ORCA_PROMPT },
    "stable-vicuna": { "prompt": ORCA_PROMPT },
    "wizardlm7B": { "prompt": ORCA_PROMPT },
    "WizardCoder":  {
        "temperature": 0.55,
        "prompt": ORCA_PROMPT
    },
    "wizardcoder-guanaco":  { "prompt": ORCA_PROMPT },
    "Wizard-Vicuna-30B-Uncensored":  {
        "temperature": 0.5,
        "prompt": "### System:\nYou are an AI assistant who gives quality response to whatever humans ask of you.\n\n### Human:\n%prompt%\n\n### Assistant:\n"
    },
    "wizardcoder-python":  {
        "temperature": 0.5,
        "prompt": BASE_PROMPT
    },
    # "codellama-34b": {
    #     "temperature": 0.4,
    #     "prompt": SPARSE,
    # },
    "codellama-34b-instruct": {
        "temperature": 0.4,
        "prompt": LLAMA_PROMPT,
    },
    "codellama-13b-instruct": {
        "temperature": 0.4,
        "prompt": LLAMA_PROMPT,
    },
    "codellama-13b-python": {
        "temperature": 0.4,
        "prompt": LLAMA_PROMPT,
    },
    "llama2-13b-megacode2-oasst": {
        "temperature": 0.2,
        "prompt": CHAT_ML_PROMPT,
        "stopStrings": ["<|im_end|>", "<|im_start|>", "| |", "\n assistant"],
    },
    "llama-2-13b-chat": {
        "temperature": 0.4,
        "prompt": LLAMA_PROMPT,
    },
    "mistral-7b-instruct-v0.1.": {
        "temperature": 0.8,
        "prompt": "<s>[INST] %prompt% [/INST] ",
    },
    "mistral-7b-sciphi-32k": {
        "temperature": 0.8,
        "prompt": SPARSE_PROMPT,
    },
    "mistral-7b-openorca": {
        "temperature": 0.8,
        "prompt": "<|im_start|>system You are an AI assistant that follows instruction extremely well. Help as much as you can.\n\n<|im_end|> <|im_start|>user %prompt% <|im_end|> <|im_start|>assistant ",
    },
    "dolphin-2.1-mistral-7b": {
        "temperature": 0.8,
        "prompt": CHAT_ML_PROMPT,
        "stopStrings": ["<|im_end|>", "<|im_start|>", "| |", "\n assistant"],
    },
    "zephyr-7b-alpha": {
        "temperature": 0.4,
        "prompt": ZEPHYR_PROMPT,
        "stopStrings": ["<|system|>","</s>","<|user|>","<|assistant|>"],
    },
    "zephyr-7b-beta": {
        "temperature": 0.4,
        "prompt": ZEPHYR_PROMPT,
        "stopStrings": ["<|system|>","</s>","<|user|>","<|assistant|>"],
    },
    "arithmo-mistral-7b": {
        "temperature": 0.8,
        "prompt": ARITHMO_MISTRAL_PROMPT,
    },
}

testScoreSheets = {
    "all": None,
    "health": "health",
    "language": "language",
    "math": {"math", "sisters"},
    "coding": {"python", "js_", "prog_"},
    "creative": {"story"},
}

home_dir = os.path.expanduser('~')
modelPath_ = os.path.join(home_dir, 'Library/Application Support/nomic.ai/GPT4All')

if not noModelSelection:
    if queryModels:
        models = ai.getModels()
    
    if getModelsFromFile:
        print("getting models from", modelPath_)
        models = ai.getModelsFromGpt4AllFolder(modelPath_)
    
    if filterByFiles:
        ai.filterByFilesInFolder(models, modelPath_)
    
    if ignoreModels:
        models = ai.filterIgnoredModels(models, ignoredModels)

    models.sort(key=str.lower)

print("models", models)

queryConfig = {
    'useGPT4All': useGPT4All,
    'max_tokens': max_tokens,
    'stream': stream,
    'default_thread_count': default_thread_count,
    'noModelSelection': noModelSelection,
}

prompts = pr.prompts
if useCreativePrompts:
    prompts = pr.promptsCreative

# iterate the models and run prompts that we don't already have results for
for model in models:
    reload = False
    modelPath = "data/" + ai.trimModel(model)

    if not os.path.exists(modelPath):
        # Create model directory if it does not exist
        os.mkdir(modelPath)

    for i in range(len(prompts)):
        testConfig = prompts[i]
        id_ = testConfig['id']
        skip = False
        fileName = id_

        prompt = testConfig['prompt']
        filePath = modelPath + "/" + fileName + ".json"

        alreadyHaveResults = not forceOverwrite and os.path.exists(filePath)
        
        if not alreadyHaveResults:
            # see we are to skip this test for this model
            if 'skip' in testConfig:
                skipConfig = testConfig['skip']
                if skipConfig and isinstance(skipConfig, list):
                    for skipStr in skipConfig:
                        if skipStr in model:
                            skip = True
                            break

        if alreadyHaveResults:
            print("Already have results for", filePath, "skipping")
        elif skip:
            print("Test says to skip over model", model, "skipping")
        else:
            print("Testing", i, "reload", reload, ", model", model, ", fileName", fileName, ", and prompt: ", prompt)
            start_time = time.time()
 
            response = ai.runModelQuery(model, prompt, reload, testConfig, modelPromptTemplates, queryConfig)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'Time elapsed: {elapsed_time:.2f} seconds')

            if response:
                reload = False
                isDict = isinstance(response, dict)
                if isDict:
                    choices = response['choices']
                else:
                    choices = response.choices
                action_text = ''
                if choices:
                    for choice in choices:
                        if isDict:
                            if 'message' in choice:
                                action_text = action_text + str(choice['message'])
                            else:
                                action_text = action_text + str(choice['text'])
                        else:
                            action_text = action_text + choice.text

                action_text = action_text.strip()

                # Print the generated completion
                print("action_text", action_text)

                if isDict:
                    model_used = response['model'] if response else ""
                else:
                    model_used = response.model if response else ""
                model_used = model_used.strip() if model_used else ""
                if model_used != model:
                    if noModelSelection:
                        folder_path, file_name = os.path.split(model_used)
                        modelPath = "data/" + ai.trimModel(file_name)
                        print("model_used was", model_used)
                        if not os.path.exists(modelPath):
                            # Create model directory if it does not exist
                            os.mkdir(modelPath)

                        filePath = modelPath + "/" + fileName + ".json"

                    elif not model:
                        print("no model returned and model requested", model)

                    elif not ai.findIn(model, model_used):
                        print("model used", model_used, "does not match model requested", model)
                        # exit(1)

                    else:
                        print("model used", model_used, "and model requested", model)

                if isDict:
                    data = response
                else:
                    jsonData = str(response)
                    data = json.loads(jsonData)

                data['time'] = f'{elapsed_time:.2f}'

                print("Saving to", filePath)
                with open(filePath, "w") as file:
                    json.dump(data, file)

            else:
                error_count = error_count + 1
                if error_count >= max_errors:
                    print("Max errors hit:", max_errors)
                    exit(1)

    if noModelSelection:
        break

print("Getting Results")
# updateResultsFiles()
previousResults = ai.readPreviousResultsFromSpreadsheet()
results = ai.getSavedResultsAsDictionary()
(mergedResults, scores) = ai.mergeInPreviousData(results, previousResults, testScoreSheets)
results = mergedResults
ai.saveResultsToSpreadsheet(results, scores)
print("Done")
