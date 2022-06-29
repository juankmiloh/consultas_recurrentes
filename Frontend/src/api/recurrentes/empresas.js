/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListEmpresas(data) {
    return request({
        url: '/empresa',
        method: 'post',
        data
    });
}
