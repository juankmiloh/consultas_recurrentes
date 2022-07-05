/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getServicio() {
    return request({
        url: '/servicio',
        method: 'get'
    });
}
