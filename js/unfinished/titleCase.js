//https://www.codewars.com/kata/5202ef17a402dd033c000009/train/javascript

function titleCase(title, minorWords) {
    var words = title.toLowerCase().split(' ');
    var final_title = '';
    var list_minorWords = (typeof minorWords == 'undefined') ? [] : minorWords.toLowercase().split(' ');
    //console.log(list_minorWords);
    for (let i = 0; i < words.length; i++) {
        var current_word = words[i];
        //console.log(current_word);
        if (i == 0) {
            var cap_word = current_word.substring(0, 1) + current_word.substring(1, current_word.length);
            final_title += cap_word + ' ';
        } else {
            if (list_minorWords.length == 0) {
                var cap_word = current_word.substring(0, 1) + current_word.substring(1, current_word.length);

            } else {
                if (list_minorWords.includes(cap_word)) {
                    final_title = cap_word + ' ';
                } else {
                    final_title = current_word.substring(0, 1).toUpperCase() + current_word.substring(1, current_word.length) + ' ';
                }
            }
        }
    }
    return (final_title.trim());
}