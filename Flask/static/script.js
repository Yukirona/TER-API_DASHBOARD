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
   
});

$('#FAM_G1').on('click', function(){
    $('#data').load('/Population #FAMG1');
    
 });

 $('#FAM_G5').on('click', function(){
    
         $('#data').load('/Population #FAMG5,#FAMG5_title');
         
      
   
});

$('#chart').on('click', function(){
  
    
 });


 $('#chart').on ('click', function() {
   console.log("Button clicked!");
   
   // Task is to execute callbackFirst
   // function first and then execute
   // callbackSecond function.
   callbackFirst();
});


{
  
}

function callbackFirst() {
   console.log("First Function start");
   var elm = document.querySelector('table[class="dataframe"]');
   console.log(elm.id);
   document.getElementById(elm.id).setAttribute("id", "datatable");
   console.log("First Function end");
   
   // Execute callbackSecond() now as its
   // the end of callbackFirst()
   callbackSecond();
}
var title = ' test '
function callbackSecond() {
   console.log("Second Function start");
   Highcharts.chart('chartcontainer', {
      data: {
        table: 'datatable'
      },
      chart: {
        type: 'bar'
      },
      title: {
        text: title
      },
      yAxis: {
        allowDecimals: false,
        title: {
          text: 'Units'
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



 