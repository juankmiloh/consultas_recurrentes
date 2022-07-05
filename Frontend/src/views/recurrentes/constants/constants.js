/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    domItem: [
        {
            type: 'select',
            prop: 'servicio',
            label: 'Servicio',
            placeholder: 'Seleccione un servicio',
            disabled: false
        },
        {
            type: 'select',
            prop: 'consulta',
            label: 'Consulta',
            placeholder: 'Seleccione una consulta',
            disabled: false
        },
        {
            type: 'select',
            prop: 'idempresa',
            label: 'Empresa',
            placeholder: 'Seleccione una empresa',
            disabled: false
        },
        {
            type: 'select',
            prop: 'ano',
            label: 'Año',
            placeholder: 'Seleccione un año',
            disabled: false
        },
        {
            type: 'select',
            prop: 'mes',
            label: 'Mes',
            placeholder: 'Seleccione un mes',
            disabled: false
        }
    ],
    rulesFormItem: {
        servicio: [{
            required: true,
            message: 'Seleccione un servicio',
            trigger: 'change'
        }],
        consulta: [{
            required: true,
            message: 'Seleccione una consulta',
            trigger: 'change'
        }],
        idempresa: [{
            required: true,
            message: 'Seleccione una empresa',
            trigger: 'change'
        }],
        ano: [{
            required: true,
            message: 'Seleccione un año',
            trigger: 'change'
        }],
        mes: [{
            required: true,
            message: 'Seleccione un mes',
            trigger: 'change'
        }],
    },
    dataFormItem: {
        // Aqui van todos los arreglos de objetos de los controles select, radiobutton, etc...
        servicio: [],
        consulta: [],
        idempresa: [],
        ano: [],
        mes: []
    },
    tableColumns: [
        {
            label: 'Id',
            prop: 'id_detalle',
            width: 50
        },
        {
            label: 'Detalle',
            prop: 'desc_det_consulta'
        },
        {
            label: 'Procedimiento BD',
            prop: 'procedimiento'
        }
    ],
    tableData: [
        {desc_det_consulta: 'Sin Agrupamiento', id_detalle: 11, procedimiento: 'SP_CONS_VENTAS_CILINDROS'},
        {desc_det_consulta: 'Sin Agrupamiento', id_detalle: 10, procedimiento: 'SP_CONS_VENTAS_DISTRIBUCION'}
    ],
};