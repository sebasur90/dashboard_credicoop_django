
var js_variable = JSON.parse(document.getElementById('valores').textContent);

console.log(js_variable)

Highcharts.chart('container2', {
    chart: {
        type: 'area',
        options3d: {
            enabled: true,
            alpha: 15,
            beta: 30,
            depth: 200
        }
    },
    title: {
        text: 'Visual comparison of Mountains Panorama'
    },
    accessibility: {
        description: 'The chart is showing the shapes of three mountain ranges as three area line series laid out in 3D behind each other.',
        keyboardNavigation: {
            seriesNavigation: {
                mode: 'serialize'
            }
        }
    },
    lang: {
        accessibility: {
            axis: {
                xAxisDescriptionPlural: 'The chart has 3 unlabelled X axes, one for each series.'
            }
        }
    },
    yAxis: {
        title: {
            text: 'Height Above Sea Level',
            x: -40
        },
        labels: {
            format: '{value:,.0f} MAMSL'
        },
        gridLineDashStyle: 'Dash'
    },
    xAxis: [{
        visible: false
    }, {
        visible: false
    }, {
        visible: false
    }],
    plotOptions: {
        area: {
            depth: 100,
            marker: {
                enabled: false
            },
            states: {
                inactive: {
                    enabled: false
                }
            }
        }
    },
    tooltip: {
        valueSuffix: ' MAMSL'
    },
    series: [{
        name: 'Tatra Mountains visible from Rusinowa polana',
        lineColor: 'rgb(180,90,50)',
        color: 'rgb(200,110,50)',
        fillColor: 'rgb(200,110,50)',
        data: js_variable[0]
    }, {
        xAxis: 1,
        lineColor: 'rgb(120,160,180)',
        color: 'rgb(140,180,200)',
        fillColor: 'rgb(140,180,200)',
        name: 'Dachstein panorama seen from Krippenstein',
        data: js_variable[1]
    }, {
        xAxis: 2,
        lineColor: 'rgb(200, 190, 140)',
        color: 'rgb(200, 190, 140)',
        fillColor: 'rgb(230, 220, 180)',
        name: 'Panorama from Col Des Mines',
        data: js_variable[2]
    }]
});