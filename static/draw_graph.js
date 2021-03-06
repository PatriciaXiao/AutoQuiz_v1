// environmental settings
console.log($('#main_container').height())
var content_height = $('#sidebar_container').height();
var name_height = $('#section_name_container').height()

var dom = document.getElementById("graph_container");

dom.style.height = (content_height - name_height) + "px";

var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    /*
    title: {
        text: 'Graph 简单示例'
    },*/
    tooltip: {},
    animationDurationUpdate: 1500,
    animationEasingUpdate: 'quinticInOut',
    series : [
        {
            type: 'graph',
            layout: 'none',
            symbolSize: 50,
            roam: true,
            label: {
                normal: {
                    show: true
                }
            },
            edgeSymbol: ['circle', 'arrow'],
            edgeSymbolSize: [4, 10],
            edgeLabel: {
                normal: {
                    textStyle: {
                        fontSize: 20
                    }
                }
            },
            data: [{
                name: '节点1',
                x: 300,
                y: 300
            }, {
                name: '节点2',
                x: 800,
                y: 300
            }, {
                name: '节点3',
                x: 550,
                y: 100
            }, {
                name: '节点4',
                x: 550,
                y: 500
            }],
            // links: [],
            links: [{
                source: 0,
                target: 1,
                symbolSize: [5, 20],
                label: {
                    normal: {
                        show: true
                    }
                },
                lineStyle: {
                    normal: {
                        width: 5,
                        curveness: 0.2
                    }
                }
            }, {
                source: '节点2',
                target: '节点1',
                label: {
                    normal: {
                        show: true
                    }
                },
                lineStyle: {
                    normal: { curveness: 0.2 }
                }
            }, {
                source: '节点1',
                target: '节点3'
            }, {
                source: '节点2',
                target: '节点3'
            }, {
                source: '节点2',
                target: '节点4'
            }, {
                source: '节点1',
                target: '节点4'
            }],
            lineStyle: {
                normal: {
                    opacity: 0.9,
                    width: 2,
                    curveness: 0
                }
            }
        }
    ]
};;
if (option && typeof option === "object") {
    myChart.setOption(option, true);
    myChart.on('click', function (params) {
        console.log(params);
        if (params.componentSubType === 'graph' && params.dataType === 'node') {
            var data = params.data;
            console.log(data.name);
            // alert(data);
            document.getElementById('modal_content').innerHTML = data.name;
            triggle_modal();
        }
    });
}