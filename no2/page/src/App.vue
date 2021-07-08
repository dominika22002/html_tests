<template>
  <div id="app">
    <div class="column is-4">
      <TopMenu menu1="ddd" menu2="eee" />
    </div>
    <div class="column is-4">
      <LeftMenu menu1="aaa" menu2="bbb" menu3="ccccc" />
    </div>
  </div>
</template>

<script>
import LeftMenu from "./components/LeftMenu.vue";
import TopMenu from "./components/TopMenu.vue";

export default {
  name: "MainPage",
  components: {
    LeftMenu,
    TopMenu,
  }
};
</script>

<style>
#MainPage {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
