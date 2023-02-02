import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import loginView from '@/views/loginView.vue'
import registerView from '@/views/registerView.vue'
import postView from '@/views/postView.vue'
import addPostView from '@/views/addPostView.vue'
import changePasswordView from '@/views/changePasswordView.vue'
import allPublicPostView from '@/views/allPublicPostView'
import friendView from '@/views/friendView.vue'
import addFriendView from '@/views/addFriendView.vue'

const routes = [

  {
    path: '/posts',
    name: 'addpost',
    component: addPostView
  },

  {
    path: '/record/:recordId',
    name: 'post',
    component: postView
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/allPublicPost',
    name: 'allPublicPost',
    component: allPublicPostView

  },
  {
    path: '/login',
    name: 'login',
    component: loginView
  },
  {
    path: '/register',
    name: 'register',
    component: registerView
  },
  {
    path: '/changePassword',
    name: 'changePassword',
    component: changePasswordView
  },
  {
    path: '/friend',
    name: 'friend',
    component: friendView
  },
  {
    path: '/addfriend',
    name: 'addfriend',
    component: addFriendView
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
