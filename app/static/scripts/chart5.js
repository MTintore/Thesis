var chart = c3.generate({
    bindto: '#chart5',
    data: {
        url: '../static/CSV/Chart_data/passed_first_all.csv?rnd='+(new Date).getTime(),
        x:'AC_YEAR',
        type: 'bar',
    },
    axis: {
        y: {
            label: {
                text:"Average number of subjects",
                position: "outer-middle"
            },
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
    bar:{
        width:{ratio:0.7}
    },        
}); 