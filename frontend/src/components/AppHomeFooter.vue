<script setup>
/* eslint-disable */
import { computed, onMounted, ref } from 'vue';
import IconUserCircleSolid from './icons/IconUserCircleSolid.vue';
import IconTwitter from './icons/IconTwitter.vue';
import IconGithub from './icons/IconGithub.vue';
import IconLinkedin from './icons/IconLinkedin.vue';
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';

// register gsap plugins
gsap.registerPlugin(ScrollTrigger)


// refs
const footerOne = ref(null)
const footerTwo = ref(null)

const year = computed(() => {
    return new Date().getFullYear();
})

// methods
const animate = () => {
    gsap.from(
        [footerOne.value],
        {
            scrollTrigger: {trigger: footerOne.value},
            duration: 1, y: 30, opacity: 0, stagger: 0.3
        }
    )
    gsap.from(
        [footerTwo.value],
        {
            scrollTrigger: {trigger: footerTwo.value},
            duration: 1, y: 30, opacity: 0, stagger: 0.3
        }
    )
}

// hooks
onMounted(() => {
    animate()
})
</script>

<template>
    <main class="w-11/12 mx-auto flex flex-col gap-5 items-center justify-between text-xs text-gray-400 py-10 md:text-sm md:flex-row">

        <div ref="footerOne" class="flex flex-col gap-2 md:gap-4">
            <div class="flex items-center gap-2">
                <p>&copy; {{year}}</p>
                <div class="flex items-center">
                    <IconUserCircleSolid class="w-5 h-5 fill-red-500" />
                    <p class="font-semibold text-gray-900">pen User Data</p>
                </div>
            </div>

            <div class="flex items-center gap-2">
                <p class="text-gray-900 font-semibold">API Docs:</p>
                <a 
                    href="https://api.openuserdata.xyz/api/v1/schema/swagger/"
                    target="_blank"
                    class="text-blue-500 font-light hover:text-blue-600">Swagger,</a>
                <a 
                    href="https://api.openuserdata.xyz/api/v1/schema/redoc/"
                    target="_blank"
                    class="text-blue-500 font-light hover:text-blue-600">REDOC</a>
            </div>
        </div>

        <div ref="footerTwo" class="flex flex-col gap-2 md:gap-4">
            <div class="flex items-center gap-2">
                <p>Developed by the</p>
                <a href="https://twitter.com/realestkma" target="_blank" rel="noopener noreferrer" class="text-blue-500 hover:text-blue-600">RealestKMA</a>
                <p>from the 234</p>
                <flag iso="ng" />
            </div>
            <div class="flex items-center justify-center gap-4 md:justify-start">
                <a href="http://twitter.com/realestkma" target="_blank" rel="noopener noreferrer">
                    <IconTwitter class="w-5 h-5 fill-gray-900" />
                </a>
                <a href="http://github.com/realestkma" target="_blank" rel="noopener noreferrer">
                    <IconGithub class="w-5 h-5 fill-gray-900" />
                </a>
                <a href="http://linkedin.com/in/realestkma" target="_blank" rel="noopener noreferrer">
                    <IconLinkedin class="w-5 h-5 fill-gray-900" />
                </a>
            </div>
        </div>

    </main>
</template>