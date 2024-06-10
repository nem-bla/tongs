## <span style="color:blue">tongs</span>

Description
________________________

- This is a ChatGPT powered language translator. 
- it uses the ChatGPT 3.5 Turbo model due to its low cost.
- it accepts an origin, target, and text variables to send to ChatGPT through the API. 
- it stores the previous translations locally in translations.json, allowing users to view all previous translations executed. 

Images
________________________
- Base Application

![Alt Text](https://github.com/nem-bla/tongs/blob/master/images/app.png?raw=true)

- Translation

![Alt Text](https://github.com/nem-bla/tongs/blob/master/images/translation.png?raw=true)

- Tranlsation History

![Alt Text](https://github.com/nem-bla/tongs/blob/master/images/history.png?raw=true)

Installation
________________________

- Clone the repository

```bash
    git clone https://github.com/nem-bla/tongs.git
```

- cd into the directory, install openair and python-dotenv with pip

```bash
    cd translator-app
    pip install openai python-dotenv
```

- create a file named .env in the project directory and add you OpenAI API key:

```
    OPENAI_API_KEY=your_openai_api_key
```

- run the application

```bash
    python main.py
```


Usage
________________________
- insert how to use the project


