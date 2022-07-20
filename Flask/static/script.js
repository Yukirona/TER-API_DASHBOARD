window.onload = function() {

document.getElementById("chart").style.visibility = "hidden";}


$('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
});

$('#clear').on('click', function(){
   $('#data').empty()
   $('#chartcontainer').empty()
   $('#tab_title').empty()


});

$('#HOME').on('click', function(){
   $('#data').load('/home');
});



$('#POP_T1').on('click', function(){
   $('#data').load('/Population #POPT1');
   document.getElementById("chart").style.visibility = "hidden";

   
});

$('#FAM_G1').on('click', function(){
    $('#data').load('/Population #FAMG1');
    document.getElementById("chart").style.visibility = "visible";

    
 });

 $('#FAM_G5').on('click', function(){
    
         $('#data').load('/Population #FAMG5,#FAMG5_title');
         document.getElementById("chart").style.visibility = "visible";
         var type_chart = 'line'
         return(type_chart)
         
});


 $('#chart').on ('click', function() {
   console.log("Button clicked!");
   
   // Task is to execute callbackFirst
   // function first and then execute
   // callbackSecond function.
   callbackFirst();
   a
});



function callbackFirst() {
   console.log("First Function start");
   var elm = document.querySelector('table[class="dataframe"]');
   console.log(elm.id);
   document.getElementById(elm.id).setAttribute("id", "datatable");
   console.log("First Function end");
   
   // Execute callbackSecond() now as its
   // the end of callbackFirst()
   callbackline();
}
var hidden = ''
function callbackbar() {
   console.log("Second Function start");
   Highcharts.chart('chartcontainer', {
      data: {
        table: 'datatable'
      },
      chart: {
        type: 'bar'
      },
      title: {
        text: hidden
      },
      credits: {
        enabled: false
      },
      yAxis: {
        allowDecimals: true,
        title: {
          text: 'pourcentage'
        }
      },
      tooltip: {
        formatter: function () {
          return '<b>' + this.series.name + '</b><br/>' +
            this.point.y + ' ' + this.point.name.toLowerCase();
        }
      }
    });
   console.log("Second Function end");
}


function callbackline() {
  console.log("Second Function start");
  Highcharts.chart('chartcontainer', {
     data: {
       table: 'datatable',
       switchRowsAndColumns: true

     },
     chart: {
       type: 'line'
     },
     title: {
       text: hidden
     },
     credits: {
       enabled: false
     },
     yAxis: {
      allowDecimals: true,
      title: {
        text: 'habitants'
      }
    },
    tooltip: {
      formatter: function () {
        return '<b>' + this.series.name + '</b><br/>' +
          this.point.y + ' ' + this.point.name.toLowerCase();
      }
    }
   });
  console.log("Second Function end");
}

 