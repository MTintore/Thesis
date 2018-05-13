'use strict';
var data = []
function loadData(){
  d3.csv('../static/CSV/Chart_data/number_students.csv?rnd='+(new Date).getTime(), function(error, data) { 
    chart(data); 
  });
}
loadData()

function chart(data){
  var chart = c3.generate({
      bindto: '#chart3',
      data: {
        type: 'bar',
        json: data,
        keys: {
          x: 'AC_YEAR',
          value: ['Total women', 'Passed women', 'Total men', 'Passed men']
  
        },
        /* x: ['AC_YEAR'], */
        groups: [
          ['Total women', 'Passed women'],
          ['Total men', 'Passed men']
        ]
  
  
      },
      axis: {
        y: {
          label: {
            text: "Number of students",
            position: "outer-middle"
          },
          max:400
        },
        x: {
          label: {
            text: "Year",
            position: "outer-center"
          },
        }
      },
      size: {
        height: 400,
        width: 800
      },
      bar: {
        width: {
          ratio: 0.7
        }
      },
      legend: {
        show: true,
        position: 'inset',
        inset: {
          anchor: 'top-right',
          x: 10,
          y: 5,
          step: 2
        }
      }
    });
    updateChart();
}

function updateChart(){
  var totalWomen = []
   var passWomen = []
   d3.selectAll('.c3-shapes-Total-women>path').attr('temp', function(d) {
     totalWomen.push(d3.select(this).node().getBBox())
   });
 
   d3.selectAll('.c3-shapes-Passed-women>path').attr('temp', function(d) {
     passWomen.push(d3.select(this).node().getBBox())
   });
 
   d3.selectAll('.c3-shapes-Total-women').selectAll('rect').data(totalWomen).enter().append('rect')
     .attr('width', function(d) {
       return d.width - 15;
     }).attr('x', function(d, i) {
       return d.x - ((d.width - 15 - passWomen[i]['width']) / 2);
     }).attr('y', function(d, i) {
       return passWomen[i]['y'] - (d.height - passWomen[i]['height']);
     }).attr('height', function(d) {
       return d.height;
     }).attr('fill', 'steelblue');
 
   d3.selectAll('.c3-shapes-Passed-women').selectAll('rect').data(passWomen).enter().append('rect').attr('x', function(d, i) {
       return d.x;
     }).attr('width', function(d) {
       return d.width;
     }).attr('y', function(d) {
       return d.y;
     }).attr('height', function(d) {
       return d.height;
     }).attr('fill', 'orange')
     .attr('opacity', '0.25');
     
     
     
 var totalMen = []
   var passMen = []
   d3.selectAll('.c3-shapes-Total-men>path').attr('width', function(d) {
     totalMen.push(d3.select(this).node().getBBox())
   });
 
   d3.selectAll('.c3-shapes-Passed-men>path').attr('width', function(d) {
     passMen.push(d3.select(this).node().getBBox())
   });
   
   d3.selectAll('.c3-shapes-Total-men').selectAll('rect').data(totalMen).enter().append('rect')
     .attr('width', function(d) {
       return d.width - 15;
     }).attr('x', function(d, i) {
       return d.x - ((d.width - 15 - passMen[i]['width']) / 2);
     }).attr('y', function(d, i) {
       return passMen[i]['y'] - (d.height - passMen[i]['height']);
     }).attr('height', function(d) {
       return d.height;
     }).attr('fill', 'darkgreen');
 
   d3.selectAll('.c3-shapes-Passed-men').selectAll('rect').data(passMen).enter().append('rect').attr('x', function(d, i) {
       return d.x;
     }).attr('width', function(d) {
       return d.width;
     }).attr('y', function(d) {
       return d.y;
     }).attr('height', function(d) {
       return d.height;
     }).attr('fill', 'red')
     .attr('opacity', '0.25');
     
 }
 
updateChart();