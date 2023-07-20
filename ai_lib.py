import math
import openai
import gpt4all
import os
from urllib.request import urlopen
import json
import pandas as pd
import requests


def set_port(port):
    openai.api_base = "http://localhost:" + str(port) + "/v1"


def getModelsFromGpt4AllFolder(modelPath_):
    files = os.listdir(modelPath_)
    models_ = []
    for file in files:
        if (file.find('.bin') >= 0):
            models_.append(file)
    return models_


def getTemplateForModel(modelTemplates, model):
    match = "default"
    keys = modelTemplates.keys()
    for key in keys:
        if (key != "default") and (model.upper().find(key.upper()) >= 0):
            match = key

    template = modelTemplates[match]
    return template


def runModelQuery(model, prompt, reload, testConfig, modelTemplates, queryConfig):
    prompt_ = prompt
    template = getTemplateForModel(modelTemplates, model)

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

    response_ = doQuerySub(model, prompt_, response_, queryConfig)

    return response_


def doQuerySub(model, prompt_, response_, queryConfig):
    try:
        if queryConfig['noModelSelection']:
            url = openai.api_base + '/chat/completions'
            headers = {'Content-Type': 'application/json'}
            data = {
                # 'messages': [{'role': 'user', 'content': 'Introduce yourself.'}],
                'messages': [{'role': 'assistant', 'content': prompt_}],
                'temperature': 0.28,
                'max_tokens': -1,
                'stream': False
            }
            
            response = requests.post(url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                response_ = response.json()
                # Do something with the data
            else:
                print(f'An error occurred: {response.status_code}')
                
            # response_ = openai.Completion.create(
            #     # model=model,
            #     prompt=prompt_,
            #     # reload=reload,
            #     # max_tokens=queryConfig['max_tokens'],
            #     temperature=0.28,
            #     top_p=0.95,
            #     n=1,  # this does not seem to be number of cores
            #     echo=True,
            #     # stream=queryConfig['stream'],
            #     # timeout=800,  # seconds
            #     # allow_download=False,
            #     # thread_count=queryConfig['default_thread_count']
            # )

            # messages = [{"role": "user", "content": prompt}]
            # # response_ = gptj.chat_completion(messages)
        elif queryConfig['useGPT4All']:
            gptj = gpt4all.GPT4All(
                model_name=model,
                # model_path=modelPath_,
                allow_download=False,
            )
            # model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")

            with gptj.chat_session():
                tokens = list(model.generate(prompt=prompt_,
                                             max_tokens=queryConfig['max_tokens'],
                                             temperature=0.28,
                                             top_p=0.95,
                                             n=1,  # this does not seem to be number of cores
                                             echo=True,
                                             stream=queryConfig['stream'],
                                             timeout=800,  # seconds
                                             allow_download=False,
                                             thread_count=queryConfig['default_thread_count'],
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
                max_tokens=queryConfig['max_tokens'],
                temperature=0.28,
                top_p=0.95,
                n=1,  # this does not seem to be number of cores
                echo=True,
                stream=queryConfig['stream'],
                timeout=800,  # seconds
                allow_download=False,
                thread_count=queryConfig['default_thread_count']
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


def filterIgnoredModels(models, ignoredModels):
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


def filterByFilesInFolder(models, modelPath_):
    global model
    fileModels = getModelsFromGpt4AllFolder(modelPath_)
    models_ = []
    for model in models:
        if model in fileModels:
            models_.append(model)
    model = models_


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
                    response = ''
                    if choice:
                        if 'text' in choice:
                            response = choice['text']
                        if 'message' in choice:
                            response = choice['message']['content']
                        response = response.strip() if response else ""
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


def saveResultsToSpreadsheet(results, scores):
    # tests = results.keys()
    # tests.sort(key=str.lower)
    tests = sorted(results.keys(), key=str.lower)
    with pd.ExcelWriter("data/summary.xls") as writer:
        for testname in tests:
            if (testname.upper() != 'SCORING'):
                testResults = results[testname]
                newTestResults = sortTestResultsByModel(testResults)

                df = pd.DataFrame(newTestResults)
                # print("test", testname, ", data: ", df)
                sheet_name = testname[0:31]
                print("Saving test", testname, ", sheetname", sheet_name)
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        for scoreType, score in scores.items():
            model = []
            better = []
            good = []
            total = []
            tests = []
            averageTime = []
            sizes = []
            metals = []
            for key in score.keys():
                model.append(key)
                betterCount = score[key]["better"]
                better.append(betterCount)
                goodCount = score[key]["good"]
                good.append(goodCount)
                total.append(goodCount + betterCount)
                testsCount = score[key]["tests"]
                tests.append(testsCount)
                size = getKeyFromScore(score, key, "Size", '')
                sizes.append(size)
                metal = getKeyFromScore(score, key, "Metal", '')
                metals.append(metal)
                averageTime_ = score[key]["averageTime"]
                averageTime.append(round(averageTime_))

            scoring_ = {
                "model": model,
                'better': better,
                "good": good,
                "total": total,
                "tests": tests,
                "averageTime": averageTime,
                "Size": sizes,
                "Metal": metals,
            }

            df = pd.DataFrame(scoring_)
            # print("test", testname, ", data: ", df)
            sheet_name = 'Scoring' if scoreType == 'all' else 'Scoring-' + scoreType
            print("Saving scores, sheetname", sheet_name)
            df.to_excel(writer, sheet_name=sheet_name, index=False)


def sortTestResultsByModel(testResults):
    models = testResults['model']
    sorted_models = sorted(models, key=lambda x: x.lower())
    newTestResults = {}
    for model in sorted_models:
        pos = models.index(model)
        for key in testResults:
            if key not in newTestResults:
                newTestResults[key] = []
            value = testResults[key][pos]
            newTestResults[key].append(value)
    return newTestResults


def getKeyFromScore(score, key, key2, default):
    size = score[key][key2] if key2 in score[key] else default
    return size


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


def mergeInPreviousData(results, previousResults, testScoreSheets):
    scores = {}
    scoring = None
    mergedResults = results.copy()
    for test in previousResults.keys():
        if (test.upper().find('SCORING') < 0):
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

            for scoreType, filter in testScoreSheets.items():
                if scoreType not in scores:
                    scores[scoreType] = {}
                testScore = scores[scoreType]
                getTestScore(mergedResults, testScore, test, filter)

        elif (test.upper() == 'SCORING'):
            scoring = previousResults[test]

    for scoreType, testScoreSheets in scores.items():
        for model, modelResults in testScoreSheets.items():
            time = modelResults['time']
            count = modelResults['tests']
            modelResults['averageTime'] = time/count

            if scoring:
                try:
                    pos = scoring['model'].index(model)
                    if pos >= 0:
                        copyKeyValue(modelResults, scoring, "Size", pos)
                        copyKeyValue(modelResults, scoring, "Metal", pos)
                except ValueError:
                    pos = -1

    return (mergedResults, scores)


def copyKeyValue(modelResults, scoring, key, pos):
    if key in scoring:
        value = scoring[key][pos]
        if (isinstance(value, float)):
            value = value if not math.isnan(value) else ''
        modelResults[key] = value


def getTestScore(mergedResults, score, test, filter=None):
    includeTest = True
    if filter:
        includeTest = False
        filter_ = [filter.upper()] if isinstance(filter, str) else list(map(str.upper, filter))
        for f in filter_:
            if test.upper().find(f) >= 0:
                includeTest = True
                break

    if includeTest:
        # total up test scores
        newModels = mergedResults[test]['model']
        newComments = mergedResults[test]['comments']
        times = mergedResults[test]['time']

        for i in range(len(newComments)):
            comment = newComments[i].upper()
            time = float(times[i])
            better = comment.find('BETTER') >= 0
            good = comment.find('GOOD') >= 0

            model = newModels[i]
            if not model in score:
                score[model] = {
                    "better": 0,
                    "good": 0,
                    "tests": 0,
                    "time": 0,
                }

            incrementScoreCount(score, model, 'tests')
            incrementScoreCount(score, model, 'time', time)
            if good:
                incrementScoreCount(score, model, 'good')
            if better:
                incrementScoreCount(score, model, 'better')


def incrementScoreCount(score, model, key, incr = 1.0):
    newValue = score[model][key] + incr
    score[model][key] = newValue


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
