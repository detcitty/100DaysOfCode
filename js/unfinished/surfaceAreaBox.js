// https://www.codewars.com/kata/565f5825379664a26b00007c/train/javascript

function getSize(width, height, depth) {
    const area = 2 * (width * depth) + 2 * (height * width) + 2 * (depth * height);
    const volumn = width * height * depth;
    return [area, volumn];
  }
  