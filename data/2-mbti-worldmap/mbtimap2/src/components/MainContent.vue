<template>
    <div id="MainContent">
        <Choropleth></Choropleth>
    </div>
</template>

<script>
import Choropleth from './Choropleth.vue'; // 导入 Choropleth 组件
export default {
    name: 'MainContent',
    components: {
        Choropleth // 注册 Choropleth 组件
    }
}
</script>

<style>

</style>