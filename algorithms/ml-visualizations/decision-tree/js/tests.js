/**
  This file tests the implementations in IMPLEMENT_ME.js
*/

// This function just checks that your implementation of calculateGiniImpurityOfSet is correct
function test_calculateGiniImpurityOfSet() {
  var fraudDatapoint = new Datapoint({}, Label.FRAUD);
  var nonFraudDatapoint = new Datapoint({}, Label.NOT_FRAUD);

  var datapoints = [];
  for (var i = 0; i < 4; i++) datapoints.push(fraudDatapoint);
  for (var i = 0; i < 6; i++) datapoints.push(nonFraudDatapoint);

  var expectedGini = 0.48;
  var actualGini = calculateGiniImpurityOfSet(datapoints);

  if (expectedGini !== actualGini) {
    console.error("Implementation of calculateGiniImpurityOfSet is incorrect!" + 
      "Found " + actualGini + " but expected " + expectedGini);
  } else {
    console.log("Implementation of calculateGiniImpurityOfSet seems correct.");
  }
}

function test_calculateGiniImpurityOfSplit() {
  var fraudDatapoint = new Datapoint({}, Label.FRAUD);
  var nonFraudDatapoint = new Datapoint({}, Label.NOT_FRAUD);

  var datapoints1 = [fraudDatapoint, fraudDatapoint, nonFraudDatapoint];
  var datapoints2 = [fraudDatapoint, nonFraudDatapoint, nonFraudDatapoint, fraudDatapoint, fraudDatapoint];

  var expectedGini = 7 / 15;
  var actualGini = calculateGiniImpurityOfSplit(datapoints1, datapoints2);

  if (expectedGini !== actualGini) {
    console.error("Implementation of calculateGiniImpurityOfSplit is incorrect!" + 
      "Found " + actualGini + " but expected " + expectedGini);
  } else {
    console.log("Implementation of calculateGiniImpurityOfSplit seems correct.");
  }
}

$(test_calculateGiniImpurityOfSet);
$(test_calculateGiniImpurityOfSplit);
