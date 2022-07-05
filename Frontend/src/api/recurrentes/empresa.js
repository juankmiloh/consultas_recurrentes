/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getEmpresa(idservicio) {
    return request({
        url: '/empresa',
        method: 'get',
        params: { 'servicio_id': idservicio }
    });
}
