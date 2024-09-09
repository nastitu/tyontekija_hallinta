

$(document).ready(function(){
    // $("p").click(function(){
    //   $(this).hide();
    // });
    $("#id_työmaakunta").change(function () { //lataa kuntien tiedot
        var url = $("#tyontekijaForm").attr("data-kunnat-url");  // kuntien lataus url html:stä
        var maakuntaId = $(this).val();  // lataa valittu maakunta html:stä
  
        $.ajax({                       // alusta AJAX request
          url: url,                    // aseta url
          data: {
            'työmaakunta': maakuntaId       // Lisää työmaakunta get parametreihin views.py etsii
          },
          success: function (data) {   // `data` on mitä `lataa_kunnat` view funktio antaa
            $("#id_työkunta").html(data);  // korvaa työkunta valikon arvot serverin antamilla
          }
        });
  
      });

    $("#id_työkunta").change(function () { //lataa työpaikkatiedot
        var url = $("#tyontekijaForm").attr("data-tyopisteet-url");  // työpisteiden lataus url html:stä
        var kuntaId = $(this).val();  // lataa valittu kunta html:stä
  
        $.ajax({                        //alusta ajax request
          url: url,                     // aseta url
          data: {
            'työkunta': kuntaId         // Lisää työkunta get parametreihin views.py etsii
          },
          success: function (data) {   // `data` on mitä `lataa_kunnat` view funktio antaa
            $("#id_työpiste").html(data);  // korvaa työpiste valikon arvot serverin antamilla
          }
        });
  
      });

});
  
function tp_k_mk(){
    alert("CSS FILE TOIMII ??")
}