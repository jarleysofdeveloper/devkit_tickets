$(document).ready(function () {
    
    const getCasesforDatabase = (()=>{
        // Inicializar la tabla DataTable
        $('#tableCases').DataTable({
            ajax: {
                url: 'http://192.168.18.5:5000/api/v1/getcases',
                dataSrc: ''
            },
            columns: [
                { data: 'id' },
                { data: 'description' },
                { data: 'dateCase'},
                {
                    // Nueva columna para el botón de acción
                    data: null,
                    render: function(data, type, row) {
                        return "<button class='btn-action btn btn-info' data-id='" + row.id + "'>Detalles</button>";
                    }
                }
            ]
        });
        

    });

    const reloadTable = (()=>{
        $('#tableCases').DataTable().ajax.reload();
        console.log('ejecucion');
    })
    
    $('#tableCases tbody').on('click', '.btn-action', function() {
        // Obtener el ID de la fila correspondiente
        var id = $(this).data('id');
        
        // Aquí puedes realizar la acción que desees con el ID, por ejemplo, mostrar un mensaje
        console.log('Realizando acción para el elemento con ID ' + id);
    });

    $('#reload').click(()=>{
        reloadTable();
    })

    getCasesforDatabase();

});