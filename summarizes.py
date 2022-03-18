import re
from gensim.summarization.summarizer import summarize

def prepro(text):
    # sentence = re.sub('([a-z])','',text) # base eng
    sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', text)  # base kor
    sentence = re.sub('[-=+,#/\?^$@*\※~&ㆍ!』\\|\[\]\<\>`\'…》]', '', sentence)  # base spec
    sentence = re.sub("\s?\\[*\]", '', sentence)
    sentence = re.sub("^\s?[▶△|\/]→*", '', sentence)  # spec0
    sentence = re.sub("▲|■|※|☎|△", '', sentence)  # spec1
    sentence = re.sub("[a-zA-Z0-9+-_]+@[a-zA-Z0-9-]+\[a-zA-Z0-9-.]+$", '', sentence)  # email
    sentence = re.sub("^\/?([가-힣]+)\s?(기자|팀)?\s*\?$", '', sentence)  # reporter
    sentence = re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", '',
                      sentence)  # homepage url
    sentence = re.sub("^\s?[▶|\/]*", '', sentence)  # spec2
    sentence = re.sub("^\s?(▲|■|※|☎|△|◆)*", '', sentence)  # spec3
    sentence = re.sub("\\\\n", '', sentence)  # \\\n
    sentence = re.sub("\\t", '', sentence)  # \t

    return sentence


def summarizes(text):
    patten = re.compile('\\n')

    content2 = []
    ratio = 0.2 # base summarizes ratio 
    a = prepro(text[0])
    try:
        b = summarize(a, ratio=ratio)
        b = re.sub(patten, '', b)

    except ValueError:
        content2.append(prepro(text))

    else:
        if b == '':
            while b == '':
                ratio += 0.1
                b = summarize(a, ratio=ratio)

                if ratio >= 0.9:
                    break
                    content2.append(prepro(text))

            content2.append(prepro(text))
        else:
            content2.append(b)

    return content2