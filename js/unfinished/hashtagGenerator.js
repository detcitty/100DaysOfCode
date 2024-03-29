// https://www.codewars.com/kata/52449b062fb80683ec000024/train/javascript
/*
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
*/
function generateHashtag(str) {
  var final_value = '';
  if (!!str) {
    const words = str.trim().split(/\s+/); // Split by
    const capwords = words.map((x) => {
      `${x.substring(0, 1).toUpperCase()}${x.substring(1)}`;
    });
    final_value =  capwords.join("");
  } else {
    final_value =  false;
  }
  return(final_value)
}

const test1 = "Do We have A Hashtag";
console.log(generateHashtag(test1));
