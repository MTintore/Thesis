var chart = c3.generate({
    bindto: '#chart13',
    data: {
        url: '../static/CSV/Chart_data/alpha.csv?rnd='+(new Date).getTime(),
        x:'AC_YEAR',
        type: 'spline'
    },
    axis: {
        y: {
            label: {
                text:"Alpha",
                position: "outer-middle"
            },
            min:0.1,
            max:0.9
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