// 监视模块
(function () {
    $(".monitor .tabs").on("click", "a", function () {
        $(this)
            .addClass('active')
            .siblings('a')
            .removeClass('active');
        $(".monitor .content")
            .eq($(this).index())
            .show()
            .siblings(".content")
            .hide();
    });
    $('.marquee-view .marquee').each(function () {
        var rows = $(this)
            .children()
            .clone();
        $(this).append(rows);
    })

})();
// 点位分布模块
(function () {
    var myChart = echarts.init(document.querySelector('.pie'))
    var option = {

        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        color: [
            '#006cff',
            '#60cda0',
            '#ed8884',
            '#ff9f7f',
            '#0096ff',
            '#9fe6b8',
            '#32c5e9',
            '#1d9dff'
        ],

        series: [
            {
                name: '点位统计',
                type: 'pie',
                radius: ['15%', '80%'],
                center: ['50%', '50%'],
                roseType: 'radius',
                data: [
                    { value: 20, name: "云南" },
                    { value: 26, name: "北京" },
                    { value: 24, name: "山东" },
                    { value: 25, name: "河北" },
                    { value: 20, name: "江苏" },
                    { value: 25, name: "浙江" },
                    { value: 30, name: "四川" },
                    { value: 42, name: "湖北" }

                ],
                label: {
                    fontSize: 10,
                    fontStyle: 'normal',
                    fontWeight: 'normal'

                },
                labelLine: {
                    length: 6,
                    length2: 8
                }
            }
        ]
    };
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        // 让我们的图表调用 resize这个方法
        myChart.resize();
    });
})();


