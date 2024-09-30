

$(document).ready(function(){

    var url2 = $("#tTable").attr("data-t-url");

    var taulu= $('#tTable').DataTable({
      language: {
        url: 'https://cdn.datatables.net/plug-ins/2.1.5/i18n/fi.json',
      },
      ajax: {
        url: url2, 
        method: "GET",
        dataSrc: '',  // Koska JSON ei ole sisäkkäinen
      },
      columns: [
        {data: 'sukunimi'},
        {data: 'etunimi'},
        {data: 'aloitus_pvm'},
        {data: 'lopetus_pvm'},
        {data: 'työsuhteen_tyyppi'},
        {data: 'työtehtävä'},
        {data: 'työkunta__nimi'},
        {data: 'työpiste__nimi'},
        {
          data: null,  // Data ei tule JSON:sta
          render: function(data, type, row) {
            // row.id on työntekijän ID JSON:sta
            var url = "/tyontekija/" + row.id;   // Käytetään rivin id:tä
            return '<a href="' + url + '" class="btn btn-primary">Muokkaa</a>';
          },
          orderable: false,  // Tämä sarake ei ole järjesteltävissä
        }
      ],
      columnDefs: [
        {
            targets: 2, // aloituspvm-sarakkeen indeksi
            render: function (data, type, row) {
                if (type === 'display' && data) {
                    // Käytetään day.js kirjastoa muotoiluun
                    return dayjs(data).format('DD.MM.YYYY');
                }
                return data;
            }
        },
        {
          targets: 3, // lopetuspvm-sarakkeen indeksi
          render: function (data, type, row) {
              if (type === 'display' && data) {
                  // Käytetään day.js kirjastoa muotoiluun
                  return dayjs(data).format('DD.MM.YYYY');
              }
              return data;
          }
      }
    ]
    });

    //suodatus kunnan mukaan
    $('#kuntaValikko').on('change', function(){
      taulu.column(6).search(this.value).draw();   
    });


    //työsuhteiden suodatus
    $('.tyosuhdeInput').on('change', function(){
      taulu.column(4).search(this.value).draw();   
    });

    //suodatin joka suodattaa entinen-nykyinen-tuleva valinnat
    $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
      // Haetaan valintaruutujen tilat
      var entinen = $('#entinen').prop('checked');
      var nykyinen = $('#nykyinen').prop('checked');
      var tuleva = $('#tuleva').prop('checked');
      var tanaan = new Date(); // Nykyinen päivämäärä (tänään)

      // Luetaan sarakkeen 2 (aloituspäivämäärä) ja sarakkeen 3 (lopetuspäivämäärä) tiedot
      var startDate = new Date(data[2]); 
      var endDate = new Date(data[3]);   

      // Entinen suodatin: Näytä rivit, joiden lopetusspäivämäärä on menneisyydessä
      if (entinen && endDate < tanaan) {
          return true;
      }

      // Nykyinen suodatin: Näytä rivit, joiden aloituspäivämäärä <= tänään ja lopetuspäivämäärä >= tänään tai tyhjä
      if (nykyinen && startDate <= tanaan && (endDate >= tanaan || data[3] === "")) {
          return true;
      }

      // Tuleva suodatin: Näytä rivit, joiden aloituspäivämäärä on tulevaisuudessa
      if (tuleva && startDate > tanaan) {
          return true;
      }

      return false; // Jos mikään ehto ei täyty, piilota rivi
  });

  // Piirretään taulukko uudelleen aina, kun jokin valintaruutu muuttuu
  $('.aikaInput').on('change', function() {
      taulu.draw(); // Päivitä DataTables-taulukko uusien suodatuskriteerien mukaan
  });
    // $('.aikaInput').on('change', function(){
    //   var entinen = $('#entinen').prop('checked');
    //   var nykyinen=$('#nykyinen').prop('checked');
    //   var tuleva =$('#tuleva').prop('checked');
    //   // var milloin= this.value;
    //   // var valittu = $(this).prop('checked');
    //   var tanaan= new Date();
    //   console.log(entinen);
    //   console.log(nykyinen);
    //   console.log(tuleva);
    //   table.column(2).search("").column(3).search(""); //nollaus
    //   // console.log(milloin)
    //   // console.log(valittu)
    //   console.log(tanaan);


    //   // if(entinen){
    //   //   table
    //   //   .column(3)
    //   //   .search((d) => new Date(d) < tanaan);
    //   // }

    //   // if(nykyinen){
    //   //   table
    //   //   .column(2)
    //   //   .search((d) => new Date(d) <= tanaan)
    //   //   .column(3)
    //   //   .search((d) => new Date(d) >= tanaan || d=="");
    //   // }
    //   // if(tuleva){
    //   //   table
    //   //   .column(2)
    //   //   .search((d) => new Date(d) > tanaan);
    //   // }

    //   if(entinen && nykyinen && tuleva){
    //     table.column(2).search("").column(3).search(""); 
    //   }else if(!entinen && nykyinen && tuleva){
    //     table
    //     .column(3)
    //     .search((d) => new Date(d) >= tanaan || d=="");
    //   }else if(entinen && !nykyinen && tuleva){//////////Ei toimi
        
    //     var aloitus;
    //     table.column(2).search((d) => {
    //       aloitus = new Date(d);
    //       return aloitus != tanaan; // Tämä palauttaa true, jos aloitus on ennen tai jälkeen
    //     }).column(3).search((d) => {
    //       const lopetus = new Date(d);
    //       if (aloitus>tanaan){
    //         return ( lopetus > tanaan) || (lopetus === ""); // Ennen tai tyhjää
    //       }else{
    //         return ( lopetus < tanaan);
    //       }
          
        
    //     });

    //     console.log(aloitus);


    //   }else if(entinen && nykyinen && !tuleva){
    //     table
    //     .column(2)
    //     .search((d) => new Date(d) <= tanaan)
    //   }else if(entinen && !nykyinen && !tuleva){
    //     table
    //     .column(3)
    //     .search((d) => new Date(d) < tanaan);
    //   }else if(!entinen && nykyinen && !tuleva){
    //     table
    //     .column(2)
    //     .search((d) => new Date(d) <= tanaan)
    //     .column(3)
    //     .search((d) => new Date(d) >= tanaan || d=="");
    //   }else if(!entinen && !nykyinen && tuleva){
    //     table
    //     .column(2)
    //     .search((d) => new Date(d) > tanaan);
    //   }else if(!entinen && !nykyinen && !tuleva){
    //     table.column(2).search("1=0").column(3).search("1=0"); // Tyhjennetään taulukko
    //   }

  
    //   table.draw();

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
  