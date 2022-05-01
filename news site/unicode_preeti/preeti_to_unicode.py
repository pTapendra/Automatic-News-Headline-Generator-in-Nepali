import npttf2utf

def convert(word):
    mapper = npttf2utf.FontMapper("posts/map.json")
    return mapper.map_to_unicode(word, from_font="Preeti", unescape_html_input=False, escape_html_output=False)