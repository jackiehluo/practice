var NUM_DATAPOINTS = 1000;
var datapoints = [];
var crossValidationSet = [];
var trainingSet = [];


// This function will populate the training and cross validation sets based on the datapoints array
var populateDatasets = function() {
  crossValidationSet = [];
  trainingSet = [];
  // We will take 1 in 2 of the datapoints for the cross validation set
  for (var i = 0; i < datapoints.length; i++) {
    if (i % 2 === 0) {
      crossValidationSet.push(datapoints[i]);
    } else {
      trainingSet.push(datapoints[i]);
    }
  };
}


/* This callback takes in the new tree, evaluates the training 
  and cross validations sets, and updates the graphs.
  */
var errorMetricsCallback = function(tree) {
  var trainingErrors = 0;
  for (var i = 0; i < trainingSet.length; i++) {
    var trainingDatapoint = trainingSet[i];
    if (tree.evaluate(trainingDatapoint) !== trainingDatapoint.label) {
      trainingErrors++;
    }
  }
  var trainingErrorRate = trainingErrors / trainingSet.length;

  var crossValidationErrors = 0;
  for (var i = 0; i < crossValidationSet.length; i++) {
    var crossValidationDatapoint = crossValidationSet[i];
    if (tree.evaluate(crossValidationDatapoint) !== crossValidationDatapoint.label) {
      crossValidationErrors++;
    }
  }
  var crossValidationErrorRate = crossValidationErrors / crossValidationSet.length;

  graphDisplay.newPoints(trainingErrorRate, crossValidationErrorRate);

}

$(function() {
  datapoints = startingDatapoints;
  populateDatasets();

  var tree = new DecisionTreeNode(trainingSet);

  graphDisplay.init();
  treeDisplay.init(tree, errorMetricsCallback);

  $("button.reset").on("click", function() {
    graphDisplay.reset();
    tree.children = undefined;
    treeDisplay.init(tree, errorMetricsCallback);
  });

  $("button.randomData").on("click", function() {
    graphDisplay.reset();

    datapoints = randomDatapoints(NUM_DATAPOINTS);
    populateDatasets();
    tree = new DecisionTreeNode(trainingSet);

    treeDisplay.init(tree, errorMetricsCallback);
  });

  $("form").on("submit", function(e) {
    e.stopPropagation();
    e.preventDefault();

    var newMinLeafSize = parseFloat($("#minLeafSize").val());
    var newMinGiniGain = parseFloat($("#minGiniGain").val());

    MIN_LEAF_SIZE = newMinLeafSize;
    MIN_GINI_GAIN = newMinGiniGain;
  });
});



