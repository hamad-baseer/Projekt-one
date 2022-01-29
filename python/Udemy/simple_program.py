def sentence_maker(sentences):
    interrogatives = ("why", "when", "how")
    if sentences.startswith(interrogatives):
        return "{}?".format(title)
    else:
        return "{}.".format(title)


result = []
inputs = input("type something: ")
for inputs in result:
    if inputs != "\end":
        result.append(sentence_maker(inputs))
    else:
        break



