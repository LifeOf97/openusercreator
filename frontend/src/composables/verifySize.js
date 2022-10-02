/* eslint-disable */
import { ref, isRef, unref, watchEffect } from "vue";

export function useVerifySize(value, size, logic) {
    // Comparison Operation between two values, using the provided javascript
    // comparison operators

    const data = ref(false)

    function compare() {
        data.value = false

        switch (logic) {
            case 'eq':
                data.value = unref(value) == size ? true : false
                break;
            case 'lt':
                data.value = unref(value) < size ? true : false
                break;
            case 'lte':
                data.value = unref(value) <= size ? true : false
                break;
            case 'gt':
                data.value = unref(value) > size ? true : false
                break;
            case 'gte':
                data.value = unref(value) >= size ? true : false
                break;
            default:
                data.value = false
        }
    }

    if (isRef(value)) watchEffect(compare)
    else compare()

    return { data }
}