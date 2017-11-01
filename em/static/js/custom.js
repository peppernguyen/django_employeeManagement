/**
 * Created by huongnm on 31/10/2017.
 */

$( document ).ready(function() {

     $('#chart-container').orgchart({
         'data' : $('#datasource'),
         'pan': true,
         // 'direction': 't2b',
         'zoom': true
      });
});

