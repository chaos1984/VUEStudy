<template>
  <v-carousel
    cycle
    height="600"
    hide-delimiter-background
    show-arrows-on-hover
  >
    <v-carousel-item
      v-for="(slide, i) in slides"
      :key="i"
    >
      <v-sheet
        height="100%"
      >
      <img :src="img[i]" height="100%" width="100%"/>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="display-3">{{ slide }} Slide</div>
        </v-row>
      </v-sheet>
      


    </v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    data () {
      return {
        img: [
          '/static/img/slide1.jpg',
          '/static/img/slide2.jpg',
          '/static/img/slide3.jpg',
        ],
        slides: [
          'First',
          'Second',
          'Third',
        ],
      }
    },
  }
</script>