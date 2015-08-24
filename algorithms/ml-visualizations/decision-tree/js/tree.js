/* Class definitions (some are defined in IMPLEMENT_ME.js) */
function Split(feature, splitValue, giniImpurityOfSplit) {
  this.feature = feature;
  this.splitValue = splitValue;
  this.giniImpurityOfSplit = giniImpurityOfSplit;
}

Split.prototype.toString = function() {
  return this.feature + " < " + roundDecimal(this.splitValue, 2);
};

function DecisionTreeNode(datapoints) {
  this.datapoints = datapoints;
  this.split = undefined;
  this.children = undefined;
}

/* A convenience method for calculating the array of children for d3 */
DecisionTreeNode.prototype.getChildren = function() {
  return this.children;
};

DecisionTreeNode.prototype.isLeaf = function() {
  return this.children ? false : true;
};

DecisionTreeNode.prototype.getLabel = function() {
  return getMajorityLabel(this.datapoints);
};

// The variables are used to control the size of the tree
var MIN_GINI_GAIN = 0;
var MIN_LEAF_SIZE = 1;

/* Splits a leaf node if the current nodes still has both FRAUD and NOT_FRAUD datapoints.
  Returns true if a split has occurred, false otherwise.
 */
DecisionTreeNode.prototype.splitLeaf = function() {
  if (!this.isLeaf()) throw "Cannot split non leaf node";

  // Don't split if we've already separated both classes
  var fraudCount = getLabelCount(this.datapoints, Label.FRAUD);
  if (fraudCount === 0 || fraudCount === this.datapoints.length) {
    console.log("Not splitting because the classes are already separated in this leaf");
    return false;
  }

  var bestSplit = findBestSplit(this.datapoints);

  // Don't split if the Gini gain is not enough
  var giniGain = calculateGiniImpurityOfSet(this.datapoints) - bestSplit.giniImpurityOfSplit;
  console.log("Gini gain: " + giniGain);
  if (giniGain < MIN_GINI_GAIN) {
    console.log("Not splitting because Gini gain (" + giniGain + ") is lower than set minimum (" + MIN_GINI_GAIN + ")");
    return false;
  }

  var leftDatapoints = getLeftDatapoints(this.datapoints, bestSplit);
  var rightDatapoints = getRightDatapoints(this.datapoints, bestSplit);

  // Don't split if leaves become too small
  if (rightDatapoints.length < MIN_LEAF_SIZE || leftDatapoints.length < MIN_LEAF_SIZE) {
    console.log("Not splitting because leaf size would be lower than set minimum (" + MIN_LEAF_SIZE + ")");
    return false;
  }

  // Move ahead with the split
  var leftChild = new DecisionTreeNode(leftDatapoints);
  var rightChild = new DecisionTreeNode(rightDatapoints);

  this.split = bestSplit;
  this.children = [leftChild, rightChild];
  return true;
};

DecisionTreeNode.prototype.collapse = function() {
  if (this.isLeaf()) throw "Cannot collapse leaf node";
  this.split = undefined;
  this.children = undefined;
};

DecisionTreeNode.prototype.getLeftChild = function() {
  if (this.isLeaf()) throw "Cannot get left child of leaf node";

  return this.children[0];
};

DecisionTreeNode.prototype.getRightChild = function() {
  if (this.isLeaf()) throw "Cannot get right child of leaf node";

  return this.children[1];
};


DecisionTreeNode.prototype.evaluate = function(datapoint) {
  if (this.isLeaf()) return this.getLabel();

  var datapointValue = datapoint.featureMap[this.split.feature];
  var splitValue = this.split.splitValue;

  if (datapointValue < splitValue) {
    return this.getLeftChild().evaluate(datapoint);
  } else {
    return this.getRightChild().evaluate(datapoint);
  }
};

function calculateGiniImpurityOfSet(datapoints) {

  if (datapoints.length === 0) return 0;

  var fraudFrequency = 0;
  var notFraudFrequency = 0;

  for (var i = 0; i < datapoints.length; i++) {
    if (datapoints[i].label === Label.FRAUD) {
      fraudFrequency++;
    } else {
      notFraudFrequency++;
    }
  };

  fraudFrequency /= datapoints.length;
  notFraudFrequency /=datapoints.length;

  return 1 - fraudFrequency * fraudFrequency - notFraudFrequency * notFraudFrequency;
}

function calculateGiniImpurityOfSplit(datapoints1, datapoints2) {
  var length1 = datapoints1.length;
  var length2 = datapoints2.length;
  var totalSize = length1 + length2;
  var gini1 = calculateGiniImpurityOfSet(datapoints1);
  var gini2 = calculateGiniImpurityOfSet(datapoints2);
  return length1 / totalSize * gini1 + length2 / totalSize * gini2; 
}

function findBestSplit(datapoints) {
  var lowestImpuritySplit;
  var lowestImpurity = Infinity;

  var features = Object.keys(Features);
  for (var i = 0; i < features.length; i++) {
    var feature = features[i];
    var bestSplitForFeature = findBestSplitForFeature(datapoints, feature);

    var impurity = bestSplitForFeature.giniImpurityOfSplit;
    if (impurity < lowestImpurity) {
      lowestImpurity = impurity;
      lowestImpuritySplit = bestSplitForFeature;
    }
  };
  return lowestImpuritySplit;
}

function findBestSplitForFeature(datapoints, feature) {
  // First we sort the datapoints by the feature we will split on
  datapoints.sort(sortByFeatureFunction(feature));

  // Then we iterate over all the possible splitting points and find the one with the lowest impurity
  var lowestImpurity = Infinity;
  var lowestImpuritySplit;

  var alreadyProcessedValue;
  for (var i = 0; i < datapoints.length; i++) {
    var splitValue = datapoints[i].featureMap[feature];

    if (splitValue === alreadyProcessedValue) continue;

    alreadyProcessedValue = splitValue;

    // the current index is the first one we've seen with splitValue
    var leftDatapoints = datapoints.slice(0, i);

    var rightDatapoints = datapoints.slice(i);

    var giniImpurityOfSplit = calculateGiniImpurityOfSplit(leftDatapoints, rightDatapoints);

    if (giniImpurityOfSplit < lowestImpurity) {
      lowestImpurity = giniImpurityOfSplit;
      lowestImpuritySplit = new Split(feature, splitValue, giniImpurityOfSplit);
    }
  }

  return lowestImpuritySplit;
}

function sortByFeatureFunction(feature) {
  return function(point1, point2) {
    if (point1.featureMap[feature] > point2.featureMap[feature])
      return 1;
    if (point1.featureMap[feature] < point2.featureMap[feature])
      return -1;
    return 0;
  };
}

function trainTree(datapoints) {
  var tree = new DecisionTreeNode(datapoints);
  if (tree.splitLeaf()) {
    tree.children = tree.children.map(function(childTree) { return trainTree(childTree.datapoints);});
  }
  return tree;
}

function getLabelCount(datapoints, label) {
  if (datapoints.length === 0) return 0;

  var labelCount = 0;

  for (var i = 0; i < datapoints.length; i++) {
    if (datapoints[i].label === label) {
      labelCount++;
    }
  }
  return labelCount;
}

function getLabelPct(datapoints, label) {
  return Math.round(100 * getLabelCount(datapoints, label) / datapoints.length);
}

function roundDecimal(num, decimals) {
  return Math.round(num * Math.pow(10, decimals)) / Math.pow(10, decimals);
}

function getMajorityLabel(datapoints) {
  if (getLabelCount(datapoints, Label.FRAUD) > datapoints.length / 2) {
    return Label.FRAUD;
  } else {
    return Label.NOT_FRAUD;
  }
}

function getLeftDatapoints(datapoints, split) { 
  return datapoints.filter(function(datapoint) {
    return datapoint.featureMap[split.feature] < split.splitValue;
  });
}

function getRightDatapoints(datapoints, split) { 
  return datapoints.filter(function(datapoint) {
    return datapoint.featureMap[split.feature] >= split.splitValue;
  });
}
