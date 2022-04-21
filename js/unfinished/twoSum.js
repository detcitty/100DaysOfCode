// https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/javascript

function twoSum(numbers, target) {
    // ...
    var index1 = 0;
    var index2 = 0;
    for (let i = 0; i < numbers.length; i++) {

        for (let j = 0; j < numbers.length; j++) {
            var values = numbers[i] + numbers[j];

            if (i == j) {
                continue
            } else {
                if (values == target) {
                    index1 = i;
                    index2 = j;
                    break
                }
            }
        }
    }
    return ((index1, index2))
}