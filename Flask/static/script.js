var chart_type = 'value1';
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
   $('#chartcontainer').empty()
   
   
});

$('#FAM_G1').on('click', function(){
    $('#data').load('/Population #FAMG1');
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
    callbacpie()
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
       switchRowsAndColumns: true

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
      formatter: function () {
        return '<b>' + this.series.name + '</b><br/>' +
          this.point.y + ' ' + this.point.name.toLowerCase();
      }
    }
   });
  console.log("Second Function end");
}