from summary_module import Summary_Module


def test_get_para_list_functionality():
    # Data from https://en.wikipedia.org/wiki/Wikipedia
    para = """
        On January 15, 2001, Jimmy Wales and Larry Sanger launched Wikipedia. Sanger coined its name as a blend of "wiki" and "encyclopedia".
        Wales was influenced by the "spontaneous order" ideas associated with Friedrich Hayek and the Austrian School of economics after being exposed to these ideas by Austrian economist and Mises Institute Senior Fellow Mark Thornton.
        Initially available only in English, versions in other languages were quickly developed.
        Its combined editions comprise more than 59 million articles, attracting around 2 billion unique device visits per month and more than 17 million edits per month (1.9 edits per second) as of November 2020.
        In 2006, Time magazine stated that the policy of allowing anyone to edit had made Wikipedia the "biggest (and perhaps best) encyclopedia in the world".
        Wikipedia has received praise for its enablement of the democratization of knowledge, extent of coverage, unique structure, culture, and reduced degree of commercial bias; but criticism for exhibiting systemic bias, particularly gender bias against women and alleged ideological bias.
        The reliability of Wikipedia was frequently criticized in the 2000s but has improved over time, as Wikipedia has been generally praised in the late 2010s and early 2020s.
        The website's coverage of controversial topics such as American politics and major events like the COVID-19 pandemic and the Russian invasion of Ukraine has received substantial media attention.
        It has been censored by world governments, ranging from specific pages to the entire site.
        In April 2018, Facebook and YouTube announced that they would help users detect fake news by suggesting fact-checking links to related Wikipedia articles.
        Articles on breaking news are often accessed as a source of frequently updated information about those events.
    """
    summary_module = Summary_Module()
    para_list = summary_module.get_para_list(para)
    print(f"[para_list]: {para_list}")

def test_generate_text_functionality():
    # Data from https://en.wikipedia.org/wiki/Wikipedia
    para = """
        On January 15, 2001, Jimmy Wales and Larry Sanger launched Wikipedia. Sanger coined its name as a blend of "wiki" and "encyclopedia".
        Wales was influenced by the "spontaneous order" ideas associated with Friedrich Hayek and the Austrian School of economics after being exposed to these ideas by Austrian economist and Mises Institute Senior Fellow Mark Thornton.
        Initially available only in English, versions in other languages were quickly developed.
        Its combined editions comprise more than 59 million articles, attracting around 2 billion unique device visits per month and more than 17 million edits per month (1.9 edits per second) as of November 2020.
        In 2006, Time magazine stated that the policy of allowing anyone to edit had made Wikipedia the "biggest (and perhaps best) encyclopedia in the world".
        Wikipedia has received praise for its enablement of the democratization of knowledge, extent of coverage, unique structure, culture, and reduced degree of commercial bias; but criticism for exhibiting systemic bias, particularly gender bias against women and alleged ideological bias.
    """
    summary_module = Summary_Module()
    text = summary_module.generate_text(para)
    print(f"[Text]: {text}")

def test_generate_summary_functionality():
    # Data from https://en.wikipedia.org/wiki/Wikipedia
    para = """
        On January 15, 2001, Jimmy Wales and Larry Sanger launched Wikipedia. Sanger coined its name as a blend of "wiki" and "encyclopedia".
        Wales was influenced by the "spontaneous order" ideas associated with Friedrich Hayek and the Austrian School of economics after being exposed to these ideas by Austrian economist and Mises Institute Senior Fellow Mark Thornton.
        Initially available only in English, versions in other languages were quickly developed.
        Its combined editions comprise more than 59 million articles, attracting around 2 billion unique device visits per month and more than 17 million edits per month (1.9 edits per second) as of November 2020.
        In 2006, Time magazine stated that the policy of allowing anyone to edit had made Wikipedia the "biggest (and perhaps best) encyclopedia in the world".
        Wikipedia has received praise for its enablement of the democratization of knowledge, extent of coverage, unique structure, culture, and reduced degree of commercial bias; but criticism for exhibiting systemic bias, particularly gender bias against women and alleged ideological bias.
    """
    summary_module = Summary_Module()
    summary = summary_module.generate_summary(para)
    print(f"[Summary]: {summary}")


if __name__== "__main__":
    test_get_para_list_functionality()
    # test_generate_text_functionality()
    # test_generate_summary_functionality()