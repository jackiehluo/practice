var treeDisplay = (function() {

  var SVG_WIDTH = $("#tree-container").width();
  var SVG_HEIGHT = $("#tree-container").height();

  var margin = {top: 100, right: 19.5, bottom: 100, left: 39.5},
    treeWidth = SVG_WIDTH - margin.right - margin.left,
    treeHeight = SVG_HEIGHT - margin.top - margin.bottom;

  //create the svg canvas
  var svg = d3.select('#tree-container')
    .insert('svg', ':first-child')
    .attr('width',SVG_WIDTH)
    .attr('height',SVG_HEIGHT)
    .append("svg:g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // Set the colors for our labels
  var COLORS = {};
  COLORS[Label.FRAUD] = "red";
  COLORS[Label.NOT_FRAUD] = "green";
  Object.freeze(COLORS);

  var tree = d3.layout.tree()
    .size([treeWidth, treeHeight])

  // This generates the bezier curve (spline) connecting the source and target of a link
  var diagonal = d3.svg.diagonal();

  // Pie chart of fraud / not fraud for each node
  var pie = d3.layout.pie()
    .value(function(d) {return d.count;});

  var arc = d3.svg.arc()
      .outerRadius(20)
      .innerRadius(0);

  // This counter is used to assign unique ids to nodes. This helps d3 determine enter and exit groups.
  var i = 0;
  var duration = 750;

  function getStatsText(d) {
    return "FRAUD: " +  getLabelCount(d.datapoints, Label.FRAUD) + "," + 
      "  NOT_FRAUD: " + getLabelCount(d.datapoints, Label.NOT_FRAUD) + "," + 
      "  Gini: " + roundDecimal(calculateGiniImpurityOfSet(d.datapoints), 2);
  }

  // Split node on click if it's a leaf
  function click(d) {
    if (d.isLeaf() && d.splitLeaf()) {
      updateTree(d);
    }
  }

  function updateTree(source) {

    // Nodes is an array of the nodes from source, with x,y, parent and children properties set by tree.nodes()
    var nodes = tree.nodes(root);

    // links is an array of the (source, target) pairs of nodes.
    var links = tree.links(nodes);

    var nodeGroup = svg.selectAll(".node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });

    // Enter any new nodes at the parent's previous position.
    var nodeEnter = nodeGroup.enter()
      .append("svg:g")
      .attr("class", "node")
      .style("opacity", 1e-6)
      .attr("transform", function(d) { return "translate(" + source.x0 + "," + source.y0 + ")"; })
      .on("mouseover", function() {
        d3.select(this).select(".info").style("display", "initial");
      })
      .on("mouseout", function() {
        d3.select(this).select(".info").style("display", "none");
      })
      .on("click", click);

    var nodePie = nodeEnter
      .append("svg:g")
      .attr("class", "pie")
      .attr("transform", function(d) { return "scale(" + 3 * Math.pow(d.datapoints.length / NUM_DATAPOINTS, 1/2) + ")";});
      
    nodePie.selectAll(".arc")
      .data(function(d) {
        var fraud = { label: Label.FRAUD, count: getLabelCount(d.datapoints, Label.FRAUD)}; 
        var notFraud = { label: Label.NOT_FRAUD, count: getLabelCount(d.datapoints, Label.NOT_FRAUD)}; 
        return pie([fraud, notFraud]);
      })
      .enter()
      .append("svg:path")
      .attr("d", arc)
      .attr("class", ".arc")
      .style("stroke", function(d) { return d.data.count === 0 ? "none" : "#fff";}) // stroke only if there is data. This avoids white lines appearing
      .style("fill", function(d) { return COLORS[d.data.label];});

    nodeGroup.selectAll(".info").remove();

    var text = nodeGroup
      .append("svg:g")
      .attr("class", "info")
      .append("svg:text")
      .attr("x", 0)
      .attr("y", 0);

    text.append("svg:tspan")
      .text(function(d) {return "Total datapoints: " + d.datapoints.length;})
      .attr("x", 0)
      .attr("y", "1em");

    text.append("svg:tspan")
      .text(getStatsText)
      .attr("x", 0)
      .attr("dy", "1em");

    text.filter(function(d) {return !d.isLeaf();})
      .append("svg:tspan")
      .attr("class", "rule")
      .text(function(d) {return d.split.toString();})
      .attr("x", 0)
      .attr("dy", "1em");

    text.filter(function(d) {return d.isLeaf();})
      .append("svg:tspan")
      .attr("class", "rule")
      .text(function(d) {return d.getLabel();})
      .attr("x", 0)
      .attr("dy", "1em");


    text.each(function() {
      var elem = d3.select(this);
      var bbox = this.getBBox();
      var parent = d3.select(this.parentNode);
      parent.insert("svg:rect", ":first-child") // this puts the bounding box behind the text
        .attr("class", "bounding-box")
        .attr("x", bbox.x - 5) // 5px margin
        .attr("y", bbox.y - 5)
        .attr("width", bbox.width + 10) // 5px + 5px marging on both sides
        .attr("height", bbox.height + 10);

      parent.attr("transform", "translate(" + (-bbox.width / 2) + "," + (-bbox.height * 4 / 2) + ")");

      parent.style("display", "none")
      parent.style("z-index", 100);

    });

    // Transition nodes to their new position.
    var nodeUpdate = nodeGroup.transition()
      .duration(duration)
      .style("opacity", 1)
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    // Transition exiting nodes to the parent's new position.
    var nodeExit = nodeGroup.exit().transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + source.x + "," + source.y + ")"; })
      .remove();

    nodeExit.select(".pie")
      .style("opacity", 1e-6);

    linkGroup = svg.selectAll("path.link")
      .data(links, function(d) { return d.target.id; });

    // Enter any new links at the parent's previous position.
    linkEnter = linkGroup.enter();

    linkEnter.insert("svg:path", ":first-child") // first child, so they are under the other elements
      .attr("class", "link")
      .style("opacity", 1e-6)
      .attr("d", function(d) {
        var o = {x: source.x0, y: source.y0};
        return diagonal({source: o, target: o});
      });

    // Transition links to their new position.
    linkGroup.transition()
      .duration(duration)
      .attr("d", diagonal)
      .style("opacity", 1.0);

    // Transition exiting nodes to the parent's new position.
    linkGroup.exit().transition()
      .duration(duration)
      .style("opacity", 1e-6) 
      .attr("d", function(d) {
        var o = {x: source.x, y: source.y};
        return diagonal({source: o, target: o});
      })
      .remove();

    // Stash the old positions for transition.
    nodes.forEach(function(d) {
      d.x0 = d.x;
      d.y0 = d.y;
    });

    updateCallback(root);
  }

  var root;
  var updateCallback;

  var init = function(root_, updateCallback_) {
    root = root_;
    root.x0 = treeWidth / 2;
    root.y0 = 0;
    updateCallback = updateCallback_;
    updateTree(root);
  };

  // expose only the init function. All other variables are "private" thanks to the closure.
  return { init: init };
})();