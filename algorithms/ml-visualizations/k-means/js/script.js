//Equalize column heights in javascript
$(function(){
  var graphColHeight = $('#graph-col').height();
  $('#steps-col').height(graphColHeight);
});

var X_MAX = 10;
var Y_MAX = 10;

points = examplePoints;

// Generate normally distributed number from Box-Muller transform
function normal(mu, sigma) {
  var u1 = Math.random();
  var u2 = Math.random();
  var theta = 2 * Math.PI * u2;
  var r = Math.sqrt(-2 * Math.log(u1));
  return r * Math.cos(theta) * sigma + mu;
}

function randomData(numClusters, numPoints) {
  var SIGMA = 0.7;
  if (numClusters === undefined) numClusters = _.random(3,5);
  if (numPoints === undefined) numPoints = 1000;

  var pointsPerCluster = Math.floor(numPoints / numClusters);

  var clusterCenters = [];

  var possibleClusterCenters = [];
  for (var x = 1; x <= X_MAX -1; x+=2) {
    for (var y = 1; y <= Y_MAX -1; y+=2) {
      possibleClusterCenters.push({x: x, y: y});
    }
  }

  for (var i = 0; i < numClusters; i++) {
    var randomIndex = _.random(possibleClusterCenters.length -1);
    clusterCenters.push(possibleClusterCenters.splice(randomIndex, 1)[0]);
  }

  var points = [];
  for (var i = 0; i < clusterCenters.length; i++) {
    var clusterCenter = clusterCenters[i];
    for (var j = 0; j < pointsPerCluster; j++) {
      var x = clusterCenter.x + normal(0, SIGMA);
      var y = clusterCenter.y + normal(0, SIGMA);

      if (x < 0 || x > X_MAX || y < 0 || y > Y_MAX) continue;

      points.push(new Point(x, y));
    }
  };

  //add a few randomly scattered points
  for (var i = 0; i < numPoints / 5; i++) {
    points.push(new Point(Math.random() * X_MAX, Math.random() * Y_MAX));
  };

  return points;
}

function addCentroid() {
  var randomPoint = points[_.random(points.length - 1)];
  centroids.push(new Centroid(randomPoint.x, randomPoint.y, centroids.length));
  redraw();
}

function removeCentroid() {
  centroids.pop();
  redraw();
}

// Solution implementation if not defined in IMPLEMENT_ME.js
if (typeof(assignCentroids) !== 'function') {
  /* For each point, assign it to the cluster represented by the closest centroid */
  var closestCentroid = function(point) {
    var minDist = Infinity;
    var closestCentroid;
    for (var i = centroids.length - 1; i >= 0; i--) {
      var centroid = centroids[i];
      var dist = squaredDistance(point, centroid);
      if (dist < minDist) {
        minDist = dist;
        closestCentroid = centroid;
      }
    };
    return closestCentroid;
  }

  var assignCentroids = function() {
    for (var i = points.length - 1; i >= 0; i--) {
      var point = points[i];
      point.centroid = closestCentroid(point);
    };
  }
}

if (typeof(updateCentroids) !== 'function') {
  /* Update the position of each centroid based on the points assigned to it. 
    The new position should be the mean of the positions of the points assigned to it.
  */
  updateCentroids = function() {
    for (var i = centroids.length - 1; i >= 0; i--) {
      var centroid = centroids[i];
      var sumX = 0;
      var sumY = 0;
      var count = 0;
      for (var j = 0; j < points.length; j++) {
        point = points[j];
        if (point.centroid === centroid) {   
          var point = points[j];
          sumX += point.x;
          sumY += point.y;
          count ++;
        };
      };
      if (count > 0) {
        centroid.x = sumX / count;
        centroid.y = sumY / count;
      };
    };
  }
}

function reset() {
  for (var i = points.length - 1; i >= 0; i--) {
    points[i].centroid = undefined;
  };
  centroids = [];
  redraw();
  updateMetric();
}

function squaredDistance (point, centroid) {
  return (point.x - centroid.x) * (point.x - centroid.x) + (point.y - centroid.y) * (point.y - centroid.y);
}

function updateMetric() {
  var metric = 0;
  for (var i = 0; i < points.length; i++) {
    var point = points[i];
    var centroid = point.centroid;
    if (centroid !== undefined) {
      metric += squaredDistance(point, centroid);
    }
  };
  $('#metricValue').html(metric);
}

/* The following sets up the graph using d3.js */

var X_WIDTH = $("#graph-col").width();
var Y_HEIGHT = 500;

var margin = {top: 19.5, right: 19.5, bottom: 39.5, left: 39.5},
  width = X_WIDTH - margin.right - margin.left,
  height = Y_HEIGHT - margin.top - margin.bottom;

//create the svg canvas
var svg = d3.select('#graph-col').insert('svg', ':first-child').attr('width',X_WIDTH).attr('height',Y_HEIGHT);

var xScale = d3.scale.linear().domain([0,X_MAX]).range([0,width]);
var yScale = d3.scale.linear().domain([0,Y_MAX]).range([0,height]);

// The x & y axes.
var xAxis = d3.svg.axis().orient("bottom").scale(xScale).ticks(10),
    yAxis = d3.svg.axis().scale(yScale).orient("left").ticks(10);

var xLabel = "x",
    yLabel = "y";

var color = d3.scale.category10();

function redraw() {

  //clear the whole canvas
  $('svg').empty();

  //draw points
  var pointDots = svg.selectAll('.pointDots').data(points);
  pointDots.enter().append('circle').attr('class','pointDots')
    .attr('r', 2)
    .attr('cx',function(d){ return xScale(d.x) + margin.left; })
    .attr('cy',function(d){ return yScale(d.y) + margin.top; })
    .attr('opacity', 0.5);

  //draw centroids
  var centroidDots = svg.selectAll('.centroidDots').data(centroids);
  centroidDots.enter().append('circle').attr('class','pointDots')
    .attr('r', 5)
    .attr('cx',function(d){ return xScale(d.x)  + margin.left; })
    .attr('cy',function(d){ return yScale(d.y) + margin.top; })
    .attr('stroke', function(d) { return color(d.id); })
    .attr('stroke-width', 3)
    .attr('fill', 'white');

  //color points
  pointDots.attr('stroke', function(d) { return d.centroid === undefined ? 'black' : color(d.centroid.id); });

  // Add the x-axis.
  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(" + margin.left + "," + (height + margin.top + 10) + ")")
      .call(xAxis);

  // Add the y-axis.
  svg.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate(" + (margin.left - 10) + "," + margin.top + ")")
      .call(yAxis);

  // // Add an x-axis label.
  svg.append("text")
      .attr("class", "x label")
      .attr("text-anchor", "end")
      .attr("x", width + margin.left)
      .attr("y", height + margin.top + 30)
      .text(xLabel);

  // // Add a y-axis label.
  svg.append("text")
      .attr("class", "y label")
      .attr("text-anchor", "end")
      .attr("y", 6)
      .attr("x", - margin.top)
      .attr("dy", ".75em")
      .attr("transform", "rotate(-90)")
      .text(yLabel);
}

redraw();


function loadRandom() {
  points = randomData();
  xLabel = "x";
  yLabel = "y";
  reset();
  redraw();
}

function loadSquare() {
  points = squarePoints;
  xLabel = "longitude";
  yLabel = "latitude";
  reset();
  redraw();
}

function loadFacebook() {
  points = facebookPoints;
  xLabel = "Likes";
  yLabel = "Posts";
  reset();
  redraw();
}

function loadExample() {
  points = examplePoints;
  xLabel = "x";
  yLabel = "y";
  reset();
  redraw();
}


//This sets up the listeners for each button
$('button#reset').click(reset);
$('button#add-centroid').click(addCentroid);
$('button#remove-centroid').click(removeCentroid);
$('button#update').click(function() {updateCentroids(); redraw(); updateMetric();});
$('button#assign').click(function() {assignCentroids(); redraw(); updateMetric();});
$('button#random-data').click(loadRandom);
$('button#fb-data').click(loadFacebook);
$('button#square-data').click(loadSquare);