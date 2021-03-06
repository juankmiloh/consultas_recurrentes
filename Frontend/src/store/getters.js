/* jshint esversion: 6 */
/* eslint-disable */
const getters = {
  sidebar: state => state.app.sidebar,
  language: state => state.app.language,
  size: state => state.app.size,
  device: state => state.app.device,
  visitedViews: state => state.tagsView.visitedViews,
  cachedViews: state => state.tagsView.cachedViews,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,
  introduction: state => state.user.introduction,
  roles: state => state.user.roles,
  usuario: state => state.user.usuario,
  privilegio: state => state.user.privilegio,
  keyaccess: state => state.user.keyaccess,
  dependencia: state => state.user.dependencia,
  idusuario: state => state.user.idusuario,
  permission_routes: state => state.permission.routes,
  addRoutes: state => state.permission.addRoutes,
  errorLogs: state => state.errorLog.logs
};
export default getters;