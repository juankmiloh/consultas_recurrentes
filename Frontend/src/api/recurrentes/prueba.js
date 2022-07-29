/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getPrueba() {
    return request({
        url: '/prueba',
        method: 'get',
        /* params: { 'servicio_id': idservicio } */
    });
}
