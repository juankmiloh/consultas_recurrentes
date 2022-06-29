/* jshint esversion: 6 */
/* eslint-disable */
import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

/* Layout */
import Layout from '@/layout';

/* Router Modules */
import componentsRouter from './modules/components';
import chartsRouter from './modules/charts';
import tableRouter from './modules/table';
import nestedRouter from './modules/nested';

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    noCache: true                if set true, the page will no be cached(default is false)
    affix: true                  if set true, the tag will affix in the tags-view
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [{
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [{
        path: '/redirect/:path*',
        component: () =>
            import('@/views/redirect/index')
    }]
},
{
    path: '/login',
    // path: 'login/:token',
    component: () =>
        import('@/views/login/index'),
    hidden: true
},
{
    path: '/auth-redirect',
    component: () =>
        import('@/views/login/auth-redirect'),
    hidden: true
},
{
    path: '/404',
    component: () =>
        import('@/views/error-page/404'),
    hidden: true
},
{
    path: '/401',
    component: () =>
        import('@/views/error-page/401'),
    hidden: true
},
{
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
        path: 'dashboard',
        component: () =>
            import('@/views/dashboard/index'),
        name: 'Dashboard',
        meta: { title: 'Principal', icon: 'component', noCache: true }
    }]
},
{
    path: '/profile',
    component: Layout,
    redirect: '/profile/index',
    hidden: true,
    children: [{
        path: 'index',
        component: () =>
            import('@/views/profile/index'),
        name: 'Profile',
        meta: { title: 'Perfil', icon: 'user', noCache: true }
    }]
},
]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [{
    path: '/permission',
    component: Layout,
    redirect: '/permission/role',
    alwaysShow: true, // will always show the root menu
    name: 'Permission',
    meta: {
        title: 'Configuración',
        icon: 'lock',
        roles: ['administrador'] // you can set roles in root nav
    },
    children: [{
            path: 'user_create',
            component: () =>
                import('@/views/roles/administrador/CreateUser'),
            name: 'UserCreate',
            meta: {
                title: 'Usuarios',
                // icon: 'user',
                roles: ['administrador']
            }
        }
    ]
},
// vistas adminsitrador
{
    path: '/datosAbiertos',
    component: Layout,
    children: [{
        path: 'index',
        component: () => import('@/views/datosAbiertos'),
        name: 'datosAbiertos',
        meta: {title: 'Datos abiertos', icon: 'education', roles: ['consulta']}
    }]
},
// {
//     path: '/formatos',
//     component: Layout,
//     children: [{path: 'index',
//         component: () => import('@/views/formatos'),
//         name: 'formatos',
//         meta: {title: 'Consulta formatos', icon: 'clipboard', roles: ['consulta']}
//     }]
// },
// {
//     path: '/consultasIG',
//     component: Layout,
//     children: [{
//         path: 'index',
//         component: () => import('@/views/consultasIG'),
//         name: 'consultasIG',
//         meta: {title: 'Consultas IG', icon: 'documentation', roles: ['consulta']}
//     }]
// },
// {
//     path: '/recurrentes',
//     component: Layout,
//     children: [
//     {
//         path: 'index',
//         component: () => import('@/views/recurrentes'),
//         name: 'recurrentes',
//         meta: {title: 'Consultas recurrentes', icon: 'nested', roles: ['consulta']}
//     }]
// },
{
    path: '/consultas',
    component: Layout,
    alwaysShow: true, // will always show the root menu
    name: 'consultas',
    redirect: '/',
    meta: {
        title: 'Consultas',
        icon: 'form',
        roles: ['consulta'] // you can set roles in root nav
    },
    children: [{
            path: 'formatos',
            component: () => import('@/views/formatos'),
            name: 'formatos',
            meta: { title: 'Consulta formatos', noCache: false, roles: ['consulta'] }
        },
        {
            path: 'consultasIG',
            component: () => import('@/views/consultasIG'),
            name: 'consultasIG',
            meta: {title: 'Consulta IG', roles: ['consulta']}
        },
        {
            path: 'recurrentes',
            component: () => import('@/views/recurrentes'),
            name: 'recurrentes',
            meta: {title: 'Consulta recurrentes', roles: ['consulta']}
        }
    ]
},
// 404 page must be placed at the end !!!
{ path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
    // mode: 'history', // require service support
    scrollBehavior: () => ({ y: 0 }),
    routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234noRedirectissuecomment-357941465
export function resetRouter() {
    const newRouter = createRouter()
    router.matcher = newRouter.matcher // reset router
}

export default router;