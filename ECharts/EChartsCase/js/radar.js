(function () {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector('.radarMap'));

    var dataMap = {};

    dataMap.datapoint1 = {
        //max : 60000,
        2014: [0.00287, 0.00961, 0.36, 0.0005, 0.0044, 0.00006],
        2013: [0.00441, 0.00705, 0.40, 0.0005, 0.0047, 0.00027],
        2012: [0.005, 0.062, 0.358, 0.0003, 0.004, 0.00021],
        2011: [0.003, 0.296, 0.37, 0.0003, 0.005, 0.0001],
        2010: [0.0005, 0.01, 0.38, 0.0003, 0.004, 0.0005],
        2009: [0.0005, 0.01, 0.45, 0.0003, 0.004, 0.0005],
        2008: [0.0005, 0.01, 0.33, 0.0003, 0.006, 0.0005],
        2007: [0.0005, 0.01, 0.47, 0.0003, 0.002, 0.0005],
        2006: [0.004, 0.01, 0.46, 0.00037, 0.005, 0.0005],
    };

    dataMap.datapoint2 = {
        //max : 4000,
        2014: [0.0035, 0.01367, 0.46, 0.0004, 0.0037, 0.00006],
        2013: [0.00426, 0.00572, 0.51, 0.0008, 0.0030, 0.00008],
        2012: [0.00448, 0.0390, 0.5200, 0.0003, 0.0041, 0.00009],
        2011: [0.0025, 0.277, 0.437, 0.0003, 0.005, 0.0001],
        2010: [0.0005, 0.01, 0.603, 0.0003, 0.005, 0.0005],
        2009: [0.0005, 0.01, 0.616, 0.0003, 0.004, 0.0005],
        2008: [0.0005, 0.01, 0.43, 0.0003, 0.0012, 0.0005],
        2007: [0.0005, 0.01, 0.73, 0.0003, 0.0012, 0.0005],
        2006: [0.007, 0.02, 0.52, 0.0005, 0.0057, 0.0005],
    };

    dataMap.datapoint3 = {
        //max : 26600,
        2014: [0.0026, 0.0087, 0.46, 0.0004, 0.0039, 0.00012],
        2013: [0.00411, 0.00557, 0.43, 0.0005, 0.0029, 0.00006],
        2012: [0.0037, 0.0493, 0.45, 0.0003, 0.0040, 0.0002],
        2011: [0.002, 0.308, 0.43, 0.0003, 0.005, 0.00016],
        2010: [0.0005, 0.01, 0.50, 0.0003, 0.005, 0.0005],
        2009: [0.0005, 0.01, 0.60, 0.0003, 0.004, 0.0005],
        2008: [0.0005, 0.01, 0.42, 0.0003, 0.001, 0.0005],
        2007: [0.0005, 0.01, 0.74, 0.0003, 0.001, 0.0005,],
        2006: [0.0005, 0.013, 0.46, 0.00045, 0.0052, 0.0005],
    };

    dataMap.datapoint4 = {
        //max : 25000,
        2014: [0.00328, 0.0061, 0.84, 0.0005, 0.0025, 0.00006],
        2013: [0.00853, 0.0110, 1.56, 0.0005, 0.0040, 0.00006],
        2012: [0.00557, 0.0374, 2.39, 0.0003, 0.0106, 0.00011],
        2011: [0.0059, 0.358, 1.86, 0.0003, 0.011, 0.0002],
        2010: [0.0005, 0.02, 1.86, 0.0003, 0.006, 0.0005],
        2009: [0.0005, 0.01, 1.57, 0.0003, 0.005, 0.0005,],
        2008: [0.0005, 0.01, 0.77, 0.0003, 0.005, 0.0005],
        2007: [0.0005, 0.072, 2.58, 0.0003, 0.001, 0.0005],
        2006: [0.007, 0.030, 1.25, 0.00054, 0.0053, 0.0005],
    };

    dataMap.datapoint5 = {
        //max : 3600,
        2014: [0.00309, 0.00849, 0.87, 0.0005, 0.0022, 0.00006],
        2013: [0.00979, 0.03553, 1.98, 0.0005, 0.0031, 0.00006],
        2012: [0.0077, 0.0729, 2.46, 0.0004, 0.0059, 0.00024],
        2011: [0.0046, 0.467, 1.76, 0.0004, 0.010, 0.00019],
        2010: [0.0005, 0.01, 2.06, 0.0003, 0.005, 0.00068],
        2009: [0.0005, 0.01, 1.76, 0.0008, 0.007, 0.0006],
        2008: [0.0005, 0.01, 1.04, 0.0005, 0.006, 0.0007],
        2007: [0.0005, 0.020, 1.77, 0.0005, 0.002, 0.0008],
        2006: [0.01, 0.031, 1.40, 0.0009, 0.0070, 0.0005],
    };

    dataMap.datapoint6 = {
        //max : 3200,
        2014: [0.00516, 0.00842, 1.06, 0.0005, 0.0022, 0.00006],
        2013: [0.0054, 0.01611, 1.17, 0.0005, 0.0025, 0.00006],
        2012: [0.0040, 0.0721, 1.10, 0.0003, 0.0041, 0.00013],
        2011: [0.002, 0.322, 1.16, 0.0003, 0.0072, 0.0002, 0.002],
        2010: [0.0005, 0.01, 1.31, 0.0003, 0.004, 0.0006],
        2009: [0.0005, 0.01, 0.94, 0.0003, 0.0048, 0.0005],
        2008: [0.0005, 0.02, 0.47, 0.0003, 0.006, 0.0005],
        2007: [0.0005, 0.01, 0.91, 0.0003, 0.0009, 0.0005],
        2006: [0.05, 0.023, 1.3, 0.00053, 0.006, 0.0005],
    };

    dataMap.datapoint7 = {
        //max : 3200,
        2014: [0.00395, 0.00862, 0.76, 0.0005, 0.0029, 0.00006],
        2013: [0.0075, 0.00591, 1.1, 0.0005, 0.0037, 0.00006],
        2012: [0.0052, 0.0613, 0.992, 0.0003, 0.0097, 0.00019],
        2011: [0.0028, 0.261, 1.55, 0.0004, 0.0137, 0.0001],
        2010: [0.0005, 0.01, 1.86, 0.0007, 0.007, 0.0005],
        2009: [0.0005, 0.01, 1.62, 0.0004, 0.011, 0.0005],
        2008: [0.0008, 0.01, 1.10, 0.0008, 0.010, 0.0007],
        2007: [0.0005, 0.01, 1.78, 0.00079, 0.003, 0.00067],
        2006: [0.01, 0.18, 1.44, 0.00077, 0.0086, 0.0005],
    };

    dataMap.datapoint8 = {
        //max : 3200,
        2014: [0.00597, 0.0064, 0.9, 0.0005, 0.0019, 0.00006],
        2013: [0.00829, 0.0147, 2.6, 0.0005, 0.0035, 0.00006],
        2012: [0.005, 0.081, 2.38, 0.0003, 0.0053, 0.00018],
        2011: [0.004, 0.373, 2.57, 0.0003, 0.0075, 0.0002],
        2010: [0, 0, 0, 0, 0, 0],
        2009: [0, 0, 0, 0, 0, 0],
        2008: [0, 0, 0, 0, 0, 0],
        2007: [0, 0, 0, 0, 0, 0],
        2006: [0, 0, 0, 0, 0, 0],
    };


    var option = {
        baseOption: {
            timeline: {
                // y: 0,
                axisType: 'category',
                // realtime: false,
                // loop: false,
                autoPlay: true,
                // currentIndex: 2,
                playInterval: 1000,
                // controlStyle: {
                //     position: 'left'
                // },
                data: ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014'],
                label: {
                    formatter: function (s) {
                        return (new Date(s)).getFullYear();
                    }
                }
            },
            title: {
                subtext: '数据来自那美克星环保局'
            },
            tooltip: {},
            legend: {
                x: 'right',
                y: 10,
                itemGap: 20,
                itemWidth: 28,
                itemHeight: 18,
                data: ['检测站点1', '检测站点2', '检测站点3', '检测站点4', '检测站点5', '检测站点6', '检测站点7', '检测站点8'],
                textStyle: {
                    color: [
                        '#006cff',
                        '#60cda0',
                        '#ed8884',
                        '#ff9f7f',
                        '#0096ff',
                        '#9fe6b8',
                        '#32c5e9',
                        '#1d9dff'
                    ]
                },

            },
            calculable: true,
            grid: {
                top: 150,
                right: '39%',
                left: '5%',
                bottom: 100,
            },
            xAxis: [{
                'type': 'category',
                'axisLabel': {
                    'interval': 0
                },
                'data': [
                    '铜', '锌', '氟化物', '硒', '砷', '铬'
                ],
                splitLine: {
                    show: true
                }
            }],
            yAxis: [{
                type: 'value',
                name: '监测结果(mg/L)',
            }],
            polar: [{
                indicator: [{
                    name: '铜',
                    max: 0.05

                }, {
                    name: '锌',
                    max: 0.47

                }, {
                    name: '氟化物',
                    max: 2.57

                }, {
                    name: '硒',
                    max: 0.001

                }, {
                    name: '砷',
                    max: 0.014

                }, {
                    name: '铬',
                    max: 0.001

                }],
                center: ['82%', '50%'],
                radius: 200
            }],
            calculable: true,

            series: [{
                name: '检测站点1',
                type: 'bar'
            }, {
                name: '检测站点2',
                type: 'bar'
            }, {
                name: '检测站点3',
                type: 'bar'
            }, {
                name: '检测站点4',
                type: 'bar'
            }, {
                name: '检测站点5',
                type: 'bar'
            }, {
                name: '检测站点6',
                type: 'bar'
            }, {
                name: '检测站点7',
                type: 'bar'
            }, {
                name: '检测站点8',
                type: 'bar'
            }, {
                name: '对比',
                type: 'radar',
            }]
        },
        options: [

            {
                title: {
                    text: '2006年地表水监测指标监测值',
                    textStyle: {
                        color: '#FFF',
                        fontWeight: 'normal',
                    },
                    subtextStyle: {
                        color: '#3fccf1',
                        fontWeight: 'normal'
                    },
                },

                series: [{
                    data: dataMap.datapoint1['2006']
                }, {
                    data: dataMap.datapoint2['2006']
                }, {
                    data: dataMap.datapoint3['2006']
                }, {
                    data: dataMap.datapoint4['2006']
                }, {
                    data: dataMap.datapoint5['2006']
                }, {
                    data: dataMap.datapoint6['2006']
                }, {
                    data: dataMap.datapoint7['2006']
                }, {
                    data: dataMap.datapoint8['2006']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2006']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2006']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2006']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2006']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2006']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2006']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2006']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2006']
                    }]
                }]
            }, {
                title: {
                    text: '2007年地表水监测指标监测值'
                },
                series: [{
                    data: dataMap.datapoint1['2007']
                }, {
                    data: dataMap.datapoint2['2007']
                }, {
                    data: dataMap.datapoint3['2007']
                }, {
                    data: dataMap.datapoint4['2007']
                }, {
                    data: dataMap.datapoint5['2007']
                }, {
                    data: dataMap.datapoint6['2007']
                }, {
                    data: dataMap.datapoint7['2007']
                }, {
                    data: dataMap.datapoint8['2007']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2007']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2007']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2007']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2007']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2007']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2007']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2007']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2007']
                    }]
                }]
            },


            {
                title: {
                    text: '2008年地表水监测指标监测值'
                },
                series: [{
                    data: dataMap.datapoint1['2008']
                }, {
                    data: dataMap.datapoint2['2008']
                }, {
                    data: dataMap.datapoint3['2008']
                }, {
                    data: dataMap.datapoint4['2008']
                }, {
                    data: dataMap.datapoint5['2008']
                }, {
                    data: dataMap.datapoint6['2008']
                }, {
                    data: dataMap.datapoint7['2008']
                }, {
                    data: dataMap.datapoint8['2008']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2008']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2008']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2008']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2008']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2008']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2008']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2008']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2008']
                    }]
                }]
            }, {
                title: {
                    text: '2009年地表水监测指标监测值'
                },
                series: [{
                    data: dataMap.datapoint1['2009']
                }, {
                    data: dataMap.datapoint2['2009']
                }, {
                    data: dataMap.datapoint3['2009']
                }, {
                    data: dataMap.datapoint4['2009']
                }, {
                    data: dataMap.datapoint5['2009']
                }, {
                    data: dataMap.datapoint6['2009']
                }, {
                    data: dataMap.datapoint7['2009']
                }, {
                    data: dataMap.datapoint8['2009']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2009']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2009']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2009']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2009']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2009']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2009']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2009']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2009']
                    }]
                }]
            }, {
                title: {
                    text: '2010年地表水监测指标监测值'
                },
                series: [{
                    data: dataMap.datapoint1['2010']
                }, {
                    data: dataMap.datapoint2['2010']
                }, {
                    data: dataMap.datapoint3['2010']
                }, {
                    data: dataMap.datapoint4['2010']
                }, {
                    data: dataMap.datapoint5['2010']
                }, {
                    data: dataMap.datapoint6['2010']
                }, {
                    data: dataMap.datapoint7['2010']
                }, {
                    data: dataMap.datapoint8['2010']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2010']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2010']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2010']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2010']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2010']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2010']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2010']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2010']
                    }]
                }]
            }, {
                title: {
                    text: '2011年地表水监测指标监测值'
                },
                series: [{
                    data: dataMap.datapoint1['2011']
                }, {
                    data: dataMap.datapoint2['2011']
                }, {
                    data: dataMap.datapoint3['2011']
                }, {
                    data: dataMap.datapoint4['2011']
                }, {
                    data: dataMap.datapoint5['2011']
                }, {
                    data: dataMap.datapoint6['2011']
                }, {
                    data: dataMap.datapoint7['2011']
                }, {
                    data: dataMap.datapoint8['2011']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2011']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2011']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2011']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2011']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2011']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2011']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2011']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2011']
                    }]
                }]
            }, {
                title: {
                    text: '2012年地表水监测指标监测值'
                },
                series: [{
                    data: dataMap.datapoint1['2012']
                }, {
                    data: dataMap.datapoint2['2012']
                }, {
                    data: dataMap.datapoint3['2012']
                }, {
                    data: dataMap.datapoint4['2012']
                }, {
                    data: dataMap.datapoint5['2012']
                }, {
                    data: dataMap.datapoint6['2012']
                }, {
                    data: dataMap.datapoint7['2012']
                }, {
                    data: dataMap.datapoint8['2012']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2012']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2012']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2012']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2012']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2012']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2012']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2012']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2012']
                    }]
                }]
            }, {
                title: {
                    text: '2013年地表水监测指标监测值'
                },
                series: [{
                    data: dataMap.datapoint1['2013']
                }, {
                    data: dataMap.datapoint2['2013']
                }, {
                    data: dataMap.datapoint3['2013']
                }, {
                    data: dataMap.datapoint4['2013']
                }, {
                    data: dataMap.datapoint5['2013']
                }, {
                    data: dataMap.datapoint6['2013']
                }, {
                    data: dataMap.datapoint7['2013']
                }, {
                    data: dataMap.datapoint8['2013']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2013']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2013']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2013']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2013']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2013']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2013']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2013']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2013']
                    }]
                }]
            }, {
                title: {
                    text: '2014年地表水监测指标监测值'
                },
                series: [{
                    data: dataMap.datapoint1['2014']
                }, {
                    data: dataMap.datapoint2['2014']
                }, {
                    data: dataMap.datapoint3['2014']
                }, {
                    data: dataMap.datapoint4['2014']
                }, {
                    data: dataMap.datapoint5['2014']
                }, {
                    data: dataMap.datapoint6['2014']
                }, {
                    data: dataMap.datapoint7['2014']
                }, {
                    data: dataMap.datapoint8['2014']
                }, {
                    data: [{
                        name: '检测站点1',
                        value: dataMap.datapoint1['2014']
                    }, {
                        name: '检测站点2',
                        value: dataMap.datapoint2['2014']
                    }, {
                        name: '检测站点3',
                        value: dataMap.datapoint3['2014']
                    }, {
                        name: '检测站点4',
                        value: dataMap.datapoint4['2014']
                    }, {
                        name: '检测站点5',
                        value: dataMap.datapoint5['2014']
                    }, {
                        name: '检测站点6',
                        value: dataMap.datapoint6['2014']
                    }, {
                        name: '检测站点7',
                        value: dataMap.datapoint7['2014']
                    }, {
                        name: '检测站点8',
                        value: dataMap.datapoint8['2014']
                    }]
                }]
            },
        ]
    };


    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        // 让我们的图表调用 resize这个方法
        myChart.resize();
    });
})();