var chart = c3.generate({
    bindto: '#chart8',
    data: {
        url: '../static/CSV/Chart_data/amean_year.csv?rnd='+(new Date).getTime(),
        x:'AC_YEAR',
        type: 'spline',
        axes:{
            Mean: "y",
            aMean: "y",
            a: "y2"
        }
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
        y2: {
            show: true,
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
});