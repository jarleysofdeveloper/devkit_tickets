$(document).ready(function () {

    var socket = io.connect('http://192.168.18.5:5000');

    
    const getCasesforDatabase = (()=>{
        var dataTable;

        $('#tableCases').DataTable({
            "language": {
                "url": "https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json"
            },
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
        
        socket.on('connect', function() {
            socket.emit('join_room', { room: 'all_users' });

            socket.emit('update_table_data');
            
        });

        // Manejar el evento 'update_table_data' para recargar solo los datos de la DataTable
        socket.on('update_table_data', function() {
            dataTable = $('#tableCases').DataTable();
            if (dataTable) {
                dataTable.ajax.reload();
                //console.log('DataTable actualizada');
            }
        });
        
        //actualiza la tabla en forma bidireccional
        socket.emit('reload_table');

    });

    /*const reloadTable = (()=>{
        $('#tableCases').DataTable().ajax.reload();

    })*/
    
    $('#tableCases tbody').on('click', '.btn-action', function() {
        // Obtener el ID de la fila correspondiente
        var id = $(this).data('id');
        
        // Aquí puedes realizar la acción que desees con el ID, por ejemplo, mostrar un mensaje
        console.log('Realizando acción para el elemento con ID ' + id);
    });

    $('#reload').click(()=>{
        //emite la actualizacion de la tabla en las diferentes pantallas donde se este visualizando
        socket.emit('reload_table');
    })
    
    getCasesforDatabase();

});