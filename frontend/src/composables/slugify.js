/* eslint-disable */
import { ref, isRef, unref, watchEffect } from "vue";

export function useSlugify(textData, replaceValue, replaceWith) {
    // replaces all occurances of replaceValue if present else replaces hyphens (-)
    // with the supplied replaceWith value if present else replace with spaces
    const data = ref(null)

    function doSlugify() {
        data.value = unref(textData).replaceAll(replaceValue?? "-", replaceWith?? " ")
    }

    if (isRef(textData)) watchEffect(doSlugify)
    else doSlugify()

    return { data }
}