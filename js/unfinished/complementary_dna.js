// https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/javascript

function map_dna(x) {
    var letters = ['A','T','G','C'];
    var trans_map = ['T','A','C','G'];

    var letter_index = letters.indexOf(x);
    return(trans_map[letter_index]);
}

function DNAStrand(dna){
    //your code here
    var split_letters = dna.split('');

    var translated = split_letters.map(x => { return(map_dna(x)) } );
    return(translated.join(''));
  }