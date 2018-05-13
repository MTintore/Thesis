var labels = true; // show the text labels beside individual boxplots?
                    
var margin = {top: 25, right: 25, bottom: 25, left: 25};
var  width = 800 - margin.left - margin.right;
var height = 400 - margin.top - margin.bottom;
                     
var min = 0,
    max = 10;
                        
// parse in the data	
d3.csv("../static/CSV/Chart_data/boxplot_year.csv?rnd="+(new Date).getTime(), function(error, csv) {
                         
    var data = [];
    data[0] = [];
    data[1] = [];
    data[2] = [];
    data[3] = [];
    data[4] = [];
    data[5] = [];
                        
    data[0][0] = "Y2010";
    data[1][0] = "Y2011";
    data[2][0] = "Y2012";
    data[3][0] = "Y2013";
    data[4][0] = "Y2014";
    data[5][0] = "Y2015";
                        
    data[0][1] = [];
    data[1][1] = [];
    data[2][1] = [];
    data[3][1] = [];
    data[4][1] = [];
    data[5][1] = [];

                        
                      
    csv.forEach(function(x) {
        var v1 = Math.floor(x.Y2010),
            v2 = Math.floor(x.Y2011),
            v3 = Math.floor(x.Y2012),
            v4 = Math.floor(x.Y2013),
            v5 = Math.floor(x.Y2014),
            v6 = Math.floor(x.Y2015);
                                    
        var rowMax = Math.max(Math.max(v1,v2), Math.max(Math.max(v3,v4), Math.max(v5,v6)));
        var rowMin = Math.min(Math.min(v1,v2), Math.min(Math.min(v3,v4), Math.min(v5,v6)));
                    
        data[0][1].push(v1);
        data[1][1].push(v2);
        data[2][1].push(v3);
        data[3][1].push(v4);
        data[4][1].push(v5);
        data[5][1].push(v6);
                             
        if (rowMax > max) max = rowMax;
        if (rowMin < min) min = rowMin;	
    });
                      
    var chart = d3.box()
        .whiskers(iqr(1.5))
        .height(height)	
        .domain([min, max])
        .showLabels(labels);
                    
    var svg = d3.select("#Boxplot").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .attr("class", "box")    
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
                        
    // the x-axis
    var x = d3.scale.ordinal()	   
        .domain( data.map(function(d) { console.log(d); return d[0]; } ) )	    
        .rangeRoundBands([0 , width], 0.7, 0.3); 		
                    
    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");
                    
    // the y-axis
    var y = d3.scale.linear()
        .domain([min, max])
        .range([height + margin.top, 0 + margin.top]);
                        
    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");
                    
    // draw the boxplots	
    svg.selectAll(".box")	   
        .data(data)
       .enter().append("g")
       .attr("transform", function(d) { return "translate(" +  x(d[0])  + "," + margin.top + ")"; } )
        .call(chart.width(x.rangeBand()));
                     
    // draw y axis
    svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
        .append("text") // and text1
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "middle")
            .style("font-size", "10px") 
            .text("Grade");		
                        
    // draw x axis	
    svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + (height  + margin.top + 10) + ")")
            .call(xAxis)
        .append("text") // text label for the x axis
            .attr("x", (width / 2) )
            .attr("y",  10 )
            .attr("dy", ".71em")
            .style("text-anchor", "middle")
            .style("font-size", "10px") 
            .text("Year"); 
});
                    
// Returns a function to compute the interquartile range.
function iqr(k) {
    return function(d, i) {
        var q1 = d.quartiles[0],
            q3 = d.quartiles[2],
            iqr = (q3 - q1) * k,
            i = -1,
            j = d.length;
        while (d[++i] < q1 - iqr);
        while (d[--j] > q3 + iqr);
        return [i, j];
    };
}