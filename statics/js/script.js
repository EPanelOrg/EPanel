$(function () {
    loadHomeAjax();
    $("#newHome").click(sentHomeAjax)
});

function loadHomeAjax() {

    $.ajax
    ({
        type: "GET",
        url: "http://127.0.0.1:8000/home-api/",
        dataType: 'json',
        headers: {
            "Authorization": "Bearer " + localStorage.token
        },
        success: function (data, status) {
//            $("#pName").html(data['profileData']['name'])
            alert(data)

        }
    })
    ;
}

function sentHomeAjax() {
    var address;
    address =  $("#address").val().toString();

    $.ajax
    ({
        type: "POST",
        url: "http://127.0.0.1:8000/home-api/",
        data: JSON.stringify({
                    address : address,
                }),
        headers: {
            "Authorization": "Bearer " + localStorage.token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function(result) {
                        alert("home added!");
      }
     });
}
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
        $('#tab-content').append($('<div class="tab-pane fade" id="home' + homeID + '"><h4>sections of home ' + homeID + ' </h4></div>'));
//                $('#ta    b-content').append($('<div class="tab-pane fade" id="home' + homeID + '"><h4>sections of home ' + homeID + ' </h4><button id="btn-add-section" type="button" class="btn btn-primary pull-right">&#43 </button><div class="grid-container" id="section' + homeID + '"></div></div>'));

        $(".edit").click(editHandler);


    });
    
    $('#tab-list').on('click', '.close', function() {
        var homeID = $(this).parents('a').attr('href');
        $(this).parents('li').remove();
        $(homeID).remove();
        // true ???
        $.ajax
            ({
                type: "DELETE",
                url: "http://127.0.0.1:8000/home-api/",
                data: JSON.stringify({
                            pk : homeID,
                        }),
                headers: {
                    "Authorization": "Bearer " + localStorage.token,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                success: function(result) {
                                alert("home deleted!");
              }
             });
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
//      $('#section1').append($('<img src="../statics/images/im.png" />'));
////        $('#tab-content').append($('<img src="../statics/images/im.png" />'));
//
//  });
//  $('#tab-content').on('click', '.close', function() {
//      var sectioneID = $(this).parents('a').attr('href');
//      $(this).parents('li').remove();
//      $(sectioneID).remove();
//  });
//});
