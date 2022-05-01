/* functions for nep to eng conversion*/


function engToNep(id) {
    var textArea = document.getElementById(id);
    textArea.addEventListener('keydown', function (e) {
        if (e.keyCode === 17){
            e.preventDefault();
            word_pos = getCurrentWordPos(id);
            word = e.target.value.substring(word_pos[0], word_pos[1]);
            if (word==='|') {
                replace_with_suggestion('|', id, word_pos);
            } else {
                performTranslation([word], id, word_pos);
            }
        }
    });
}


async function performTranslation(
    word, id, word_pos, suggestionNo = 3, language = "ne-t-i0-und" //nepali 
) {
    console.log("requesting translation for, " + word);
    const url = `https://inputtools.google.com/request?text=${word}&itc=${language}&num=${suggestionNo}`;
    let response = await fetch(url);
    let data = (await response.json());
    if (data[0] == "SUCCESS") {
        let suggestions = data[1][0][1];
        console.log("suggestions: " + suggestions);
        replace_with_suggestion(suggestions[0], id, word_pos);
        renderSuggestions(suggestions, id, word_pos);
    }
}


function replace_with_suggestion(suggestion, id, word_pos) {
    let textArea = document.getElementById(id);
    old_val = textArea.value;
    textArea.value = old_val.substring(0, word_pos[0]) + suggestion + old_val.substring(word_pos[1], old_val.length);
    document.getElementById(id).selectionEnd = word_pos[0] + suggestion.length + 1;
}


function renderSuggestions(suggestions, id, word_pos) {
    var suggestion_list = document.getElementById("suggestion");
    suggestion_list.innerHTML = "";
    suggestions.forEach(element => {
        var span = document.createElement("span");
        span.setAttribute('style', 'margin: 0.1em !important; padding: 0.3em !important;');
        span.setAttribute('class', 'alert alert-primary');
        span.setAttribute('onclick', 'replace_with_rendered_suggestion(this.innerText, '+ id +')');
        span.appendChild(document.createTextNode(element.split(" ").pop()));
        suggestion_list.appendChild(span);
    });
}


function replace_with_rendered_suggestion(suggestion, id) {
    id = id.id;
    word_pos = getCurrentWordPos(id);
    replace_with_suggestion(suggestion, id, word_pos);
}

 
function getCurrentWordPos(id) {
    // obtaining the current cursor position
    cursor_pos = document.getElementById(id).selectionEnd;
    
    //moving cursor position backwards, if it is at a blank space
    while(document.getElementById(id).value[cursor_pos-1]===' '){
        console.log('from: ' + cursor_pos);
        cursor_pos = cursor_pos - 1;
        console.log('shifting cursor backward to: ' + cursor_pos);
    }
    
    // initially set output postions to 0
    var word_start_pos = 0, word_end_pos = 0;
    
    //moving cursor position backwards for obtaining starting postion of the word
    for(var i=cursor_pos; i>0; i--) {
        console.log('moving back...')
        console.log('now at '+document.getElementById(id).value[i-1]);
        if (document.getElementById(id).value[i-1]===' ' || document.getElementById(id).value[i-1]==='\n'){
            word_start_pos = i;
            break;
        }
    }
    
    //moving cursor position forward for obtaining ending position of the word
    for(var i=cursor_pos; i < cursor_pos + 100; i++) {
        console.log('moving forward...')
        console.log('now at ' + document.getElementById(id).value[i]);
        if (document.getElementById(id).value[i]==='\n' || document.getElementById(id).value[i]===' ' || document.getElementById(id).value[i] === undefined){
            word_end_pos = i;
            break;
        }
    }
    
    console.log('start: ' + word_start_pos);
    console.log('end: ' + word_end_pos);
    return [word_start_pos, word_end_pos]
}