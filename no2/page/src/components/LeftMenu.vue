<template>
  <div class="LeftMenu">
    <div class="columns">
      <!-- <menubar> -->
      <div class="column is-4" id="menubar">
        <a href="#">{{menu1}}</a>
        {{memory}}{{message}}
      </div>
      <div class="column is-4">
        <a href="#">{{menu2}}</a>
      </div>
      <div class="column is-4">
        <a href="#">{{menu3}}</a>
        {{greeting}}
      </div>
      <div id="components-demo">
        <button-counter></button-counter>
      </div>
      <!-- </menubar> -->
    </div>
    <Icon
      msg="aaa"
      imgs="/Users/dominika/podstawy_Programowania/my_own_programming_course/HTML/My first page/no2/page/src/assets/logo.png"
      hrefs="aaaaaaa"
    />
  </div>
</template>

<script>
// import Icon from "/Users/dominika/podstawy_Programowania/my_own_programming_course/HTML/My first page/no2/page/src/components/Icon.vue";
import Icon from "./Icon.vue";

export default {
  name: "LeftMenu",
  props: {
    menu1: String,
    menu2: String,
    menu3: String
  },
  components: {
    Icon
  },

  data: function() {
    return {
      greeting: "helloo"
    };
  },

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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