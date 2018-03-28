import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        players: {}
    },
    getters: {
        getPlayerCopy(state, pid) {
            return JSON.parse(JSON.stringify(state.players[pid]))
        }
    },
    mutations: {
        addPlayer(state, player) {
            state.players[player.doc_id] = player.player;
        }
    },
    actions: {
        addPlayer(context, player) {
            return fetch("http://localhost:5000/data/players", {
                method: "POST",
                body: JSON.stringify(player)
            }).then((res) => res.json()).then(function (res) {
                if (res.results === undefined)
                    return Promise.reject(res.error);
                context.commit("addPlayer", res.results);
                return Promise.resolve(res.results);
            }).catch((e) => Promise.reject(e))
        }
    }
})
