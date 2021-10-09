'use strict';

let myChart;
let myChart2;

$('#plant_id').on('change', function(){
    const selectedPlant = $(this).val()
    
    let defaultData = [];
    let defaultData2 = [];
    
    $.ajax({
        method: 'GET',
        url: 'api/chart/' + selectedPlant,
        success: function (data) {
            const ctx = $('#myChart');
            if (myChart) myChart.destroy();;

            defaultData = data.generation_points;
            defaultData2 = data.irradiation_points;

            myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    datasets: [{
                        label: 'Generation',
                        data: defaultData,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                        ],
                        borderWidth: 1
                    },
                    {
                        label: 'Irradiation',
                        data: defaultData2,
                        backgroundColor: [
                            'rgba(255, 206, 86, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255, 206, 86, 1)',
                        ],
                        borderWidth: 1
                    }
                    ]
                },
                options: {
                scales: {
                 y: {
                        beginAtZero: true
                }
            }
        }
        });
        }
    });

    
});

