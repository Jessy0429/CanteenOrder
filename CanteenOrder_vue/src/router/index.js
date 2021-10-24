import Vue from 'vue'
import Router from 'vue-router'
import AppUser from "../components/AppUser";
import UserMain from "../components/UserMain";
import UserOrders from "../components/UserOrders";
import UserInfo from "../components/UserInfo";


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AppUser',
      component: AppUser,
      redirect:'/usermain',
      children:[
        {path: '/usermain', name: 'usermain', component: UserMain},
        {path: '/userorders', name: 'userorders', component: UserOrders},
        {path: '/userinfo', name: 'userinfo', component: UserInfo}
      ]
    }
  ]
})
