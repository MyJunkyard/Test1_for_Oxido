# Test1_for_Oxido

## Script use
### Instalation: 
```pip install -r requirements.txt```

### Script run: 
```python image_paste.py```

Important: script needs an OpenAI API key stored in an .env file under the following variable:
```OPENAI_API_KEY```

### Tests run: 
```python -m pytest test_image_paste.py -v```

## Description
The script takes a raw text file and converts it into HTML code using OpenAI API with gpt-4o-mini model. OpenAI API is also used to place image placeholders with context-relevant captions and promt proposition for AI image generation.

### Outputs:
1. artykul.html containing just the inside of a <body> tag as per request.
2. podglad.html embedding the above in a fully functional html file for review purpose.

Input and output files names are predefined inside the code in 'config' dictionary enabling easy further development if specific input and output options are needed.
