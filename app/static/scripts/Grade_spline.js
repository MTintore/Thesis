var chart = c3.generate({
    bindto: '#Grade_spline',
    data: {
        url: '../static/CSV/Chart_data/grade_year.csv?rnd='+(new Date).getTime(),
        x:'AC_YEAR',
        type: 'area-spline',
        labels: true
    },
    axis: {
        y: {
            label: {
                text:"Grade",
                position: "outer-middle"
            },
            min:1,
            max:9
        },
        x: {
            label: {
                text:"Year",
                position: "outer-center"
            },
        }
    },
    size: {
        height: 400,
        width: 800
    },
    grid: {
        y: {
            show:true,
            lines: [
                {
                    value: 5, 
                    text: 'Passing grade'
                }
            ]
        }
    },
    bar:{
        width:{ratio:0.7}
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