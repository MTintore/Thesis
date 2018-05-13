var chart = c3.generate({
    bindto: '#chart6',
    data: {
        url: '../static/CSV/Chart_data/alpha_access.csv?rnd='+(new Date).getTime(),
        x:'AC_GRADE',
        type: 'scatter'
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
                text:"Access grade PAU",
                position: "outer-center"
            },
            min:9,
            max:14
        }
    },
    size: {
        height: 400,
        width: 800
    },
    zoom: {
        enabled: true
    }     
});