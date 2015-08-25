/* Class definitions */

/* A datapoint has features and a label. */
function Datapoint(featureMap, label) {
  this.featureMap = featureMap;
  this.label = label;
}

/* Label "enum". The freeze prevents these values from being changed. */
var Label = Object.freeze({
  FRAUD: "FRAUD",
  NOT_FRAUD: "NOT_FRAUD"
});

/* Features "enum". The freeze prevents these values from being changed. */
var Features = Object.freeze({
  NUM_CHARGEBACKS: "NUM_CHARGEBACKS",
  AGE_OF_ACCOUNT_IN_DAYS: "AGE_OF_ACCOUNT_IN_DAYS",
  DECLINE_RATE: "DECLINE_RATE",
  CARD_DIVERSITY: "CARD_DIVERSITY"
});

/*
  The Gini impurity of a set is defined as 1 - sum(freq_i^2), where freq_i are the frequencies for each class.
*/
function calculateGiniImpurityOfSet(datapoints) {
  if (datapoints.length === 0) return 0;
  var fraud = 0;
  var notfraud = 0;
  for (i = 0; i < datapoints.length; i++) {
    if (datapoints[i].label === "FRAUD") {
      fraud++;
    }
    else {
      notfraud++;
    }
  }
  return 1 - Math.pow(fraud / datapoints.length, 2) -
    Math.pow(notfraud / datapoints.length, 2);
}

/*
  The Gini impurity of a split is the average of the Gini impurities of each subset,
  weighted by the size of each subset.
*/
function calculateGiniImpurityOfSplit(datapoints1, datapoints2) {
  var total = datapoints1.length + datapoints2.length;
  return calculateGiniImpurityOfSet(datapoints1) * datapoints1.length / total +
    calculateGiniImpurityOfSet(datapoints2) * datapoints2.length / total;
}