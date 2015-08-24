var graphDisplay = (function() {

  var SeriesNames = Object.freeze({
    TRAINING_ERROR: "Training Error",
    CROSS_VALIDATION_ERROR: "Cross Validation Error"
  });

  var errorSeries = [
    { name: SeriesNames.TRAINING_ERROR, values: []},
    { name: SeriesNames.CROSS_VALIDATION_ERROR, values: []}
  ];

  var SVG_WIDTH = SVG_HEIGHT = $("#graph-container").width(); 

  var margin = {top: 20, right: 70, bottom: 40, left: 40},
    width = SVG_WIDTH - margin.right - margin.left,
    height = SVG_HEIGHT - margin.top - margin.bottom; 

  
  var color = d3.scale.category10();
  

  //create the svg canvas
  var svg = d3.select('#graph-container')
    .insert('svg', ':first-child')
    .attr('width',SVG_WIDTH)
    .attr('height',SVG_HEIGHT)
    .append("svg:g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var x = d3.scale.linear()
    .range([0, width]);

  var y = d3.scale.linear()
    .range([height, 0]);

  y.domain([0, 0.5]);


  var xAxis = d3.svg.axis()
    .scale(x)
    .tickFormat("")
    .orient("bottom");

  var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

  var line = d3.svg.line()
    .interpolate("linear")
    .x(function(d, i) { return x(i); })
    .y(function(d) { return y(d); });

  svg.append("svg:g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

  svg.append("svg:g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Error rate (%)"); 

  var init = function() {
    
  };

  var update = function() {

    x.domain([0, Math.max(10, errorSeries[0].values.length)])

    xAxis.ticks(errorSeries[0].values.length);

    svg.selectAll(".x.axis")
      .call(xAxis);

    var errorLine = svg.selectAll(".errorLine")
      .data(errorSeries);
      
    var errorLineEnter = errorLine.enter().append("svg:g")
        .attr("class", "errorLine");

    errorLineEnter.append("svg:path")
      .attr("class", "line")
      .style("stroke", function(d) { return color(d.name); });
      
    errorLineEnter.append("text")
      .attr("x", 3)
      .attr("dy", ".35em");

    errorLine.selectAll(".line")
      .attr("d", function(d) { return line(d.values); })

    errorLine.selectAll("text")
      .text(function(d) { return d.name; })
      .attr("transform", function(d, i) { return "translate(" + x(d.values.length - 1) + "," + y(d.values[d.values.length - 1]) + ")"; });

  };

  var newPoints = function(trainingErrorRate, crossValidationErrorRate) {
    errorSeries[0].values.push(trainingErrorRate);
    errorSeries[1].values.push(crossValidationErrorRate);
    update();
  };

  var reset = function() {
    errorSeries[0].values = [];
    errorSeries[1].values = [];
  }

  // expose only these functions. All other variables are "private" thanks to the closure.
  return { 
    init: init,
    newPoints: newPoints,
    reset: reset,
  };
})();