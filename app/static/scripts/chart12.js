var chart = c3.generate({
    bindto: '#chart12',
    data: {
        url: '../static/CSV/Chart_data/amean.csv?rnd='+(new Date).getTime(),
        x:'AC_YEAR',
        type: 'spline'
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