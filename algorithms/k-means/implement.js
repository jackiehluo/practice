/* Class definitions */

/* A Point has a position defined by x, y and a centroid that it can be assigned to.
  When no centroid is assigned, the following is true: this.centroid === undefined
  Points are created when data is loaded. You shouldn't need to call new Point(...).
*/
function Point(x, y, centroid) {
  this.x = x;
  this.y = y;
  this.centroid = centroid;
}

/* A Centroid has a position defined by x,y.
  Centroids are created and removed by clicking on the Add Centroid and Remove Centroid buttons.
  You shouldn't need to call new Centroid(...).
  The id field is needed so that the same color is always used when displaying the centroid. Ignore this field.
*/
function Centroid(x, y, id) {
  this.x = x;
  this.y = y;
  this.id = id;
}

/* App variables */

//centroids is a list of the current centroids. It starts empty until you click on add centroid.
var centroids = [];

//points is a list of currently displayed points.
var points = [];


/* IMPLEMENT THE FUNCTIONS BELOW
--------------------------------
*/

/* For each point, assign it to the cluster represented by the closest centroid */
function assignCentroids() {
  for (i = 0; i < points.length; i++) {
    var min = Infinity;
    for (j = 0; j < centroids.length; j++) {
      var distance = Math.sqrt(Math.pow((points[i].x - centroids[j].x), 2) +
        Math.pow((points[i].y - centroids[j].y), 2));
      if (distance < min) {
        min = distance;
        points[i].centroid = centroids[j];
      }
    }
  }
}

/* Update the position of each centroid based on the points assigned to it. 
  The new position should be the mean of the positions of the points assigned to it.
*/
function updateCentroids() {
  for (i = 0; i < centroids.length; i++) {
    var count = 0;
    var total_x = 0;
    var total_y = 0;
    for (j = 0; j < points.length; j++) {
      if (points[j].centroid == centroids[i]) {
        count++;
        total_x += points[j].x;
        total_y += points[j].y;
      }
    }
    centroids[i].x = total_x / count;
    centroids[i].y = total_y / count;
  }
}
