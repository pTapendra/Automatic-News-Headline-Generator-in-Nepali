import npttf2utf

def convert(word):
    mapper = npttf2utf.FontMapper("posts/map.json")
    return mapper.map_to_preeti(word, from_font="unicode", unescape_html_input=False, escape_html_output=False)