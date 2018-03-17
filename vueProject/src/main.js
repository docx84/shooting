import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bulma/css/bulma.css'
import 'buefy/lib/buefy.css'
import 'font-awesome/css/font-awesome.css'
import Buefy from 'buefy'
import vueBulmaComponents from 'vue-bulma-components'
import Menu from '@/components/navbar.vue'

Vue.use(Buefy)
Vue.use(vueBulmaComponents)

Vue.component("m-menu", Menu)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
