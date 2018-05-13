                        var chart = c3.generate({
                            bindto: '#chart7',
                            data: {
                                url: '../static/CSV/Chart_data/amean_access.csv?rnd='+(new Date).getTime(),
                                x:'AC_GRADE',
                                type: 'scatter'
                            },
                            axis: {
                                y: {
                                    label: {
                                        text:"Alpha*mean",
                                        position: "outer-middle"
                                    },
                                    min:1,
                                    max:9
                                },
                                x: {
                                    label: {
                                        text:"Access grade",
                                        position: "outer-center"
                                    },
                                    min:1,
                                    max:9
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