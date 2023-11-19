from gpt4all import GPT4All

class GenerativeAI:
    def interact(self, prompt):
        input = "Give me two chapters titles about this: {}".format(prompt)

        print(input)
        # print("please wait...")
        model = GPT4All(model_name="gpt4all-13b-snoozy-q4_0.gguf", model_path="/Users/sebastian.williams/Github/youtube-chapterizer/gpt4all-bindings/youtube-chapterizer/models", allow_download=False)

        return model.generate(prompt=input)

    def table_generator(items):
        htmlItems = []

        for item in items:
            ls = "<li>{}</li>".format(item)
            htmlItems.append(ls)

        return "<ul>{}</ul>".format(''.join(str(e) for e in htmlItems))
