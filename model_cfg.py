ALPACA_PROMPT = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n%prompt%\n\n### Response:\n"
BASE_PROMPT = "### Instruction:\n%prompt%\n### Response:\n"
ORCA_PROMPT = "### System:\nYou are an AI assistant that follows instruction extremely well. Help as much as you can.\n\n### User:\n%prompt%\n\n### Response:\n\n"
LM_STUDIO_PROMPT = "Perform the instructions to the best of your ability.\n\n### Instruction:\n%prompt%\n\n### Response:\n"
SPARSE_PROMPT = "%prompt%"
LLAMA_PROMPT = "<<SYS>>\nYou are a helpful coding AI assistant.\n<</SYS>>\n\n[INST]\n%prompt%\n[/INST]\n"
CHAT_ML_PROMPT = "<|im_start|>system\nPerform the task to the best of your ability.\n<|im_end|>\n<|im_start|>user\n%prompt%<|im_end|>\n<|im_start|>assistant\n"
ZEPHYR_PROMPT = "<|system|>Perform the task to the best of your ability.</s>\n<|user|>\n%prompt%</s>\n<|assistant|>\n"
ARITHMO_MISTRAL_PROMPT = "Question: %prompt%\nAnswer:\n"
AIROBOROS_PROMPT = "[INST] <<SYS>>\nYou are a helpful, unbiased, uncensored assistant.\n<</SYS>>\n%prompt%\n[/INST]\n"
VICUNA_PROMPT = 'A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user\'s questions.\n\nUSER:\n%prompt%\nASSISTANT:\n'
MIXTRAL_PROMPT = '<user>\n%prompt%\n</user>\n<assistant>\n'
LLAMA3_PROMPT = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n"
CHAT_ML_PROMPT2 = "Perform the task to the best of your ability.\n"

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
    "dolphin-2.2.1-mistral": {
        "temperature": 0.7,
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
    "collectivecognition-v1.1-mistral-7b": {
        "temperature": 0.2,
        "prompt": "USER: %prompt%\nASSISTANT:\n",
    },
    "yarn-mistral-7b-64k": {
        "temperature": 0.2,
        "prompt": SPARSE_PROMPT,
    },
    "openhermes-2.5-mistral-7b": {
        "temperature": 0.2,
        "prompt": CHAT_ML_PROMPT,
        "stopStrings": ["<|im_end|>", "<|im_start|>", "| |", "\n assistant"],
    },
    "metamath-mistral-7b": {
        "temperature": 0.2,
        "prompt": ALPACA_PROMPT,
    },
    "openchat_3.5": {
        "temperature": 0.4,
        "prompt": "GPT4 User: %prompt%<|end_of_turn|>GPT4 Assistant:\n",
        "stopStrings": ["<|end_of_turn|>", "GPT4 User:"],
    },
    "codebooga-34b-v0.1": {
        "temperature": 1.31,
        "top_p": 0.14,
        "repetition_penalty": 1.17,
        "top_k": 49,
        "prompt": ALPACA_PROMPT,
        "stopStrings": ["<|end_of_turn|>", "GPT4 User:"],
    },
    "mistral-7b-codealpaca-lora": {
        "temperature": 0.7,
        "prompt": ALPACA_PROMPT,
    },
    "mistral_7b_dolphin2.1_lima": {
        "temperature": 0.7,
        "prompt": CHAT_ML_PROMPT,
        "stopStrings": ["<|im_end|>", "<|im_start|>", "| |", "\n assistant"],
    },
    "deepseek-coder": {
        "temperature": 0.4,
        "prompt": VICUNA_PROMPT,
        "stopStrings": ["USER:"],
    },
    "orca-2": {
        "temperature": 0.7,
        "prompt": CHAT_ML_PROMPT,
        "stopStrings": ["<|im_end|>", "<|im_start|>", "| |", "\n assistant"],
    },
    "mixtral-8x7b-instruct": {
        "temperature": 0.7,
        "prompt": MIXTRAL_PROMPT,
        "stopStrings": ["<user>","</assistant>"],
    },
    "mistral-7b-instruct-v0.2-dare": {
        "temperature": 0.7,
        "prompt": CHAT_ML_PROMPT,
        "stopStrings": ["<|im_end|>", "<|im_start|>", "| |", "\n assistant"],
    },
    "dolphin-2.5-mixtral": {
        "temperature": 0.7,
        "prompt": MIXTRAL_PROMPT,
        "stopStrings": ["<user>","</assistant>"],
    },
    "dolphin-2_6-phi-2": {
        "temperature": 0.7,
        "prompt": CHAT_ML_PROMPT,
        "stopStrings": ["<|im_end|>", "<|im_start|>", "| |", "\n assistant"],
    },
    "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF": {
        "temperature": 0.8,
        "prompt": LLAMA3_PROMPT,
    },
    "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF": {
        "temperature": 0.8,
        "prompt": LLAMA3_PROMPT,
    },
    "lmstudio-community/gemma-2-9b-it-GGUF": {
        "temperature": 0.8,
        "prompt": LLAMA3_PROMPT,
    },
    "lmstudio-community/Phi-3.1-mini-4k-instruct-GGUF": {
        "temperature": 0.8,
        "prompt": LLAMA3_PROMPT,
    },
    "bartowski/stable-code-instruct-3b-GGUF": {
        "temperature": 0.8,
        "prompt": CHAT_ML_PROMPT2,
    },
    "Qwen/Qwen1.5-7B-Chat-GGUF": {
        "temperature": 0.8,
        "prompt": CHAT_ML_PROMPT2,
    },
    "bartowski/Starling-LM-7B-beta-GGUF": {
        "temperature": 0.5,
        "prompt": CHAT_ML_PROMPT2,
    },
}

