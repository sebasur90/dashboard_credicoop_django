// const accion = JSON.parse(document.getElementById('lista'));
var js_variable = JSON.parse(document.getElementById('lista').textContent);

console.log(js_variable)

const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: js_variable,
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});