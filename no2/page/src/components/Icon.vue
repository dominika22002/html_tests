<template>
  <div class="Icon">
      <div class="background">
         <a :href='hrefs'><img :src='imgs' style="height: 20px;"></a> 
          {{msg}}
      </div>
    </div>
    
</template>

<script>
export default {
  name: 'Icon',
  props: {
    msg: String,
    imgs: String,
    hrefs: String,
  }
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.background{
    font-size: small;
    /* background-color: rgb(145, 206, 206); */
    width: 50px;
    height: 20px;
    float: left;
    
}
</style>
