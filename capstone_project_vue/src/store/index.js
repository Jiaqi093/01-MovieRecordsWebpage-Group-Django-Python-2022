import { createStore } from 'vuex'

export default createStore({
  state: {
    authenticated: false,
    user_id: '',
    AccountID:''
  },
  getters: {
  },
  mutations: {
    SET_AUTH: (state, auth) => state.authenticated = auth,
    SET_USER_ID: (state, id) => state.user_id = id,
    SET_ACCOUNT_ID: (state, accountID) => state.AccountID = accountID
  },
  actions: {
    setAuth: ({commit},auth) => commit('SET_AUTH',auth),
    setUserID: ({commit},id) => commit('SET_USER_ID',id),
    setAccountID: ({commit},accountID) => commit('SET_ACCOUNT_ID',accountID),

  },
  modules: {
  }
})
