// https://www.codewars.com/kata/58e26b5d92d04c7a4f00020a/train/javascript

function palindrome(num) {
    //Code goes here
    //check if num
    let len = num.length;
    for (let i = 0; i < len / 2; i++) {
        //Help
        if (len % 2 === 0) {

        }
        else 
        {
            
        }
    }
    return();
}

describe("Tests", () => {
    it("test", () => {
        Test.assertEquals(palindrome(1212), true);
        Test.assertEquals(palindrome(89698), true);
        Test.assertEquals(palindrome(7653356), true);
        Test.assertEquals(palindrome(100134), false);
        Test.assertEquals(palindrome(13598), false);
        Test.assertEquals(palindrome("ACCDDCCA"), "Not valid");
        Test.assertEquals(palindrome("1212"), "Not valid");
        Test.assertEquals(palindrome(-4505), "Not valid");
    });
});

console.log();