
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
 
});






