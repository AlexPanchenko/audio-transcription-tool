# Audio Transcription Tool

This is a demo project that lets you play with OpenAI Transcription API.

## Initial Configuration
Add you OpenAI Api Key to be able to call OpenAI API. You can use one the following options:
a) set OPENAI_API_KEY environment variable using your teminal
b) set value for OPENAI_API_KEY environment variable in the .env file for this project.


## Installing / Getting started

1. Create a Python 3 virtual environment:
```shell
python3 -m venv venv
```

2. Activate the virtual environment:
```shell
source venv/bin/activate
```

3. Install packages
```shell
pip install -r requirements.txt
```

4. Execute script
```shell
python3 speech_to_text.py sample.m4a 
```

Result text will be written to txt file.