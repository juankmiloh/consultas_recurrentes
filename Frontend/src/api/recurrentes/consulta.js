/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getConsulta(idservicio) {
    return request({
        url: '/consulta',
        method: 'get',
        params: { 'servicio_id': idservicio }
    });
}

export function getConsultaDetalle(idcategoria) {
    return request({
        url: '/consulta_detalle',
        method: 'get',
        params: { 'category_id': idcategoria }
    });
}
