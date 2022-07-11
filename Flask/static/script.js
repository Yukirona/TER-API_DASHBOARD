
$(document).ready(function () {
   $('#sidebarCollapse').on('click', function () {
       $('#sidebar').toggleClass('active');
   });

   $('#clear').on('click', function(){
      $('#data').empty()
   
   });

   $('#HOME').on('click', function(){
      $('#data').load('/home');
   });

   $('#POPT0').on('click', function(){
      $('#data').load('/Population #POPT0');
   
   });

   $('#sidebarCollapse').on('click', function(){
      
   
   });
   
   $('#POPT1').on('click', function(){
      $('#data').load('/Population #POPT1');
      

      
   
   });
   $('#POPT2').on('click', function(){
      $('#data').load('/Population #POPT2');
   
   });
   $('#POPT2M').on('click', function(){
      $('#data').load('/Population #POPT2M');
   
   });

   $('#POPG2').on('click', function(){
      $('#data').load('/Population #POPG2');
   
   });


   $('#chart').on('click', function() {
      

      Highcharts.chart('chartcontain', {
   
          data: {
   
              table: 'datatable'
   
          },
   
          chart: {
   
              type: 'column'
              
   
          },
   
          title: {
   
              text: 'Data extracted from a HTML table in the page'
   
          },
   
          yAxis: {
   
              allowDecimals: false,
   
              title: {
   
                  text: 'Units'
   
              }
   
          },
   
          tooltip: {
   
              formatter: function() {
   
                  return '<b>' + this.series.name + '</b><br/>' +
   
                      this.point.y + ' ' + this.point.name.toLowerCase();
   
              }
   
          }
   
      });
   
   
   
   });
   
   

});





