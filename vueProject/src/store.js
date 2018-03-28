import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

function dataUrl(path) {
    return "http://localhost:5000/data/" + path
}

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
        },
        setPlayers(state, players) {
            state.players = players;
        }
    },
    actions: {
        addPlayer(context, player) {
            return fetch(dataUrl("players"), {
                method: "POST",
                body: JSON.stringify(player)
            }).then((res) => res.json()).then(function (res) {
                if (res.results === undefined)
                    return Promise.reject(res.error);
                context.commit("addPlayer", res.results);
                return Promise.resolve(res.results);
            }).catch((e) => Promise.reject(e))
        },
        getPlayers(context) {
            return fetch(dataUrl("players")).then((res) => res.json()).then(function (res) {
                if (res.results === undefined)
                    return Promise.reject(res.error);
                context.commit("setPlayers", res.results);
                return Promise.resolve(res.results)
            })
        }
    }
})
