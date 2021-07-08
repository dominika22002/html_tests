<template>
  <div class="TopMenu">
    <div class="columns">
      <!-- <menubar> -->
      <div class="column is-4" id="menubar">
        <a href="#">{{menu1}}</a>
        {{memory}}{{message}}
      </div>
      <div class="column is-8">
        <a href="#">{{menu2}}</a>
      </div>
      <div id="components-demo">
        <button-counter></button-counter>
      </div>
      <!-- </menubar> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "TopMenu",
  props: {
    menu1: String,
    menu2: String,
  },
  components: {
    // Icon
  }
};

</script>




<style scoped>
#leftmenu {
  margin: 0.3em;
  background-color: #42b983;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: stretch;
}

div.LeftMenu {
  background-color: aqua;
  text-align: center;
}
#aaa {
  background-color: rgb(77, 99, 99);
  text-align: center;
}

div {
  background-color: rgb(98, 78, 189);
}
div a {
  text-decoration: none;
  color: white;
  /* font-size: 20px; */
  /* padding: 15px; */
  /* display: inline-block; */
}
:hover {
  background: rgb(139, 41, 41);
}
:active {
  background: rgb(77, 59, 59);
}
</style>