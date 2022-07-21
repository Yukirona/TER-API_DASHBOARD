var chart_type = 'value1';
window.onload = function() {

document.getElementById("chart").style.visibility = "hidden";

$('#data').load('/home');
$('#data').empty();
$('#tab_title').empty();
}


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
   $('#chartcontainer').empty();
   document.getElementById("chart").style.visibility = "hidden";

   
});



$('#POP_T1').on('click', function(){
   $('#data').load('/Population #POPT1,#POPT1_title');
   document.getElementById("chart").style.visibility = "hidden";
   $('#chartcontainer').empty()
   
   
});

$('#FAM_G1').on('click', function(){
    $('#data').load('/Population #FAMG1,#FAMG1_title');
    document.getElementById("chart").style.visibility = "visible";
    $('#chartcontainer').empty()
    chart_type = 'line';
    
    
 });

 $('#FAM_G5').on('click', function(){
    
    $('#data').load('/Population #FAMG5,#FAMG5_title');
    document.getElementById("chart").style.visibility = "visible";
    $('#chartcontainer').empty()
    chart_type = 'bar';
    
         
         
});

$('#LOG_G2').on('click', function(){
    
  $('#data').load('/Population #LOGG2,#LOGG2_title');
  document.getElementById("chart").style.visibility = "visible";
  $('#chartcontainer').empty()
  chart_type = 'pie';
  
       
       
});


 $('#chart').on ('click', function() {
   console.log("Button clicked!");
   console.log(chart_type);
   // Task is to execute callbackFirst
   // function first and then execute
   // callbackSecond function.
   callbackFirst();
   
});



function callbackFirst() {
   console.log("First Function start");
   var elm = document.querySelector('table[class="dataframe"]');
   document.getElementById(elm.id).setAttribute("id", "datatable");
   console.log("First Function end");
   console.log(chart_type);
   if (chart_type == 'line') {
    callbackline()
   }
   else if (chart_type == 'bar') {
    callbackbar()
   }
   else if (chart_type == 'pie') {
    callbackpie()
   }
   
   
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

function callbackpie() {
  console.log("Second Function start");
  Highcharts.chart('chartcontainer', {
     data: {
       table: 'datatable',
       switchRowsAndColumns: false

     },
     chart: {
       type: 'pie'
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
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
      pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {
              enabled: true,
              format: '<b>{point.name}</b>: {point.percentage:.1f} %'
          }
      }
  },
   });
  console.log("Second Function end");
}