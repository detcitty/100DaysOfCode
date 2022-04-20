//https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/javascript

function getGrade(s1, s2, s3) {
  // Code here
  var avg_var = (s1 + s2 + s3) / 3;
  var score = "";

  if (avg_var >= 90) {
    score = "A";
  } else if (avg_var >= 80) {
    score = "B";
  } else if (avg_var >= 70) {
    score = "C";
  } else if (avg_var >= 60) {
    score = "D";
  } else if (avg_var < 60) {
    score = "F";
  }
  return score;
}
