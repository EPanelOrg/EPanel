var button='<button class="close" type="button" title="Remove this page">×</button>';
var homeID = 0;

function resetTab(){
	var tabs=$("#tab-list li:not(:first)");
	var len=1
	$(tabs).each(function(k,v){
		len++;
		$(this).find('a').html('home ' + len + button);
	})
	homeID--;
}

$(document).ready(function() {
    $('#btn-add-tab').click(function() {
        homeID++;
        $('#tab-list').append($('<li><a href="#home' + homeID + '" role="tab" data-toggle="tab"><span> 	&#127968;' + homeID + '</span> <span class="glyphicon glyphicon-pencil text-muted edit"></span> <button class="close" type="button" title="Remove this page">×</button></a></li>'));
        $('#tab-content').append($('<div class="tab-pane fade" id="home' + homeID + '"><h4>sections of home ' + homeID + ' <h4><div class="grid-container" id="home' + homeID + '"'));
        $(".edit").click(editHandler);


    });
    
    $('#tab-list').on('click', '.close', function() {
        var homeID = $(this).parents('a').attr('href');
        $(this).parents('li').remove();
        $(homeID).remove();
    });

    var list = document.getElementById("tab-list");
});

var editHandler = function() {
  var t = $(this);
  t.css("visibility", "hidden");
  $(this).prev().attr("contenteditable", "true").focusout(function() {
    $(this).removeAttr("contenteditable").off("focusout");
    t.css("visibility", "visible");
  });
};

//var sectionID =1;
//$(document).ready(function() {
//  $('#btn-add-section').click(function() {
//      sectionID++;
////      $('#section-content').append($('<img src="../statics/images/im.png" />'));
//        $('#tab-content').append($('<img src="../statics/images/im.png" />'));
//
//  });

//  $('#tab-content').on('click', '.close', function() {
//      var sectioneID = $(this).parents('a').attr('href');
//      $(this).parents('li').remove();
//      $(sectioneID).remove();
//  });

//});
