(function () {
    var myChart = echarts.init(document.querySelector('.line'));
    var option = null;
    var ROOT_PATH = 'https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples';
    var updateFrequency = 2000;
    var dimension = 0;

    // var countryColors = { "Australia": "#006cff", "Canada": "#60cda0", "China": "#ed8884", "Cuba": "#ff9f7f", "Finland": "#0096ff", "France": "#9fe6b8", "Germany": "#32c5e9", "Iceland": "#1d9dff", "India": "#f93", "Japan": "#bc002d", "North Korea": "#024fa2", "South Korea": "#000", "New Zealand": "#00247d", "Norway": "#ef2b2d", "Poland": "#dc143c", "Russia": "#d52b1e", "Turkey": "#e30a17", "United Kingdom": "#00247d", "United States": "#b22234" };

    $.when(
        $.getJSON('https://cdn.jsdelivr.net/npm/emoji-flags@1.3.0/data.json'),
        $.getJSON(ROOT_PATH + '/data/asset/data/life-expectancy-table.json')
    ).done(function (res0, res1) {
        var flags = res0[0];
        var data = res1[0];
        var years = [];
        for (var i = 0; i < data.length; ++i) {
            if (years.length === 0 || years[years.length - 1] !== data[i][4]) {
                years.push(data[i][4]);
            }
        }

        function getFlag(countryName) {
            if (!countryName) {
                return '';
            }
            return (flags.find(function (item) {
                return item.name === countryName;
            }) || {}).emoji;
        }
        var startIndex = 10;
        var startYear = years[startIndex];

        var option = {

            grid: {
                top: 5,
                bottom: 30,
                left: '28%',
                right: '10%'
            },
            xAxis: {
                max: 'dataMax',
                label: {
                    formatter: function (n) {
                        return Math.round(n);
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: 'rgba(148, 208, 240,0.8)',
                        // width: 1,//这里是为了突出显示加上的
                    }
                },
            },
            dataset: {
                source: data.slice(1).filter(function (d) {
                    return d[4] === startYear;
                })
            },
            yAxis: {
                type: 'category',
                inverse: true,
                max: 15,
                axisLine: {
                    lineStyle: {
                        color: 'rgba(148, 208, 240,0.8)',
                        width: 3,//这里是为了突出显示加上的
                    }
                },
                axisLabel: {
                    show: true,
                    textStyle: {
                        fontSize: 14
                    },
                    formatter: function (value) {
                        return value + '{flag|' + getFlag(value) + '}';
                    },
                    rich: {
                        flag: {
                            fontSize: 25,
                            padding: 5
                        }
                    }
                },
                animationDuration: 300,
                animationDurationUpdate: 300
            },
            series: [{
                realtimeSort: true,
                seriesLayoutBy: 'column',
                type: 'bar',
                itemStyle: {
                    // color: function (param) {
                    // return countryColors[param.value[3]] || '#5470c6';
                    // }
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(10, 67, 188,1)'
                    }, {
                        offset: 1,
                        color: 'rgba(65,65,65,0.1)'
                    }])

                },
                encode: {
                    x: dimension,
                    y: 3
                },
                label: {
                    show: true,
                    precision: 1,
                    position: 'right',
                    valueAnimation: true,
                    fontFamily: 'monospace'
                }
            }],
            // Disable init animation.
            animationDuration: 0,
            animationDurationUpdate: updateFrequency,
            animationEasing: 'linear',
            animationEasingUpdate: 'linear',
            graphic: {
                elements: [{
                    type: 'text',
                    right: 160,
                    bottom: 60,
                    style: {
                        text: startYear,
                        font: 'bolder 80px monospace',
                        fill: 'rgba(100, 100, 100, 0.25)'
                    },
                    z: 100
                }]
            }
        };

        // console.log(option);
        myChart.setOption(option);

        for (var i = startIndex; i < years.length - 1; ++i) {
            (function (i) {
                setTimeout(function () {
                    updateYear(years[i + 1]);
                }, (i - startIndex) * updateFrequency);
            })(i);
        }

        function updateYear(year) {
            var source = data.slice(1).filter(function (d) {
                return d[4] === year;
            });
            option.series[0].data = source;
            option.graphic.elements[0].style.text = year;
            myChart.setOption(option);
        }
    })


    // window.addEventListener("resize", function () {
    //     // 让我们的图表调用 resize这个方法
    //     myChart.resize();
    // });
    // console.log(_rawData);
})();