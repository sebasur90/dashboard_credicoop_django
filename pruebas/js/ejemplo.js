var ctx = document.getElementById("grafica").getContext("2d");
var myCharts = new Chart(ctx, {
    type: "bar",
    data: {
        labels: ['col1', 'col2', 'col3'],
        datasets: [{
            label: "Num Datos",
            data: [10, 9, 15],
            borderWidth: 2,
            borderRadius: 25,
            // borderSkipped: false,

        }]


    }
})