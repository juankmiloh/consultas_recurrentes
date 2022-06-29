/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    formItem: {
        servicio: '',
        consulta: '',
        empresa: '',
        ano: '',
        mes: ''
    },
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
            prop: 'empresa',
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
            required: false,
            message: 'Seleccione un servicio',
            trigger: 'change'
        }],
        consulta: [{
            required: false,
            message: 'Seleccione una consulta',
            trigger: 'change'
        }],
        empresa: [{
            required: false,
            message: 'Seleccione una empresa',
            trigger: 'change'
        }],
        ano: [{
            required: false,
            message: 'Seleccione un año',
            trigger: 'change'
        }],
        mes: [{
            required: false,
            message: 'Seleccione un mes',
            trigger: 'change'
        }],
    },
    dataFormItem: {
        // Aqui van todos los arreglos de objetos de los controles select, radiobutton, etc...
        servicio: [{
            id: 1,
            nombre: 'Persona natural'
        },
        {
            id: 2,
            nombre: 'Persona jurídica'
        }],
        consulta: [],
        empresa: [],
        ano: [],
        mes: []
    }
};