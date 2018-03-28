<template>
    <div>
        <b-button :is-loading="loading" @click="dispatch">
            <slot></slot>
        </b-button>
    </div>
</template>

<script>
    export default {
        name: "action-button",
        props: ["action", "payload"],
        data: function () {
            return {
                loading: false,
                error: null
            }
        },
        methods: {
            dispatch() {
                this.loading = true;
                let outcome = this.$store.dispatch(this.action, this.payload);
                outcome.then((res) => {
                    this.$emit("success", res)
                    this.loading = false;
                });
                outcome.catch((error) => {
                    this.$emit("error", error)
                    this.loading = false;
                })
            }
        }
    }
</script>

<style scoped>

</style>