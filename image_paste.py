import os
from openai import OpenAI
import codecs

config = {
        "input_file_name": "Zadanie dla JJunior AI Developera - tresc artykulu.txt",
        "output_file_name": "artykul.html",
        "template_file_name": "szablon.html",
        "full_html_file_name": "podglad.html",
        "encoding": "UTF-16"
    }


def get_input_text(source_file_name: str) -> str:
    with open(source_file_name, "r") as raw_text_file_handle:
        raw_text = raw_text_file_handle.read()
    if raw_text == "":
        raise ValueError(f"File {source_file_name} has no content.")
    return raw_text


def generate_article_html(raw_article_text: str, encoding: str) -> str:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f'''You are a experienced frontend developer.
                HTML you write is always well-structured, standard-compliant, semantic, valid and accessible.
                Encode the output in {encoding}.
                Add proper HTML tags to the text given by user to make it a content of a an article.
                Make sure not to include any tags outside of <article>.
                Do not prefix the article with "html" string.
                Also, find good places for adding images to the article and annote them with <img src="image_placeholder.jpg" alt=""> 
                and fill in the alt atrribute with a promt suggestion for creating an appropriate image.
                Wrap img tags in <figure> and generate appropriate captions.'''
            },
            {
                "role": "user",
                "content": raw_article_text,
            }
        ],
        model="gpt-4o-mini",
    )
    return chat_completion.choices[0].message.content


def write_output_html(html: str, output_file_name: str, encoding: str):
    with codecs.open(output_file_name, "w", encoding) as output_file_handle:
        output_file_handle.write(html)


def fill_template(template: str, content: str) -> str:
    return template.replace("<body></body>", "<body>\n"+content+"\n</body>")


def main(config: dict):
    input_text = get_input_text(config["input_file_name"])
    html = generate_article_html(input_text, config["encoding"])
    write_output_html(html, config["output_file_name"], config["encoding"])

    template = get_input_text(config["template_file_name"])
    full_html = fill_template(template, html)
    write_output_html(full_html, config["full_html_file_name"], config["encoding"])


if __name__ == "__main__":
    main(config)
