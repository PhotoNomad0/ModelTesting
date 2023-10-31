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
        "id": "sisters_age_short",
        "prompt": "when I was 6, my sister was half my age. Now I am 80. How old is my sister now?",
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
        "skip": ["airoboros-c34b-3.1.2.Q5_K_M.gguf"]
    },
    {
        "id": "math_X_power",
        "prompt": "In 8^X+2^X=130 show how to solve for X",
        "skip": ["ggml-llama-30b.ggmlv3.q4_K_M.bin"]
    },
    {
        "id": "ai_poem",
        "prompt": "Write a poem about AI with exactly 50 words",
        "skip": ["airoboros-c34b-3.1.2.Q5_K_M.gguf"]
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
        "id": "math_number_clues",
        "prompt": "I am not a prime number.\nI am between 20 and 40.\nI am one more than a square number.\nWhat number am I?"
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
        "id": "sisters_explain",
        "prompt":  "Sally has 3 brothers. Her brothers have 2 sisters. How many sisters does Sally have? Explain your answer",
    },
    {
        "id": "sisters2",
        "prompt":  "Sally is a girl with 3 brothers. Her brothers have 2 sisters. How many sisters does Sally have?",
    },
    {
        "id": "sisters2_explain",
        "prompt":  "Sally is a girl with 3 brothers. Her brothers have 2 sisters. How many sisters does Sally have? Explain your answer",
    },
    {
        "id": "math_qubic",
        "prompt": "in ax^3+bx^2+c*x+d=0, use the cardano's formula to get the value for x where a=1, b=0, c=1 and d=-130",
        "skip": ["WizardCoder-15B-1.0"]
    },
    {
        "id": "math_qubic_simple",
        "prompt": "in x^3+x-130=0, use the cardano's formula to get the value for x",
        "skip": ["ggml-model-gpt4all-falcon-q4_0.bin", "WizardCoder-15B-1.0"]
    },
    {
        "id": "math_qubic_nohint",
        "prompt": "in x^3+x-130=0, solve for the value for x",
        "skip": ["ggml-model-gpt4all-falcon-q4_0.bin"]
    },
    {
        "id": "python_math",
        "prompt": "in ax^3+bx^2+c*x+d=0, write a python program to solve for all possible values of x",
    },
    {
        "id": "python_capitals",
        "prompt": "Python program\nWrite a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters",
    },
    {
        "id": "python_min_max",
        "prompt":  "Python program\nDefine a function named largest_difference that takes a list of numbers as its only parameter.\nYour function should compute and return the difference between the largest and smallest number in the list.",
    },
    {
        "id": "python_primes",
        "prompt":  "write a Python program to print out the first 100 prime numbers",
    },
    {
        "id": "python_insensitive_sort",
        "prompt":  "write a Python function to do a case insensitive sort of a list of strings",
    },
    {
        "id": "python_filter",
        "prompt":  "write a python function to filter out the empty strings in a list of strings.",
    },
    {
        "id": "python_read_sheet",
        "prompt":  "write a python function to read from a spreadsheet",
    },
    {
        "id": "python_read_excel",
        "prompt":  "write a python function to read from an excel spreadsheet.",
    },
    {
        "id": "python_plot",
        "prompt":  "in python make a plot that compares two columns in a dataframe.",
    },
    {
        "id": "python_ave_stddev",
        "prompt":  "in python calculate the average and standard deviation of a list of numbers",
    },
    {
        "id": "python_ave_stddev2",
        "prompt":  "Write a python function to calculate the average and standard deviation of a list of numbers",
    },
    {
        "id": "dry_socks",
        "prompt": "Tom washed 10 pairs of socks. The socks are now wet from the wash, so Tom hangs the 10 pairs of socks outside to dry. 10 hours later, he comes back outside to check on the socks. He feels each sock and notices they are all dry. He takes them back inside because they are all dry. How long will it take Tom to dry seven pairs of socks presuming the same weather conditions?" ,
    },
    {
        "id": "TOT_socks",
        "prompt": "Three experts with exceptional logical thinking skills are collaboratively answering a question using a Tree of Thoughts method. Each expert will share their thought process in detail, taking into account the previous thoughts of others and emitting any errors. They will iteratively refine and expand upon each other's ideas, giving credit where it's due. The process continues until a conclusive answer is found. Organize the entire response in a markdown format. The question is, \"Tom washed 10 pairs of socks. The socks are now wet from the wash, so Tom hangs the 10 pairs of socks outside to dry. 10 hours later, he comes back outside to check on the socks. He feels each sock and notices they are all dry. He takes them back inside because they are all dry. How long will it take Tom to dry seven pairs of socks presuming the same weather conditions?\"",
        "skip": ["wizardcoder-guanaco", "openassistant-llama2-13b-orca-8k-3319"]
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
        "id": "presidents",
        "prompt": "Create a csv of the first 5 presidents of the United states with their names, age when they started office, year they started office, and number of years they served",
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
    {
        "id": "language_metonymy",
        "prompt": "what is a metonymy?",
    },
    {
        "id": "language_merism",
        "prompt": "what is a merism?",
    },
    {
        "id": "language_figures",
        "prompt": "what are the categories of figures of speech?",
    },
    {
        "id": "language_hendiadys",
        "prompt": "what is a Hendiadys?",
    },
    {
        "id": "language_verb_types",
        "prompt": "what are the types of verbs?",
    },
    {
        "id": "language_verb_tenses",
        "prompt": "what are the verb tenses?",
    },
    {
        "id": "linux_ssh",
        "prompt": "what does this command do: ssh -i \"~/UserKey.pem\" -C -L 25900:localhost:5900 user@ec2-34-221-131-108.us-west-2.compute.amazonaws.com",
    },
    {
        "id": "linux_ssh_troubleshoot",
        "prompt": "why does this command give error Permission denied (publickey):\n\nssh -i \"~/UserKey.pem\" -C -L 25900:localhost:5900 ec2-34-221-131-108.us-west-2.compute.amazonaws.com",
    },
    {
        "id": "prog_css",
        "prompt": "How do you align a row of divs to the right using flex in css?  Show me an example."
    },
    {
        "id": "js_sort",
        "prompt":  "In javascript output the values in a dictionary sorted by key alphabetically.",
    },
    {
        "id": "prog_excel",
        "prompt":  "For libreoffice calc write an expression to copy contents from another cell and remove all single quotes",
    },
    {
        "id": "python_sql",
        "prompt":  "in python, using sqlite, get all records where field age is greater than 32"
    },
    {
        "id": "js_localstorage",
        "prompt":  "in javascript how do you save to and read back from localstorage",
    },
    {
        "id": "js_save",
        "prompt":  "in a javascript web app, how do you save text to a local file",
    },
    {
        "id": "prog_regex",
        "prompt":  "create a regex expression to extract a three character code like \"1Jn\" from a filename in format \"57-1Jn.usfm\".  The characters can be upper or lower case letters or digits. And the filename extension must be \".usfm\".",
    },
    {
        "id": "js_regex",
        "prompt":  "create a javascript function that uses regex to extract a three character code like \"1Jn\" from a filename in format \"57-1Jn.usfm\".  The characters can be upper or lower case letters or digits. And the filename extension must be \".usfm\".",
    },
    {
        "id": "python_thousands",
        "prompt":  "Write a python function named format_number that takes a number as its only parameter.\nYour function should convert the number to a string and add commas as a thousands separator."
    },
    {
        "id": "prog_json",
        "prompt":  "Create a JSON for the following. There are three people, two males. One is Mark, another is Joe. Third person who's a woman is Sam. The woman is 30 and two men are both 19."
    },
    {
        "id": "python_number_clues",
        "prompt": "Write a python program to solve this math problem: \"I am not a prime number.\nI am between 20 and 40.\nI am one more than a square number.\nWhat number am I?\""
    },
    {
        "id": "python_regex",
        "prompt":  "Create a python function that uses regex to extract a three character code like \"1Jn\" from a filename in format \"57-1Jn.usfm\".  The characters can be upper or lower case letters or digits. And the filename extension must be \".usfm\".  The function must catch any exceptions and return None",
    },
]

promptsCreative = [
    {
        "id": "story_gilligan",
        "prompt": "write an episode for Gilligan's Island"
    },
    {
        "id": "story_gilligan",
        "prompt": "write an episode for Lost in Space"
    }
]
