<script setup>
/* eslint-disable */
import AppHomeHero from '../components/AppHomeHero.vue';
import AppHomeNav from '../components/AppHomeNav.vue';
import AppHomeCRUD from '../components/AppHomeCRUD.vue';
import AppHomeAuthentication from '../components/AppHomeAuthentication.vue';
import AppHomeResourcesAndEndpoints from '../components/AppHomeResourcesAndEndpoints.vue';
import AppHomeQueryParameters from '../components/AppHomeQueryParameters.vue';
import AppHomeFooter from '../components/AppHomeFooter.vue';
</script>

<template>
  <main class="w-full h-full bg-white font-Poppins">

    <header>
      <AppHomeHero />
    </header>

    <nav class="hidden sticky top-10 z-20 md:block">
      <AppHomeNav />
    </nav>

    <section>
      <AppHomeCRUD />
    </section>

    <section>
      <AppHomeAuthentication />
    </section>

    <aside>
      <AppHomeResourcesAndEndpoints />
    </aside>

    <article>
      <AppHomeQueryParameters />
    </article>

    <footer class="border-t border-gray-100">
      <AppHomeFooter />
    </footer>

  </main>
</template>
