$(function() {
  var API_delete = "/api/_delete/",
      API_add = "/api/_add",
      $movies = $(".movies"),
      $status = $(".status"),
      $noRecords = $(".noMovies");

  var checkForEmpty = function(){
    // if there are no records, show "no records" msg
    hasNoRecords() ? $noRecords.show() : $noRecords.hide();
  };

  var manageStatus = function(msg, doShow){
    $status.html(msg);
    doShow ? $status.fadeIn(10, "linear") : $status.fadeOut(4000, "easeInOutQuad");
  };

  var hasNoRecords = function() {
    // do not consider "no-records" a record
    return $movies.find("li").length > 0 ? false : true;
  };

  var delete_record = function(e) {
    e.preventDefault();
    e.stopImmediatePropagation();

    // get data attrib of "data-id" on el
    var theID = $(this).parent().attr("data-id");

    $.getJSON(API_delete + theID, function(data) {

      // remove the record for the ID returned
      $('*[data-id="'+data.id+'"]').fadeOut(400, function() {
        $(this).remove();
        checkForEmpty();
      });
    });
    return false;
  };

  var add_record = function(e) {
      e.preventDefault();
      e.stopImmediatePropagation();
      var movie = {
          title: $("#id-title").val(),
          year:$("#id-year").val(),
          genre:$("#id-genre").val()
      }

      manageStatus("Status: Sending request...", true);

      $.ajax({
          url: API_add,
          type: 'post',
          dataType: 'json',
          data: movie,
          success: function (data) {

              // report status
              manageStatus("Status: " + data.result, false);

              // add new record to list
              $movies.prepend(data.html);

              // fade out new record background color...
              $('*[data-id="'+data.movie_id+'"]').removeClass("added", 4000, "easeInOutQuad");
              checkForEmpty();
          }
      });
  };

   var init = function(){

    // bind click events for all elements
    // present and future
    $movies.on('click','a.delete',delete_record);
    $("input.add").on('click',add_record);

    // handle messaging
    checkForEmpty();
  };

  init();

});

