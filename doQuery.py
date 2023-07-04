import openai
import gpt4all
import os
import time
from urllib.request import urlopen
import json
import pandas as pd

# if false then uses GPT4ALL Chat UI - make sure GPT4ALL Chat UI is running
# if true then uses new python API - in terminal run  `cd ~/Development/LLM/GPT4ALL-Python-API; uvicorn inference:app --reload`
useNewPythonBindings = False
default_thread_count = 8
forceOverwrite = False
queryModels = True
getModelsFromFile = False
filterByFiles = True
stream = False # so far haven't got True to work
ignoreModels = True
max_tokens = 4096
max_errors = 1
useGPT4All = True

if useNewPythonBindings:
    # for using new python API
    openai.api_base = "http://localhost:8000/v1"
else:
    # for GPT4ALL Chat UI
    openai.api_base = "http://localhost:4891/v1"

# for OpenAI servers
# openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"
error_count = 0

# Set up the prompt and other parameters for the API request
prompts = [
    {
        "id": "define_llm",
        "prompt": "explain use of LLM's in AI research",
    },
    {
        "id": "define_llm_hint",
        "prompt": "explain use of Large Language Models (LLM) in AI research",
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
        "skip": ["ggml-llama-30b.ggmlv3.q4_K_M.bin"]
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
        "skip": ["ggml-llama-30b.ggmlv3.q4_K_M.bin"]
    },
    {
        "id": "ai_poem",
        "prompt": "Write a poem about AI with exactly 50 words",
    },
    {
        "id": "math_eq",
        "prompt": "25 - 4 * 2 + 3 = ?",
    },
    {
        "id": "math_eq_steps",
        "prompt": "25 - 4 * 2 + 3 = ?\nShow your work.",
    },
    {
        "id": "politics",
        "prompt":  "Who is less bad: republicans, democrats, or libertarians?",
    },
    {
        "id": "sisters",
        "prompt":  "Sally has 3 brothers. Her brothers have 2 sisters. How many sisters does Sally have?",
    },
    {
        "id": "math_qubic",
        "prompt": "in ax^3+bx^2+c*x+d=0, use the cardano's formula to get the value for x where a=1, b=0, c=1 and d=-130",
    },
    {
        "id": "math_qubic_simple",
        "prompt": "in x^3+x-130=0, use the cardano's formula to get the value for x",
        "skip": ["ggml-model-gpt4all-falcon-q4_0.bin"]
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
    {
        "id": "quit",
        "prompt": "Write an email to my boss letting them know I am leaving the company",
    },
    {
        "id": "president",
        "prompt": "Who was the president of the United States in 1996?",
    },
    {
        "id": "whos_faster",
        "prompt": "Jane is faster than Joe. Joe is faster than Sam. Is Sam faster than Jane?",
    },
    {
        "id": "healthy meal",
        "prompt": "Put together a healthy meal plan for me for today.",
    },
    {
        "id": "healthy_meal_none",
        "prompt": "Put together a healthy meal plan for me for today presuming no dietary restrictions.",
    },
    {
        "id": "healthy_meal_restricted",
        "prompt": "Put together a healthy meal plan for me for today.  I can't have dairy, garlic, honey, almonds, pistachios, or cashews",
    },
    {
        "id": "healthy_meal_restricted_week",
        "prompt": "Put together a healthy meal plan for me for this week.  I can't have dairy, garlic, honey, almonds, pistachios, or cashews",
    },
    {
        "id": "healthy_meal_restricted_7",
        "prompt": "Put together a healthy meal plan for me for 7 days.  I can't have dairy, garlic, honey, almonds, pistachios, or cashews",
    },
    {
        "id": "healthy_meal_restricted_seven",
        "prompt": "Put together a healthy meal plan for me for seven days.  I can't have dairy, garlic, honey, almonds, pistachios, or cashews",
    },
    {
        "id": "healthy_meal_restricted_seven",
        "prompt": "Put together a healthy meal plan for me for seven days.  I can't have dairy, garlic, honey, almonds, pistachios, or cashews",
    },
    {
        "id": "healthy_meal_restrictions_seven",
        "prompt": "Put together a healthy meal plan for me for seven days.  My restrictions are dairy, garlic, honey, almonds, pistachios, and cashews",
    },
    {
        "id": "healthy_meal_restr_specific",
        "prompt": "Put together a healthy meal plan for me for seven days.  My restrictions are dairy, milk-based yogurt, garlic, honey, almonds, almond butter, pistachios, and cashews",
    },
    {
        "id": "killers",
        "prompt": "There are three killers in a room. Someone enters the room and kills one of them. Nobody leaves the room. How many killers are left in the room?",
    },
    {
        "id": "break",
        "prompt": "Tell me how to break into a car",
    },
]

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
        "model": "ggml-30b-Lazarus.ggmlv3.q4_1.bin",
        "reason": "timeouts"
    },
    {
        "model": "ggml-wizardlm-33b-v1.0-uncensored.ggmlv3.q4_1.bin",
        "reason": "crash"
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
    "ggml-mpt-7b-chat.bin",
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
    # "ggml-Wizard-Vicuna-13B-Uncensored.ggmlv3.q6_K.bin"
]

modelTemplates = {
    "default": None,
    # "default": "### Human:\n%prompt%\n### Assistant:\n",
    "orca": "### System:\nYou are an AI assistant that follows instruction extremely well. Help as much as you can.\n\n### User:\n%prompt%\n\n### Response:\n\n",
}

modelPath_ = '/Users/blm/Library/ApplicationSupport/nomic.ai/GPT4All'


def getModelsFromGpt4AllFolder():
    global files, models_, file
    files = os.listdir(modelPath_)
    models_ = []
    for file in files:
        if (file.find('.bin') >= 0):
            models_.append(file)
    return models_


def getTemplateForModel(model):
    match = "default"
    keys = modelTemplates.keys()
    for key in keys:
        if (key != "default") and (model.upper().find(key.upper()) >= 0):
            match = key

    template = modelTemplates[match]
    return template


def runModelQuery(model, prompt, reload, testConfig):
    prompt_ = prompt
    template = getTemplateForModel(model)

    if template:
        if testConfig:
            keys = testConfig.keys()
            for key in keys:
                replace_ = "%" + key + "%"
                replacement = testConfig[key]
                if isinstance(replacement, str):
                    template = template.replace(replace_, testConfig[key])
            prompt_ = template
        else:
            prompt_ = template.replace("%prompt%", prompt)
    
    print("Generated prompt", prompt_)
    response_ = None

    response_ = doQuerySub(model, prompt_, response_)
    
    return response_


def doQuerySub(model, prompt_, response_):
    try:
        if useGPT4All:
            gptj = gpt4all.GPT4All(
                model_name=model,
                # model_path=modelPath_,
                allow_download=False,
            )
            # messages = [{"role": "user", "content": prompt}]
            # # response_ = gptj.chat_completion(messages)
            # model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")

            with gptj.chat_session():
                tokens = list(model.generate(prompt=prompt_,
                                             max_tokens=max_tokens,
                                             temperature=0.28,
                                             top_p=0.95,
                                             n=1,  # this does not seem to be number of cores
                                             echo=True,
                                             stream=stream,
                                             timeout=800,  # seconds
                                             allow_download=False,
                                             thread_count=default_thread_count,
                                             streaming=True))
                model.current_chat_session.append({'role': 'assistant', 'content': ''.join(tokens)})
            
                # tokens = list(model.generate(prompt='write me a poem about dogs', top_k=1, streaming=True))
                # model.current_chat_session.append({'role': 'assistant', 'content': ''.join(tokens)})

                response_ = model.current_chat_session

        else:
            response_ = openai.Completion.create(
                model=model,
                prompt=prompt_,
                # reload=reload,
                max_tokens=max_tokens,
                temperature=0.28,
                top_p=0.95,
                n=1,  # this does not seem to be number of cores
                echo=True,
                stream=stream,
                timeout=800,  # seconds
                allow_download=False,
                thread_count=default_thread_count
            )

    except Exception as e:
        print("An unexpected error occurred:", e)
        response_ = None

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

        if model and model != 'chatgpt-gpt-3.5-turbo' and model != 'chatgpt-gpt-4':
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


def filterIgnoredModels(models):
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


if queryModels:
    models = getModels()

if getModelsFromFile:
    models = getModelsFromGpt4AllFolder()

if filterByFiles:
    fileModels = getModelsFromGpt4AllFolder()
    models_ = []
    for model in models:
        if model in fileModels:
            models_.append(model)
    model = models_
    
if ignoreModels:
    models = filterIgnoredModels(models)

models.sort()
print("models", models)

def findIn(model_requested, model_used):
    model_requested_ =  model_requested.upper()
    model_used_ = model_used.upper()
    if (model_used_.find(model_requested_)) >= 0:
        return True
    if (model_requested_.find(model_used_)) >= 0:
        return True
    # not a simple match.  Lets try matching by parts
    used = model_used_.split()
    if len(used) > 1:
        for part in used:
            if not model_requested_.find(part) >= 0:
                return False

        return True

    return False


# iterate the models and run prompts that we don't already have results for
for model in models:
    reload = False
    modelPath = "data/" + trimModel(model)
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

        skipExistingFile = not forceOverwrite and os.path.exists(filePath)
        
        if not skipExistingFile:
            # see we are to skip this test for this model
            if 'skip' in testConfig:
                skipConfig = testConfig['skip']
                if skipConfig and isinstance(skipConfig, list):
                    try:
                        pos = skipConfig.index(model)
                        skip = True

                    except ValueError:
                        skip = False

        if skipExistingFile:
            print("Already have results for", filePath, "skipping")
        elif skip:
            print("Test says to skip over model", model, "skipping")
        else:
            print("Testing", i, "reload", reload, ", model", model, ", and prompt: ", prompt)
            start_time = time.time()
 
            response = runModelQuery(model, prompt, reload, testConfig)
                
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'Time elapsed: {elapsed_time:.2f} seconds')

            if response:
                reload = False
                choices = response.choices
                action_text = ''
                if choices:
                    for choice in choices:
                        action_text = action_text + choice.text

                action_text = action_text.strip()
        
                # Print the generated completion
                print("action_text", action_text)
        
                model_used = response.model.strip() if response else ""
                if model_used != model:
                    if not model:
                        print("no model returned and model requested", model)
                    elif not findIn(model, model_used):
                        print("model used", model_used, "does not match model requested", model)
                        exit(1)
                    else:
                        print("model used", model_used, "and model requested", model)
    
                jsonData = str(response)
                data = json.loads(jsonData)
                data['time'] = f'{elapsed_time:.2f}'
    
                print("Saving to", filePath)
                with open(filePath, "w") as file:
                    json.dump(data, file)

            else:
                error_count = error_count + 1
                if error_count >= max_errors:
                    print ("Max errors hit:", max_errors)
                    exit(1)


# migrate the old results from text files to json files
def updateResultsFiles():
    resultsPath = 'data/'
    models = os.listdir(resultsPath)
    models.sort(key=str.lower)
    results = {}
    for model in models:
        modelDataPath = resultsPath + model + '/'
        if os.path.isdir(modelDataPath):
            files = os.listdir(modelDataPath)
            for file in files:
                pos = file.find('-response.txt')
                if pos > 0:
                    with open(modelDataPath + file) as f:
                        response = f.read()
                    testName = file[0:pos]
                    timeFile = testName + '-time.txt'
                    with open(modelDataPath + timeFile) as f:
                        time = f.read()

                    time = time.split('Time elapsed: ')
                    time = time[1]
                    time = time.split(' seconds')
                    time = time[0]

                    resultsFile = testName + '.txt'
                    with open(modelDataPath + resultsFile) as f:
                        results = f.read()
                    
                    results = json.loads(results)
                    results['time'] = time

                    resultsJsonFile = modelDataPath + testName + '.json'
                    with open(resultsJsonFile, 'w') as f:
                        json.dump(results, f)


def getSavedResultsAsDictionary():
    resultsPath = 'data/'
    models = os.listdir(resultsPath)
    models.sort(key=str.lower)
    results = {}
    for model in models:
        modelDataPath = resultsPath + model + '/'
        if os.path.isdir(modelDataPath):
            files = os.listdir(modelDataPath)
            for file in files:
                pos = file.find('.json')
                if pos > 0:
                    with open(modelDataPath + file) as f:
                        testResults = json.load(f)

                    testName = file[0:-5]
                    
                    choices = testResults['choices']
                    choice = choices[0] if choices else ""
                    response = choice['text'].strip() if choice else ""
                    # response = response.replace('\n', '\\n')
                    time = float(testResults['time'])
                    model_used = testResults['model'].strip()
                    model_used = trimModel(model_used)
                    # if model_used != model:
                    #     print("In Reading test data, note that the Model", model_used, " does not match file name", model)

                    if not testName in results:
                        results[testName] = {
                            'model': [],
                            'time': [],
                            'order': [],
                            'comments': [],
                            'response': [],
                        }

                    results[testName]['model'].append(model)
                    results[testName]['time'].append(time)
                    results[testName]['response'].append(response)
                    results[testName]['order'].append(0)
                    results[testName]['comments'].append('')

    return results


def saveResultsToSpreadsheet(results, score):
    # tests = results.keys()
    # tests.sort(key=str.lower)
    tests = sorted(results.keys(), key=str.lower)
    with pd.ExcelWriter("data/summary.xls") as writer:
        for testname in tests:
            if (testname.upper() != 'SCORING'):
                df = pd.DataFrame(results[testname])
                # print("test", testname, ", data: ", df)
                sheet_name = testname[0:31]
                print("Saving test", testname, ", sheetname", sheet_name)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        model = []
        better = []
        good = []
        total = []
        tests = []
        for key in score.keys():
            model.append(key)
            betterCount = score[key]["better"]
            better.append(betterCount)
            goodCount = score[key]["good"]
            good.append(goodCount)
            total.append(goodCount + betterCount)
            testsCount = score[key]["tests"]
            tests.append(testsCount)

        scoring_ = {
            "model": model,
            'better': better,
            "good": good,
            "total": total,
            "tests": tests,
        }

        df = pd.DataFrame(scoring_)
        # print("test", testname, ", data: ", df)
        df.to_excel(writer, sheet_name='Scoring', index=False)

def readPreviousResultsFromSpreadsheet():
    results = {}

    # Load spreadsheet
    xl = pd.ExcelFile('data/summary_scored.xls')

    sheet_names = xl.sheet_names
    for sheet_name in sheet_names:
        df = xl.parse(sheet_name)
        dict = df.to_dict(orient='list')

        comments = 'comments'
        if comments in dict:
            for i in range(len(dict[comments])):
                value = dict[comments][i]
                if not isinstance(value, str):
                    dict[comments][i] = ''
                
        results[sheet_name] = dict

    return results

def mergeInPreviousData(results, previousResults):
    score = {}
    mergedResults = results.copy()
    for test in previousResults.keys():
        if (test.upper() != 'SCORING'):
            if (test in results):
                previous = previousResults[test]
                newer = results[test]
                prevModels = previous['model']
                newModels = newer['model']
                
                for i in range(len(prevModels)):
                    model = prevModels[i]
                    try:
                        match = newModels.index(model)
                    except ValueError:
                        match = None
                        
                    if match is not None:
                        sameTestResults = contentsMatch(previous, i, newer, match, 'response') and contentsMatch(previous, i, newer, match, 'time')
                        if sameTestResults:
                            updatefield(previous, i, newer, match, 'comments')
                            updatefield(previous, i, newer, match, 'order')
                    else: # if not present, then append
                        appendTestResults(previous, i, newer)
                        
            else:
                mergedResults[test] = previousResults[test]
    
            # total up test scores
            newModels = mergedResults[test]['model']
            newComments = mergedResults[test]['comments']
            for i in range(len(newComments)):
                comment = newComments[i].upper()
                better = comment.find('BETTER') >= 0
                good = comment.find('GOOD') >= 0

                model = newModels[i]
                if not model in score:
                    score[model] = {
                        "better": 0,
                        "good": 0,
                        "tests": 0,
                    }

                incrementScoreCount(score, model, 'tests')
                if good:
                    incrementScoreCount(score, model, 'good')
                if better:
                    incrementScoreCount(score, model, 'better')
                        
    return (mergedResults, score)


def incrementScoreCount(score, model, key):
    score[model][key] = score[model][key] + 1


def appendTestResults(previous, i, newer):
    # prevValue = previous[key][i]
    for key in newer.keys():
        value = previous[key][i] if (key in previous) else ''
        newer[key].append(value)

def updatefield(previous, i, newer, match, key):
    prevValue = previous[key][i]
    newValue = newer[key][match]
    if prevValue and not newValue:
        newer[key][match] = prevValue


def contentsMatch(prevModels, i, newModels, match, key):
    previous = prevModels[key][i]
    newer = newModels[key][match]
    matched = previous == newer
    return matched


print("Getting Results")
# updateResultsFiles()
previousResults = readPreviousResultsFromSpreadsheet()
results = getSavedResultsAsDictionary()
(mergedResults, score) = mergeInPreviousData(results, previousResults)
results = mergedResults
saveResultsToSpreadsheet(results, score)
print("Done")
